from telegraf.client import TelegrafClient
import time

DB_ADDR='192.168.1.44'
DB_PORT=8094

def send_fwhm(fwhm):
    client = TelegrafClient(host=DB_ADDR, port=DB_PORT, tags={'host': 'CPD'})
    client.metric('FWHM', {'C080': fwhm})

def main(nodo,t1,t2,t3,t4,vcc):
    client = TelegrafClient(host=DB_ADDR, port=DB_PORT, tags={'host':nodo})
    #seeing_simulado = round(random.uniform(0.4, 1.9), 2)
    #client.metric('Seeing',seeing_simulado)
    #time.sleep(0.5)
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