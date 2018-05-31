# Sergio Rueda Teruel. 2018
# Este software ha sido desarrollado para el trabajo fin de máster de la titulación
# Máster Universitario en Ingeniería de Telecomunicación UOC-URL de la
# Universidad Oberta de Catalunya y lleva por título
# "Diseño de una WSN para la estimación del seeing de la cúpula D080,
# en el Observatorio Astrofísico de Javalambre."
# Para la realización de este código se han utilizado las librerías Python
# que la empresa Digi (Digi International Inc.) proporciona en su página web
# (https://www.digi.com/blog/xbee/introducing-the-official-digi-xbee-python-library/)
# este código está sometido a licencia de Reconocimiento-NoComercial-CompartirIgual
# 3.0 España de Creative Commons.

# Este módulo se utiliza para la lectura de los parámetros de configuración a través de
# RF de un nodo remoto, dicha lectura se hace a través del nodo local.
# Los parámetros se muestran por pantalla y se crea un log que puede ser
# recogido por otros módulos para su visualización. (Módulo gui.py en este proyecto)

from digi.xbee.devices import XBeeDevice
from digi.xbee.devices import RemoteZigBeeDevice
from digi.xbee.util import utils
from digi.xbee.models.address import XBee64BitAddress
import sys
import read_sys_config
sys.tracebacklimit = 0

# Valor del nodo remoto por defecto si no le pasamos otro valor
PARAM_VALUE_REMOTE_NODE_ADDR="0013A200416299FE"


# Parámetros de conexión con el puerto serie al dispositivo local
PORT=read_sys_config.ReadLocalPortFromFile()
BAUD_RATE = read_sys_config.ReadLocalBaudRateFromFile()



def main(NodeAddress):
    if NodeAddress =="":
        NodeAddress=PARAM_VALUE_REMOTE_NODE_ADDR
    Address=XBee64BitAddress.from_hex_string(NodeAddress)

    print(" +------------------------------------------------------+")
    print(" |  Get Remote XBee (" + NodeAddress + ") parameters       |")
    print(" +------------------------------------------------------+\n")

    local_device = XBeeDevice(PORT, BAUD_RATE)


    try:
        local_device.open()
        remote_device = RemoteZigBeeDevice(local_device, Address)

        # Determinar que versión de hardware es el nodo para saber que parámetros
        # se pueden configurar
        Hardware_Extended = read_sys_config.ReadHardwareVersionWhithP5ToP9PinsFromFile()
       # Get parameters.
        # Diagnostic Commads
        VR = utils.hex_to_string(remote_device.get_parameter("VR"))
        HV = utils.hex_to_string(remote_device.get_parameter("HV"))
        AI = utils.hex_to_string(remote_device.get_parameter("AI"))
        DB = utils.hex_to_string(remote_device.get_parameter("DB"))
        V =  utils.hex_to_string(remote_device.get_parameter("%V"))
        # Networking
        ID = utils.hex_to_string(remote_device.get_parameter("ID"))
        SC = utils.hex_to_string(remote_device.get_parameter("SC"))
        SD = utils.hex_to_string(remote_device.get_parameter("SD"))
        ZS = utils.hex_to_string(remote_device.get_parameter("ZS"))
        NJ = utils.hex_to_string(remote_device.get_parameter("NJ"))
        NW = utils.hex_to_string(remote_device.get_parameter("NW"))
        JV = utils.hex_to_string(remote_device.get_parameter("JV"))
        JN = utils.hex_to_string(remote_device.get_parameter("JN"))
        OP = utils.hex_to_string(remote_device.get_parameter("OP"))
        OI = utils.hex_to_string(remote_device.get_parameter("OI"))
        CH = utils.hex_to_string(remote_device.get_parameter("CH"))
        NC = utils.hex_to_string(remote_device.get_parameter("NC"))
        CE = utils.hex_to_string(remote_device.get_parameter("CE"))
        DO = utils.hex_to_string(remote_device.get_parameter("DO"))
        DC = utils.hex_to_string(remote_device.get_parameter("DC"))
        # Addressing
        SH = utils.hex_to_string(remote_device.get_parameter("SH"))
        SL = utils.hex_to_string(remote_device.get_parameter("SL"))
        MY = utils.hex_to_string(remote_device.get_parameter("MY"))
        MP = utils.hex_to_string(remote_device.get_parameter("MP"))
        DH = utils.hex_to_string(remote_device.get_parameter("DH"))
        DL = utils.hex_to_string(remote_device.get_parameter("DL"))
        NI = remote_device.get_parameter("NI").decode()
        NH = utils.hex_to_string(remote_device.get_parameter("NH"))
        BH = utils.hex_to_string(remote_device.get_parameter("BH"))
        AR = utils.hex_to_string(remote_device.get_parameter("AR"))
        DD = utils.hex_to_string(remote_device.get_parameter("DD"))
        NT = utils.hex_to_string(remote_device.get_parameter("NT"))
        NO = utils.hex_to_string(remote_device.get_parameter("NO"))
        NP = utils.hex_to_string(remote_device.get_parameter("NP"))
        CR = utils.hex_to_string(remote_device.get_parameter("CR"))
        # ZigBee Addressing
        SE = utils.hex_to_string(remote_device.get_parameter("SE"))
        DE = utils.hex_to_string(remote_device.get_parameter("DE"))
        CI = utils.hex_to_string(remote_device.get_parameter("CI"))
        TO = utils.hex_to_string(remote_device.get_parameter("TO"))
        # RF Interfacing
        PL = utils.hex_to_string(remote_device.get_parameter("PL"))
        PM = utils.hex_to_string(remote_device.get_parameter("PM"))
        PP = utils.hex_to_string(remote_device.get_parameter("PP"))
        # Security
        EE = utils.hex_to_string(remote_device.get_parameter("EE"))
        EO = utils.hex_to_string(remote_device.get_parameter("EO"))
        KY = utils.hex_to_string(remote_device.get_parameter("KY"))
        NK = utils.hex_to_string(remote_device.get_parameter("NK"))
        # Serial Interfacing
        BD = utils.hex_to_string(remote_device.get_parameter("BD"))
        NB = utils.hex_to_string(remote_device.get_parameter("NB"))
        SB = utils.hex_to_string(remote_device.get_parameter("SB"))
        RO = utils.hex_to_string(remote_device.get_parameter("RO"))
        D6 = utils.hex_to_string(remote_device.get_parameter("D6"))
        D7 = utils.hex_to_string(remote_device.get_parameter("D7"))
        AP = utils.hex_to_string(remote_device.get_parameter("AP"))
        AO = utils.hex_to_string(remote_device.get_parameter("AO"))
        # AT Command Options
        CT = utils.hex_to_string(remote_device.get_parameter("CT"))
        GT = utils.hex_to_string(remote_device.get_parameter("GT"))
        CC = utils.hex_to_string(remote_device.get_parameter("CC"))
        # Sleep Modes
        SP = utils.hex_to_string(remote_device.get_parameter("SP"))
        SN = utils.hex_to_string(remote_device.get_parameter("SN"))
        SM = utils.hex_to_string(remote_device.get_parameter("SM"))
        ST = utils.hex_to_string(remote_device.get_parameter("ST"))
        SO = utils.hex_to_string(remote_device.get_parameter("SO"))
        WH = utils.hex_to_string(remote_device.get_parameter("WH"))
        PO = utils.hex_to_string(remote_device.get_parameter("PO"))
        # I/O Settomgs
        D0 = utils.hex_to_string(remote_device.get_parameter("D0"))
        D1 = utils.hex_to_string(remote_device.get_parameter("D1"))
        D2 = utils.hex_to_string(remote_device.get_parameter("D2"))
        D3 = utils.hex_to_string(remote_device.get_parameter("D3"))
        D4 = utils.hex_to_string(remote_device.get_parameter("D4"))
        D5 = utils.hex_to_string(remote_device.get_parameter("D5"))
        D8 = utils.hex_to_string(remote_device.get_parameter("D8"))
        D9 = utils.hex_to_string(remote_device.get_parameter("D9"))
        P0 = utils.hex_to_string(remote_device.get_parameter("P0"))
        P1 = utils.hex_to_string(remote_device.get_parameter("P1"))
        P2 = utils.hex_to_string(remote_device.get_parameter("P2"))
        P3 = utils.hex_to_string(remote_device.get_parameter("P3"))
        P4 = utils.hex_to_string(remote_device.get_parameter("P4"))
        if HV == Hardware_Extended:
            P5 = utils.hex_to_string(remote_device.get_parameter("P5"))
            P6 = utils.hex_to_string(remote_device.get_parameter("P6"))
            P7 = utils.hex_to_string(remote_device.get_parameter("P7"))
            P8 = utils.hex_to_string(remote_device.get_parameter("P8"))
            P9 = utils.hex_to_string(remote_device.get_parameter("P9"))
        PR = utils.hex_to_string(remote_device.get_parameter("PR"))
        PD = utils.hex_to_string(remote_device.get_parameter("PD"))
        LT = utils.hex_to_string(remote_device.get_parameter("LT"))
        RP = utils.hex_to_string(remote_device.get_parameter("RP"))
        # I/O Sampling
        IR = utils.hex_to_string(remote_device.get_parameter("IR"))
        IC = utils.hex_to_string(remote_device.get_parameter("IC"))
        Vplus = utils.hex_to_string(remote_device.get_parameter("V+"))

        # log parameters
        log = " +-----------------------------+\n"
        log = log + " | Networking                  |\n"
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


    except:
        log="No device found\n"
        if local_device.is_open():
            local_device.close()
        pass


    finally:
        if local_device.is_open():
            local_device.close()

    return log

if __name__ == '__main__':
    main(PARAM_VALUE_REMOTE_NODE_ADDR)