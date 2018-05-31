# Sergio Rueda Teruel. 2018
# Este software ha sido desarrollado para el trabajo fin de máster de la titulación
# Máster Universitario en Ingeniería de Telecomunicación UOC-URL de la
# Universidad Oberta de Catalunya y lleva por título
# "Diseño de una WSN para la estimación del seeing de la cúpula D080,
# en el Observatorio Astrofísico de Javalambre."
# Este código está sometido a licencia de Reconocimiento-NoComercial-CompartirIgual
# 3.0 España de Creative Commons.

# Este módulo incorpora una serie de funciones que son llamadas por otros módulos para
# el envío de las métricas a telegraf y así este agente las incorporará en la BD
# Se ha hecho uso de la librería pytelegraf


from telegraf.client import TelegrafClient
import time

#DB_ADDR='192.168.1.44'
DB_ADDR='10.10.64.109'
DB_PORT=8094

# Envío de la metrica de fwhm con timestamp de la adquisición
def send_fwhm_with_timestamp(fwhm, time):
    client = TelegrafClient(host=DB_ADDR, port=DB_PORT, tags={'host': 'CPD'})
    client.metric('FWHM', {'time': time})
    client.metric('FWHM', {'C080': fwhm})

# Envío de la metrica de fwhm el timestamp es el del momento de la inserción
def send_fwhm(fwhm):
    client = TelegrafClient(host=DB_ADDR, port=DB_PORT, tags={'host': 'CPD'})
    client.metric('FWHM', {'C080': fwhm})

# Envío de la metrica de temperatura de los 4 sensores de un nodo y de su valor de alimentación
def main(nodo,t1,t2,t3,t4,vcc):
    client = TelegrafClient(host=DB_ADDR, port=DB_PORT, tags={'host':nodo})
    client.metric('Temperatura',{'Sensor1':round(t1,3)})
    client.metric('Temperatura',{'Sensor2':round(t2,3)})
    client.metric('Temperatura',{'Sensor3':round(t3,3)})
    client.metric('Temperatura',{'Sensor4':round(t4,3)})
    client.metric('Temperatura',{'diff_s1-s2':round(t1-t2,3)})
    client.metric('Temperatura',{'diff_s3-s4': round(t3 - t4, 3)})
    client.metric('Temperatura', {'mean': round((t1+t2+t3+t4)/4, 3)})
    client.metric('Power_Supply',{'Power': round(vcc/1000,2)}) # en voltios
    time.sleep(1)


if __name__ == '__main__':
    main('Remoto_1',0,0,0,0,0)