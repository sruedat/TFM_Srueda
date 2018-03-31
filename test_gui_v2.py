from tkinter import *
from tkinter import ttk

root = Tk()

root.title("Digi XBee-Zigbee Network management. Srueda (TFM - uoc 2018)")
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)


left_right_pane = PanedWindow(root, orient=HORIZONTAL, relief='groove', borderwidth=4, width=700, heigh=500)
left_right_pane.grid(column=0, row=0, sticky=(W,S,E,N), columnspan=2)
left_right_pane.rowconfigure(0, weight=1)
left_right_pane.columnconfigure(0, weight=1)
left_right_pane.rowconfigure(1, weight=1)
left_right_pane.columnconfigure(1, weight=1)


leftframe = ttk.Frame(root, relief='groove', borderwidth=2)
leftframe.grid(column=0, row=0, sticky=(N, W, E, S), rowspan=2)
leftframe.rowconfigure(0, weight=1)
leftframe.columnconfigure(0, weight=1)
left_right_pane.add(leftframe, width=300) #aquí me he quedado

top_bottom_pane = PanedWindow(root, orient=VERTICAL)
top_bottom_pane.grid(column=1, row=0, rowspan=2, sticky=(N, W, E, S))
top_bottom_pane.rowconfigure(0, weight=1)
top_bottom_pane.columnconfigure(0, weight=1)
left_right_pane.add(top_bottom_pane)

upperframe = ttk.Frame(root, relief='groove', borderwidth=2)
upperframe.grid(column=1, row=0, sticky=(N, W, E, S))
upperframe.columnconfigure(1, weight=1)
upperframe.rowconfigure(0, weight=1)
top_bottom_pane.add(upperframe)

bottomframe = ttk.Frame(top_bottom_pane, relief='groove', borderwidth=2)
bottomframe.grid(column=1, row=1, sticky=(N, W, E, S))
bottomframe.columnconfigure(1, weight=1)
bottomframe.rowconfigure(1, weight=1)
top_bottom_pane.add(bottomframe)

entry = ttk.Entry(leftframe)
entry.grid(column=0, row=0, sticky=(W,S,E,N))

top = Label(upperframe, text="top pane")
top.grid(column=1, row=0, sticky=(W,S,E,N))

bottom = Label(bottomframe, text="bottom pane")
bottom.grid(column=1, row=1, sticky=(W,S,E,N))

mainloop()