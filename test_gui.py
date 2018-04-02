from tkinter import *
from tkinter import ttk
import time
import DiscoverDevices_XBee

Texto = "Press ' Discover Nodes' button to find remote devices \n"

class Application(Frame):


    def UpdateDiscoverStatus(self):
        self.texto.set("Discovering devices 1...")
        self.discoverlab.config(textvar=self.texto)
        #time.sleep(1)
        #self.texto.set("Discovering devices 2...")
        #self.discoverlab.config(textvar=self.texto)


       #DiscoverDevices_XBee.main()


    def createWidgets(self):
        # Contenedor paneles izquierdos
        left_pane = PanedWindow(root, orient=VERTICAL)
        left_pane.grid(column=0, row=0, rowspan=2, sticky=(N, W, E, S))
        left_pane.rowconfigure(0, weight=1)
        left_pane.columnconfigure(0, weight=1)
        left_upperframe = ttk.Frame(root, relief='groove', borderwidth=2)
        left_upperframe.grid(column=0, row=0, sticky=(N, W, E, S))
        left_upperframe.columnconfigure(0, weight=1)
        left_upperframe.rowconfigure(0, weight=1)
        left_pane.add(left_upperframe, heigh=430, width=300)
        left_bottomframe = ttk.Frame(left_pane, relief='groove', borderwidth=2)
        left_bottomframe.grid(column=0, row=1, sticky=(N, W, E, S))
        left_bottomframe.columnconfigure(0, weight=1)
        left_bottomframe.rowconfigure(0, weight=1)
        left_pane.add(left_bottomframe, heigh=40)


        # Contenedor paneles derechos
        right_pane = PanedWindow(root, orient=VERTICAL)
        right_pane.grid(column=1, row=0, rowspan=2, sticky=(N, W, E, S))
        right_pane.rowconfigure(0, weight=1)
        right_pane.columnconfigure(0, weight=1)
        right_upperframe = ttk.Frame(root, relief='groove', borderwidth=2)
        right_upperframe.grid(column=1, row=0, sticky=(N, W, E, S))
        right_upperframe.columnconfigure(0, weight=1)
        right_upperframe.rowconfigure(0, weight=1)
        right_pane.add(right_upperframe, width=600, heigh=430)
        right_bottomframe = ttk.Frame(right_pane, relief='groove', borderwidth=2)
        right_bottomframe.grid(column=1, row=1, sticky=(N, W, E, S))
        right_bottomframe.columnconfigure(0, weight=1)
        right_bottomframe.rowconfigure(0, weight=1)
        right_pane.add(right_bottomframe)


        #self.QUIT = Button(self)
        #self.QUIT["text"] = "QUIT"
        #self.QUIT["fg"]   = "red"
        #self.QUIT["command"] =  self.quit

        #self.QUIT.pack({"side": "left"})
        # Botones
        discover = Button(left_bottomframe)
        discover["text"] = "Discover Nodes"
        discover["command"] = self.UpdateDiscoverStatus
        discover.grid(column=0, row=0, sticky=(W, S, E, N))


        #textos variables
        #if DiscoverDevices_XBee.state == 0:
        #    texto = "Press ' Discover Nodes' button to find remote devices \n"
        #elif DiscoverDevices_XBee.state == 1:
        #    texto = "Discovering remote XBee devices..."


        self.discoverlab=Label(left_upperframe)
        self.texto = StringVar()
        self.texto.set("Press ' Discover Nodes' button to find remote devices \n")
        self.discoverlab.config(textvar=self.texto)
        self.discoverlab.grid(column=0, row=0, sticky=W, pady=4, padx=5)

    def __init__(self, master=None):
        Frame.__init__(self, master)
        master.title("Digi XBee-Zigbee Network management. Srueda (TFM - uoc 2018)")
        master.columnconfigure(1, weight=1)
        master.columnconfigure(1, weight=1)
        master.rowconfigure(1, weight=1)
        master.rowconfigure(1, weight=1)
        self.createWidgets()
        self.discoverStep=0;


root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()