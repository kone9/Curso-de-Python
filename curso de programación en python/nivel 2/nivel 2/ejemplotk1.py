from Tkinter import *

class Interface:
    def __init__(self,contenedor):
        self.e1=Label(contenedor,text="Etiqueta 1", fg="black",bg="white")
        self.e1.pack()

ventana = Tk ()
MiInterface= Interface(ventana)
ventana.mainloop()


