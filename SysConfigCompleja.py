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

settings = configparser.ConfigParser()
settings.read("config.ini")

def ReadHardwareVersionWhithP5ToP9PinsFromFile():
    return settings.get("COMMON", "HARDWARE_VERSION_WITH_P5_TO_P9")

def ReadLocalPortFromFile():
    return settings.get("LOCAL_NODE", "PORT")


def ReadLocalBaudRateFromFile():
    return settings.get("LOCAL_NODE", "PORT_BAUD_RATE")


# Obtenemos del fichero de configuración el acrónimo del comando para obtener los datos
# Networking
def ReadPanIDCmdFromFile():
    return settings.get("PARAMS", "PAN_ID")


def ReadScanChannelsCmdFromFile():
    return settings.get("PARAMS", "SCAN_CHANNELS")


def ReadScanDurationCmdFromFile():
    return settings.get("PARAMS", "SCAN_DURATION")


def ReadZigBeeStackProfileCmdFromFile():
    return settings.get("PARAMS", "ZIGBEE_STACK_PROFILE")


def ReadNodeJoinTimeCmdFromFile():
    return settings.get("PARAMS", "NODE_JOIN_TIME")


def ReadNetworkWatchdogTimeoutCmdFromFile():
    return settings.get("PARAMS", "NETWORK_WATCHDOG_TIMEOUT")


def ReadChannelVerificationCmdFromFile():
    return settings.get("PARAMS", "CHANNEL_VERIFICATION")


def ReadJoinNotificationCmdFromFile():
    return settings.get("PARAMS", "JOIN_NOTIFICATION")


def ReadOperatingPanIdCmdFromFile():
    return settings.get("PARAMS", "OPERATING_PAN_ID")


def ReadOperating16BitPanIdCmdFromFile():
    return settings.get("PARAMS", "OPERATING_16_BIT_PAN_ID")


def ReadOperatingChannelCmdFromFile():
    return settings.get("PARAMS", "OPERATING_CHANNEL")


def ReadNumberOfRemainingChildrenCmdFromFile():
    return settings.get("PARAMS", "NUMBER_OF_REMAINING_CHILDREN")


def ReadCoordinatorEnableCmdFromFile():
    return settings.get("PARAMS", "COORDINATOR_ENABLE")


def ReadDeviceOptionsCmdFromFile():
    return settings.get("PARAMS", "DEVICE_OPTIONS")


def ReadDeviceControlsCmdFromFile():
    return settings.get("PARAMS", "DEVICE_CONTROLS")


# Addressing
def ReadSerialNumberHighCmdFromFile():
    return settings.get("PARAMS", "SERIAL_NUMBER_HIGH")


def ReadSerialNumberLowCmdFromFile():
    return settings.get("PARAMS", "SERIAL_NUMBER_LOW")


def Read16BitNetworkAddressCmdFromFile():
    return settings.get("PARAMS", "16_BIT_NETWORK_ADDRESS")


def Read16BitParentAddressCmdFromFile():
    return settings.get("PARAMS", "16_BIT_PARENT_ADDRESS")


def ReadDestinationAddressHighCmdFromFile():
    return settings.get("PARAMS", "DESTINATION_ADDRESS_HIGH")


def ReadDestinationAddressLowCmdFromFile():
    return settings.get("PARAMS", "DESTINATION_ADDRESS_LOW")


def ReadNodeIdentifierCmdFromFile():
    return settings.get("PARAMS", "NODE_IDENTIFIER")


def ReadMaximumHopsCmdFromFile():
    return settings.get("PARAMS", "MAXIMUM_HOPS")


def ReadBroadcastRadiusCmdFromFile():
    return settings.get("PARAMS", "BROADCAST_RADIUS")


def ReadManyToOneRouteBroadcastTimeCmdFromFile():
    return settings.get("PARAMS", "MANY_TO_ONE_ROUTE_BROADCAST_TIME")


def ReadDeviceTypeIdentifierCmdFromFile():
    return settings.get("PARAMS", "DEVICE_TYPE_IDENTIFIER")


def ReadNodeDiscoveryBackoffCmdFromFile():
    return settings.get("PARAMS", "NODE_DISCOVERY_BACKOFF")


def ReadNodeDiscoveryOptionsCmdFromFile():
    return settings.get("PARAMS", "NODE_DISCOVERY_OPTIONS")


def ReadMaximumNumberOfTransmissionBytesCmdFromFile():
    return settings.get("PARAMS", "MAXIMUM_NUMBER_OF_TRANSMISSION_BYTES")


def ReadPanConflictThresholdCmdFromFile():
    return settings.get("PARAMS", "PAN_CONFLICT_THRESHOLD")


# ZigBee Addressing
def ReadZigBeeSourceEndPointCmdFromFile():
    return settings.get("PARAMS", "ZIGBEE_SOURCE_ENDPOINT")


def ReadZigBeeDestinationEndpointCmdFromFile():
    return settings.get("PARAMS", "ZIGBEE_DESTINATION_ENDPOINT")


def ReadZigBeeClusterIDCmdFromFile():
    return settings.get("PARAMS", "ZIGBEE_CLUSTER_ID")


def ReadTransmitOptionsCmdFromFile():
    return settings.get("PARAMS", "TRANSMIT_OPTIONS")


# RF Interfacing
def ReadTxPowerLevelCmdFromFile():
    return settings.get("PARAMS", "TX_POWER_LEVEL")


def ReadPowerModeCmdFromFile():
    return settings.get("PARAMS", "POWER_MODE")


def ReadPowerAtPL4CmdFromFile():
    return settings.get("PARAMS", "POWER_AT_PL4")


# Security
def ReadEncryptionEnableCmdFromFile():
    return settings.get("PARAMS", "ENCRYPTION_ENABLE")


def ReadEncryptionOptionsCmdFromFile():
    return settings.get("PARAMS", "ENCRYPTION_OPTIONS")


def ReadEncryptionKeyCmdFromFile():
    return settings.get("PARAMS", "ENCRYPTION_KEY")


def ReadNetworkEncryptionKeyCmdFromFile():
    return settings.get("PARAMS", "NETWORK_ENCRYPTION_KEY")


# Serial Interfacing
def ReadBaudRateCmdFromFile():
    return settings.get("PARAMS", "BAUD_RATE")


def ReadParityCmdFromFile():
    return settings.get("PARAMS", "PARITY")


def ReadStopBitsCmdFromFile():
    return settings.get("PARAMS", "STOP_BITS")


def ReadPacketizationTimeoutCmdFromFile():
    return settings.get("PARAMS", "PACKETIZATION_TIMEOUT")


def ReadDIO6ConfigurationCmdFromFile():
    return settings.get("PARAMS", "DI06_CONFIGURATION")


def ReadDIO7ConfigurationCmdFromFile():
    return settings.get("PARAMS", "DI07_CONFIGURATION")


def ReadApiEnableCmdFromFile():
    return settings.get("PARAMS", "API_ENABLE")


def ReadApiOutputModeCmdFromFile():
    return settings.get("PARAMS", "API_OUTPUT_MODE")


# AT Command
def ReadATCommandModeTimeoutCmdFromFile():
    return settings.get("PARAMS", "AT_COMMAND_MODE_TIMEOUT")


def ReadGuardTimesCmdFromFile():
    return settings.get("PARAMS", "GUARD_TIMES")


def ReadCommandSequenceCharacterCmdFromFile():
    return settings.get("PARAMS", "COMMAND_SEQUENCE_CHARACTER")


# Sleep Modes
def ReadCyclicSleepPeriodCmdFromFile():
    return settings.get("PARAMS", "CYCLIC_SLEEP_PERIOD")


def ReadNumberOfCyclicSleepPeriodsCmdFromFile():
    return settings.get("PARAMS", "NUMBER_OF_CYCLIC_SLEEP_PERIODS")


def ReadSleepModeCmdFromFile():
    return settings.get("PARAMS", "SLEEP_MODE")


def ReadTimeBeforeSleepCmdFromFile():
    return settings.get("PARAMS", "TIME_BEFORE_SLEEP")


def ReadSleepOptionsCmdFromFile():
    return settings.get("PARAMS", "SLEEP_OPTIONS")


def ReadWakeHostCmdFromFile():
    return settings.get("PARAMS", "WAKE_HOST")


def ReadPollRateCmdFromFile():
    return settings.get("PARAMS", "POLL_RATE")


# I/O Settings
def ReadDIO0AD0ConfigurationCmdFromFile():
    return settings.get("PARAMS", "DIO0_AD0_CONFIGURATION")


def ReadDIO1AD1ConfigurationCmdFromFile():
    return settings.get("PARAMS", "DIO1_AD1_CONFIGURATION")


def ReadDIO2AD2ConfigurationCmdFromFile():
    return settings.get("PARAMS", "DIO2_AD2_CONFIGURATION")


def ReadDIO3AD3ConfigurationCmdFromFile():
    return settings.get("PARAMS", "DIO3_AD3_CONFIGURATION")


def ReadDIO4ConfigurationCmdFromFile():
    return settings.get("PARAMS", "DIO4_AD4_CONFIGURATION")


def ReadDIO5ConfigurationCmdFromFile():
    return settings.get("PARAMS", "DIO5_CONFIGURATION")


def ReadDIO8ConfigurationCmdFromFile():
    return settings.get("PARAMS", "DIO8_CONFIGURATION")


def ReadDIO9ConfigurationCmdFromFile():
    return settings.get("PARAMS", "DIO9_CONFIGURATION")


def ReadDIO10ConfigurationCmdFromFile():
    return settings.get("PARAMS", "DIO10_CONFIGURATION")


def ReadDIO11ConfigurationCmdFromFile():
    return settings.get("PARAMS", "DIO11_CONFIGURATION")


def ReadDIO12ConfigurationCmdFromFile():
    return settings.get("PARAMS", "DIO12_CONFIGURATION")


def ReadDIO13ConfigurationCmdFromFile():
    return settings.get("PARAMS", "DIO13_CONFIGURATION")


def ReadDIO14ConfigurationCmdFromFile():
    return settings.get("PARAMS", "DIO14_CONFIGURATION")

def ReadDIO15ConfigurationCmdFromFile():
    return settings.get("PARAMS", "DIO15_CONFIGURATION")

def ReadDIO16ConfigurationCmdFromFile():
    return settings.get("PARAMS", "DIO16_CONFIGURATION")

def ReadDIO17ConfigurationCmdFromFile():
    return settings.get("PARAMS", "DIO17_CONFIGURATION")

def ReadDIO18ConfigurationCmdFromFile():
    return settings.get("PARAMS", "DIO18_CONFIGURATION")

def ReadDIO19ConfigurationCmdFromFile():
    return settings.get("PARAMS", "DIO19_CONFIGURATION")


def ReadPullUpResistorEnableCmdFromFile():
    return settings.get("PARAMS", "PULL_UP_RESISTOR_ENABLE")


def ReadPullUpDownDirectionCmdFromFile():
    return settings.get("PARAMS", "PULL_UP_DOWN_DIRECTION")


def ReadAssociatedLedBlinkTimeCmdFromFile():
    return settings.get("PARAMS", "ASSOCIATED_LED_BLINK_TIME")


def ReadRssiPwmTimerCmdFromFile():
    return settings.get("PARAMS", "RSSI_PWM_TIMER")

# I/O Sampling
def ReadIOSamplingRateCmdFromFile():
    return settings.get("PARAMS", "IO_SAMPLING_RATE")


def ReadDigitalIOChangeDetectionCmdFromFile():
    return settings.get("PARAMS", "DIGITAL_IO_CHANGE_DETECTION")


def ReadSupplyVoltageHihgThresholdCmdFromFile():
    return settings.get("PARAMS", "SUPPLY_VOLTAGE_HIGH_THRESHOLD")

# Diagnostic Commands
def ReadFirmwareVersionCmdFromFile():
    return settings.get("PARAMS", "FIRMWARE_VERSION")


def ReadHardwareVersionCmdFromFile():
    return settings.get("PARAMS", "HARDWARE_VERSION")


def ReadAssociationIndicationCmdFromFile():
    return settings.get("PARAMS", "ASSOCIATION_INDICATION")


def ReadRSSIOfLastPacketCmdFromFile():
    return settings.get("PARAMS", "RSSI_OF_LAST_PACKET")


def ReadSupplyVotageCmdFromFile():
    return settings.get("PARAMS", "SUPPLY_VOLTAGE")



def main():
    try:
        settings = configparser.ConfigParser()
        settings.read("config.ini")

    except:
        print("error opening config.ini")


if __name__ == '__main__':
    main()
