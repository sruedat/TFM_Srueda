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
import time, sys, threading, math, string
import read_sys_config
import temp_simulator

sys.tracebacklimit = 0

# Parámetros de conexión con el puerto serie al dispositivo local
port = read_sys_config.ReadLocalPortFromFile()
baud_rate = read_sys_config.ReadLocalBaudRateFromFile()

REMOTE_NODE_ID = "REMOTO_1"

IOLINE_IN_3 = IOLine.DIO3_AD3
IOLINE_IN_2 = IOLine.DIO2_AD2
IOLINE_IN_1 = IOLine.DIO1_AD1
IOLINE_IN_0 = IOLine.DIO0_AD0
MAX_VOLTAGE_INPUT = 1200
MAX_LECTURES = 1
vcc = 3080  # mv
VOLTAGE_SHIFT = 0


def ntc10k_calculate_temp(raw_value, volts):
    B = 3975
    B = 3892
    # mV
    voltage = (MAX_VOLTAGE_INPUT * raw_value / 1024)
    Rntc = 210000 * (voltage / (volts - voltage))
    #Rntc = 5326.04
    print(Rntc)
    #temperatureC = 1 / (math.log(Rntc / 10000, 2) / B + 1 / 298.15) - 273.15
    #temperatureC = B / (math.log(Rntc / 10500, 2) + (B / 298.15)) - 273.15

    #steinhart = Rntc / 10000  # (R / Ro)
    #steinhart = math.log(steinhart, 2)  # ln(R / Ro)
    #steinhart /= B  # 1 / B * ln(R / Ro)
    #steinhart += 1.0 / (25 + 273.15)  # + (1 / To)
    #steinhart = 1.0 / steinhart  # Invert
    #steinhart -= 273.15  # convert to C

    #temperatureC = steinhart

    #AJUSTE LOGARÍTMCO
    temperatureC=-20.45*math.log1p(Rntc)+213.23

    #AJUSTE POLINÓMICO ORDEN 5
    #temperatureC = 4e-18*pow(Rntc,4) + 9e-13*pow(Rntc,3) + 8e-8*pow(Rntc,2) - 0.0034*Rntc + 52.479

    log = "ntc 10K temper: %.2f" % temperatureC
    print(log)
    return temperatureC


def tmp36_calculate_tmp(raw_value):
    # mV
    voltage = ((MAX_VOLTAGE_INPUT * raw_value) + 512) / 1023
    temperatureC = ((voltage / 1000) - 0.5) * 100
    log = "Temperatura: %.2f" % temperatureC


def lmt84_calculate_tmp(raw_value):
    # mV
    voltage = (MAX_VOLTAGE_INPUT * raw_value / 1024.0) + VOLTAGE_SHIFT
    temperatureC = ((5.506 - math.sqrt(math.pow(-5.506, 2) + 4 * 0.00176 * (870.6 - voltage))) / (2 * -0.00176)) + 30
    log = "LMT84 Temperatura: %.2f" % temperatureC
    return temperatureC


def main():
    print(" +--------------------------------------------+")
    print(" | XBee Python Library Read Remote ADC Sample |")
    print(" +--------------------------------------------+\n")
    local_device = XBeeDevice(port, baud_rate)
    xbee_network = local_device.get_network()
    local_device.open()
    remote_device = xbee_network.discover_device(REMOTE_NODE_ID)
    remote_device.set_io_configuration(IOLINE_IN_0, IOMode.ADC)
    remote_device.set_io_configuration(IOLINE_IN_1, IOMode.ADC)
    remote_device.set_io_configuration(IOLINE_IN_2, IOMode.ADC)
    remote_device.set_io_configuration(IOLINE_IN_3, IOMode.ADC)
    stop = False
    th = None
    time.sleep(1)
    try:

        # Obtain the remote XBee device from the XBee network.

        if remote_device is None:
            print("Could not find the remote device")
            exit(1)

        time.sleep(1)

        def read_adc_task():
            while not stop:
                # Read the analog value from the remote input line.
                total = 0
                lectura = list(range(MAX_LECTURES))
                # filtro por software
                # *********************************************************************
                # borra vector
                # for n in range(0,MAX_LECTURES):
                #    lectura[n]=0
                # acumula valor entrada
                # for n in range(0, MAX_LECTURES):
                #       lectura[n] = remote_device.get_adc_value(IOLINE_IN_3)
                #       total = total + lectura[n]
                #       time.sleep(0.3)
                # promedia
                # value_3 = total/MAX_LECTURES
                value_0 = remote_device.get_adc_value(IOLINE_IN_0)

                # print(IOLINE_IN_3)
                # tmp36_calculate_tmp(value)
                tlmt84 = lmt84_calculate_tmp(value_0)
                # print()
                # ************************************************************************
                total = 0
                # for n in range(0,MAX_LECTURES):
                #   lectura[n]=0
                # acumula valor entrada
                # for n in range(0, MAX_LECTURES):
                #       lectura[n] = remote_device.get_adc_value(IOLINE_IN_0)
                #       total = total + lectura[n]
                #       time.sleep(0.3)
                # promedia
                # value_1 = total/MAX_LECTURES
                # print(IOLINE_IN_3)
                # tmp36_calculate_tmp(value)
                vcc = remote_device.get_parameter("%V")
                vcc = int(utils.hex_to_string(vcc).replace(' ', ''), 16)
                time.sleep(2)
                #print("Voltaje: %f" % vcc)
                value_1 = remote_device.get_adc_value(IOLINE_IN_0)
                value_2 = remote_device.get_adc_value(IOLINE_IN_1)
                value_3 = remote_device.get_adc_value(IOLINE_IN_2)
                value_4 = remote_device.get_adc_value(IOLINE_IN_3)

                tntc_1 = ntc10k_calculate_temp(value_1, vcc)
                tntc_2 = ntc10k_calculate_temp(value_2, vcc)
                tntc_3 = ntc10k_calculate_temp(value_3, vcc)
                tntc_4 = ntc10k_calculate_temp(value_4, vcc)
                # ************************************************************************
                temp_simulator.main(tntc_1, tntc_2, tntc_3, tntc_4)
                print("")

                # value = remote_device.get_adc_value(IOLINE_IN_2)
                # print(IOLINE_IN_2)
                # tmp36_calculate_tmp(value)
                # lmt84_calculate_tmp(value)
                # print("\n")
                time.sleep(15)

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
