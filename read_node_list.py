# Sergio Rueda Teruel. 2018
# Este software ha sido desarrollado para el trabajo fin de máster de la titulación
# Máster Universitario en Ingeniería de Telecomunicación UOC-URL de la
# Universidad Oberta de Catalunya y lleva por título
# "Diseño de una WSN para la estimación del seeing de la cúpula D080,
# en el Observatorio Astrofísico de Javalambre."
# Este código está sometido a licencia de Reconocimiento-NoComercial-CompartirIgual
# 3.0 España de Creative Commons.

# Este módulo incorpora una función que es llamada por otros módulos para
# determinar el número de nodos que queramos encuestar para la aquisición
# de datos y el NI (Node identificator) de cada uno de ellos.

CONFIG_FILE = "config/list_of_nodes.ini"

def ReadListOfNodesFromFile():
    with open(CONFIG_FILE, "r") as ins:
        array = []
        for line in ins:
            array.append(line.strip('\n'))
    return array


if __name__ == '__main__':
    ReadListOfNodesFromFile()




