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
from digi.xbee.devices import RemoteZigBeeDevice
from digi.xbee.util import utils
from digi.xbee.models.address import XBee64BitAddress
import read_sys_config
import read_node_config_file
import sys
sys.tracebacklimit = 0

# Parámetros de conexión con el puerto serie al dispositivo local
PORT=read_sys_config.ReadLocalPortFromFile()
BAUD_RATE = read_sys_config.ReadLocalBaudRateFromFile()

REMOTE_1 = "0013A200416299FE"


def main(Node_Address):

    NodeAddress = XBee64BitAddress.from_hex_string(Node_Address)

    print(" +-------------------------------------------------------+")
    print(" |  Write Remote XBee (" +Node_Address+ ") parameters      |")
    print(" +---------------------------------------------------- --+\n")

    local_device = XBeeDevice(PORT, BAUD_RATE)
    local_device.open()
    remote_device = RemoteZigBeeDevice(local_device, NodeAddress)

    try:


        # Get Hardware Models with extended DIO (P5 to P9)
        Hardware_Extended = read_sys_config.ReadHardwareVersionWhithP5ToP9PinsFromFile()
        HV = utils.hex_to_string(remote_device.get_parameter("HV"))
        # Set file name source of the params
        print("0013A200416299FE")
        read_node_config_file.set_path_to_file(Node_Address)
        #No se puede modificar la PAN ID vía RF porque se pierde conexión
        #remote_device.set_parameter("ID",utils.hex_string_to_bytes(SysConfig.ReadScanChannelsFromFile(Node_Address)))

        print(read_node_config_file.ReadScanChannelsFromFile(Node_Address))
        remote_device.set_parameter("SC", utils.hex_string_to_bytes(read_node_config_file.ReadScanChannelsFromFile(Node_Address)))
        remote_device.set_parameter("SD", utils.hex_string_to_bytes(read_node_config_file.ReadScanDurationFromFile(Node_Address)))
        remote_device.set_parameter("ZS", utils.hex_string_to_bytes(read_node_config_file.ReadZigBeeStackProfileFromFile(Node_Address)))
        remote_device.set_parameter("NJ", utils.hex_string_to_bytes(read_node_config_file.ReadNodeJoinTimeFromFile(Node_Address)))
        remote_device.set_parameter("NW", utils.hex_string_to_bytes(read_node_config_file.ReadNetworkWatchdogTimeoutFromFile(Node_Address)))
        remote_device.set_parameter("JV", utils.hex_string_to_bytes(read_node_config_file.ReadChannelVerificationFromFile(Node_Address)))
        remote_device.set_parameter("JN", utils.hex_string_to_bytes(read_node_config_file.ReadJoinNotificationFromFile(Node_Address)))
        remote_device.set_parameter("CE", utils.hex_string_to_bytes(read_node_config_file.ReadCoordinatorEnableFromFile(Node_Address)))
        remote_device.set_parameter("DO", utils.hex_string_to_bytes(read_node_config_file.ReadDeviceOptionsFromFile(Node_Address)))
        remote_device.set_parameter("DC", utils.hex_string_to_bytes(read_node_config_file.ReadDeviceControlsFromFile(Node_Address)))
        # Addressing
        remote_device.set_parameter("DH", utils.hex_string_to_bytes(read_node_config_file.ReadDestinationAddressHighFromFile(Node_Address)))
        remote_device.set_parameter("DL", utils.hex_string_to_bytes(read_node_config_file.ReadDestinationAddressLowFromFile(Node_Address)))
        remote_device.set_parameter("NI", bytearray(read_node_config_file.ReadNodeIdentifierFromFile(Node_Address), 'utf8'))
        remote_device.set_parameter("NH", utils.hex_string_to_bytes(read_node_config_file.ReadMaximumHopsFromFile(Node_Address)))
        remote_device.set_parameter("BH", utils.hex_string_to_bytes(read_node_config_file.ReadBroadcastRadiusFromFile(Node_Address)))
        remote_device.set_parameter("AR", utils.hex_string_to_bytes(read_node_config_file.ReadManyToOneRouteBroadcastTimeFromFile(Node_Address)))
        remote_device.set_parameter("DD", utils.hex_string_to_bytes(read_node_config_file.ReadDeviceTypeIdentifierFromFile(Node_Address)))
        remote_device.set_parameter("NT", utils.hex_string_to_bytes(read_node_config_file.ReadNodeDiscoveryBackoffFromFile(Node_Address)))
        remote_device.set_parameter("NO", utils.hex_string_to_bytes(read_node_config_file.ReadNodeDiscoveryOptionsFromFile(Node_Address)))
        remote_device.set_parameter("CR", utils.hex_string_to_bytes(read_node_config_file.ReadPanConflictThresholdFromFile(Node_Address)))
        # ZigBee Addressing
        remote_device.set_parameter("SE", utils.hex_string_to_bytes(read_node_config_file.ReadZigBeeSourceEndPointFromFile(Node_Address)))
        remote_device.set_parameter("DE", utils.hex_string_to_bytes(read_node_config_file.ReadZigBeeDestinationEndpointFromFile(Node_Address)))
        remote_device.set_parameter("CI", utils.hex_string_to_bytes(read_node_config_file.ReadZigBeeClusterIDFromFile(Node_Address)))
        remote_device.set_parameter("TO", utils.hex_string_to_bytes(read_node_config_file.ReadTransmitOptionsFromFile(Node_Address)))
        # RF Interfacing
        remote_device.set_parameter("PL", utils.hex_string_to_bytes(read_node_config_file.ReadTxPowerLevelFromFile(Node_Address)))
        remote_device.set_parameter("PM", utils.hex_string_to_bytes(read_node_config_file.ReadPowerModeFromFile(Node_Address)))
        # Security
        remote_device.set_parameter("EE", utils.hex_string_to_bytes(read_node_config_file.ReadEncryptionEnableFromFile(Node_Address)))
        remote_device.set_parameter("EO", utils.hex_string_to_bytes(read_node_config_file.ReadEncryptionOptionsFromFile(Node_Address)))
        # No se pueden cambiar las keys vía RF
        #remote_device.set_parameter("KY",utils.hex_string_to_bytes(SysConfig.ReadEncryptionKeyFromFile(Node_Address)))
        #remote_device.set_parameter("NK",utils.hex_string_to_bytes(SysConfig.ReadNetworkEncryptionKeyFromFile(Node_Address)))
        # Serial Interfacing
        remote_device.set_parameter("BD", utils.hex_string_to_bytes(read_node_config_file.ReadBaudRateFromFile(Node_Address)))
        remote_device.set_parameter("NB", utils.hex_string_to_bytes(read_node_config_file.ReadParityFromFile(Node_Address)))
        remote_device.set_parameter("SB", utils.hex_string_to_bytes(read_node_config_file.ReadStopBitsFromFile(Node_Address)))
        remote_device.set_parameter("RO", utils.hex_string_to_bytes(read_node_config_file.ReadPacketizationTimeoutFromFile(Node_Address)))
        remote_device.set_parameter("D6", utils.hex_string_to_bytes(read_node_config_file.ReadDIO6ConfigurationFromFile(Node_Address)))
        remote_device.set_parameter("D7", utils.hex_string_to_bytes(read_node_config_file.ReadDIO7ConfigurationFromFile(Node_Address)))
        remote_device.set_parameter("AP", utils.hex_string_to_bytes(read_node_config_file.ReadApiEnableFromFile(Node_Address)))
        remote_device.set_parameter("AO", utils.hex_string_to_bytes(read_node_config_file.ReadApiOutputModeFromFile(Node_Address)))
        # AT Command Options
        remote_device.set_parameter("CT", utils.hex_string_to_bytes(read_node_config_file.ReadATCommandModeTimeoutFromFile(Node_Address)))
        remote_device.set_parameter("GT", utils.hex_string_to_bytes(read_node_config_file.ReadGuardTimesFromFile(Node_Address)))
        remote_device.set_parameter("CC", utils.hex_string_to_bytes(read_node_config_file.ReadCommandSequenceCharacterFromFile(Node_Address)))
        # Sleep Modes
        remote_device.set_parameter("SP", utils.hex_string_to_bytes(read_node_config_file.ReadCyclicSleepPeriodFromFile(Node_Address)))
        remote_device.set_parameter("SN", utils.hex_string_to_bytes(read_node_config_file.ReadNumberOfCyclicSleepPeriodsFromFile(Node_Address)))
        remote_device.set_parameter("SM", utils.hex_string_to_bytes(read_node_config_file.ReadSleepModeFromFile(Node_Address)))
        remote_device.set_parameter("ST", utils.hex_string_to_bytes(read_node_config_file.ReadTimeBeforeSleepFromFile(Node_Address)))
        remote_device.set_parameter("SO", utils.hex_string_to_bytes(read_node_config_file.ReadSleepOptionsFromFile(Node_Address)))
        remote_device.set_parameter("WH", utils.hex_string_to_bytes(read_node_config_file.ReadWakeHostFromFile(Node_Address)))
        remote_device.set_parameter("PO", utils.hex_string_to_bytes(read_node_config_file.ReadPollRateFromFile(Node_Address)))
        # I/O Settings
        remote_device.set_parameter("D0", utils.hex_string_to_bytes(read_node_config_file.ReadDIO0AD0ConfigurationFromFile(Node_Address)))
        remote_device.set_parameter("D1", utils.hex_string_to_bytes(read_node_config_file.ReadDIO1AD1ConfigurationFromFile(Node_Address)))
        remote_device.set_parameter("D2", utils.hex_string_to_bytes(read_node_config_file.ReadDIO2AD2ConfigurationFromFile(Node_Address)))
        remote_device.set_parameter("D3", utils.hex_string_to_bytes(read_node_config_file.ReadDIO3AD3ConfigurationFromFile(Node_Address)))
        remote_device.set_parameter("D4", utils.hex_string_to_bytes(read_node_config_file.ReadDIO4ConfigurationFromFile(Node_Address)))
        remote_device.set_parameter("D5", utils.hex_string_to_bytes(read_node_config_file.ReadDIO5ConfigurationFromFile(Node_Address)))
        remote_device.set_parameter("D8", utils.hex_string_to_bytes(read_node_config_file.ReadDIO8ConfigurationFromFile(Node_Address)))
        remote_device.set_parameter("D9", utils.hex_string_to_bytes(read_node_config_file.ReadDIO9ConfigurationFromFile(Node_Address)))
        remote_device.set_parameter("P0", utils.hex_string_to_bytes(read_node_config_file.ReadDIO10ConfigurationFromFile(Node_Address)))
        remote_device.set_parameter("P1", utils.hex_string_to_bytes(read_node_config_file.ReadDIO11ConfigurationFromFile(Node_Address)))
        remote_device.set_parameter("P2", utils.hex_string_to_bytes(read_node_config_file.ReadDIO12ConfigurationFromFile(Node_Address)))
        remote_device.set_parameter("P3", utils.hex_string_to_bytes(read_node_config_file.ReadDIO13ConfigurationFromFile(Node_Address)))
        remote_device.set_parameter("P4", utils.hex_string_to_bytes(read_node_config_file.ReadDIO14ConfigurationFromFile(Node_Address)))
        if HV == Hardware_Extended:
            remote_device.set_parameter("P5", utils.hex_string_to_bytes(read_node_config_file.ReadDIO15ConfigurationFromFile(Node_Address)))
            remote_device.set_parameter("P6", utils.hex_string_to_bytes(read_node_config_file.ReadDIO16ConfigurationFromFile(Node_Address)))
            remote_device.set_parameter("P7", utils.hex_string_to_bytes(read_node_config_file.ReadDIO17ConfigurationFromFile(Node_Address)))
            remote_device.set_parameter("P8", utils.hex_string_to_bytes(read_node_config_file.ReadDIO18ConfigurationFromFile(Node_Address)))
            remote_device.set_parameter("P9", utils.hex_string_to_bytes(read_node_config_file.ReadDIO19ConfigurationFromFile(Node_Address)))
        remote_device.set_parameter("PR", utils.hex_string_to_bytes(read_node_config_file.ReadPullUpResistorEnableFromFile(Node_Address)))
        remote_device.set_parameter("PD", utils.hex_string_to_bytes(read_node_config_file.ReadPullUpDownDirectionFromFile(Node_Address)))
        remote_device.set_parameter("LT", utils.hex_string_to_bytes(read_node_config_file.ReadAssociatedLedBlinkTimeFromFile(Node_Address)))
        remote_device.set_parameter("RP", utils.hex_string_to_bytes(read_node_config_file.ReadRssiPwmTimerFromFile(Node_Address)))
        # I/O Sampling
        remote_device.set_parameter("IR", utils.hex_string_to_bytes(read_node_config_file.ReadIOSamplingRateFromFile(Node_Address)))
        remote_device.set_parameter("IC", utils.hex_string_to_bytes(read_node_config_file.ReadDigitalIOChangeDetectionFromFile(Node_Address)))
        remote_device.set_parameter("V+", utils.hex_string_to_bytes(read_node_config_file.ReadSupplyVoltageHihgThresholdFromFile(Node_Address)))

        # Make params permanent
        remote_device.write_changes()  # make changes permanet"""

        # print parameters
        log ="  Success!! All Parameters Were Written  \n\n"
        print("  Success!! All Parameters Were Written  ")


    except:
        log = "  Sorry, an error has happened during writting operation\n"
        if local_device.is_open():
            local_device.close()
        pass


    finally:
        if local_device is not None and local_device.is_open():
            local_device.close()

    return log


if __name__ == '__main__':
    main(REMOTE_1)