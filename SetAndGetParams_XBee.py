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
from digi.xbee.devices import RemoteZigBeeDevice
from digi.xbee.util import utils
from digi.xbee.models.address import XBee64BitAddress


# TODO: Replace with the serial port where your local module is connected to.
PORT = "COM6"
# TODO: Replace with the baud rate of your local module.
BAUD_RATE = 9600

PARAM_NODE_ID = "NI"
PARAM_PAN_ID = "ID"
PARAM_DEST_ADDRESS_H = "DH"
PARAM_DEST_ADDRESS_L = "DL"
PARAM_SLEEP_PER ="SP"

PARAM_VALUE_NODE_ID = "Yoda"
PARAM_VALUE_PAN_ID = utils.hex_string_to_bytes("2015")
PARAM_VALUE_DEST_ADDRESS_H = utils.hex_string_to_bytes("00")
PARAM_VALUE_DEST_ADDRESS_L = utils.hex_string_to_bytes("FFFF")

PARAM_VALUE_REMOTE_NODE_ADDR=XBee64BitAddress.from_hex_string("0013A200415BFC59")
PARAM_VALUE_REMOTE_NODE_ID = "Luke"
PARAM_VALUE_REMOTE_NODE_SP=utils.hex_string_to_bytes("1FF")



def main():
    print(" +-----------------------------------------------+")
    print(" | XBee Python Library Set/Get parameters Sample |")
    print(" +-----------------------------------------------+\n")

    local_device = XBeeDevice(PORT, BAUD_RATE)


    try:
        local_device.open()
        remote_device = RemoteZigBeeDevice(local_device, PARAM_VALUE_REMOTE_NODE_ADDR)

        # Set parameters.
        local_device.set_parameter(PARAM_NODE_ID, bytearray(PARAM_VALUE_NODE_ID, 'utf8'))
        local_device.set_parameter(PARAM_PAN_ID, PARAM_VALUE_PAN_ID)
        local_device.set_parameter(PARAM_DEST_ADDRESS_H, PARAM_VALUE_DEST_ADDRESS_H)
        local_device.set_parameter(PARAM_DEST_ADDRESS_L, PARAM_VALUE_DEST_ADDRESS_L)

        # Get parameters.
        print("Node ID:                     %s" % local_device.get_parameter(PARAM_NODE_ID).decode())
        print("PAN ID:                      %s" % utils.hex_to_string(local_device.get_parameter(PARAM_PAN_ID)))
        print("Destination address high:    %s" % utils.hex_to_string(local_device.get_parameter(PARAM_DEST_ADDRESS_H)))
        print("Destination address low:     %s" % utils.hex_to_string(local_device.get_parameter(PARAM_DEST_ADDRESS_L)))

        # Set remote parameters.
        remote_device.set_parameter(PARAM_NODE_ID, bytearray(PARAM_VALUE_REMOTE_NODE_ID, 'utf8'))
        remote_device.set_parameter(PARAM_SLEEP_PER, PARAM_VALUE_REMOTE_NODE_SP)
        remote_device.write_changes() #make changes permanet

        # Get remote parameters.
        print("Remote Node ID:              %s" % remote_device.get_parameter(PARAM_NODE_ID).decode())
        print("Remote Node SP:              %s" % utils.hex_to_string(remote_device.get_parameter(PARAM_SLEEP_PER)))

        print("")
        print("All parameters were set correctly!")

    finally:
        if local_device is not None and local_device.is_open():
            local_device.close()


if __name__ == '__main__':
    main()