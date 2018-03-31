import tkinter

class PanedWindow(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        self.title("Digi XBee-Zigbee Network management. Srueda (TFM - uoc 2018)")

        panedwindow = tkinter.PanedWindow(width=800, height= 800)
        panedwindow.config(handlesize=8)
        panedwindow.config(sashwidth=3)
        panedwindow.config(sashrelief=tkinter.RAISED)
        panedwindow.pack(fill=tkinter.BOTH, expand=1)

        label = tkinter.Label(text="Label in Pane 1", width=35)
        panedwindow.add(label)
        label = tkinter.Label(text="Label in Pane 2", bg="white")
        panedwindow.add(label)
        label = tkinter.Label(orient=1, bg="white")
        panedwindow.add(label)

if __name__ == "__main__":
    application = PanedWindow()
application.mainloop()