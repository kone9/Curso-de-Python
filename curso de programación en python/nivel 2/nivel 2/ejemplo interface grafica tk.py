#importo la libreria
from Tkinter import *

class Interface:



    def __init__(self,contenedor):#creo el texto que va a ir dentro del contenedor
        #self.TextoE1 = StringVar

        self.e1 = Label(contenedor,text= "color", fg= "black", bg= "white")#esto es un texto
        self.e2 = Button(contenedor, text="amarillo", fg="yellow", bg="white",command=self.CambiarColorAmarillo)#esto es un boton
        self.e3 = Button(contenedor, text="rojo", fg="red", bg="white",command=self.CambiarColorRojo)#esto es un boton
        self.e4 = Button(contenedor, text="blanco", fg="pink", bg="white",command=self.CambiarColorBlanco)#esto es un botn

        #Aqui acomodo toda la interface
        self.e1.pack(fill=X)#posiciono el texto arriba y pongo el fondo blanco
        self.e2.pack(side=RIGHT)#posiciono boton en izquierda
        self.e3.pack(side=LEFT)#posiciono boton en medio
        self.e4.pack(side=BOTTOM)#posiciono boton en derecha


    def CambiarColorAmarillo(self):
        print "estoy cambiando el color a amarillo"
        self.e1.configure(fg= "yellow")#utilizo el valor de la variable para cambiar el color

    def CambiarColorRojo(self):
        print " estoy cambiando el color a rojo"
        self.e1.configure(fg="red")

    def CambiarColorBlanco(self):
        print "estoy cambiando el color a blanco"
        self.e1.configure(fg="pink")


#creo la ventana
ventana= Tk ()
miInterface= Interface(ventana)
ventana.mainloop()
