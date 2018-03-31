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
import SysConfig
import sys
sys.tracebacklimit = 0

# Parámetros de conexión con el puerto serie al dispositivo local
PORT=SysConfig.ReadLocalPortFromFile()
BAUD_RATE = SysConfig.ReadLocalBaudRateFromFile()

NODE_ADDRESS = "0013A20041679E85"

def main(NodeAddress):
    print(" +-----------------------------------------------+")
    print(" |           Write Local XBee parameters         |")
    print(" +-----------------------------------------------+\n")

    local_device = XBeeDevice(PORT, BAUD_RATE)


    try:
        local_device.open()
       # Get Hardware Models with extended DIO (P5 to P9)
        Hardware_Extended = SysConfig.ReadHardwareVersionWhithP5ToP9PinsFromFile()
        HV = utils.hex_to_string(local_device.get_parameter("HV"))
       # Set parameters.
        # Networking
        local_device.set_parameter("ID", utils.hex_string_to_bytes(SysConfig.ReadPanIDFromFile(NodeAddress)))
        local_device.set_parameter("SC", utils.hex_string_to_bytes(SysConfig.ReadScanChannelsFromFile(NodeAddress)))
        local_device.set_parameter("SD", utils.hex_string_to_bytes(SysConfig.ReadScanDurationFromFile(NodeAddress)))
        local_device.set_parameter("ZS", utils.hex_string_to_bytes(SysConfig.ReadZigBeeStackProfileFromFile(NodeAddress)))
        local_device.set_parameter("NJ", utils.hex_string_to_bytes(SysConfig.ReadNodeJoinTimeFromFile(NodeAddress)))
        local_device.set_parameter("NW", utils.hex_string_to_bytes(SysConfig.ReadNetworkWatchdogTimeoutFromFile(NodeAddress)))
        local_device.set_parameter("JV", utils.hex_string_to_bytes(SysConfig.ReadChannelVerificationFromFile(NodeAddress)))
        local_device.set_parameter("JN", utils.hex_string_to_bytes(SysConfig.ReadJoinNotificationFromFile(NodeAddress)))
        local_device.set_parameter("CE", utils.hex_string_to_bytes(SysConfig.ReadCoordinatorEnableFromFile(NodeAddress)))
        local_device.set_parameter("DO", utils.hex_string_to_bytes(SysConfig.ReadDeviceOptionsFromFile(NodeAddress)))
        local_device.set_parameter("DC", utils.hex_string_to_bytes(SysConfig.ReadDeviceControlsFromFile(NodeAddress)))
        # Addressing
        local_device.set_parameter("DH", utils.hex_string_to_bytes(SysConfig.ReadDestinationAddressHighFromFile(NodeAddress)))
        local_device.set_parameter("DL", utils.hex_string_to_bytes(SysConfig.ReadDestinationAddressLowFromFile(NodeAddress)))
        local_device.set_parameter("NI", bytearray(SysConfig.ReadNodeIdentifierFromFile(NodeAddress),'utf8'))
        local_device.set_parameter("NH", utils.hex_string_to_bytes(SysConfig.ReadMaximumHopsFromFile(NodeAddress)))
        local_device.set_parameter("BH", utils.hex_string_to_bytes(SysConfig.ReadBroadcastRadiusFromFile(NodeAddress)))
        local_device.set_parameter("AR", utils.hex_string_to_bytes(SysConfig.ReadManyToOneRouteBroadcastTimeFromFile(NodeAddress)))
        local_device.set_parameter("DD", utils.hex_string_to_bytes(SysConfig.ReadDeviceTypeIdentifierFromFile(NodeAddress)))
        local_device.set_parameter("NT", utils.hex_string_to_bytes(SysConfig.ReadNodeDiscoveryBackoffFromFile(NodeAddress)))
        local_device.set_parameter("NO", utils.hex_string_to_bytes(SysConfig.ReadNodeDiscoveryOptionsFromFile(NodeAddress)))
        local_device.set_parameter("CR", utils.hex_string_to_bytes(SysConfig.ReadPanConflictThresholdFromFile(NodeAddress)))
        # ZigBee Addressing
        local_device.set_parameter("SE", utils.hex_string_to_bytes(SysConfig.ReadZigBeeSourceEndPointFromFile(NodeAddress)))
        local_device.set_parameter("DE", utils.hex_string_to_bytes(SysConfig.ReadZigBeeDestinationEndpointFromFile(NodeAddress)))
        local_device.set_parameter("CI", utils.hex_string_to_bytes(SysConfig.ReadZigBeeClusterIDFromFile(NodeAddress)))
        local_device.set_parameter("TO", utils.hex_string_to_bytes(SysConfig.ReadTransmitOptionsFromFile(NodeAddress)))
        # RF Interfacing
        local_device.set_parameter("PL", utils.hex_string_to_bytes(SysConfig.ReadTxPowerLevelFromFile(NodeAddress)))
        local_device.set_parameter("PM", utils.hex_string_to_bytes(SysConfig.ReadPowerModeFromFile(NodeAddress)))
        # Security
        local_device.set_parameter("EE", utils.hex_string_to_bytes(SysConfig.ReadEncryptionEnableFromFile(NodeAddress)))
        local_device.set_parameter("EO", utils.hex_string_to_bytes(SysConfig.ReadEncryptionOptionsFromFile(NodeAddress)))
        local_device.set_parameter("KY", utils.hex_string_to_bytes(SysConfig.ReadEncryptionKeyFromFile(NodeAddress)))
        local_device.set_parameter("NK", utils.hex_string_to_bytes(SysConfig.ReadNetworkEncryptionKeyFromFile(NodeAddress)))
        # Serial Interfacing
        local_device.set_parameter("BD", utils.hex_string_to_bytes(SysConfig.ReadBaudRateFromFile(NodeAddress)))
        local_device.set_parameter("NB", utils.hex_string_to_bytes(SysConfig.ReadParityFromFile(NodeAddress)))
        local_device.set_parameter("SB", utils.hex_string_to_bytes(SysConfig.ReadStopBitsFromFile(NodeAddress)))
        local_device.set_parameter("RO", utils.hex_string_to_bytes(SysConfig.ReadPacketizationTimeoutFromFile(NodeAddress)))
        local_device.set_parameter("D6", utils.hex_string_to_bytes(SysConfig.ReadDIO6ConfigurationFromFile(NodeAddress)))
        local_device.set_parameter("D7", utils.hex_string_to_bytes(SysConfig.ReadDIO7ConfigurationFromFile(NodeAddress)))
        local_device.set_parameter("AP", utils.hex_string_to_bytes(SysConfig.ReadApiEnableFromFile(NodeAddress)))
        local_device.set_parameter("AO", utils.hex_string_to_bytes(SysConfig.ReadApiOutputModeFromFile(NodeAddress)))
        # AT Command Options
        local_device.set_parameter("CT", utils.hex_string_to_bytes(SysConfig.ReadATCommandModeTimeoutFromFile(NodeAddress)))
        local_device.set_parameter("GT", utils.hex_string_to_bytes(SysConfig.ReadGuardTimesFromFile(NodeAddress)))
        local_device.set_parameter("CC", utils.hex_string_to_bytes(SysConfig.ReadCommandSequenceCharacterFromFile(NodeAddress)))
        # Sleep Modes
        local_device.set_parameter("SP", utils.hex_string_to_bytes(SysConfig.ReadCyclicSleepPeriodFromFile(NodeAddress)))
        local_device.set_parameter("SN", utils.hex_string_to_bytes(SysConfig.ReadNumberOfCyclicSleepPeriodsFromFile(NodeAddress)))
        local_device.set_parameter("SM", utils.hex_string_to_bytes(SysConfig.ReadSleepModeFromFile(NodeAddress)))
        local_device.set_parameter("ST", utils.hex_string_to_bytes(SysConfig.ReadTimeBeforeSleepFromFile(NodeAddress)))
        local_device.set_parameter("SO", utils.hex_string_to_bytes(SysConfig.ReadSleepOptionsFromFile(NodeAddress)))
        local_device.set_parameter("WH", utils.hex_string_to_bytes(SysConfig.ReadWakeHostFromFile(NodeAddress)))
        local_device.set_parameter("PO", utils.hex_string_to_bytes(SysConfig.ReadPollRateFromFile(NodeAddress)))
        # I/O Settings
        local_device.set_parameter("D0", utils.hex_string_to_bytes(SysConfig.ReadDIO0AD0ConfigurationFromFile(NodeAddress)))
        local_device.set_parameter("D1", utils.hex_string_to_bytes(SysConfig.ReadDIO1AD1ConfigurationFromFile(NodeAddress)))
        local_device.set_parameter("D2", utils.hex_string_to_bytes(SysConfig.ReadDIO2AD2ConfigurationFromFile(NodeAddress)))
        local_device.set_parameter("D3", utils.hex_string_to_bytes(SysConfig.ReadDIO3AD3ConfigurationFromFile(NodeAddress)))
        local_device.set_parameter("D4", utils.hex_string_to_bytes(SysConfig.ReadDIO4ConfigurationFromFile(NodeAddress)))
        local_device.set_parameter("D5", utils.hex_string_to_bytes(SysConfig.ReadDIO5ConfigurationFromFile(NodeAddress)))
        local_device.set_parameter("D8", utils.hex_string_to_bytes(SysConfig.ReadDIO8ConfigurationFromFile(NodeAddress)))
        local_device.set_parameter("D9", utils.hex_string_to_bytes(SysConfig.ReadDIO9ConfigurationFromFile(NodeAddress)))
        local_device.set_parameter("P0", utils.hex_string_to_bytes(SysConfig.ReadDIO10ConfigurationFromFile(NodeAddress)))
        local_device.set_parameter("P1", utils.hex_string_to_bytes(SysConfig.ReadDIO11ConfigurationFromFile(NodeAddress)))
        local_device.set_parameter("P2", utils.hex_string_to_bytes(SysConfig.ReadDIO12ConfigurationFromFile(NodeAddress)))
        local_device.set_parameter("P3", utils.hex_string_to_bytes(SysConfig.ReadDIO13ConfigurationFromFile(NodeAddress)))
        local_device.set_parameter("P4", utils.hex_string_to_bytes(SysConfig.ReadDIO14ConfigurationFromFile(NodeAddress)))
        if HV == Hardware_Extended:
            local_device.set_parameter("P5", utils.hex_string_to_bytes(SysConfig.ReadDIO15ConfigurationFromFile(NodeAddress)))
            local_device.set_parameter("P6", utils.hex_string_to_bytes(SysConfig.ReadDIO16ConfigurationFromFile(NodeAddress)))
            local_device.set_parameter("P7", utils.hex_string_to_bytes(SysConfig.ReadDIO17ConfigurationFromFile(NodeAddress)))
            local_device.set_parameter("P8", utils.hex_string_to_bytes(SysConfig.ReadDIO18ConfigurationFromFile(NodeAddress)))
            local_device.set_parameter("P9", utils.hex_string_to_bytes(SysConfig.ReadDIO19ConfigurationFromFile(NodeAddress)))
        local_device.set_parameter("PR", utils.hex_string_to_bytes(SysConfig.ReadPullUpResistorEnableFromFile(NodeAddress)))
        local_device.set_parameter("PD", utils.hex_string_to_bytes(SysConfig.ReadPullUpDownDirectionFromFile(NodeAddress)))
        local_device.set_parameter("LT", utils.hex_string_to_bytes(SysConfig.ReadAssociatedLedBlinkTimeFromFile(NodeAddress)))
        local_device.set_parameter("RP", utils.hex_string_to_bytes(SysConfig.ReadRssiPwmTimerFromFile(NodeAddress)))
        # I/O Sampling
        local_device.set_parameter("IR", utils.hex_string_to_bytes(SysConfig.ReadIOSamplingRateFromFile(NodeAddress)))
        local_device.set_parameter("IC", utils.hex_string_to_bytes(SysConfig.ReadDigitalIOChangeDetectionFromFile(NodeAddress)))
        local_device.set_parameter("V+", utils.hex_string_to_bytes(SysConfig.ReadSupplyVoltageHihgThresholdFromFile(NodeAddress)))

        # Make params permanent
        local_device.write_changes()  # make changes permanet


        #print parameters
        print("  Success!! All Parameters Were Written  ")


    except:
        if local_device.is_open():
            local_device.close()
        pass


    finally:
        if local_device is not None and local_device.is_open():
            local_device.close()


if __name__ == '__main__':
    main(NODE_ADDRESS)