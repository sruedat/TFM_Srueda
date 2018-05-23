
from digi.xbee.devices import XBeeDevice
from digi.xbee.io import IOLine, IOMode
from digi.xbee.util import utils
from digi.xbee.exception import TimeoutException



import logging
import re
import threading
import time

import read_node_list
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
IO_SAMPLING_RATE = 5 # 5 seconds
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
    print(" +----------------------------------------------+")
    print(" | XBee Python Library Handle IO Samples Sample |")
    print(" +----------------------------------------------+\n")

    device = XBeeDevice(port, baud_rate)

    try:
        device.open()

        # Obtain the remote XBee device from the XBee network.
        xbee_network = device.get_network()
        remote_device = xbee_network.discover_device('REMOTO_2')
        if remote_device is None:
            print("Could not find the remote device")
            exit(1)

        # Set the local device as destination address of the remote.
        remote_device.set_dest_address(device.get_64bit_addr())

        remote_device.set_io_configuration(IOLINE_IN_3 , IOMode.ADC)
        remote_device.set_io_configuration(IOLINE_IN_2 , IOMode.ADC)
        remote_device.set_io_configuration(IOLINE_IN_1, IOMode.ADC)
        remote_device.set_io_configuration(IOLINE_IN_0, IOMode.ADC)

        # Enable periodic sampling every IO_SAMPLING_RATE seconds in the remote device.
        remote_device.set_io_sampling_rate(IO_SAMPLING_RATE)


        def parse_sample(sample):
            for i in range (0,4):
                sample=str(sample).replace('IOLine.DIO'+str(i)+'_AD'+str(i)+':',"")
            sample = sample.replace('[','')
            sample = sample.replace (']','')
            sample = sample.replace('{','')
            sample = sample.replace('}','')
            sample=sample.split(',')
            for i in range (0,len(sample)):
                sample[i]=int(sample[i])
            return sample

        def get_voltaje(remote):
            vcc= remote.get_parameter("%V")
            vcc = int(utils.hex_to_string(vcc).replace(' ', ''), 16)
            return vcc

        # Register a listener to handle the samples received by the local device.
        def io_samples_callback(sample, remote, time):
            print("New sample received from %s - %s" % (remote.get_64bit_addr(), sample))
            vcc = remote.get_parameter("%V")
            vcc = int(utils.hex_to_string(vcc).replace(' ', ''), 16)
            print(vcc)
            raw_values = parse_sample (sample)
            temp_1= ntc10k_calculate_temp(raw_values[0],3300)
            print(temp_1)



        device.add_io_sample_received_callback(io_samples_callback)


        input()

    finally:

        if device is not None and device.is_open():
            device.del_io_sample_received_callback(io_samples_callback)
            device.close()


if __name__ == '__main__':
    main()