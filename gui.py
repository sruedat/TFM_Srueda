# Sergio Rueda Teruel. 2018
# Este software ha sido desarrollado para el trabajo fin de máster de la titulación
# Máster Universitario en Ingeniería de Telecomunicación UOC-URL de la
# Universidad Oberta de Catalunya y lleva por título
# "Diseño de una WSN para la estimación del seeing de la cúpula D080,
# en el Observatorio Astrofísico de Javalambre."
# Este código está sometido a licencia de Reconocimiento-NoComercial-CompartirIgual
# 3.0 España de Creative Commons.

# Este módulo se utiliza para la creación de la interface gráfica con la que gestionar
# toda la red, permite leer la configuración del nodo local, la configuración de nodos
# remotos indicando su dirección. Además, también permite escribir la configuración del
# nodo local y/o remotos mediante sus correspondientes archivos de configuración

import tkinter as tk
from tkinter import ttk
import threading
import queue
import time
import os
import platform
import subprocess

# módulos espcificamente desarrollados para este TFM
import discover_devices_xbee    # Este módulo gestiona el decubrimiento de nodos remotos vía RF
import read_local_params_xbee   # Desde este módulo se leen los parámetros del nodo conectado al puerto serie
import read_remote_params_xbee  # Desde este módulo se leen los parámetros de un nodo remoto vía RF
import write_remote_params_xbee # Con este módulo se escriben parámetros a un nodo remoto vía RF
import write_local_params_xbee  # Con este módulo se escriben parámetros al nodo local por puerto serie


# Aplicación
class Application(tk.Frame):
    # Creación del master frame que alberga todos los componentes
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        master.title("SRueda. - Xbee Zigbee Tool")
        master.columnconfigure(1, weight=1)
        master.columnconfigure(1, weight=1)
        master.rowconfigure(1, weight=1)
        master.rowconfigure(1, weight=1)
        self.queue = queue.Queue()
        self.create_widgets()

    # Función para definir el directorio dónde están los arhivos de configuración que son leídos por varios de los
    # módulos importados, es válido para SO Windows, Mac y GNU-Linux
    def open_config_file(self):
        dirname= os.path.dirname(__file__)+ "/config"
        if platform.system() == "Windows":
            os.startfile(dirname)
        elif platform.system() == "Darwin":
            subprocess.Popen(["open", dirname])
        else:
            subprocess.Popen(["xdg-open", dirname])

    # Desde esta función se habilitan todos los botones de la apliación ::::::::::::::::::
    def enable_all_bottons(self):
        self.discover['state'] = "normal"
        self.clear_discover['state'] = "normal"
        self.read_local_conf['state'] = "normal"
        self.write_local_conf['state'] = "normal"
        self.read_remote_conf['state'] = "normal"
        self.write_remote_conf['state'] = "normal"
        self.clear_params['state'] = "normal"
        self.open_file['state'] = "normal"
    #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

    # Función para deshabilitar todos los botones de la aplicación ::::::::::::::::::::
    def disable_all_bottons(self):
        self.discover['state']=tk.DISABLED
        self.clear_discover['state']=tk.DISABLED
        self.read_local_conf['state']=tk.DISABLED
        self.write_local_conf['state']=tk.DISABLED
        self.read_remote_conf['state']=tk.DISABLED
        self.write_remote_conf['state']=tk.DISABLED
        self.clear_params['state']=tk.DISABLED
        self.open_file['state']=tk.DISABLED
    #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

    # Desde estas funciones se realiza la lectura de parámetros de un módulo remoto,
    # la selección del módulo se realiza en base a su dirección MAC introducida en la GUI
    @staticmethod
    def read_remote_xbee_cmmd(self):
        # Comprobamos que la dirección del nodo introducida tenga una longitud
        # de 16 caracteres, si no es así, se completa con ceros a la izquierda
        data = self.remote_address.get()[:16]
        if len(data)<16:
            for n in range (len(data),16):
                data= "0" + data
        # Indicamos en el panel de texto que se va a intentar acceder al nodo remoto
        self.text_params.config(state="normal")
        self.text_params.insert(tk.INSERT,'Trying to access to remote device: ' + data + '\n\n')
        # Se llama al módulo para la lectura de parámetros del nodo remoto pasándole la dirección
        self.text_params.insert(tk.INSERT, read_remote_params_xbee.main(data))
        self.text_params.config(state=tk.DISABLED)
        self.enable_all_bottons()

    def read_remote_xbee(self):
        # Indicamos en el panel de texto que se va a lanzar la lectura del nodo remoto
        self.text_params.config(state="normal")
        self.text_params.delete('1.0', tk.END)
        self.text_params.insert(tk.INSERT, " \nReading remote node... \n\n")
        self.text_params.config(state=tk.DISABLED)
        self.disable_all_bottons()
        # Para evitar que la aplicación se bloque mientras se realiza la lectura del módulo remoto
        # se hace la llamada en multihilo, así se realiza por un lado el mainloop y por el otro la
        # lectura del nodo remoto
        threading.Thread(target=self.read_remote_xbee_cmmd,
                         args=(self, )).start()
    #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

    # Desde estas funciones se realiza la escritura de parámetros a un módulo remoto,
    # la selección del módulo se realiza en base a su dirección MAC introducida en la GUI
    @staticmethod
    def write_remote_xbee_cmmd(self, boton1, boton2, boton3):
        self.text_params.config(state="normal")
        # the propper length of the address is 2 bytes, we must
        address = self.remote_address.get()[:16]
        if len(address)<16:
            for n in range (len(address),16):
                address= "0" + address
        self.text_params.insert(tk.INSERT,'Trying to access to remote device: ' + address + '\n\n')
        self.text_params.insert(tk.INSERT, write_remote_params_xbee.main(address))
        self.text_params.config(state=tk.DISABLED)
        self.enable_all_bottons()

    def write_remote_xbee(self):
        self.text_params.config(state="normal")
        self.text_params.delete('1.0', tk.END)
        self.text_params.insert(tk.INSERT, " \nWriting remote node... \n\n")
        self.text_params.config(state=tk.DISABLED)
        self.disable_all_bottons()
        threading.Thread(target=self.write_remote_xbee_cmmd,
                         args=(self, self.read_local_conf, self.read_remote_conf, self.clear_params,)).start()
    #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::


    # Desde estas funciones se realiza la lectura de parámetros del módulo local conectado al puerto serie
    def read_local_xbee(self):
        self.text_params.config(state="normal")
        self.text_params.delete('1.0', tk.END)
        self.text_params.insert(tk.INSERT, " \nReading local node... \n\n")
        self.text_params.config(state=tk.DISABLED)
        self.disable_all_bottons()
        threading.Thread(target=self.read_local_xbee_cmmd, args=(self,)).start()

    @staticmethod
    def read_local_xbee_cmmd(self):
        self.text_params.config(state="normal")
        self.text_params.insert(tk.INSERT, read_local_params_xbee.main())
        self.text_params.config(state=tk.DISABLED)
        self.enable_all_bottons()
    #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

    # Desde estas funciones se realiza la escritura de parámetros del módulo local conectado al puerto serie
    def write_local_xbee(self):
        self.text_params.config(state="normal")
        self.text_params.delete('1.0', tk.END)
        self.text_params.insert(tk.INSERT, " \nWriting local node... \n\n")
        self.text_params.config(state=tk.DISABLED)
        self.disable_all_bottons()
        threading.Thread(target=self.write_local_xbee_cmmd,
                             args=(self, )).start()

    @staticmethod
    def write_local_xbee_cmmd(self):
        self.text_params.config(state="normal")
        # the propper length of the address is 2 bytes, we must
        address = "local_node"
        self.text_params.insert(tk.INSERT, 'Trying to access to local device: ' + address + '\n\n')
        self.text_params.insert(tk.INSERT, write_local_params_xbee.main(address))
        self.text_params.config(state=tk.DISABLED)
        self.enable_all_bottons()
    #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

    #Esta función borra la información de los parámetros del nodo
    def clear_readed_params(self):
        self.text_params.config(state="normal")
        self.text_params.delete('1.0', tk.END)
        self.text_params.insert(tk.INSERT, '\n Please press "Read local conf." to read local node params\n'
                                           ' or put address and press "Read remote conf." to read remote node params')
        self.text_params.config(state=tk.DISABLED)
    #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

    #Esta función borra la lista de nodos descubiertos
    def clear_discovered_nodes(self):
        self.text_discover.config(state="normal")
        self.text_discover.delete('1.0', tk.END)
        self.text_discover.insert(tk.INSERT, '\nPress "Search Nodes" to find remote XBees \n')
        self.text_discover.config(state=tk.DISABLED)
    #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

    # Estas funciones actualizan los mensajes por pantalla en el proceso de descubrimiento de los nodos remotos
    @staticmethod
    # Mientras que no se haya acabado el proceso de descubrimiento va leyendo el log y lo mete en la cola
    def update_discover_log(self,cola):
        self.disable_all_bottons()
        while self.discover_status != 1:
            log=discover_devices_xbee.passlog()
            cola.put(log)
            time.sleep(0.1)

    # Si el status devuelto por el modulo para descubrir nodos es = 1 se acabó el proceso de descubrimiento
    def search(self):
        self.discover_status=discover_devices_xbee.main()
        self.enable_all_bottons()

    # Gestión de las colas del log, mientras la cola no está vacía va sacando mensajes
    def process_queue(self):
        try:
            data = self.queue.get_nowait()
            self.text_discover.config(state="normal")
            self.text_discover.delete('1.0', tk.END)
            self.text_discover.insert(tk.INSERT,data)
        except queue.Empty:
            pass
        self.master.after(100, self.process_queue)

    # Función principal de la gestión de mensajes por pantalla en el proceso de descubrimiento, se trata de unas
    # llamadas multi-hilo para la llamada al módulo importado desde el que se realiza el proceso de descubrimiento
    # y para el llenado de la cola de mensajes del procedimiento
    def update_status(self):
        self.discover_status = 0
        self.text_discover.delete('1.0', tk.END)
        self.clear_discover['state']=tk.DISABLED
        threading.Thread(target=self.update_discover_log,
                         args=(self, self.queue,)).start()
        threading.Thread(target=self.search).start()
        self.after(100, self.process_queue)
    #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::




    # Función para la creación del inteface gráfico en sí mismo, crea paneles, botones, etc.
    def create_widgets(self):
        # Panel izquierdo
        left_pane = tk.PanedWindow(root, orient=tk.VERTICAL)
        left_pane.grid(column=0, row=0, rowspan=2, sticky=(tk.N, tk.W, tk.E, tk.S))
        left_upperframe = ttk.Frame(root, relief='groove', borderwidth=2)
        left_upperframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        left_upperframe.columnconfigure(0, weight=1)
        left_upperframe.rowconfigure(0, weight=1)
        left_pane.add(left_upperframe, heigh=500, width=400)
        left_bottomframe = ttk.Frame(left_pane, relief='groove', borderwidth=2)
        left_bottomframe.grid(column=0, row=1, sticky=(tk.N, tk.W, tk.E, tk.S))
        left_bottomframe.columnconfigure(0, weight=1)
        left_bottomframe.rowconfigure(0, weight=1)
        left_pane.add(left_bottomframe, heigh=40)

        # Panel derecho
        right_pane = tk.PanedWindow(root, orient=tk.VERTICAL)
        right_pane.grid(column=1, row=0, rowspan=2, sticky=(tk.N, tk.W, tk.E, tk.S))
        right_upperframe = ttk.Frame(root, relief='groove', borderwidth=2)
        right_upperframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        right_upperframe.rowconfigure(0, weight=3)
        right_pane.add(right_upperframe, width=600, heigh=500)
        right_bottomframe = ttk.Frame(right_pane, relief='groove', borderwidth=2)
        right_bottomframe.grid(column=0, row=1, sticky=(tk.N, tk.W, tk.E, tk.S))
        right_bottomframe.columnconfigure(0, weight=1)
        right_bottomframe.rowconfigure(0, weight=1)
        right_pane.add(right_bottomframe)

        # Botones
        #discover
        self.discover = tk.Button(left_bottomframe)
        self.discover["text"] = "Search Nodes"
        self.discover["command"] = self.update_status
        self.discover.grid(column=0, row=0, sticky=(tk.W, tk.S, tk.E, tk.N))
        #clear discover
        self.clear_discover = tk.Button(left_bottomframe)
        self.clear_discover["text"] = "Clear"
        self.clear_discover["command"] = self.clear_discovered_nodes  # self.UpdateDiscoveringState
        self.clear_discover.grid(column=1, row=0, sticky=(tk.W, tk.S, tk.E, tk.N))
        #read local configuration
        self.read_local_conf = tk.Button(right_bottomframe)
        self.read_local_conf["text"] = "Read local conf."
        self.read_local_conf["command"] = self.read_local_xbee
        self.read_local_conf.grid(column=2, row=1, sticky=(tk.W, tk.S, tk.E, tk.N))
        # write local configuration
        self.write_local_conf = tk.Button(right_bottomframe)
        self.write_local_conf["text"] = "Write local conf."
        self.write_local_conf["command"] = self.write_local_xbee
        self.write_local_conf.grid(column=3, row=1, sticky=(tk.W, tk.S, tk.E, tk.N))
        # read remote configuration
        self.read_remote_conf = tk.Button(right_bottomframe)
        self.read_remote_conf["text"] = "Read remote conf."
        self.read_remote_conf["command"] = self.read_remote_xbee
        self.read_remote_conf.grid(column=2, row=0, sticky=(tk.W, tk.S, tk.E, tk.N))
        # write remote configuration
        self.write_remote_conf = tk.Button(right_bottomframe)
        self.write_remote_conf["text"] = "Write remote conf."
        self.write_remote_conf["command"] = self.write_remote_xbee
        self.write_remote_conf.grid(column=3, row=0, sticky=(tk.W, tk.S, tk.E, tk.N))
        # clear params
        self.clear_params = tk.Button(right_bottomframe)
        self.clear_params["text"] = "Clear"
        self.clear_params["command"] = self.clear_readed_params
        self.clear_params.grid(column=4, row=0, sticky=(tk.W, tk.S, tk.E, tk.N))
        # open file
        self.open_file = tk.Button(right_bottomframe)
        self.open_file["text"] = "Open config files"
        self.open_file["command"] = self.open_config_file
        self.open_file.grid(column=4, row=1, sticky=(tk.W, tk.S, tk.E, tk.N))
        # textos
        # Discovering status text
        self.text_discover = tk.Text(left_upperframe, borderwidth=3, relief="sunken", bg="lavender")
        self.text_discover.config (font=("consolas", 10), undo=True, wrap ='word')
        self.text_discover.config(state="normal")
        self.text_discover.insert(tk.INSERT, '\nPress "Search Nodes" to find remote XBees \n')
        self.text_discover.config(state=tk.DISABLED)
        self.text_discover.grid(row=0, column=0, sticky=(tk.W, tk.S, tk.E, tk.N))
        yscrollbar = tk.Scrollbar(left_upperframe, command=self.text_discover.yview)
        yscrollbar.grid(row=0, column=1, sticky=tk.N + tk.S)
        self.text_discover['yscrollcommand'] = yscrollbar.set
        # Texto Xbee parámetros
        self.text_params = tk.Text(right_upperframe, borderwidth=3, relief="sunken", bg="lavender")
        self.text_params.config(font=("consolas", 10), undo=True, wrap='word')
        self.text_params.config(state="normal")
        self.text_params.insert(tk.INSERT, '\n Please press "Read local conf." to read local node params\n'
                                             ' or put address and press "Read remote conf." to read remote node params')
        self.text_params.config(state=tk.DISABLED)
        self.text_params.grid(row=0, column=0, sticky=(tk.W, tk.S, tk.E, tk.N))
        yscrollbar = tk.Scrollbar(right_upperframe, command=self.text_params.yview)
        yscrollbar.grid(row=0, column=1, sticky=tk.N + tk.S)
        self.text_params['yscrollcommand'] = yscrollbar.set

        # Entry address text
        self.lbladdress = tk.Label(right_bottomframe)
        self.lbladdress['text']="Remote Address: "
        #self.lbladdress.config(0,weight=1)
        self.lbladdress.grid(column=0, row=0,sticky=(tk.N, tk.W, tk.E, tk.S))
        self.remote_address = tk.Entry(right_bottomframe)
        #self.address.config(0,weight=3)
        self.remote_address.grid(column=1, row=0,sticky=(tk.N, tk.W, tk.E, tk.S))



if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()