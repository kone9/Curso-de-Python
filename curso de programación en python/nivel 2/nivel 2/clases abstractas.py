from abc import ABCMeta,abstractmethod

class Persona:
    __metaclass__ = ABCMeta

    def __init__(self,edad,nombre):
        self.edad= edad
        self.nombre= nombre
        print "se ha creado a ",self.nombre," de ",self.edad

    @abstractmethod
    def hablar(self):pass



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

    def hablar(self,*palabras):
        for frase in palabras:
            print self.nombre,':',frase



luis=Deportista(20,'luis','natacion')
luis.hablar("hola,estoy hablando","este soy yo")
luis.practicardeporte()
print "luis practica", luis.vermideporte()
