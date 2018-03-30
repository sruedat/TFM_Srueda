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
       # Get Hardware Models with extended DIO (P5 to P9)
        Hardware_Extended = SysConfig.ReadHardwareVersionWhithP5ToP9PinsFromFile()
       # Get parameters.
        # Diagnostic Commads
        VR = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadFirmwareVersionCmdFromFile()))
        HV = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadHardwareVersionCmdFromFile()))
        AI = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadAssociationIndicationCmdFromFile()))
        DB = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadRSSIOfLastPacketCmdFromFile()))
        V =  utils.hex_to_string(local_device.get_parameter(SysConfig.ReadSupplyVotageCmdFromFile()))
        # Networking
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
        # Addressing
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
        # ZigBee Addressing
        SE = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadZigBeeSourceEndPointCmdFromFile()))
        DE = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadZigBeeDestinationEndpointCmdFromFile()))
        CI = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadZigBeeClusterIDCmdFromFile()))
        TO = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadTransmitOptionsCmdFromFile()))
        # RF Interfacing
        PL = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadTxPowerLevelCmdFromFile()))
        PM = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadPowerModeCmdFromFile()))
        PP = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadPowerAtPL4CmdFromFile()))
        # Security
        EE = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadEncryptionEnableCmdFromFile()))
        EO = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadEncryptionOptionsCmdFromFile()))
        KY = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadEncryptionKeyCmdFromFile()))
        NK = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadNetworkEncryptionKeyCmdFromFile()))
        # Serial Interfacing
        BD = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadBaudRateCmdFromFile()))
        NB = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadParityCmdFromFile()))
        SB = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadStopBitsCmdFromFile()))
        RO = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadPacketizationTimeoutCmdFromFile()))
        D6 = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadDIO6ConfigurationCmdFromFile()))
        D7 = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadDIO7ConfigurationCmdFromFile()))
        AP = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadApiEnableCmdFromFile()))
        AO = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadApiOutputModeCmdFromFile()))
        # AT Command Options
        CT = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadATCommandModeTimeoutCmdFromFile()))
        GT = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadGuardTimesCmdFromFile()))
        CC = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadCommandSequenceCharacterCmdFromFile()))
        # Sleep Modes
        SP = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadCyclicSleepPeriodCmdFromFile()))
        SN = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadNumberOfCyclicSleepPeriodsCmdFromFile()))
        SM = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadSleepModeCmdFromFile()))
        ST = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadTimeBeforeSleepCmdFromFile()))
        SO = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadSleepOptionsCmdFromFile()))
        WH = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadWakeHostCmdFromFile()))
        PO = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadPollRateCmdFromFile()))
        # I/O Settomgs
        D0 = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadDIO0AD0ConfigurationCmdFromFile()))
        D1 = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadDIO1AD1ConfigurationCmdFromFile()))
        D2 = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadDIO2AD2ConfigurationCmdFromFile()))
        D3 = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadDIO3AD3ConfigurationCmdFromFile()))
        D4 = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadDIO4ConfigurationCmdFromFile()))
        D5 = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadDIO5ConfigurationCmdFromFile()))
        D8 = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadDIO8ConfigurationCmdFromFile()))
        D9 = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadDIO9ConfigurationCmdFromFile()))
        P0 = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadDIO10ConfigurationCmdFromFile()))
        P1 = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadDIO11ConfigurationCmdFromFile()))
        P2 = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadDIO12ConfigurationCmdFromFile()))
        P3 = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadDIO13ConfigurationCmdFromFile()))
        P4 = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadDIO14ConfigurationCmdFromFile()))
        if HV == Hardware_Extended:
            P5 = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadDIO15ConfigurationCmdFromFile()))
            P6 = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadDIO16ConfigurationCmdFromFile()))
            P7 = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadDIO17ConfigurationCmdFromFile()))
            P8 = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadDIO18ConfigurationCmdFromFile()))
            P9 = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadDIO19ConfigurationCmdFromFile()))
        PR = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadPullUpResistorEnableCmdFromFile()))
        PD = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadPullUpDownDirectionCmdFromFile()))
        LT = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadAssociatedLedBlinkTimeCmdFromFile()))
        RP = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadRssiPwmTimerCmdFromFile()))
        # I/O Sampling
        IR = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadIOSamplingRateCmdFromFile()))
        IC = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadDigitalIOChangeDetectionCmdFromFile()))
        Vplus = utils.hex_to_string(local_device.get_parameter(SysConfig.ReadSupplyVoltageHihgThresholdCmdFromFile()))




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
        print(" Number of Remaining Children:%s" % NC)
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
        print(" DIO6/nRTS Configuration  :   %s" % D6)
        print(" DIO7/nCTS Configuration:     %s" % D7)
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

        print(" +-----------------------------+")
        print(" | I/O Settings                |")
        print(" +-----------------------------+")
        print(" DIO0/ADO/CB Configuration:   %s" % D0)
        print(" DIO1/AD1 Configuration:      %s" % D1)
        print(" DIO2/AD2 Configuration:      %s" % D2)
        print(" DIO3/AD3 Configuration:      %s" % D3)
        print(" DIO4 Configuration:          %s" % D4)
        print(" DIO5 Configuration:          %s" % D5)
        print(" DIO8 Configuration:          %s" % D8)
        print(" DIO9 Configuration:          %s" % D9)
        print(" DIO10 Configuration:         %s" % P0)
        print(" DIO11 Configuration:         %s" % P1)
        print(" DIO12 Configuration:         %s" % P2)
        print(" DIO13 Configuration:         %s" % P3)
        print(" DIO14 Configuration:         %s" % P4)
        if HV == Hardware_Extended:
            print(" DIO15 Configuration:         %s" % P5)
            print(" DIO16 Configuration:         %s" % P6)
            print(" DIO17 Configuration:         %s" % P7)
            print(" DIO18 Configuration:         %s" % P8)
            print(" DIO19 Configuration:         %s" % P9)
        print(" Pull-UP Resistor Enable:     %s" % PR)
        print(" Pull-Up/down Direction:      %s" % PD)
        print(" Associate LED Blink Time:    %s" % LT)
        print(" RSSI PWM Timer:              %s" % RP + "\n")

        print(" +-----------------------------+")
        print(" | I/O Sampling                |")
        print(" +-----------------------------+")
        print(" IO Sampling Rate:            %s" % IR)
        print(" Digital IO Change Detection: %s" % IC)
        print(" Supply Votage High Thres.:   %s" % Vplus + "\n")

        print(" +-----------------------------+")
        print(" | Diagnostic Commands         |")
        print(" +-----------------------------+")
        print(" Firmaware Version:           %s" % VR)
        print(" Hardware Version:            %s" % HV)
        print(" Association Indication:      %s" % AI)
        print(" RSSI of Last Packet:         %s" % DB)
        print(" Supply Votage:               %s" % V + "\n")



    finally:
        if local_device is not None and local_device.is_open():
            local_device.close()


if __name__ == '__main__':
    main()