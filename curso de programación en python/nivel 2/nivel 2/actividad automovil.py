#creando un objeto(osea una clase) de tipo automovil tipo road fighter
#el nombre de una clase siempre comienza con mayuscula
class Automovil:

    #estos son los atributos en el metodo constructor,osea caracteristicas del auto que luego pueden ser llamadas y nombradas.
    def __init__(self,color,marca,vidrios):
        self.color=color
        self.marca=marca
        self.vidrios=vidrios

    #estos son los metodos,osea funciones cosas que pueden hacer el auto.
    def Acelerar(self):
    #aqui utilizo el atributo color,marca y vidrios en el metodo acelerar
        print ("el auto de color ",self.color , "con vidrios de color ", self.vidrios," de marca ",self.marca," esta acelerando")

    def Frenar(self):
        print("el auto esta frenando")

    def Doblar(self):
        print ("el auto esta doblando")


#primero llamo a la clase para construir el auto los caracteres entre comillas los numeros sin comillas
auto=Automovil("rojo","porsche","negros")

#luego llamo al metodo o mejor dicho a la funcion del auto que es acelerar
auto.Acelerar()