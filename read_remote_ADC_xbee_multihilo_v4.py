
from digi.xbee.devices import XBeeDevice
from digi.xbee.io import IOLine, IOMode
from digi.xbee.util import utils
from digi.xbee.exception import TimeoutException



import logging
import sys
import threading
import time


from datetime import datetime

import read_sys_config
import read_node_list
import send_data_to_telegraf


REMOTE_NODES_ID = read_node_list.ReadListOfNodesFromFile()
MAX_INTENTOS_DESCUBRIMIENTO = 3
MAX_INTENTOS_LEER_DATOS = 20 # número máximo de intentos de descubrir a un nodo

IOLINE_IN_3 = IOLine.DIO3_AD3
IOLINE_IN_2 = IOLine.DIO2_AD2
IOLINE_IN_1 = IOLine.DIO1_AD1
IOLINE_IN_0 = IOLine.DIO0_AD0
MAX_VOLTAGE_INPUT = 1200
LONG_WAIT=30
SHORT_WAIT=1

# Parámetros de conexión con el puerto serie al dispositivo local
port = read_sys_config.ReadLocalPortFromFile()
baud_rate = read_sys_config.ReadLocalBaudRateFromFile()

def ntc10k_calculate_temp(raw_value, volts):
    # mV
    voltage = (MAX_VOLTAGE_INPUT * raw_value / 1024)
    Rntc = 210000 * (voltage / (volts - voltage))
    #AJUSTE_CUADRÁTICO
    a=574.1
    b=-0.1242
    c= -158
    temperatureC =a*(pow(Rntc,b))+c
    logging.debug('ntc 10K temper: %.2f',temperatureC)
    return temperatureC




def main():
    class ReadAD:
        def __init__(self, start=0):
            self.lock = threading.Lock()
            self.value = start


        def read_AD(self, indice):
            logging.debug('Waiting for lock')
            self.lock.acquire()
            try:
                self.timeout = False
                logging.debug('Acquired lock')
                vcc = nodos_activos[indice].get_parameter("%V")
                vcc = int(utils.hex_to_string(vcc).replace(' ', ''), 16)
                # Leemos el valor crudo de las entradas analógicas
                raw_value_1 = nodos_activos[indice].get_adc_value(IOLINE_IN_0)
                raw_value_2 = nodos_activos[indice].get_adc_value(IOLINE_IN_1)
                raw_value_3 = nodos_activos[indice].get_adc_value(IOLINE_IN_2)
                raw_value_4 = nodos_activos[indice].get_adc_value(IOLINE_IN_3)

                # Calculamos el valor de temperatura en cada entrada en función de la tensión de alimentación y del
                tntc_1 = ntc10k_calculate_temp(raw_value_1, vcc)
                tntc_2 = ntc10k_calculate_temp(raw_value_2, vcc)
                tntc_3 = ntc10k_calculate_temp(raw_value_3, vcc)
                tntc_4 = ntc10k_calculate_temp(raw_value_4, vcc)

                # ************************************************************************
                # ESTA ES LA PARTE DE TELEGRAF
                send_data_to_telegraf.main(REMOTE_NODES_ID[indice], tntc_1, tntc_2, tntc_3, tntc_4, float(vcc))


            except TimeoutException:
                self.timeout = True
                logging.debug('ADC error')
                local_device.reset()

            finally:
                self.lock.release()

            return self.timeout


    timeouts=[]
    def worker(c,i):
        #La petición se hace con tiempo variable, si no se encuentra si dat timeout se hacen más rápidas para no
        #haberlo pillado en una secuencia de sueño, si sobre pasa el límite de timeouts cortos ya no se le pregunta más
        timeouts.append(0)
        try:
            while True and (timeouts[i]< MAX_INTENTOS_LEER_DATOS):
                logging.debug('Stamp: %s',  str(datetime.now()))
                if c.read_AD(i):
                    timeouts[i]+=1
                    logging.debug("Timeouts %s", timeouts)
                    pause=SHORT_WAIT
                else:
                    timeouts[i] = 0 #reseteamos la cuenta de timeouts
                    pause = LONG_WAIT
                logging.debug('Sleeping %0.02f', pause)
                time.sleep(pause)
        except ValueError:
             logging.debug('Worker error')







    nodos_activos=[]
    def descubre_nodos():
        index_devices=0
        try:
            for index in range (0, len(REMOTE_NODES_ID)):
                nodo_descubierto=False
                intentos_descubir=0
                # Procedimiento de descubrimiento de nodos, ver que pasa si uno está apagado
                while (nodo_descubierto != True)and intentos_descubir< MAX_INTENTOS_DESCUBRIMIENTO:
                    remote_device=(xbee_network.discover_device(REMOTE_NODES_ID[index]))
                    if remote_device is None:
                        logging.debug('Could not find the remote device: %s', REMOTE_NODES_ID[index])
                        intentos_descubir+=1
                        logging.debug("Nodo: %s" , (REMOTE_NODES_ID[index]))
                        logging.debug('Intentos descubrimiento restantes: %s', (MAX_INTENTOS_DESCUBRIMIENTO-intentos_descubir))
                        time.sleep(1)
                    else:
                        nodos_activos.append(remote_device)
                        index_devices+=1
                        logging.debug('Descubierto: %s',remote_device)
                        nodo_descubierto = True
        except:
            logging.debug('Error proceso descubrimiento')







    logging.basicConfig(
        level=logging.DEBUG,
        format='(%(threadName)-10s) %(message)s',
    )

#Conexión al nodo local
    local_device = XBeeDevice(port, baud_rate)
    xbee_network = local_device.get_network()
    local_device.open()
    descubre_nodos()

    try:
        lectura = ReadAD()
        for i in range(len(nodos_activos)):
            logging.debug('creando hilo')
            t = threading.Thread(name=nodos_activos[i], target=worker, args=(lectura, i,))
            t.start()
        if len(nodos_activos)==0:
            logging.debug('No nodes found')
            sys.exti(-1)
        else:
            logging.debug('Waiting for worker threads')
            main_thread = threading.main_thread()
            for t in threading.enumerate():
                if t is not main_thread:
                    t.join()
            logging.debug('Counter: %d', lectura.value)

    except:
        logging.debug('exept')
        sys.exit(1)











if __name__ == '__main__':
    main()

