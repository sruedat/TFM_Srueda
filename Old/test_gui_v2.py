from tkinter import *
from tkinter import ttk

import discover_devices_xbee

root = Tk()

root.title("Digi XBee-Zigbee Network management. Srueda (TFM - uoc 2018)")
root.columnconfigure(1, weight=1)
root.columnconfigure(1, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(1, weight=1)

#contenedor paneles izquierdos
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

#contenedor paneles derechos
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



# etiquetas
top = Label(right_upperframe, text="top pane")
top.grid(column=1, row=0, sticky=(W,S,E,N))

entry = ttk.Frame(right_bottomframe)
entry2 = ttk.Entry(right_bottomframe)
entry.grid(column=2, row=1, sticky=(W,S,E,N))
entry2.grid(column=3, row=1, sticky=(W,S,E,N))
entry.columnconfigure(0, weight=1)
entry2.rowconfigure(0, weight=3)
lbl = Label(entry, text="Node Address:")
lbl.grid(sticky=W, pady=4, padx=5)

# Botones
discover = ttk.Button(left_bottomframe, text="Discover Network", command=discover_devices_xbee)
discover.grid(column=0, row=0, sticky=(W,S,E,N))
if discover_devices_xbee.state == 0:
    texto = "Press 'Discover Network' button to find devices \n"
elif discover_devices_xbee.state == 1:
    texto = "Discovering remote XBee devices..."

discoverlab =Label (left_upperframe, text = texto)
#discoverlab.pack()
discoverlab.grid(column =0, row= 0, sticky=W, pady=4, padx=5)





mainloop()