# Sergio Rueda Teruel. 2018
# Este software ha sido desarrollado para el trabajo fin de máster de la titulación
# Máster Universitario en Ingeniería de Telecomunicación UOC-URL de la
# Universidad Oberta de Catalunya y lleva por título
# "Diseño de una WSN para la estimación del seeing de la cúpula D080,
# en el Observatorio Astrofísico de Javalambre."
# Este código está sometido a licencia de Reconocimiento-NoComercial-CompartirIgual
# 3.0 España de Creative Commons.

# Este módulo incorpora una serie de funciones que son llamadas por otros módulos para
# la lectura de los parámetros de configuración del puerto serie.
# También se indica que versión de hardware presenta entradas P5 a P9, ya que no todas
# las versiones de hardware lo hacen


import configparser

CONFIG_FILE = "config/sys_config.ini"

settings = configparser.ConfigParser()
settings.read(CONFIG_FILE)



def ReadHardwareVersionWhithP5ToP9PinsFromFile():
    return settings.get("COMMON", "HARDWARE_VERSION_WITH_P5_TO_P9")

def ReadLocalPortFromFile():
    return settings.get("COMMON", "PORT")


def ReadLocalBaudRateFromFile():
    return settings.get("COMMON", "PORT_BAUD_RATE")

def main():
    try:
        settings.read(CONFIG_FILE)

    except:
        print("error openning config.ini")


if __name__ == '__main__':
    main()




