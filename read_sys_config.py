# Copyright 2018, Sergio Rueda.
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


import configparser

CONFIG_FILE = "config/sys_config.ini"

settings = configparser.ConfigParser()
settings.read(CONFIG_FILE)



def ReadHardwareVersionWhithP5ToP9PinsFromFile():
    return settings.get("COMMON", "HARDWARE_VERSION_WITH_P5_TO_P9")

def ReadLocalPortFromFile():
    return settings.get("COMMON", "PORT")


def ReadLocalBaudRateFromFile():
    return settings.get("COMMON", "PORT_BAUD_RATE")



def main():
    try:
        settings.read(CONFIG_FILE)

    except:
        print("error openning config.ini")


if __name__ == '__main__':
    main()




