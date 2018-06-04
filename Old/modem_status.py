
from digi.xbee.devices import XBeeDevice
from digi.xbee.util import utils

# TODO: Replace with the serial port where your local module is connected to. 
PORT = "COM6"
# TODO: Replace with the baud rate of your local module.
BAUD_RATE = 9600


def main():
    print(" +-------------------------------------------------+")
    print(" | XBee Python Library Receive Modem Status Sample |")
    print(" +-------------------------------------------------+\n")

    device = XBeeDevice(PORT, BAUD_RATE)

    try:
        device.open()



        print("Waiting for Modem Status events...\n")
        input()

    finally:
        if device is not None and device.is_open():
            device.close()


if __name__ == '__main__':
    main()