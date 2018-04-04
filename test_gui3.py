import tkinter as tk
from tkinter import ttk
import threading
import queue
import time
import DiscoverDevices_XBee
import read_local_params_xbee
import read_remote_params_xbee
import write_remote_params_xbee
import os


class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        master.title("SRueda. - Xbee Zigbee Tool")
        master.columnconfigure(1, weight=1)
        master.columnconfigure(1, weight=1)
        master.rowconfigure(1, weight=1)
        master.rowconfigure(1, weight=1)
        self.queue = queue.Queue()
        self.create_widgets()


    def open_config_file(self):
        dirname= os.path.dirname(__file__)+ "/config/sys_config.ini"
        print (dirname)
        os.startfile(dirname)

    @staticmethod
    def read_remote_xbee_cmmd(self, boton1, boton2, boton3):
        self.text_params.config(state="normal")
        # the propper length of the address is 2 bytes, we must
        data = self.remote_address.get()[:16]
        if len(data)<16:
            for n in range (len(data),16):
                data= "0" + data
        self.text_params.insert(tk.INSERT,'Trying to access to remote device: ' + data + '\n\n')
        self.text_params.insert(tk.INSERT, read_remote_params_xbee.main(data))
        boton1['state'] = "normal"
        boton2['state'] = "normal"
        boton3['state'] = "normal"
        self.text_params.config(state=tk.DISABLED)

    def read_remote_xbee(self):
        self.text_params.config(state="normal")
        self.text_params.delete('1.0', tk.END)
        self.read_local_conf['state'] = tk.DISABLED
        self.read_remote_conf['state'] = tk.DISABLED
        self.clear_params['state'] = tk.DISABLED
        self.text_params.insert(tk.INSERT, " \nReading remote node... \n\n")
        self.text_params.config(state=tk.DISABLED)
        threading.Thread(target=self.read_remote_xbee_cmmd,
                         args=(self, self.read_local_conf, self.read_remote_conf, self.clear_params)).start()
        self.master.after(100, self.update_status)


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
        boton1['state'] = "normal"
        boton2['state'] = "normal"
        boton3['state'] = "normal"
        self.text_params.config(state=tk.DISABLED)

    def write_remote_xbee(self):
        self.text_params.config(state="normal")
        self.text_params.delete('1.0', tk.END)
        self.read_local_conf['state'] = tk.DISABLED
        self.read_remote_conf['state'] = tk.DISABLED
        self.clear_params['state'] = tk.DISABLED
        self.text_params.insert(tk.INSERT, " \nWriting remote node... \n\n")
        self.text_params.config(state=tk.DISABLED)
        threading.Thread(target=self.write_remote_xbee_cmmd,
                         args=(self, self.read_local_conf, self.read_remote_conf, self.clear_params,)).start()
        #self.master.after(100, self.update_status)



    def read_local_xbee(self):
        self.text_params.config(state="normal")
        self.text_params.delete('1.0', tk.END)
        self.read_local_conf['state'] = tk.DISABLED
        self.read_remote_conf['state'] = tk.DISABLED
        self.clear_params['state'] = tk.DISABLED
        self.text_params.insert(tk.INSERT, " \nReading local node... \n\n")
        self.text_params.config(state=tk.DISABLED)
        threading.Thread(target=self.read_local_xbee_cmmd, args=(self,self.read_local_conf, self.read_remote_conf,self.clear_params)).start()
        self.master.after(100, self.update_status)


    @staticmethod
    def read_local_xbee_cmmd(self, boton1, boton2, boton3):
        self.text_params.config(state="normal")
        self.text_params.insert(tk.INSERT, read_local_params_xbee.main())
        boton1['state'] = "normal"
        boton2['state'] = "normal"
        boton3['state'] = "normal"
        self.text_params.config(state=tk.DISABLED)

    def clear_readed_params(self):
        self.text_params.config(state="normal")
        self.text_params.delete('1.0', tk.END)
        self.text_params.insert(tk.INSERT, '\n Please press "Read local conf." to read local node params\n'
                                           ' or put address and press "Read remote conf." to read remote node params')
        self.text_params.config(state=tk.DISABLED)

    @staticmethod
    def update_discover_log(self,cola,boton1,boton2):
        boton2['state']=tk.DISABLED
        while self.discover_status != 1:
            cola.put(DiscoverDevices_XBee.passlog())
            time.sleep(0.1)
        boton1['state'] = "normal"
        boton2['state'] = "normal"



    def search(self):
        self.discover_status=DiscoverDevices_XBee.main()



    def clear_discovered_nodes(self):
        self.text_discover.config(state="normal")
        self.text_discover.delete('1.0', tk.END)
        self.text_discover.insert(tk.INSERT, '\nPress "Search Nodes" to find remote XBees \n')
        self.text_discover.config(state=tk.DISABLED)



    def update_status(self):
        self.discover_status = 0
        self.text_discover.delete('1.0', tk.END)
        self.clear_discover['state']=tk.DISABLED
        threading.Thread(target=self.search).start()
        threading.Thread(target=self.update_discover_log,
                         args=(self, self.queue, self.clear_discover, self.discover,)).start()
        self.after(100, self.process_queue)


    def process_queue(self):
        try:
            data = self.queue.get_nowait()
            self.text_discover.config(state="normal")
            self.text_discover.delete('1.0', tk.END)
            self.text_discover.insert(tk.INSERT,data)
            self.text_discover.config(state=tk.DISABLED)
        except queue.Empty:
            pass
        self.master.after(100, self.process_queue)



    def create_widgets(self):
        # lef pane
        left_pane = tk.PanedWindow(root, orient=tk.VERTICAL)
        left_pane.grid(column=0, row=0, rowspan=2, sticky=(tk.N, tk.W, tk.E, tk.S))
        #left_pane.rowconfigure(0, weight=1)
        #left_pane.columnconfigure(0, weight=1)
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


        # right pane
        right_pane = tk.PanedWindow(root, orient=tk.VERTICAL)
        right_pane.grid(column=1, row=0, rowspan=2, sticky=(tk.N, tk.W, tk.E, tk.S))
        #right_pane.rowconfigure(0, weight=1)
        #right_pane.columnconfigure(0, weight=1)
        right_upperframe = ttk.Frame(root, relief='groove', borderwidth=2)
        right_upperframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        #right_upperframe.columnconfigure(0, weight=1)
        right_upperframe.rowconfigure(0, weight=3)
        right_pane.add(right_upperframe, width=600, heigh=500)
        right_bottomframe = ttk.Frame(right_pane, relief='groove', borderwidth=2)
        right_bottomframe.grid(column=0, row=1, sticky=(tk.N, tk.W, tk.E, tk.S))
        right_bottomframe.columnconfigure(0, weight=1)
        right_bottomframe.rowconfigure(0, weight=1)
        right_pane.add(right_bottomframe)

        # buttons
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
        #self.write_local_conf["command"] = self.write_remote_xbee
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
        self.open_file["text"] = "Open config file"
        self.open_file["command"] = self.open_config_file
        self.open_file.grid(column=4, row=1, sticky=(tk.W, tk.S, tk.E, tk.N))

        # text
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

        # Xbee params text
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