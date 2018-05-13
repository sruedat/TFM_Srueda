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
MAX_INTENTOS = 10 # número máximo de intentos de comunicación


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


    # configura las entradas de los módulos
    #configuro nodos:
    #nodo 1:
    remote_device1 = xbee_network.discover_device("REMOTO_1")
    #remote_device1.set_io_configuration(IOLINE_IN_0, IOMode.ADC)
    #remote_device1.set_io_configuration(IOLINE_IN_1, IOMode.ADC)
    #remote_device1.set_io_configuration(IOLINE_IN_2, IOMode.ADC)
    #remote_device1.set_io_configuration(IOLINE_IN_3, IOMode.ADC)
    # nodo 2:
    remote_device2 = xbee_network.discover_device("REMOTO_2")
    #remote_device2.set_io_configuration(IOLINE_IN_0, IOMode.ADC)
    #remote_device2.set_io_configuration(IOLINE_IN_1, IOMode.ADC)
    #remote_device2.set_io_configuration(IOLINE_IN_2, IOMode.ADC)
    #remote_device2.set_io_configuration(IOLINE_IN_3, IOMode.ADC)



    stop = False
    th = None
    time.sleep(1)
    try:

        if remote_device1 is None:
            print("Could not find the remote device REMOTO_1")  # ESTOY HAY QUE VER COMO SE HACE
            exit(1)

        if remote_device2 is None:
            print("Could not find the remote device REMOTO_2")  # ESTOY HAY QUE VER COMO SE HACE
            exit(1)

        time.sleep(1)

        def read_adc_task():
            intentos = 0#YMAX_INTENTOS
            while not stop:

                try:
                #Nodo 1:
                # Leemos el valor del nodo para luego calcular el valor de la resistencia del termistor mediante la
                # ley de Ohm para un divisor de tensión
                    vcc = remote_device1.get_parameter("%V")
                    vcc = int(utils.hex_to_string(vcc).replace(' ', ''), 16)
                    time.sleep(0.1)
                # Leemos el valor crudo de las entradas analógicas
                    raw_value_1 = remote_device1.get_adc_value(IOLINE_IN_0)
                    time.sleep(0.1)
                    raw_value_2 = remote_device1.get_adc_value(IOLINE_IN_1)
                    time.sleep(0.1)
                    raw_value_3 = remote_device1.get_adc_value(IOLINE_IN_2)
                    time.sleep(0.1)
                    raw_value_4 = remote_device1.get_adc_value(IOLINE_IN_3)
                    time.sleep(0.1)
                # Calculamos el valor de temperatura en cada entrada en función de la tensión de alimentación y del
                # valor crudo
                    tntc_1 = ntc10k_calculate_temp(raw_value_1, vcc)
                    tntc_2 = ntc10k_calculate_temp(raw_value_2, vcc)
                    tntc_3 = ntc10k_calculate_temp(raw_value_3, vcc)
                    tntc_4 = ntc10k_calculate_temp(raw_value_4, vcc)
                # ************************************************************************
                # ESTA ES LA PARTE DE TELEGRAF
                    send_data_to_telegraf.main("REMOTO_1", tntc_1, tntc_2, tntc_3, tntc_4, float(vcc))
                    print("")
                    # Esperamos hasta la siguiente toma de muestras
                    time.sleep(1)
                #Ndodo 2:
                    vcc = remote_device2.get_parameter("%V")
                    time.sleep(0.1)
                    vcc = int(utils.hex_to_string(vcc).replace(' ', ''), 16)
                    raw_value_1 = remote_device2.get_adc_value(IOLINE_IN_0)
                    time.sleep(0.1)
                    raw_value_2 = remote_device2.get_adc_value(IOLINE_IN_1)
                    time.sleep(0.1)
                    raw_value_3 = remote_device2.get_adc_value(IOLINE_IN_2)
                    time.sleep(0.1)
                    raw_value_4 = remote_device2.get_adc_value(IOLINE_IN_3)
                    time.sleep(0.1)
                    print ("R2")
                    tntc_1 = ntc10k_calculate_temp(raw_value_1, vcc)
                    tntc_2 = ntc10k_calculate_temp(raw_value_2, vcc)
                    tntc_3 = ntc10k_calculate_temp(raw_value_3, vcc)
                    tntc_4 = ntc10k_calculate_temp(raw_value_4, vcc)
                    send_data_to_telegraf.main("REMOTO_2", tntc_1, tntc_2, tntc_3, tntc_4, float(vcc))
                    print("Timeouts: %s" %intentos)

                except TimeoutException as ex:
                    intentos += 1
                    print("intentos %s" % intentos)
                    #if intentos == 0:
                    #    local_device.close()
                    #    raise ex

                # Esperamos hasta la siguiente toma de muestras
                time.sleep(20)


        th = threading.Thread(target=read_adc_task)
        time.sleep(1)
        th.start()
        input()



    finally:
        stop = True
        if th is not None and th.isAlive():
            th.join()
        if local_device is not None and local_device.is_open():
            local_device.close()


if __name__ == '__main__':
    main()
