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
MAX_INTENTOS = 3 # número máximo de intentos de comunicación


def ntc10k_calculate_temp(raw_value, volts):
    # mV
    voltage = (MAX_VOLTAGE_INPUT * raw_value / 1024)
    Rntc = 210000 * (voltage / (volts - voltage))
    log=""
    log=str(Rntc)
    #AJUSTE LOGARÍTMCO
    temperatureC=-20.45*math.log1p(Rntc)+213.23

    #AJUSTE POLINÓMICO ORDEN 5 (funciona peor)
    #temperatureC = 4e-18*pow(Rntc,4) + 9e-13*pow(Rntc,3) + 8e-8*pow(Rntc,2) - 0.0034*Rntc + 52.479

    log = log +" ntc 10K temper: %.2f" % temperatureC
    print(log)
    return temperatureC



def main():
    print (len(REMOTE_NODES_ID))
    print(" +--------------------------------------------+")
    print(" | XBee Python Library Read Remote ADC Sample |")
    print(" +--------------------------------------------+\n")
    local_device = XBeeDevice(port, baud_rate)
    xbee_network = local_device.get_network()
    local_device.open()



    stop = False
    th = None
    time.sleep(1)


    def read_adc_task(indice):

       # remote_device.set_io_configuration(IOLINE_IN_0, IOMode.ADC)
       # remote_device.set_io_configuration(IOLINE_IN_1, IOMode.ADC)
       # remote_device.set_io_configuration(IOLINE_IN_2, IOMode.ADC)
       # remote_device.set_io_configuration(IOLINE_IN_3, IOMode.ADC)
       # time.sleep(3)


        intentos = MAX_INTENTOS

        while True:
            try:
                print ("Nodo %s" % indice)
                # Leemos el valor del nodo para luego calcular el valor de la resistencia del termistor mediante la
                # ley de Ohm para un divisor de tensión
                vcc = nodos_activos[index].get_parameter("%V")
                vcc = int(utils.hex_to_string(vcc).replace(' ', ''), 16)
                time.sleep(0.5)
                # Leemos el valor crudo de las entradas analógicas
                raw_value_1 = nodos_activos[indice].get_adc_value(IOLINE_IN_0)
                raw_value_2 = nodos_activos[indice].get_adc_value(IOLINE_IN_1)
                raw_value_3 = nodos_activos[indice].get_adc_value(IOLINE_IN_2)
                raw_value_4 = nodos_activos[indice].get_adc_value(IOLINE_IN_3)
                # Calculamos el valor de temperatura en cada entrada en función de la tensión de alimentación y del
                # valor crudo
                tntc_1 = ntc10k_calculate_temp(raw_value_1, vcc)
                tntc_2 = ntc10k_calculate_temp(raw_value_2, vcc)
                tntc_3 = ntc10k_calculate_temp(raw_value_3, vcc)
                tntc_4 = ntc10k_calculate_temp(raw_value_4, vcc)
                print("")
                # ************************************************************************
                # ESTA ES LA PARTE DE TELEGRAF
                send_data_to_telegraf.main(REMOTE_NODES_ID[indice], tntc_1, tntc_2, tntc_3, tntc_4, float(vcc))
                # Esperamos hasta la siguiente toma de muestras

            except TimeoutException as ex:
                intentos -= 1
                print (REMOTE_NODES_ID[indice])
                print("ADC intentos %s" % intentos)
                if intentos == 0:
                    raise ex

            time.sleep(10)





    try:
        index_devices=0
        nodos_activos=[]
        for index in range (0, len(REMOTE_NODES_ID)):
            nodo_descubierto=False
            intentos = MAX_INTENTOS
            # Procedimiento de descubrimiento de nodos, ver que pasa si uno está apagado
            while (nodo_descubierto != True)and intentos>0:
                #nodo = REMOTE_NODES_ID[index]
                # configura las entradas de los módulos
                remote_device=( xbee_network.discover_device(REMOTE_NODES_ID[index]))
                if remote_device is None:
                    print("Could not find the remote device: " + REMOTE_NODES_ID[index])  # ESTOY HAY QUE VER COMO SE HACE
                    intentos -=1
                    print ("Nodo: %s" % index)
                    print ("Intentos descubrimiento restantes: %s" %intentos)
                    time.sleep(3)
                    # exit(1)
                else:
                    nodos_activos.append(remote_device)
                    index_devices+=1
                    print ('Descubierto: %s' % remote_device)
                    nodo_descubierto = True
        #ejecución de los hilos
        for index in range (0, index_devices):
            th = threading.Thread(name=nodos_activos[index], target=read_adc_task, args=(index,))
            th.start()
        #time.sleep(0.3)






    finally:
        if th is not None and th.isAlive():
            th.join()
        if local_device is not None and local_device.is_open():
            local_device.close()


if __name__ == '__main__':
    main()
