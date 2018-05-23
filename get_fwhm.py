from telegraf.client import TelegrafClient
from random import uniform
import time

DB_ADDR='192.168.1.44'
DB_PORT=8094
def main( ):
    try:
        while True:
            fwhm = round(uniform (0.5, 1.2),2)
            client = TelegrafClient(host=DB_ADDR, port=DB_PORT, tags={'host':'cpd'})
            client.metric('FWHM',{'C080':fwhm})
            time.sleep(60)

    except Exception as ex:
        print (ex)

if __name__ == '__main__':
    main()