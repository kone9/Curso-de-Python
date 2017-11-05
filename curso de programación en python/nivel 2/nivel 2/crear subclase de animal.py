#crear 2 subclases de animal

#aqui creo la clase animal
class animal():
    def __init__(self,nombre):
        self.nombre=nombre
        print "ah nacido un animal",nombre

    def rugir(self,sonido):
        self.sonido=sonido
        print "hace el ruido",sonido

#Aqui creo la subclase perro que hereda metodos y atributos de animal
class perro(animal):
        pass

#aqui creo la subclase gato que hereda metodos y atributos de animal
class gato(animal):
       pass

#aqui creo el perro dogui y le asigno parametros
dogui=perro("perro llamado dogui")
dogui.rugir("guau,guau")

#aqui creo el gato michu y le asigno parametros
michu=gato("gato llamado michu")
michu.rugir("miau,miau")
