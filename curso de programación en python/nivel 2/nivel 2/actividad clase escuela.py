#creando un objeto(osea una clase) de tipo automovil tipo road fighter
#el nombre de una clase siempre comienza con mayuscula
class maestro:

    #estos son los atributos en el metodo constructor,osea caracteristicas del auto que luego pueden ser llamadas y nombradas.
    def __init__(self,nombre,materia,cantidadalumnos):
        self.nombre=nombre
        self.materia=materia
        self.cantidadalumnos=cantidadalumnos

    #estos son los metodos,osea funciones cosas que pueden hacer el auto.
    def empiezalaclase(self):
        #aqui utilizo el atributo color,marca y vidrios en el metodo acelerar
        print 'el/la profesor/a ',self.nombre , 'de la materia ', self.materia,' con la cantidad de ',self.cantidadalumnos,'alumnos a empezado la clase'

    def terminarclase(self):
        print 'el/la profesor/a ',self.nombre , 'de la materia ', self.materia,' con la cantidad de ',self.cantidadalumnos,'alumnos a terminado la clase'

    def faltado(self):
        print 'el/la profesor/a ',self.nombre , 'de la materia ', self.materia,' con la cantidad de ',self.cantidadalumnos,' alumnos a faltado a la clase'



#primero llamo a la clase para construir el auto los caracteres entre comillas los numeros sin comillas
escuela= maestro("julia","matematica","35")
escuela.empiezalaclase()

escuela=maestro("sebastian","biologia","20")
escuela.terminarclase()

escuela=maestro("jose","historia","50")
escuela.faltado()