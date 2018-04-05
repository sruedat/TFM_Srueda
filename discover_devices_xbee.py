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

import time, sys
from digi.xbee.util import utils


from digi.xbee.models.status import NetworkDiscoveryStatus
from digi.xbee.devices import XBeeDevice
sys.tracebacklimit = 0

# TODO: Replace with the serial port where your local module is connected to.
PORT = "COM6"
# TODO: Replace with the baud rate of your local module.
BAUD_RATE = 9600
log=""


def passlog():
    global log
    time.sleep(0.2)
    return log

def main():
    global log
    print(" +---------------------------------------------+")
    print(" | XBee Python Library Discover Devices Sample |")
    print(" +---------------------------------------------+\n")
    device = XBeeDevice(PORT, BAUD_RATE)
    log =""
    try:
        device.open()

        xbee_network = device.get_network()

        xbee_network.set_discovery_timeout(15)  # 15 seconds.

        xbee_network.clear()

        # Callback for discovered devices.
        def callback_device_discovered(remote):
            global log
            #print("Device discovered:\n" + "%s" % remote)
            log =log+"Device discovered:\n" + "%s" % remote +"\n\n"







        # Callback for discovery finished.
        def callback_discovery_finished(status):
            global log
            if status == NetworkDiscoveryStatus.SUCCESS:
                #print("\n"+"Discovery process finished successfully.")
                log=log+"Discovery process finished successfully.\n"
            else:
                #print("There was an error discovering devices: %s" % status.description)
                log= log+"There was an error discovering devices: %s\n" % status.description



        xbee_network.add_device_discovered_callback(callback_device_discovered)

        xbee_network.add_discovery_process_finished_callback(callback_discovery_finished)

        xbee_network.start_discovery_process()

        #print("Discovering remote XBee devices...")
        log = "\nDiscovering remote XBee devices...\n\n"


        while xbee_network.is_discovery_running():
            passlog()
            time.sleep(0.1)








    except:
        if device.is_open():
            device.close()
        pass

    finally:
        if device is not None and device.is_open():
            device.close()

    state=1
    return state




if __name__ == '__main__':
    main()


