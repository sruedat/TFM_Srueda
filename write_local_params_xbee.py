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


from digi.xbee.devices import XBeeDevice
from digi.xbee.util import utils
import read_sys_config
import read_node_config_file
import sys
sys.tracebacklimit = 0

# Parámetros de conexión con el puerto serie al dispositivo local
PORT=read_sys_config.ReadLocalPortFromFile()
BAUD_RATE = read_sys_config.ReadLocalBaudRateFromFile()
node_address="local_node"


def main(NodeAddress):
    print(" +-----------------------------------------------+")
    print(" |           Write Local XBee parameters         |")
    print(" +-----------------------------------------------+\n")



    local_device = XBeeDevice(PORT, BAUD_RATE)


    try:
        local_device.open()
       # Get Hardware Models with extended DIO (P5 to P9)
        Hardware_Extended = read_sys_config.ReadHardwareVersionWhithP5ToP9PinsFromFile()
        HV = utils.hex_to_string(local_device.get_parameter("HV"))
       # Set filne name source of the params
        read_node_config_file.set_path_to_file(NodeAddress)

        # Networking

        local_device.set_parameter("ID", utils.hex_string_to_bytes(read_node_config_file.ReadPanIDFromFile(NodeAddress)))

        local_device.set_parameter("SC", utils.hex_string_to_bytes(read_node_config_file.ReadScanChannelsFromFile(NodeAddress)))
        local_device.set_parameter("SD", utils.hex_string_to_bytes(read_node_config_file.ReadScanDurationFromFile(NodeAddress)))
        local_device.set_parameter("ZS", utils.hex_string_to_bytes(read_node_config_file.ReadZigBeeStackProfileFromFile(NodeAddress)))
        local_device.set_parameter("NJ", utils.hex_string_to_bytes(read_node_config_file.ReadNodeJoinTimeFromFile(NodeAddress)))
        local_device.set_parameter("NW", utils.hex_string_to_bytes(read_node_config_file.ReadNetworkWatchdogTimeoutFromFile(NodeAddress)))
        local_device.set_parameter("JV", utils.hex_string_to_bytes(read_node_config_file.ReadChannelVerificationFromFile(NodeAddress)))
        local_device.set_parameter("JN", utils.hex_string_to_bytes(read_node_config_file.ReadJoinNotificationFromFile(NodeAddress)))
        local_device.set_parameter("CE", utils.hex_string_to_bytes(read_node_config_file.ReadCoordinatorEnableFromFile(NodeAddress)))
        local_device.set_parameter("DO", utils.hex_string_to_bytes(read_node_config_file.ReadDeviceOptionsFromFile(NodeAddress)))
        local_device.set_parameter("DC", utils.hex_string_to_bytes(read_node_config_file.ReadDeviceControlsFromFile(NodeAddress)))
        # Addressing
        local_device.set_parameter("DH", utils.hex_string_to_bytes(read_node_config_file.ReadDestinationAddressHighFromFile(NodeAddress)))
        local_device.set_parameter("DL", utils.hex_string_to_bytes(read_node_config_file.ReadDestinationAddressLowFromFile(NodeAddress)))
        local_device.set_parameter("NI", bytearray(read_node_config_file.ReadNodeIdentifierFromFile(NodeAddress), 'utf8'))
        local_device.set_parameter("NH", utils.hex_string_to_bytes(read_node_config_file.ReadMaximumHopsFromFile(NodeAddress)))
        local_device.set_parameter("BH", utils.hex_string_to_bytes(read_node_config_file.ReadBroadcastRadiusFromFile(NodeAddress)))
        local_device.set_parameter("AR", utils.hex_string_to_bytes(read_node_config_file.ReadManyToOneRouteBroadcastTimeFromFile(NodeAddress)))
        local_device.set_parameter("DD", utils.hex_string_to_bytes(read_node_config_file.ReadDeviceTypeIdentifierFromFile(NodeAddress)))
        local_device.set_parameter("NT", utils.hex_string_to_bytes(read_node_config_file.ReadNodeDiscoveryBackoffFromFile(NodeAddress)))
        local_device.set_parameter("NO", utils.hex_string_to_bytes(read_node_config_file.ReadNodeDiscoveryOptionsFromFile(NodeAddress)))
        local_device.set_parameter("CR", utils.hex_string_to_bytes(read_node_config_file.ReadPanConflictThresholdFromFile(NodeAddress)))
        # ZigBee Addressing
        local_device.set_parameter("SE", utils.hex_string_to_bytes(read_node_config_file.ReadZigBeeSourceEndPointFromFile(NodeAddress)))
        local_device.set_parameter("DE", utils.hex_string_to_bytes(read_node_config_file.ReadZigBeeDestinationEndpointFromFile(NodeAddress)))
        local_device.set_parameter("CI", utils.hex_string_to_bytes(read_node_config_file.ReadZigBeeClusterIDFromFile(NodeAddress)))
        local_device.set_parameter("TO", utils.hex_string_to_bytes(read_node_config_file.ReadTransmitOptionsFromFile(NodeAddress)))
        # RF Interfacing
        local_device.set_parameter("PL", utils.hex_string_to_bytes(read_node_config_file.ReadTxPowerLevelFromFile(NodeAddress)))
        local_device.set_parameter("PM", utils.hex_string_to_bytes(read_node_config_file.ReadPowerModeFromFile(NodeAddress)))
        # Security
        local_device.set_parameter("EE", utils.hex_string_to_bytes(read_node_config_file.ReadEncryptionEnableFromFile(NodeAddress)))
        local_device.set_parameter("EO", utils.hex_string_to_bytes(read_node_config_file.ReadEncryptionOptionsFromFile(NodeAddress)))
        local_device.set_parameter("KY", utils.hex_string_to_bytes(read_node_config_file.ReadEncryptionKeyFromFile(NodeAddress)))
        local_device.set_parameter("NK", utils.hex_string_to_bytes(read_node_config_file.ReadNetworkEncryptionKeyFromFile(NodeAddress)))
        # Serial Interfacing
        local_device.set_parameter("BD", utils.hex_string_to_bytes(read_node_config_file.ReadBaudRateFromFile(NodeAddress)))
        local_device.set_parameter("NB", utils.hex_string_to_bytes(read_node_config_file.ReadParityFromFile(NodeAddress)))
        local_device.set_parameter("SB", utils.hex_string_to_bytes(read_node_config_file.ReadStopBitsFromFile(NodeAddress)))
        local_device.set_parameter("RO", utils.hex_string_to_bytes(read_node_config_file.ReadPacketizationTimeoutFromFile(NodeAddress)))
        local_device.set_parameter("D6", utils.hex_string_to_bytes(read_node_config_file.ReadDIO6ConfigurationFromFile(NodeAddress)))
        local_device.set_parameter("D7", utils.hex_string_to_bytes(read_node_config_file.ReadDIO7ConfigurationFromFile(NodeAddress)))
        local_device.set_parameter("AP", utils.hex_string_to_bytes(read_node_config_file.ReadApiEnableFromFile(NodeAddress)))
        local_device.set_parameter("AO", utils.hex_string_to_bytes(read_node_config_file.ReadApiOutputModeFromFile(NodeAddress)))
        # AT Command Options
        local_device.set_parameter("CT", utils.hex_string_to_bytes(read_node_config_file.ReadATCommandModeTimeoutFromFile(NodeAddress)))
        local_device.set_parameter("GT", utils.hex_string_to_bytes(read_node_config_file.ReadGuardTimesFromFile(NodeAddress)))
        local_device.set_parameter("CC", utils.hex_string_to_bytes(read_node_config_file.ReadCommandSequenceCharacterFromFile(NodeAddress)))
        # Sleep Modes
        local_device.set_parameter("SP", utils.hex_string_to_bytes(read_node_config_file.ReadCyclicSleepPeriodFromFile(NodeAddress)))
        local_device.set_parameter("SN", utils.hex_string_to_bytes(read_node_config_file.ReadNumberOfCyclicSleepPeriodsFromFile(NodeAddress)))
        local_device.set_parameter("SM", utils.hex_string_to_bytes(read_node_config_file.ReadSleepModeFromFile(NodeAddress)))
        local_device.set_parameter("ST", utils.hex_string_to_bytes(read_node_config_file.ReadTimeBeforeSleepFromFile(NodeAddress)))
        local_device.set_parameter("SO", utils.hex_string_to_bytes(read_node_config_file.ReadSleepOptionsFromFile(NodeAddress)))
        local_device.set_parameter("WH", utils.hex_string_to_bytes(read_node_config_file.ReadWakeHostFromFile(NodeAddress)))
        local_device.set_parameter("PO", utils.hex_string_to_bytes(read_node_config_file.ReadPollRateFromFile(NodeAddress)))
        # I/O Settings
        local_device.set_parameter("D0", utils.hex_string_to_bytes(read_node_config_file.ReadDIO0AD0ConfigurationFromFile(NodeAddress)))
        local_device.set_parameter("D1", utils.hex_string_to_bytes(read_node_config_file.ReadDIO1AD1ConfigurationFromFile(NodeAddress)))
        local_device.set_parameter("D2", utils.hex_string_to_bytes(read_node_config_file.ReadDIO2AD2ConfigurationFromFile(NodeAddress)))
        local_device.set_parameter("D3", utils.hex_string_to_bytes(read_node_config_file.ReadDIO3AD3ConfigurationFromFile(NodeAddress)))
        local_device.set_parameter("D4", utils.hex_string_to_bytes(read_node_config_file.ReadDIO4ConfigurationFromFile(NodeAddress)))
        local_device.set_parameter("D5", utils.hex_string_to_bytes(read_node_config_file.ReadDIO5ConfigurationFromFile(NodeAddress)))
        local_device.set_parameter("D8", utils.hex_string_to_bytes(read_node_config_file.ReadDIO8ConfigurationFromFile(NodeAddress)))
        local_device.set_parameter("D9", utils.hex_string_to_bytes(read_node_config_file.ReadDIO9ConfigurationFromFile(NodeAddress)))
        local_device.set_parameter("P0", utils.hex_string_to_bytes(read_node_config_file.ReadDIO10ConfigurationFromFile(NodeAddress)))
        local_device.set_parameter("P1", utils.hex_string_to_bytes(read_node_config_file.ReadDIO11ConfigurationFromFile(NodeAddress)))
        local_device.set_parameter("P2", utils.hex_string_to_bytes(read_node_config_file.ReadDIO12ConfigurationFromFile(NodeAddress)))
        local_device.set_parameter("P3", utils.hex_string_to_bytes(read_node_config_file.ReadDIO13ConfigurationFromFile(NodeAddress)))
        local_device.set_parameter("P4", utils.hex_string_to_bytes(read_node_config_file.ReadDIO14ConfigurationFromFile(NodeAddress)))
        if HV == Hardware_Extended:
            local_device.set_parameter("P5", utils.hex_string_to_bytes(read_node_config_file.ReadDIO15ConfigurationFromFile(NodeAddress)))
            local_device.set_parameter("P6", utils.hex_string_to_bytes(read_node_config_file.ReadDIO16ConfigurationFromFile(NodeAddress)))
            local_device.set_parameter("P7", utils.hex_string_to_bytes(read_node_config_file.ReadDIO17ConfigurationFromFile(NodeAddress)))
            local_device.set_parameter("P8", utils.hex_string_to_bytes(read_node_config_file.ReadDIO18ConfigurationFromFile(NodeAddress)))
            local_device.set_parameter("P9", utils.hex_string_to_bytes(read_node_config_file.ReadDIO19ConfigurationFromFile(NodeAddress)))
        local_device.set_parameter("PR", utils.hex_string_to_bytes(read_node_config_file.ReadPullUpResistorEnableFromFile(NodeAddress)))
        local_device.set_parameter("PD", utils.hex_string_to_bytes(read_node_config_file.ReadPullUpDownDirectionFromFile(NodeAddress)))
        local_device.set_parameter("LT", utils.hex_string_to_bytes(read_node_config_file.ReadAssociatedLedBlinkTimeFromFile(NodeAddress)))
        local_device.set_parameter("RP", utils.hex_string_to_bytes(read_node_config_file.ReadRssiPwmTimerFromFile(NodeAddress)))
        # I/O Sampling
        local_device.set_parameter("IR", utils.hex_string_to_bytes(read_node_config_file.ReadIOSamplingRateFromFile(NodeAddress)))
        local_device.set_parameter("IC", utils.hex_string_to_bytes(read_node_config_file.ReadDigitalIOChangeDetectionFromFile(NodeAddress)))
        local_device.set_parameter("V+", utils.hex_string_to_bytes(read_node_config_file.ReadSupplyVoltageHihgThresholdFromFile(NodeAddress)))

        # Make params permanent
        local_device.write_changes()  # make changes permanet


        #print parameters
        print("  Success!! All Parameters Were Written  ")
        log = "  Success!! All Parameters Were Written  \n\n"

    except:
        log = "  Sorry, an error has happened during writting operation\n"
        if local_device.is_open():
            local_device.close()
        pass


    finally:
        if local_device is not None and local_device.is_open():
            local_device.close()
        else:
            log = "  No local device found\n"

    return log

if __name__ == '__main__':
    main(node_address)