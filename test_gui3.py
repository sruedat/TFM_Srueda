import tkinter as tk
from tkinter import ttk
import threading
import queue
import time
import DiscoverDevices_XBee


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



    def clear_status(self):
        self.texto.config(state="normal")
        self.texto.delete('1.0', tk.END)
        self.texto.insert(tk.INSERT, "\nPress ""Search Nodes"" to find remote XBees \n")
        self.texto.config(state=tk.DISABLED)



    def update_status(self):
        self.discover_status = 0
        self.texto.delete('1.0', tk.END)
        self.clear_discover['state']=tk.DISABLED
        threading.Thread(target=self.search).start()
        threading.Thread(target=self.update_discover_log,
                         args=(self, self.queue, self.clear_discover, self.discover,)).start()
        self.after(100, self.process_queue)


    def process_queue(self):
        try:
            data = self.queue.get_nowait()
            self.texto.config(state="normal")
            self.texto.delete('1.0', tk.END)
            self.texto.insert(tk.INSERT,data)
            self.texto.config(state=tk.DISABLED)
        except queue.Empty:
            pass
        self.master.after(100, self.process_queue)



    def create_widgets(self):
        # lef pane
        left_pane = tk.PanedWindow(root, orient=tk.VERTICAL)
        left_pane.grid(column=0, row=0, rowspan=2, sticky=(tk.N, tk.W, tk.E, tk.S))
        left_pane.rowconfigure(0, weight=1)
        left_pane.columnconfigure(0, weight=1)
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
        right_pane.rowconfigure(0, weight=1)
        right_pane.columnconfigure(0, weight=1)
        right_upperframe = ttk.Frame(root, relief='groove', borderwidth=2)
        right_upperframe.grid(column=1, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        right_upperframe.columnconfigure(0, weight=1)
        right_upperframe.rowconfigure(0, weight=1)
        right_pane.add(right_upperframe, width=600, heigh=500)
        right_bottomframe = ttk.Frame(right_pane, relief='groove', borderwidth=2)
        right_bottomframe.grid(column=1, row=1, sticky=(tk.N, tk.W, tk.E, tk.S))
        right_bottomframe.columnconfigure(0, weight=1)
        right_bottomframe.rowconfigure(0, weight=1)
        right_pane.add(right_bottomframe)

        # buttons
        self.discover = tk.Button(left_bottomframe)
        self.discover["text"] = "Search Nodes"
        self.discover["command"] = self.update_status
        self.discover.grid(column=0, row=0, sticky=(tk.W, tk.S, tk.E, tk.N))
        self.clear_discover = tk.Button(left_bottomframe)
        self.clear_discover["text"] = "Clear"
        self.clear_discover["command"] = self.clear_status  # self.UpdateDiscoveringState
        self.clear_discover.grid(column=1, row=0, sticky=(tk.W, tk.S, tk.E, tk.N))

        # Discovering status text
        self.texto = tk.Text(left_upperframe, borderwidth=3, relief="sunken", bg="lavender")
        self.texto.config (font=("consolas", 10), undo=True, wrap ='word')
        self.texto.config(state="normal")
        self.texto.insert(tk.INSERT, "\nPress ""Search Nodes"" to find remote XBees \n")
        self.texto.config(state=tk.DISABLED)
        self.texto.grid(row=0, column=0, sticky=(tk.W, tk.S, tk.E, tk.N))

        yscrollbar = tk.Scrollbar(left_upperframe, command=self.texto.yview)
        yscrollbar.grid(row=0, column=1, sticky=tk.N + tk.S)
        self.texto['yscrollcommand'] = yscrollbar.set


if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()