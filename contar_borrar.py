import threading, time

def contar(hil):
    contador = 0
    while contador<10:
        contador += 1
        print (str(hil)+" "+ str(contador))
        time.sleep(5)



NUM_HILOS = 3

for num_hilo in range(NUM_HILOS):
    hilo = threading.Thread(name='hilo%s' %num_hilo,
                            target=contar, args=(num_hilo,))
    hilo.start()