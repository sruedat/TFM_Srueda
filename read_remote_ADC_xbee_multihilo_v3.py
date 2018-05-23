# Copyright 2017, Digi International Inc.
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
from digi.xbee.io import IOLine, IOMode
from digi.xbee.util import utils
from digi.xbee.exception import TimeoutException
from datetime import datetime
import time, sys, threading, math
import read_sys_config
import read_node_list
import queue
import send_data_to_telegraf

sys.tracebacklimit = 0

# Parámetros de conexión con el puerto serie al dispositivo local
port = read_sys_config.ReadLocalPortFromFile()
baud_rate = read_sys_config.ReadLocalBaudRateFromFile()

#REMOTE_NODE_ID = "REMOTO_1"
REMOTE_NODES_ID = read_node_list.ReadListOfNodesFromFile()
IOLINE_IN_3 = IOLine.DIO3_AD3
IOLINE_IN_2 = IOLine.DIO2_AD2
IOLINE_IN_1 = IOLine.DIO1_AD1
IOLINE_IN_0 = IOLine.DIO0_AD0
MAX_VOLTAGE_INPUT = 1200
MAX_INTENTOS_DESCUBRIMIENTO = 10 # número máximo de intentos de descubrir a un nodo
MAX_INTENTOS_LEER_DATOS = 10 # número máximo de intentos de descubrir a un nodo
LONG_WAIT=30
SHORT_WAIT=0.5




#Calculo de las temperaturas en función del valor de la entrada analógica y la tensión de suministro
def ntc10k_calculate_temp(raw_value, volts):
    # mV
    voltage = (MAX_VOLTAGE_INPUT * raw_value / 1024)
    Rntc = 210000 * (voltage / (volts - voltage))
    log=""
    log=str(Rntc)
    #AJUSTE_CUADRÁTICO
    a=574.1
    b=-0.1242
    c= -158
    temperatureC =a*(pow(Rntc,b))+c
    log = log +" ntc 10K temper: %.2f" % temperatureC
    print(log)
    return temperatureC






def main():

    exitFlag = 0

    class myThread (threading.Thread):
        def __init__(self, threadID, name, q):
            threading.Thread.__init__(self)
            self.threadID = threadID
            self.name = name
            self.q = q

        def run(self):
            print ("Starting " + self.name)
            process_data(self.name, self.q)
            print ("Exiting " + self.name)

    def process_data(threadName, q):
        while not exitFlag:
            queueLock.acquire()
            if not workQueue.empty():
                data = q.get()
                queueLock.release()
                print ("%s processing %s" % (threadName, data))
            else:
                queueLock.release()
                print("ssssss")
                time.sleep(1)


    threadList = ["Thread-1", "Thread-2", "Thread-3", "Thread-4"]
    nameList = ["One", "Two", "Three", "Four", "Five"]
    queueLock = threading.Lock()
    workQueue = queue.Queue(10)
    threads = []
    threadID = 1

# Create new threads
    for tName in threadList:
        thread = myThread(threadID, tName, workQueue)
        thread.start()
        threads.append(thread)
        threadID += 1

# Fill the queue
    queueLock.acquire()
    for word in nameList:
        workQueue.put(word)
    queueLock.release()

# Wait for queue to empty
    while not workQueue.empty():
        pass

# Notify threads it's time to exit
    exitFlag = 1

# Wait for all threads to complete
    for t in threads:
        t.join()
    print ("Exiting Main Thread")



if __name__ == '__main__':
    main()
