class Persona:
    def __init__(self,edad,nombre):
        self.edad= edad
        self.nombre= nombre
        print "se ha creado a ",self.nombre," de ",self.edad

    def hablar(self ,**palabras):
        for frase in palabras:
            print self.nombre,' : ',palabras[frase]

juan=Persona(18,'juan')
juan.hablar(t1="hola,estoy hablando",t2="este soy yo")

luis=Persona(20,'luis')
luis.hablar(t1="hola,estoy hablando",t2="este soy yo")