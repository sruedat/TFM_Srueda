# Sergio Rueda Teruel. 2018
# Este software ha sido desarrollado para el trabajo fin de máster de la titulación
# Máster Universitario en Ingeniería de Telecomunicación UOC-URL de la
# Universidad Oberta de Catalunya y lleva por título
# "Diseño de una WSN para la estimación del seeing de la cúpula D080,
# en el Observatorio Astrofísico de Javalambre."
# Este código está sometido a licencia de Reconocimiento-NoComercial-CompartirIgual
# 3.0 España de Creative Commons.

# Este módulo incorpora una serie de funciones que son llamadas por otros módulos para
# la lectura de los parámetros de configuración desde unos archivos tipo ini.
# Existirá uno de estos archivos ini por nodo que queramos configurar, y el módulo de
# configuración utilizará las funciones aquí desarrolladas para parsear los datos del
# fichero a valores que pueda utilizar en la configuración



import configparser

config_file = "config/"
settings = configparser.ConfigParser()




def set_path_to_file(path):
    global config_file
    config_file = "config/" + path +".ini"
    settings.read(config_file)




# Obtenemos del fichero de configuración los valores para cada parámetro
# Networking
def ReadPanIDFromFile(Address):
    return settings.get(Address, "ID")


def ReadScanChannelsFromFile(Address):
    print ("aqui")
    return settings.get(Address, "SC")


def ReadScanDurationFromFile(Address):
    return settings.get(Address, "SD")


def ReadZigBeeStackProfileFromFile(Address):
    return settings.get(Address, "ZS")


def ReadNodeJoinTimeFromFile(Address):
    return settings.get(Address, "NJ")


def ReadNetworkWatchdogTimeoutFromFile(Address):
    return settings.get(Address, "NW")


def ReadChannelVerificationFromFile(Address):
    return settings.get(Address, "JV")


def ReadJoinNotificationFromFile(Address):
    return settings.get(Address, "JN")


def ReadCoordinatorEnableFromFile(Address):
    return settings.get(Address, "CE")


def ReadDeviceOptionsFromFile(Address):
    return settings.get(Address, "DO")


def ReadDeviceControlsFromFile(Address):
    return settings.get(Address, "DC")


# Addressing
def ReadDestinationAddressHighFromFile(Address):
    return settings.get(Address, "DH")


def ReadDestinationAddressLowFromFile(Address):
    return settings.get(Address, "DL")


def ReadNodeIdentifierFromFile(Address):
    return settings.get(Address, "NI")


def ReadMaximumHopsFromFile(Address):
    return settings.get(Address, "NH")


def ReadBroadcastRadiusFromFile(Address):
    return settings.get(Address, "BH")


def ReadManyToOneRouteBroadcastTimeFromFile(Address):
    return settings.get(Address, "AR")


def ReadDeviceTypeIdentifierFromFile(Address):
    return settings.get(Address, "DD")


def ReadNodeDiscoveryBackoffFromFile(Address):
    return settings.get(Address, "NT")


def ReadNodeDiscoveryOptionsFromFile(Address):
    return settings.get(Address, "NO")


def ReadPanConflictThresholdFromFile(Address):
    return settings.get(Address, "CR")


# ZigBee Addressing
def ReadZigBeeSourceEndPointFromFile(Address):
    return settings.get(Address, "SE")


def ReadZigBeeDestinationEndpointFromFile(Address):
    return settings.get(Address, "DE")


def ReadZigBeeClusterIDFromFile(Address):
    return settings.get(Address, "CI")


def ReadTransmitOptionsFromFile(Address):
    return settings.get(Address, "TO")


# RF Interfacing
def ReadTxPowerLevelFromFile(Address):
    return settings.get(Address, "PL")


def ReadPowerModeFromFile(Address):
    return settings.get(Address, "PM")


# Security
def ReadEncryptionEnableFromFile(Address):
    return settings.get(Address, "EE")


def ReadEncryptionOptionsFromFile(Address):
    return settings.get(Address, "EO")


def ReadEncryptionKeyFromFile(Address):
    return settings.get(Address, "KY")


def ReadNetworkEncryptionKeyFromFile(Address):
    return settings.get(Address, "NK")


# Serial Interfacing
def ReadBaudRateFromFile(Address):
    return settings.get(Address, "BD")


def ReadParityFromFile(Address):
    return settings.get(Address, "NB")


def ReadStopBitsFromFile(Address):
    return settings.get(Address, "SB")


def ReadPacketizationTimeoutFromFile(Address):
    return settings.get(Address, "RO")


def ReadDIO6ConfigurationFromFile(Address):
    return settings.get(Address, "D6")


def ReadDIO7ConfigurationFromFile(Address):
    return settings.get(Address, "D7")


def ReadApiEnableFromFile(Address):
    return settings.get(Address, "AP")


def ReadApiOutputModeFromFile(Address):
    return settings.get(Address, "AO")


# AT Command
def ReadATCommandModeTimeoutFromFile(Address):
    return settings.get(Address, "CT")


def ReadGuardTimesFromFile(Address):
    return settings.get(Address, "GT")


def ReadCommandSequenceCharacterFromFile(Address):
    return settings.get(Address, "CC")


# Sleep Modes
def ReadCyclicSleepPeriodFromFile(Address):
    return settings.get(Address, "SP")


def ReadNumberOfCyclicSleepPeriodsFromFile(Address):
    return settings.get(Address, "SN")


def ReadSleepModeFromFile(Address):
    return settings.get(Address, "SM")


def ReadTimeBeforeSleepFromFile(Address):
    return settings.get(Address, "ST")


def ReadSleepOptionsFromFile(Address):
    return settings.get(Address, "SO")


def ReadWakeHostFromFile(Address):
    return settings.get(Address, "WH")


def ReadPollRateFromFile(Address):
    return settings.get(Address, "PO")


# I/O Settings
def ReadDIO0AD0ConfigurationFromFile(Address):
    return settings.get(Address, "D0")


def ReadDIO1AD1ConfigurationFromFile(Address):
    return settings.get(Address, "D1")


def ReadDIO2AD2ConfigurationFromFile(Address):
    return settings.get(Address, "D2")


def ReadDIO3AD3ConfigurationFromFile(Address):
    return settings.get(Address, "D3")


def ReadDIO4ConfigurationFromFile(Address):
    return settings.get(Address, "D4")


def ReadDIO5ConfigurationFromFile(Address):
    return settings.get(Address, "D5")


def ReadDIO8ConfigurationFromFile(Address):
    return settings.get(Address, "D8")


def ReadDIO9ConfigurationFromFile(Address):
    return settings.get(Address, "D9")


def ReadDIO10ConfigurationFromFile(Address):
    return settings.get(Address, "P0")


def ReadDIO11ConfigurationFromFile(Address):
    return settings.get(Address, "P1")


def ReadDIO12ConfigurationFromFile(Address):
    return settings.get(Address, "P2")


def ReadDIO13ConfigurationFromFile(Address):
    return settings.get(Address, "P3")


def ReadDIO14ConfigurationFromFile(Address):
    return settings.get(Address, "P4")

def ReadDIO15ConfigurationFromFile(Address):
    return settings.get(Address, "P5")

def ReadDIO16ConfigurationFromFile(Address):
    return settings.get(Address, "P6")

def ReadDIO17ConfigurationFromFile(Address):
    return settings.get(Address, "P7")

def ReadDIO18ConfigurationFromFile(Address):
    return settings.get(Address, "P8")

def ReadDIO19ConfigurationFromFile(Address):
    return settings.get(Address, "P9")


def ReadPullUpResistorEnableFromFile(Address):
    return settings.get(Address, "PR")


def ReadPullUpDownDirectionFromFile(Address):
    return settings.get(Address, "PD")


def ReadAssociatedLedBlinkTimeFromFile(Address):
    return settings.get(Address, "LT")


def ReadRssiPwmTimerFromFile(Address):
    return settings.get(Address, "RP")

# I/O Sampling
def ReadIOSamplingRateFromFile(Address):
    return settings.get(Address, "IR")


def ReadDigitalIOChangeDetectionFromFile(Address):
    return settings.get(Address, "IC")


def ReadSupplyVoltageHihgThresholdFromFile(Address):
    return settings.get(Address, "V+")



def main():
    try:
        settings.read(config_file)

    except:
        print("error opening config.ini")


if __name__ == '__main__':
    main()
