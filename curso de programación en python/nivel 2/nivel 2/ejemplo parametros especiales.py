class Persona:
    def __init__(self,edad,nombre):
        self.edad= edad
        self.nombre= nombre
        print "se ha creado a ",self.nombre," de ",self.edad

    def hablar(self ,palabras='nose que decir'):
            print self.nombre,' : ',palabras

juan=Persona(18,"juan")
juan.hablar("hola soy juan y estoy hablando")

luis= Persona(20," luis")
luis.hablar("hola soy luis y estoy hablando")