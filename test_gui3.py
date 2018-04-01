from tkinter import *
from tkinter import ttk
import DiscoverDevices_XBee

class Application(Frame):

    def UpdateDiscoveringState(self):
        self.DiscoverState=1

    def DiscoveringSateMachine(self):
        if self.DiscoverState==0:
            self.text.set(" Press 'Discover Node' button to find remote nodes")
            self.labl.config(textvar=self.text)
        elif self.DiscoverState==1:
            self.text.set(" Discovering remote nodes...")
            self.labl.config(textvar=self.text)
            self.DiscoverState = 3
        elif self.DiscoverState==3:
            DiscoverDevices_XBee.main()
            self.DiscoverState = 4
        elif self.DiscoverState == 4:
            self.text.set(" Discovery process finished successfully")



    def createWidgets(self):
        #Inicializa variables
        self.DiscoverState=0


        # lef pane
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


        # right pane
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


        # button
        discover = Button(left_bottomframe)
        discover["text"] = "Button"
        discover["command"] = self.UpdateDiscoveringState
        discover.grid(column=0, row=0, sticky=(W, S, E, N))


        # label
        self.labl=Label(left_upperframe)
        self.text = StringVar()
        self.text.set("Inicial text \n")
        self.labl.config(textvar=self.text)
        self.labl.grid(column=0, row=0, sticky=W, pady=4, padx=5)

    def __init__(self, master=None):
        Frame.__init__(self, master)
        master.title("Window Title")
        master.columnconfigure(1, weight=1)
        master.columnconfigure(1, weight=1)
        master.rowconfigure(1, weight=1)
        master.rowconfigure(1, weight=1)
        self.createWidgets()



root = Tk()
app = Application(master=root)
while True:
    #root.update_idletasks()
    #root.update()
    app.DiscoveringSateMachine()

root.destroy()

#app.mainloop()
