class Persona:
    def __init__(self,edad,nombre):
        self.edad= edad
        self.nombre= nombre
        print "se ha creado a ",self.nombre," de ",self.edad

    def hablar(self ,*palabras):
        for frase in palabras:
            print self.nombre,' : ',frase

juan=Persona(18,'juan')
juan.hablar("hola,estoy hablando,este soy yo")

luis=Persona(20,'luis')
luis.hablar("hola,estoy hablando,este soy yo")