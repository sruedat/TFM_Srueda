# Sergio Rueda Teruel. 2018
# Este sofware ha sido desarrollado para el trabajo fin de master de la titulación
# Máster Unviersitario en Ingeniería de TElecomuniación UOC-URL de la
# Universisdad Oberta de Catalunya y lleva por título
# "Diseño de una WSN para la estimación del seein de l cúpla D080,
# en el Observatorio Astrofísico de Javalambre."

# Para la realización de este código se han utilizado las librerías python
# que la empresa Digi (Digi International Inc.) proporciona en su página web
# (https://www.digi.com/blog/xbee/introducing-the-official-digi-xbee-python-library/)

# este código está sometído a licencia de Reconocimiento-NoComercial-CompartirIgual
# 3.0 España de Creative Commons.



# Este módulo se utiliza para descubrir equipos remotos conectados a la misma red (PAN ID)
# que el equipo local, es desde este equipo local desde el que se realizan las tareas de
# descubrimiento.

import time, sys, argparse
import read_sys_config
from digi.xbee.models.status import NetworkDiscoveryStatus
from digi.xbee.devices import XBeeDevice
sys.tracebacklimit = 0

# Se admiten parámetros de depuración para la invocacción directa del módulo
# el parámetro -v VERBOSE muestra por consola la evolución del módulo
# discover-devices_xbee -v VERBOSE
parser= argparse.ArgumentParser()
parser.add_argument("-v","--verbose", help="Activates Verbose output")
args=parser.parse_args()

# Parámetros de conexión con el puerto serie al dispositivo local
port = read_sys_config.ReadLocalPortFromFile()
baud_rate = read_sys_config.ReadLocalBaudRateFromFile()



# La varible log será utilizada para ir registrando el avnace de todo el proceso
# y se devolvera en el procedimiento passlog para que pueda ser leida accedida
# por otros módulos
log=""

# Este procedimiento puede ser invocado por otros módulos para ir conociendo el estado
# del proceso de descrubirmiento de nodos en la red
def passlog():
    global log
    time.sleep(0.2)
    return log

# Procedimiento principla que gestiona las tareas de descubrimiento
def main():
    global log
    state = 0
    if args.verbose:
        print(" +---------------------------------------------+")
        print(" |       XBee Discover Devices Module          |")
        print(" +---------------------------------------------+\n")

    local_device = XBeeDevice(port, baud_rate)
    try:
        log=""
        local_device.open()

        xbee_network = local_device.get_network()

        xbee_network.set_discovery_timeout(15)  # 15 seconds.

        xbee_network.clear()

        # Callback for discovered devices.
        def callback_device_discovered(remote):
            global log
            log =log+"Device discovered:\n" + "%s" % remote +"\n\n"
            if args.verbose:
                print("Device discovered: " + "%s" % remote)
        # Callback for discovery finished.
        def callback_discovery_finished(status):
            global log
            if status == NetworkDiscoveryStatus.SUCCESS:
                log=log+"Discovery process finished successfully.\n"

                if args.verbose:
                    print("Discovery process finished successfully.")
            else:
                log= "There was an error discovering devices: %s\n" % status.description
                if args.verbose:
                    print("There was an error discovering devices: %s" % status.description)

        xbee_network.add_device_discovered_callback(callback_device_discovered)

        xbee_network.add_discovery_process_finished_callback(callback_discovery_finished)

        xbee_network.start_discovery_process()

        log = "\nDiscovering remote XBee devices...\n\n"
        if args.verbose:
            print("Discovering remote XBee devices...")


        while xbee_network.is_discovery_running():
            # Actualiza el log para otros módulos
            passlog()
            time.sleep(0.1)

        state = 1
        return state


    except:
        if local_device.is_open():
            local_device.close()
        pass

        # Si es invocado por otros módulos devuleve un 1 indicando que ya ha acabdo la fase de descubrimiento

    finally:
        if local_device is not None and local_device.is_open():
            local_device.close()
        sys._clear_type_cache()



if __name__ == '__main__':
    main()
