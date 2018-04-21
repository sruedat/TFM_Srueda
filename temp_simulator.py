from telegraf.client import TelegrafClient
import random
import time


def main(t1,t2,t3,t4):
    client = TelegrafClient(host='192.168.1.20', port=8094, tags={'host':'Remoto_1'})
    #temp_simulada=25.0
    seeing_simulado=0.7
    #while True:
    seeing_simulado = round(random.uniform(0.4, 1.9), 2)
    #temp_simulada= round(temp_simulada+random.uniform(-1.0,1.0),2)
    #temp_simulada2=round(temp+random.uniform(-1.0,1.0),2)
    #temp_simulada3 = round(tempada2 + random.uniform(-1.0, 1.0), 2)
    #temp_simulada3=25
    temp_simulada4=24
    #if nodo==1:
    #    temp_simulada=temp
    #elif nodo==2:
    #    temp_simulada2=temp
    #temp_simulada4 = round(temp_simulada3 + random.uniform(-1.0, 1.0), 2)
    #time.sleep(15)
    #print(seeing_simulado)
    #print(temp_simulada)
    #print(temp_simulada2)
    #print(temp_simulada3)
    #print(temp_simulada4)
    client.metric('Seeing',seeing_simulado)
    time.sleep(0.5)
    client.metric('Temperatura',{'Sensor1':round(t1,3)})
    client.metric('Temperatura',{'Sensor2':round(t2,3)})
    client.metric('Temperatura',{'Sensor3':t3})
    client.metric('Temperatura',{'Sensor4':t4})
    time.sleep(1)


if __name__ == '__main__':
    main(0,0,0,0)