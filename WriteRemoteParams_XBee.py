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
import SysConfig
import sys
sys.tracebacklimit = 0

# Parámetros de conexión con el puerto serie al dispositivo local
PORT=SysConfig.ReadLocalPortFromFile()
BAUD_RATE = SysConfig.ReadLocalBaudRateFromFile()

REMOTE_1 = "0013A200415BFC59"


def main(Node_Address):

    NodeAddress = XBee64BitAddress.from_hex_string(Node_Address)

    print(" +-------------------------------------------------------+")
    print(" |  Write Remote XBee (" +Node_Address+ ") parameters      |")
    print(" +---------------------------------------------------- --+\n")

    local_device = XBeeDevice(PORT, BAUD_RATE)


    try:
        local_device.open()
        remote_device = RemoteZigBeeDevice(local_device, NodeAddress)
       # Get Hardware Models with extended DIO (P5 to P9)
        Hardware_Extended = SysConfig.ReadHardwareVersionWhithP5ToP9PinsFromFile()
        HV = utils.hex_to_string(remote_device.get_parameter("HV"))
       # Set parameters.
        #No se puede modificar la PAN ID vía RF porque se pierde conexión
        #remote_device.set_parameter("ID",utils.hex_string_to_bytes(SysConfig.ReadScanChannelsFromFile(Node_Address)))
        remote_device.set_parameter("SC",utils.hex_string_to_bytes(SysConfig.ReadScanChannelsFromFile(Node_Address)))
        remote_device.set_parameter("SD",utils.hex_string_to_bytes(SysConfig.ReadScanDurationFromFile(Node_Address)))
        remote_device.set_parameter("ZS",utils.hex_string_to_bytes(SysConfig.ReadZigBeeStackProfileFromFile(Node_Address)))
        remote_device.set_parameter("NJ",utils.hex_string_to_bytes(SysConfig.ReadNodeJoinTimeFromFile(Node_Address)))
        remote_device.set_parameter("NW",utils.hex_string_to_bytes(SysConfig.ReadNetworkWatchdogTimeoutFromFile(Node_Address)))
        remote_device.set_parameter("JV",utils.hex_string_to_bytes(SysConfig.ReadChannelVerificationFromFile(Node_Address)))
        remote_device.set_parameter("JN",utils.hex_string_to_bytes(SysConfig.ReadJoinNotificationFromFile(Node_Address)))
        remote_device.set_parameter("CE",utils.hex_string_to_bytes(SysConfig.ReadCoordinatorEnableFromFile(Node_Address)))
        remote_device.set_parameter("DO",utils.hex_string_to_bytes(SysConfig.ReadDeviceOptionsFromFile(Node_Address)))
        remote_device.set_parameter("DC",utils.hex_string_to_bytes(SysConfig.ReadDeviceControlsFromFile(Node_Address)))
        # Addressing
        remote_device.set_parameter("DH",utils.hex_string_to_bytes(SysConfig.ReadDestinationAddressHighFromFile(Node_Address)))
        remote_device.set_parameter("DL",utils.hex_string_to_bytes(SysConfig.ReadDestinationAddressLowFromFile(Node_Address)))
        remote_device.set_parameter("NI",bytearray(SysConfig.ReadNodeIdentifierFromFile(Node_Address), 'utf8'))
        remote_device.set_parameter("NH",utils.hex_string_to_bytes(SysConfig.ReadMaximumHopsFromFile(Node_Address)))
        remote_device.set_parameter("BH",utils.hex_string_to_bytes(SysConfig.ReadBroadcastRadiusFromFile(Node_Address)))
        remote_device.set_parameter("AR",utils.hex_string_to_bytes(SysConfig.ReadManyToOneRouteBroadcastTimeFromFile(Node_Address)))
        remote_device.set_parameter("DD",utils.hex_string_to_bytes(SysConfig.ReadDeviceTypeIdentifierFromFile(Node_Address)))
        remote_device.set_parameter("NT",utils.hex_string_to_bytes(SysConfig.ReadNodeDiscoveryBackoffFromFile(Node_Address)))
        remote_device.set_parameter("NO",utils.hex_string_to_bytes(SysConfig.ReadNodeDiscoveryOptionsFromFile(Node_Address)))
        remote_device.set_parameter("CR",utils.hex_string_to_bytes(SysConfig.ReadPanConflictThresholdFromFile(Node_Address)))
        # ZigBee Addressing
        remote_device.set_parameter("SE",utils.hex_string_to_bytes(SysConfig.ReadZigBeeSourceEndPointFromFile(Node_Address)))
        remote_device.set_parameter("DE",utils.hex_string_to_bytes(SysConfig.ReadZigBeeDestinationEndpointFromFile(Node_Address)))
        remote_device.set_parameter("CI",utils.hex_string_to_bytes(SysConfig.ReadZigBeeClusterIDFromFile(Node_Address)))
        remote_device.set_parameter("TO",utils.hex_string_to_bytes(SysConfig.ReadTransmitOptionsFromFile(Node_Address)))
        # RF Interfacing
        remote_device.set_parameter("PL",utils.hex_string_to_bytes(SysConfig.ReadTxPowerLevelFromFile(Node_Address)))
        remote_device.set_parameter("PM",utils.hex_string_to_bytes(SysConfig.ReadPowerModeFromFile(Node_Address)))
        # Security
        remote_device.set_parameter("EE",utils.hex_string_to_bytes(SysConfig.ReadEncryptionEnableFromFile(Node_Address)))
        remote_device.set_parameter("EO",utils.hex_string_to_bytes(SysConfig.ReadEncryptionOptionsFromFile(Node_Address)))
        # No se pueden cambiar las keys vía RF
        #remote_device.set_parameter("KY",utils.hex_string_to_bytes(SysConfig.ReadEncryptionKeyFromFile(Node_Address)))
        #remote_device.set_parameter("NK",utils.hex_string_to_bytes(SysConfig.ReadNetworkEncryptionKeyFromFile(Node_Address)))
        # Serial Interfacing
        remote_device.set_parameter("BD",utils.hex_string_to_bytes(SysConfig.ReadBaudRateFromFile(Node_Address)))
        remote_device.set_parameter("NB",utils.hex_string_to_bytes(SysConfig.ReadParityFromFile(Node_Address)))
        remote_device.set_parameter("SB",utils.hex_string_to_bytes(SysConfig.ReadStopBitsFromFile(Node_Address)))
        remote_device.set_parameter("RO",utils.hex_string_to_bytes(SysConfig.ReadPacketizationTimeoutFromFile(Node_Address)))
        remote_device.set_parameter("D6",utils.hex_string_to_bytes(SysConfig.ReadDIO6ConfigurationFromFile(Node_Address)))
        remote_device.set_parameter("D7",utils.hex_string_to_bytes(SysConfig.ReadDIO7ConfigurationFromFile(Node_Address)))
        remote_device.set_parameter("AP",utils.hex_string_to_bytes(SysConfig.ReadApiEnableFromFile(Node_Address)))
        remote_device.set_parameter("AO",utils.hex_string_to_bytes(SysConfig.ReadApiOutputModeFromFile(Node_Address)))
        # AT Command Options
        remote_device.set_parameter("CT",utils.hex_string_to_bytes(SysConfig.ReadATCommandModeTimeoutFromFile(Node_Address)))
        remote_device.set_parameter("GT",utils.hex_string_to_bytes(SysConfig.ReadGuardTimesFromFile(Node_Address)))
        remote_device.set_parameter("CC",utils.hex_string_to_bytes(SysConfig.ReadCommandSequenceCharacterFromFile(Node_Address)))
        # Sleep Modes
        remote_device.set_parameter("SP",utils.hex_string_to_bytes(SysConfig.ReadCyclicSleepPeriodFromFile(Node_Address)))
        remote_device.set_parameter("SN",utils.hex_string_to_bytes(SysConfig.ReadNumberOfCyclicSleepPeriodsFromFile(Node_Address)))
        remote_device.set_parameter("SM",utils.hex_string_to_bytes(SysConfig.ReadSleepModeFromFile(Node_Address)))
        remote_device.set_parameter("ST",utils.hex_string_to_bytes(SysConfig.ReadTimeBeforeSleepFromFile(Node_Address)))
        remote_device.set_parameter("SO",utils.hex_string_to_bytes(SysConfig.ReadSleepOptionsFromFile(Node_Address)))
        remote_device.set_parameter("WH",utils.hex_string_to_bytes(SysConfig.ReadWakeHostFromFile(Node_Address)))
        remote_device.set_parameter("PO",utils.hex_string_to_bytes(SysConfig.ReadPollRateFromFile(Node_Address)))
        # I/O Settings
        remote_device.set_parameter("D0",utils.hex_string_to_bytes(SysConfig.ReadDIO0AD0ConfigurationFromFile(Node_Address)))
        remote_device.set_parameter("D1",utils.hex_string_to_bytes(SysConfig.ReadDIO1AD1ConfigurationFromFile(Node_Address)))
        remote_device.set_parameter("D2",utils.hex_string_to_bytes(SysConfig.ReadDIO2AD2ConfigurationFromFile(Node_Address)))
        remote_device.set_parameter("D3",utils.hex_string_to_bytes(SysConfig.ReadDIO3AD3ConfigurationFromFile(Node_Address)))
        remote_device.set_parameter("D4",utils.hex_string_to_bytes(SysConfig.ReadDIO4ConfigurationFromFile(Node_Address)))
        remote_device.set_parameter("D5",utils.hex_string_to_bytes(SysConfig.ReadDIO5ConfigurationFromFile(Node_Address)))
        remote_device.set_parameter("D8",utils.hex_string_to_bytes(SysConfig.ReadDIO8ConfigurationFromFile(Node_Address)))
        remote_device.set_parameter("D9",utils.hex_string_to_bytes(SysConfig.ReadDIO9ConfigurationFromFile(Node_Address)))
        remote_device.set_parameter("P0",utils.hex_string_to_bytes(SysConfig.ReadDIO10ConfigurationFromFile(Node_Address)))
        remote_device.set_parameter("P1",utils.hex_string_to_bytes(SysConfig.ReadDIO11ConfigurationFromFile(Node_Address)))
        remote_device.set_parameter("P2",utils.hex_string_to_bytes(SysConfig.ReadDIO12ConfigurationFromFile(Node_Address)))
        remote_device.set_parameter("P3",utils.hex_string_to_bytes(SysConfig.ReadDIO13ConfigurationFromFile(Node_Address)))
        remote_device.set_parameter("P4",utils.hex_string_to_bytes(SysConfig.ReadDIO14ConfigurationFromFile(Node_Address)))
        if HV == Hardware_Extended:
            remote_device.set_parameter("P5",utils.hex_string_to_bytes(SysConfig.ReadDIO15ConfigurationFromFile(Node_Address)))
            remote_device.set_parameter("P6",utils.hex_string_to_bytes(SysConfig.ReadDIO16ConfigurationFromFile(Node_Address)))
            remote_device.set_parameter("P7",utils.hex_string_to_bytes(SysConfig.ReadDIO17ConfigurationFromFile(Node_Address)))
            remote_device.set_parameter("P8",utils.hex_string_to_bytes(SysConfig.ReadDIO18ConfigurationFromFile(Node_Address)))
            remote_device.set_parameter("P9",utils.hex_string_to_bytes(SysConfig.ReadDIO19ConfigurationFromFile(Node_Address)))
        remote_device.set_parameter("PR",utils.hex_string_to_bytes(SysConfig.ReadPullUpResistorEnableFromFile(Node_Address)))
        remote_device.set_parameter("PD",utils.hex_string_to_bytes(SysConfig.ReadPullUpDownDirectionFromFile(Node_Address)))
        remote_device.set_parameter("LT",utils.hex_string_to_bytes(SysConfig.ReadAssociatedLedBlinkTimeFromFile(Node_Address)))
        remote_device.set_parameter("RP",utils.hex_string_to_bytes(SysConfig.ReadRssiPwmTimerFromFile(Node_Address)))
        # I/O Sampling
        remote_device.set_parameter("IR",utils.hex_string_to_bytes(SysConfig.ReadIOSamplingRateFromFile(Node_Address)))
        remote_device.set_parameter("IC",utils.hex_string_to_bytes(SysConfig.ReadDigitalIOChangeDetectionFromFile(Node_Address)))
        remote_device.set_parameter("V+",utils.hex_string_to_bytes(SysConfig.ReadSupplyVoltageHihgThresholdFromFile(Node_Address)))

        # Make params permanent
        local_device.write_changes()  # make changes permanet"""

        # print parameters
        print("  Success!! All Parameters Were Written  ")


    except:
        if local_device.is_open():
            local_device.close()
        pass


    finally:
        if local_device is not None and local_device.is_open():
            local_device.close()


if __name__ == '__main__':
    main(REMOTE_1)