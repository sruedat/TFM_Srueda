import tkinter as tk
from tkinter import ttk
import time
import threading
import queue




class Application(tk.Frame):
    def __init__(self, master=None):
        super(Application, self).__init__(master)
        master.title("Window Title")
        master.columnconfigure(1, weight=1)
        master.columnconfigure(1, weight=1)
        master.rowconfigure(1, weight=1)
        master.rowconfigure(1, weight=1)
        self.queue = queue.Queue()
        self.create_widgets()

    @staticmethod
    def contador(cola):
        cola.put("Contando hasta 10...")
        time.sleep(2)
        for n in range(10):
            cola.put(str(n))
            time.sleep(2)
        time.sleep(2)
        cola.put("He terminado!")


    def update_status(self):
        threading.Thread(target=self.contador, args=(self.queue,)).start()
        self.after(100, self.process_queue)


    def process_queue(self):
        try:
            data = self.queue.get_nowait()
            self.text.set(data)
        except queue.Empty:
            pass

        self.master.after(100, self.process_queue)



    def create_widgets(self):
        # left pane
        self.left_pane = tk.PanedWindow(root, orient=tk.VERTICAL)
        self.left_pane.grid(column=0, row=0, rowspan=2, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.left_pane.rowconfigure(0, weight=1)
        self.left_pane.columnconfigure(0, weight=1)
        self.left_upperframe = ttk.Frame(root, relief='groove', borderwidth=2)
        self.left_upperframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.left_upperframe.columnconfigure(0, weight=1)
        self.left_upperframe.rowconfigure(0, weight=1)
        self.left_pane.add(self.left_upperframe, heigh=430, width=300)
        self.left_bottomframe = ttk.Frame(self.left_pane, relief='groove', borderwidth=2)
        self.left_bottomframe.grid(column=0, row=1, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.left_bottomframe.columnconfigure(0, weight=1)
        self.left_bottomframe.rowconfigure(0, weight=1)
        self.left_pane.add(self.left_bottomframe, heigh=40)


        # right pane
        self.right_pane = tk.PanedWindow(root, orient=tk.VERTICAL)
        self.right_pane.grid(column=1, row=0, rowspan=2, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.right_pane.rowconfigure(0, weight=1)
        self.right_pane.columnconfigure(0, weight=1)
        self.right_upperframe = ttk.Frame(root, relief='groove', borderwidth=2)
        self.right_upperframe.grid(column=1, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.right_upperframe.columnconfigure(0, weight=1)
        self.right_upperframe.rowconfigure(0, weight=1)
        self.right_pane.add(self.right_upperframe, width=600, heigh=430)
        self.right_bottomframe = ttk.Frame(self.right_pane, relief='groove', borderwidth=2)
        self.right_bottomframe.grid(column=1, row=1, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.right_bottomframe.columnconfigure(0, weight=1)
        self.right_bottomframe.rowconfigure(0, weight=1)
        self.right_pane.add(self.right_bottomframe)


        # button
        self.discover = tk.Button(self.left_bottomframe)
        self.discover["text"] = "Button"
        self.discover["command"] = self.update_status
        self.discover.grid(column=0, row=0, sticky=(tk.W, tk.S, tk.E, tk.N))


        # label
        self.labl=tk.Label(self.left_upperframe)
        self.text = tk.StringVar()
        self.text.set("Inicial text \n")
        self.labl.config(textvar=self.text)
        self.labl.grid(column=0, row=0, sticky=tk.W, pady=4, padx=5)


if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()