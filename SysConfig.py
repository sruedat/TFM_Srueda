import configparser
settings = configparser.ConfigParser()
settings.read("config.ini")


def ReadLocalPortFromFile():
    return settings.get("DEFAULT", "LOCAL_PORT")


def ReadLocalBaudRateFromFile():
    return settings.get("DEFAULT", "LOCAL_PORT_BAUD_RATE")


def main():
    try:
        settings = configparser.ConfigParser()
        settings.read("config.ini")
        ReadLocalPortFromFile()
        ReadLocalBaudRateFromFile()

    except:
        print ("error opening config.ini")



if __name__ == '__main__':
    main()
