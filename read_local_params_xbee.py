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
import sys
import read_sys_config
sys.tracebacklimit = 1

def main():
    #log=""
    # Parámetros de conexión con el puerto serie al dispositivo local
    port = read_sys_config.ReadLocalPortFromFile()
    baud_rate = read_sys_config.ReadLocalBaudRateFromFile()
    local_device = XBeeDevice(port, baud_rate)


    try:

        print(" +-----------------------------------------------+")
        print(" |         Get Local XBee Parameters             |")
        print(" +-----------------------------------------------+\n")

        local_device.open()
       # Get Hardware Models with extended DIO (P5 to P9)
        Hardware_Extended = read_sys_config.ReadHardwareVersionWhithP5ToP9PinsFromFile()
       # Get parameters.
        # Diagnostic Commads
        VR = utils.hex_to_string(local_device.get_parameter("VR"))
        HV = utils.hex_to_string(local_device.get_parameter("HV"))
        AI = utils.hex_to_string(local_device.get_parameter("AI"))
        DB = utils.hex_to_string(local_device.get_parameter("DB"))
        V =  utils.hex_to_string(local_device.get_parameter("%V"))
        # Networking
        ID = utils.hex_to_string(local_device.get_parameter("ID"))
        SC = utils.hex_to_string(local_device.get_parameter("SC"))
        SD = utils.hex_to_string(local_device.get_parameter("SD"))
        ZS = utils.hex_to_string(local_device.get_parameter("ZS"))
        NJ = utils.hex_to_string(local_device.get_parameter("NJ"))
        NW = utils.hex_to_string(local_device.get_parameter("NW"))
        JV = utils.hex_to_string(local_device.get_parameter("JV"))
        JN = utils.hex_to_string(local_device.get_parameter("JN"))
        OP = utils.hex_to_string(local_device.get_parameter("OP"))
        OI = utils.hex_to_string(local_device.get_parameter("OI"))
        CH = utils.hex_to_string(local_device.get_parameter("CH"))
        NC = utils.hex_to_string(local_device.get_parameter("NC"))
        CE = utils.hex_to_string(local_device.get_parameter("CE"))
        DO = utils.hex_to_string(local_device.get_parameter("DO"))
        DC = utils.hex_to_string(local_device.get_parameter("DC"))
        # Addressing
        SH = utils.hex_to_string(local_device.get_parameter("SH"))
        SL = utils.hex_to_string(local_device.get_parameter("SL"))
        MY = utils.hex_to_string(local_device.get_parameter("MY"))
        MP = utils.hex_to_string(local_device.get_parameter("MP"))
        DH = utils.hex_to_string(local_device.get_parameter("DH"))
        DL = utils.hex_to_string(local_device.get_parameter("DL"))
        NI = local_device.get_parameter("NI").decode()
        NH = utils.hex_to_string(local_device.get_parameter("NH"))
        BH = utils.hex_to_string(local_device.get_parameter("BH"))
        AR = utils.hex_to_string(local_device.get_parameter("AR"))
        DD = utils.hex_to_string(local_device.get_parameter("DD"))
        NT = utils.hex_to_string(local_device.get_parameter("NT"))
        NO = utils.hex_to_string(local_device.get_parameter("NO"))
        NP = utils.hex_to_string(local_device.get_parameter("NP"))
        CR = utils.hex_to_string(local_device.get_parameter("CR"))
        # ZigBee Addressing
        SE = utils.hex_to_string(local_device.get_parameter("SE"))
        DE = utils.hex_to_string(local_device.get_parameter("DE"))
        CI = utils.hex_to_string(local_device.get_parameter("CI"))
        TO = utils.hex_to_string(local_device.get_parameter("TO"))
        # RF Interfacing
        PL = utils.hex_to_string(local_device.get_parameter("PL"))
        PM = utils.hex_to_string(local_device.get_parameter("PM"))
        PP = utils.hex_to_string(local_device.get_parameter("PP"))
        # Security
        EE = utils.hex_to_string(local_device.get_parameter("EE"))
        EO = utils.hex_to_string(local_device.get_parameter("EO"))
        KY = utils.hex_to_string(local_device.get_parameter("KY"))
        NK = utils.hex_to_string(local_device.get_parameter("NK"))
        # Serial Interfacing
        BD = utils.hex_to_string(local_device.get_parameter("BD"))
        NB = utils.hex_to_string(local_device.get_parameter("NB"))
        SB = utils.hex_to_string(local_device.get_parameter("SB"))
        RO = utils.hex_to_string(local_device.get_parameter("RO"))
        D6 = utils.hex_to_string(local_device.get_parameter("D6"))
        D7 = utils.hex_to_string(local_device.get_parameter("D7"))
        AP = utils.hex_to_string(local_device.get_parameter("AP"))
        AO = utils.hex_to_string(local_device.get_parameter("AO"))
        # AT Command Options
        CT = utils.hex_to_string(local_device.get_parameter("CT"))
        GT = utils.hex_to_string(local_device.get_parameter("GT"))
        CC = utils.hex_to_string(local_device.get_parameter("CC"))
        # Sleep Modes
        SP = utils.hex_to_string(local_device.get_parameter("SP"))
        SN = utils.hex_to_string(local_device.get_parameter("SN"))
        SM = utils.hex_to_string(local_device.get_parameter("SM"))
        ST = utils.hex_to_string(local_device.get_parameter("ST"))
        SO = utils.hex_to_string(local_device.get_parameter("SO"))
        WH = utils.hex_to_string(local_device.get_parameter("WH"))
        PO = utils.hex_to_string(local_device.get_parameter("PO"))
        # I/O Settomgs
        D0 = utils.hex_to_string(local_device.get_parameter("D0"))
        D1 = utils.hex_to_string(local_device.get_parameter("D1"))
        D2 = utils.hex_to_string(local_device.get_parameter("D2"))
        D3 = utils.hex_to_string(local_device.get_parameter("D3"))
        D4 = utils.hex_to_string(local_device.get_parameter("D4"))
        D5 = utils.hex_to_string(local_device.get_parameter("D5"))
        D8 = utils.hex_to_string(local_device.get_parameter("D8"))
        D9 = utils.hex_to_string(local_device.get_parameter("D9"))
        P0 = utils.hex_to_string(local_device.get_parameter("P0"))
        P1 = utils.hex_to_string(local_device.get_parameter("P1"))
        P2 = utils.hex_to_string(local_device.get_parameter("P2"))
        P3 = utils.hex_to_string(local_device.get_parameter("P3"))
        P4 = utils.hex_to_string(local_device.get_parameter("P4"))
        if HV == Hardware_Extended:
            P5 = utils.hex_to_string(local_device.get_parameter("P5"))
            P6 = utils.hex_to_string(local_device.get_parameter("P6"))
            P7 = utils.hex_to_string(local_device.get_parameter("P7"))
            P8 = utils.hex_to_string(local_device.get_parameter("P8"))
            P9 = utils.hex_to_string(local_device.get_parameter("P9"))
        PR = utils.hex_to_string(local_device.get_parameter("PR"))
        PD = utils.hex_to_string(local_device.get_parameter("PD"))
        LT = utils.hex_to_string(local_device.get_parameter("LT"))
        RP = utils.hex_to_string(local_device.get_parameter("RP"))
        # I/O Sampling
        IR = utils.hex_to_string(local_device.get_parameter("IR"))
        IC = utils.hex_to_string(local_device.get_parameter("IC"))
        Vplus = utils.hex_to_string(local_device.get_parameter("V+"))

        #print parameters
        log= " +-----------------------------+\n"
        log= log + " | Networking                  |\n"
        log = log + " +-----------------------------+\n"
        log = log + " PAN ID:                      %s" % ID + "\n"
        log = log + " Scan Channel:                %s" % SC + "\n"
        log = log + " Scan Duration:               %s" % SD + "\n"
        log = log + " Network Watchdog Timeout:    %s" % NW + "\n"
        log = log + " Channel Verification:        %s" % JV + "\n"
        log = log + " Join Notification:           %s" % JN + "\n"
        log = log + " Operating PAN ID:            %s" % OP + "\n"
        log = log + " Operating 16-bit PAN ID:     %s" % OI + "\n"
        log = log + " Operating Channel:           %s" % CH + "\n"
        log = log + " Number of Remaining Children:%s" % NC + "\n"
        log = log + " Coordinator Enable:          %s" % CE + "\n"
        log = log + " Device Options:              %s" % DO + "\n"
        log = log + " Device Controls:             %s" % DC + "\n\n"

        log = log + " +-----------------------------+\n"
        log = log + " | Addressing                  |\n"
        log = log + " +-----------------------------+\n"
        log = log + " Serial Number High:          %s" % SH + "\n"
        log = log + " Serial Number Low:           %s" % SL + "\n"
        log = log + " 16-bit Network Address:      %s" % MY + "\n"
        log = log + " 16-bit Parent Address:       %s" % MP + "\n"
        log = log + " Destination Address High:    %s" % DH + "\n"
        log = log + " Destination Address Low:     %s" % DL + "\n"
        log = log + " Node Identifier:             %s" % NI + "\n"
        log = log + " Maximum Hops:                %s" % NH + "\n"
        log = log + " Broadcast Radius:            %s" % BH + "\n"
        log = log + " Many-to-One Route Bro. Time: %s" % AR + "\n"
        log = log + " Device Type Identifier:      %s" % DD + "\n"
        log = log + " Node Discovery Backoff:      %s" % NT + "\n"
        log = log + " Node Discovery Options:      %s" % NO + "\n"
        log = log + " Maximum Num.Trans. Bytes:    %s" % NP + "\n"
        log = log + " PAN Conflict Threshold:      %s" % CR + "\n\n"

        log = log + " +-----------------------------+\n"
        log = log + " | ZigBee Addressing           |\n"
        log = log + " +-----------------------------+\n"
        log = log + " Zigbee Source Endpoint:      %s" % SE + "\n"
        log = log + " Zigbee Destination Endpoint: %s" % DE + "\n"
        log = log + " Zigbee Cluster ID:           %s" % CI + "\n"
        log = log + " Transmit Options:            %s" % TO + "\n\n"

        log = log + " +-----------------------------+\n"
        log = log + " | RF Interfacing              |\n"
        log = log + " +-----------------------------+\n"
        log = log + " Tx Power Level:              %s" % PL + "\n"
        log = log + " Power Mode:                  %s" % PM + "\n"
        log = log + " Power at PL4:                %s" % PP + "\n\n"

        log = log + " +-----------------------------+\n"
        log = log + " | Security                    |\n"
        log = log + " +-----------------------------+\n"
        log = log + " Encryption Enable:           %s" % EE + "\n"
        log = log + " Encryption Options:          %s" % EO + "\n"
        log = log + " Encryption Key:              %s" % KY + "\n"
        log = log + " Network Encryption Key:      %s" % NK + "\n\n"

        log = log + " +-----------------------------+\n"
        log = log + " | Serial Interfacing          |\n"
        log = log + " +-----------------------------+\n"
        log = log + " Baud Rate:                   %s" % BD + "\n"
        log = log + " Parity:                      %s" % NB + "\n"
        log = log + " Stop Bits:                   %s" % SB + "\n"
        log = log + " Packetization Timeout:       %s" % RO + "\n"
        log = log + " DIO6/nRTS Configuration  :   %s" % D6 + "\n"
        log = log + " DIO7/nCTS Configuration:     %s" % D7 + "\n"
        log = log + " API Enable:                  %s" % AP + "\n"
        log = log + " API Output Mode:             %s" % AO + "\n\n"

        log = log + " +-----------------------------+\n"
        log = log + " | AT Command Options          |\n"
        log = log + " +-----------------------------+\n"
        log = log + " AT Command Mode Timeout:     %s" % CT + "\n"
        log = log + " Guard Times:                 %s" % GT + "\n"
        log = log + " Command Sequence Character:  %s" % CC + "\n\n"

        log = log + " +-----------------------------+\n"
        log = log + " | Sleep Modes                 |\n"
        log = log + " +-----------------------------+\n"
        log = log + " Cyclic Sleep Period:         %s" % SP + "\n"
        log = log + " Number of Cyclic Sleep Per.: %s" % SN + "\n"
        log = log + " Sleep Mode:                  %s" % SM + "\n"
        log = log + " Time Before Sleep:sss        %s" % ST + "\n"
        log = log + " Sleep Options:               %s" % SO + "\n"
        log = log + " Wake Hosts:                  %s" % WH + "\n"
        log = log + " Poll Rate:                   %s" % PO + "\n\n"

        log = log + " +-----------------------------+\n"
        log = log + " | I/O Settings                |\n"
        log = log + " +-----------------------------+\n"
        log = log + " DIO0/ADO/CB Configuration:   %s" % D0 + "\n"
        log = log + " DIO1/AD1 Configuration:      %s" % D1 + "\n"
        log = log + " DIO2/AD2 Configuration:      %s" % D2 + "\n"
        log = log + " DIO3/AD3 Configuration:      %s" % D3 + "\n"
        log = log + " DIO4 Configuration:          %s" % D4 + "\n"
        log = log + " DIO5 Configuration:          %s" % D5 + "\n"
        log = log + " DIO8 Configuration:          %s" % D8 + "\n"
        log = log + " DIO9 Configuration:          %s" % D9 + "\n"
        log = log + " DIO10 Configuration:         %s" % P0 + "\n"
        log = log + " DIO11 Configuration:         %s" % P1 + "\n"
        log = log + " DIO12 Configuration:         %s" % P2 + "\n"
        log = log + " DIO13 Configuration:         %s" % P3 + "\n"
        log = log + " DIO14 Configuration:         %s" % P4 + "\n"
        if HV == Hardware_Extended:
            log = log + " DIO15 Configuration:         %s" % P5 + "\n"
            log = log + " DIO16 Configuration:         %s" % P6 + "\n"
            log = log + " DIO17 Configuration:         %s" % P7 + "\n"
            log = log + " DIO18 Configuration:         %s" % P8 + "\n"
            log = log + " DIO19 Configuration:         %s" % P9 + "\n"
        log = log + " Pull-UP Resistor Enable:     %s" % PR + "\n"
        log = log + " Pull-Up/down Direction:      %s" % PD + "\n"
        log = log + " Associate LED Blink Time:    %s" % LT + "\n"
        log = log + " RSSI PWM Timer:              %s" % RP + "\n\n"

        log = log + " +-----------------------------+\n"
        log = log + " | I/O Sampling                |\n"
        log = log + " +-----------------------------+\n"
        log = log + " IO Sampling Rate:            %s" % IR + "\n"
        log = log + " Digital IO Change Detection: %s" % IC + "\n"
        log = log + " Supply Votage High Thres.:   %s" % Vplus + "\n\n"

        log = log + " +-----------------------------+\n"
        log = log + " | Diagnostic Commands         |\n"
        log = log + " +-----------------------------+\n"
        log = log + " Firmaware Version:           %s" % VR + "\n"
        log = log + " Hardware Version:            %s" % HV + "\n"
        log = log + " Association Indication:      %s" % AI + "\n"
        log = log + " RSSI of Last Packet:         %s" % DB + "\n"
        log = log + " Supply Votage:               %s" % V + "\n\n"
        print (log)
        '''
        #print(" +-----------------------------+")
        #print(" | Networking                  |")
        print(" ZigBee Stack Profile:        %s" % ZS)
        print(" Node Join Time:              %s" % NJ)
        print(" +-----------------------------+")
        print(" PAN ID:                      %s" % ID)
        print(" Scan Channel:                %s" % SC)
        print(" Scan Duration:               %s" % SD)
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
'''
    except:
        if local_device.is_open():
            local_device.close()
        log ="Sorry an error has happened"
        pass


    finally:
        if local_device is not None and local_device.is_open():
            local_device.close()
        pass


    return log

if __name__ == '__main__':
    main()