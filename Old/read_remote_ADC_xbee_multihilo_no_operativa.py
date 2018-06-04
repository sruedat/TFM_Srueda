# Copyright 2017, Digi International Inc.
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

from digi.xbee.devices import XBeeDevice
from digi.xbee.io import IOLine, IOMode
from digi.xbee.util import utils
from digi.xbee.exception import TimeoutException
from datetime import datetime
import time, sys, threading, math
import read_sys_config
import read_node_list
import send_data_to_telegraf

sys.tracebacklimit = 0

# Parámetros de conexión con el puerto serie al dispositivo local
port = read_sys_config.ReadLocalPortFromFile()
baud_rate = read_sys_config.ReadLocalBaudRateFromFile()

#REMOTE_NODE_ID = "REMOTO_1"
REMOTE_NODES_ID = read_node_list.ReadListOfNodesFromFile()
IOLINE_IN_3 = IOLine.DIO3_AD3
IOLINE_IN_2 = IOLine.DIO2_AD2
IOLINE_IN_1 = IOLine.DIO1_AD1
IOLINE_IN_0 = IOLine.DIO0_AD0
MAX_VOLTAGE_INPUT = 1200
MAX_INTENTOS_DESCUBRIMIENTO = 3 # número máximo de intentos de descubrir a un nodo
MAX_INTENTOS_LEER_DATOS = 10 # número máximo de intentos de descubrir a un nodo
LONG_WAIT=30
SHORT_WAIT=0.5



def ntc10k_calculate_temp(raw_value, volts):
    # mV
    voltage = (MAX_VOLTAGE_INPUT * raw_value / 1024)
    Rntc = 210000 * (voltage / (volts - voltage))
    log=""
    log=str(Rntc)
    #AJUSTE_CUADRÁTICO
    a=574.1
    b=-0.1242
    c= -158
    temperatureC =a*(pow(Rntc,b))+c

    #AJUSTE LOGARÍTMCO
    #temperatureC=-20.45*math.log1p(Rntc)+213.23

    #AJUSTE POLINÓMICO ORDEN 5 (funciona peor)
    #temperatureC = 4e-18*pow(Rntc,4) + 9e-13*pow(Rntc,3) + 8e-8*pow(Rntc,2) - 0.0034*Rntc + 52.479

    log = log +" ntc 10K temper: %.2f" % temperatureC
    print(log)
    return temperatureC


systembusy=False
def main():

    def read_adc_task(indice):
        while True or intentos[indice] < MAX_INTENTOS_LEER_DATOS:
            try:
                # Leemos el valor del nodo para luego calcular el valor de la resistencia del termistor mediante la
                # ley de Ohm para un divisor de tensión
                if systembusy == False:
                    systembusy = True
                    #time.sleep(1)
                    vcc = nodos_activos[indice].get_parameter("%V")
                    vcc = int(utils.hex_to_string(vcc).replace(' ', ''), 16)
                # Leemos el valor crudo de las entradas analógicas
                    raw_value_1 = nodos_activos[indice].get_adc_value(IOLINE_IN_0)
                    raw_value_2 = nodos_activos[indice].get_adc_value(IOLINE_IN_1)
                    raw_value_3 = nodos_activos[indice].get_adc_value(IOLINE_IN_2)
                    raw_value_4 = nodos_activos[indice].get_adc_value(IOLINE_IN_3)
                # Calculamos el valor de temperatura en cada entrada en función de la tensión de alimentación y del
                # valor crudo

                print("Nodo %s" % nodos_activos[indice])
                tntc_1 = ntc10k_calculate_temp(raw_value_1, vcc)
                tntc_2 = ntc10k_calculate_temp(raw_value_2, vcc)
                tntc_3 = ntc10k_calculate_temp(raw_value_3, vcc)
                tntc_4 = ntc10k_calculate_temp(raw_value_4, vcc)

                # ************************************************************************
                # ESTA ES LA PARTE DE TELEGRAF
                intentos[indice]=0
                print(str(datetime.now()))
                send_data_to_telegraf.main(REMOTE_NODES_ID[indice], tntc_1, tntc_2, tntc_3, tntc_4, float(vcc))
                systembusy = False
                # Esperamos hasta la siguiente toma de muestras
                espera = LONG_WAIT
            #except TimeoutException as ex:
            except:
                intentos[indice] += 1
                print (REMOTE_NODES_ID[indice])
                print("ADC timeouts %s" % intentos)
                systembusy = False
                espera=SHORT_WAIT
                if intentos[indice] > MAX_INTENTOS_LEER_DATOS:
                    th[indice].join()
                   # raise
            #print("Espera: %s" % espera)
            print("")
            time.sleep(espera)






    index_devices = 0
    th = []
    nodos_activos = []
    intentos = []
    print("Cantidad de nodos: %s" % len(REMOTE_NODES_ID))
    print(" +----------------------------------------+")
    print(" | XBee Python Read Remote ADC multi-hilo |")
    print(" +----------------------------------------+\n")

    try:
        local_device = XBeeDevice(port, baud_rate)
        xbee_network = local_device.get_network()
        local_device.open()


        for index in range (0, len(REMOTE_NODES_ID)):
            nodo_descubierto=False
            intentos.append(0)
            # Procedimiento de descubrimiento de nodos, ver que pasa si uno está apagado
            while (nodo_descubierto != True)and intentos[index]<MAX_INTENTOS_DESCUBRIMIENTO:
                remote_device=( xbee_network.discover_device(REMOTE_NODES_ID[index]))
                if remote_device is None:
                    print("Could not find the remote device: " + REMOTE_NODES_ID[index])  # ESTOY HAY QUE VER COMO SE HACE
                    intentos [index]+=1
                    print ("Nodo: %s" % (REMOTE_NODES_ID[index]))
                    print ("Intentos descubrimiento restantes: %s" % (MAX_INTENTOS_DESCUBRIMIENTO-intentos[index]))
                    time.sleep(3)
                else:
                    nodos_activos.append(remote_device)
                    index_devices+=1
                    print ('Descubierto: %s' % remote_device)
                    nodo_descubierto = True
        #ejecución de los hilos
        for index in range (0, index_devices):
            thread=threading.Thread(name=nodos_activos[index], target=read_adc_task, args=(index,))
            th.append(thread)
        intentos=[]
        for index in range(0, index_devices):
            intentos.append(0)
            th[index].start()
            time.sleep(1)

    except:
       print("eRRor")

    finally:
        for index in range(0, index_devices):
            if th[index] is not None and th[index].isAlive():
                th[index].join()
        if local_device.is_open():
            local_device.close()
        exit(-1)




if __name__ == '__main__':
    main()
