class Persona:
    def __init__(self,edad,nombre):
        self.edad= edad
        self.nombre= nombre
        print "se ha creado a ",self.nombre," de ",self.edad

    def hablar(self ,**palabras):
        for frase in palabras:
            print self.nombre,' : ',palabras[frase]


class Deportista(Persona):

    def __init__(self,edad,nombre,deporte):
        self.edad=edad
        self.nombre=nombre
        self.__deporte=deporte
        print "se ah creado a ", self.nombre ,"de",self.edad

    def practicardeporte(self):
        print self.nombre, "voy a practicar deporte"

    def vermideporte(self):
        return self.__deporte

juan=Persona(18,'juan')
juan.hablar(t1="hola estoy hablando este soy yo")
luis=Deportista(20,'luis','natacion')
luis.hablar(t1="hola,estoy hablando",t2="este soy yo")
luis.practicardeporte()
print "luis practica", luis.vermideporte()
