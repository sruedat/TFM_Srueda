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

# Parámetros de conexión con el puerto serie al dispositivo local
PORT=SysConfig.ReadLocalPortFromFile()
BAUD_RATE = SysConfig.ReadLocalBaudRateFromFile()



def main():
    print(" +-----------------------------------------------+")
    print(" |            Get Local XBee parameters          |")
    print(" +-----------------------------------------------+\n")

    local_device = XBeeDevice(PORT, BAUD_RATE)


    try:
        local_device.open()
       # Get parameters.
        ID = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadPanIDCmdFromFile()))
        SC = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadScanChannelsCmdFromFile()))
        SD = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadScanDurationCmdFromFile()))
        ZS = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadZigBeeStackProfileCmdFromFile()))
        NJ = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadNodeJoinTimeCmdFromFile()))
        NW = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadNetworkWatchdogTimeoutCmdFromFile()))
        JV = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadChannelVerificationCmdFromFile()))
        JN = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadJoinNotificationCmdFromFile()))
        OP = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadOperatingPanIdCmdFromFile()))
        OI = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadOperating16BitPanIdCmdFromFile()))
        CH = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadOperatingChannelCmdFromFile()))
        NC = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadNumberOfRemainingChildrenCmdFromFile()))
        CE = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadCoordinatorEnableCmdFromFile()))
        DO = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadDeviceOptionsCmdFromFile()))
        DC = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadDeviceControlsCmdFromFile()))

        SH = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadSerialNumberHighCmdFromFile()))
        SL = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadSerialNumberLowCmdFromFile()))
        MY = utils.hex_to_string(local_device.get_parameter(SysConfig.Read16BitNetworkAddressCmdFromFile()))
        MP = utils.hex_to_string(local_device.get_parameter(SysConfig.Read16BitParentAddressCmdFromFile()))
        DH = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadDestinationAddressHighCmdFromFile()))
        DL = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadDestinationAddressLowCmdFromFile()))
        NI = local_device.get_parameter(SysConfig.ReadNodeIdentifierCmdFromFile()).decode()
        NH = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadMaximumHopsCmdFromFile()))
        BH = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadBroadcastRadiusCmdFromFile()))
        AR = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadManyToOneRouteBroadcastTimeCmdFromFile()))
        DD = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadDeviceTypeIdentifierCmdFromFile()))
        NT = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadNodeDiscoveryBackoffCmdFromFile()))
        NO = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadNodeDiscoveryOptionsCmdFromFile()))
        NP = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadMaximumNumberOfTransmissionBytesCmdFromFile()))
        CR = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadPanConflictThresholdCmdFromFile()))

        SE = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadZigBeeSourceEndPointCmdFromFile()))
        DE = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadZigBeeDestinationEndpointCmdFromFile()))
        CI = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadZigBeeClusterIDCmdFromFile()))
        TO = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadTransmitOptionsCmdFromFile()))

        PL = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadTxPowerLevelCmdFromFile()))
        PM = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadPowerModeCmdFromFile()))
        PP = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadPowerAtPL4CmdFromFile()))

        EE = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadEncryptionEnableCmdFromFile()))
        EO = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadEncryptionOptionsCmdFromFile()))
        KY = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadEncryptionKeyCmdFromFile()))
        NK = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadNetworkEncryptionKeyCmdFromFile()))

        BD = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadBaudRateCmdFromFile()))
        NB = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadParityCmdFromFile()))
        SB = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadStopBitsCmdFromFile()))
        RO = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadPacketizationTimeoutCmdFromFile()))
        D6 = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadPin29Dio6nRTSConfigurationCmdFromFile()))
        D7 = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadPin25Dio7nCTSConfigurationCmdFromFile()))
        AP = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadApiEnableCmdFromFile()))
        AO = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadApiOutputModeCmdFromFile()))

        CT = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadATCommandModeTimeoutCmdFromFile()))
        GT = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadGuardTimesCmdFromFile()))
        CC = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadCommandSequenceCharacterCmdFromFile()))

        SP = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadCyclicSleepPeriodCmdFromFile()))
        SN = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadNumberOfCyclicSleepPeriodsCmdFromFile()))
        SM = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadSleepModeCmdFromFile()))
        ST = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadTimeBeforeSleepCmdFromFile()))
        SO = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadSleepOptionsCmdFromFile()))
        WH = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadWakeHostCmdFromFile()))
        PO = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadPollRateCmdFromFile()))

        #print parameters
        print(" +-----------------------------+")
        print(" | Networking                  |")
        print(" +-----------------------------+")
        print(" PAN ID:                      %s" % ID)
        print(" Scan Channel:                %s" % SC)
        print(" Scan Duration:               %s" % SD)
        print(" ZigBee Stack Profile:        %s" % ZS)
        print(" Node Join Time:              %s" % NJ)
        print(" Network Watchdog Timeout:    %s" % NW)
        print(" Channel Verification:        %s" % JV)
        print(" Join Notification:           %s" % JN)
        print(" Operating PAN ID:            %s" % OP)
        print(" Operating 16-bit PAN ID:     %s" % OI)
        print(" Operating Channel:           %s" % CH)
        print(" Number of Ramining Children: %s" % NC)
        print(" Coordinator Enable:          %s" % CE)
        print(" Device Options:              %s" % DO)
        print(" Device Controls:             %s" % DC + "\n")

        print(" +-----------------------------+")
        print(" | Addressing                  |")
        print(" +-----------------------------+")
        print(" Serial Number High:          %s" % SH)
        print(" Serial Number Low:           %s" % SL)
        print(" 16-bit Network Address:      %s" % MY)
        print(" 16-bit Parent Address:       %s" % MP)
        print(" Destination Address High:    %s" % DH)
        print(" Destination Address Low:     %s" % DL)
        print(" Node Identifier:             %s" % NI)
        print(" Maximum Hops:                %s" % NH)
        print(" Broadcast Radius:            %s" % BH)
        print(" Many-to-One Route Bro. Time: %s" % AR)
        print(" Device Type Identifier:      %s" % DD)
        print(" Node Discovery Backoff:      %s" % NT)
        print(" Node Discovery Options:      %s" % NO)
        print(" Maximum Num.Trans. Bytes:    %s" % NP)
        print(" PAN Conflict Threshold:      %s" % CR + "\n")

        print(" +-----------------------------+")
        print(" | ZigBee Addressing           |")
        print(" +-----------------------------+")
        print(" Zigbee Source Endpoint:      %s" % SE)
        print(" Zigbee Destination Endpoint: %s" % DE)
        print(" Zigbee Cluster ID:           %s" % CI)
        print(" Transmit Options:            %s" % TO + "\n")

        print(" +-----------------------------+")
        print(" | RF Interfacing              |")
        print(" +-----------------------------+")
        print(" Tx Power Level:              %s" % PL)
        print(" Power Mode:                  %s" % PM)
        print(" Power at PL4:                %s" % PP + "\n")

        print(" +-----------------------------+")
        print(" | Security                    |")
        print(" +-----------------------------+")
        print(" Encryption Enable:           %s" % EE)
        print(" Encryption Options:          %s" % EO)
        print(" Encryption Key:              %s" % KY)
        print(" Network Encryption Key:      %s" % NK + "\n")

        print(" +-----------------------------+")
        print(" | Serial Interfacing          |")
        print(" +-----------------------------+")
        print(" Baud Rate:                   %s" % BD)
        print(" Parity:                      %s" % NB)
        print(" Stop Bits:                   %s" % SB)
        print(" Packetization Timeout:       %s" % RO)
        print(" Pin 29 DIO6 Configuration:   %s" % D6)
        print(" Pin 25 DIO7 Configuration:   %s" % D7)
        print(" API Enable:                  %s" % AP)
        print(" API Output Mode:             %s" % AO + "\n")

        print(" +-----------------------------+")
        print(" | AT Command Options          |")
        print(" +-----------------------------+")
        print(" AT Command Mode Timeout:     %s" % CT)
        print(" Guard Times:                 %s" % GT)
        print(" Command Sequence Character:  %s" % CC + "\n")

        print(" +-----------------------------+")
        print(" | Sleep Modes                 |")
        print(" +-----------------------------+")
        print(" Cyclic Sleep Period:         %s" % SP)
        print(" Number of Cyclic Sleep Per.: %s" % SN)
        print(" Sleep Mode:                  %s" % SM)
        print(" Time Before Sleep:sss        %s" % ST)
        print(" Sleep Options:               %s" % SO)
        print(" Wake Hosts:                  %s" % WH)
        print(" Poll Rate:                   %s" % PO + "\n")




    finally:
        if local_device is not None and local_device.is_open():
            local_device.close()


if __name__ == '__main__':
    main()