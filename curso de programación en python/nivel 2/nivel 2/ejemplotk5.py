from Tkinter import *

class Interface:
    def __init__(self,contenedor):
        self.E3= StringVar()

        self.e1=Label(contenedor,text="convertir celcius a farenhaid", fg="black")
        self.e2=Label(contenedor,text="celcius", fg="black")
        self.e3= Label(contenedor, text="farenhaid", fg="black",)
        self.e4= Button(contenedor, text="convertir", fg="black", bg="cyan",command=self.hacerConversion)
        self.e5= Entry(contenedor, fg="black", bg="white")
        self.e6= Label(contenedor, text="", fg="black",textVariable=self.textoE3)

        self.e1.grid(column=0,row=0,columnspan=2)
        self.e2.grid(column=0,row=1)
        self.e3.grid(column=0,row=2)
        self.e4.grid(column=0, row=3,columnspan=2)
        self.e5.grid(column=1, row=1)
        self.e6.grid(column=1, row=2)

    def hacerConversion(self):
        cel=float(self.e5.get())
        far=(cel*1.8)+32
        self.E3.set(far)



ventana = Tk()
MiInterface= Interface(ventana)
ventana.mainloop()