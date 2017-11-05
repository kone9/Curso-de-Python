from abc import ABCMeta, abstractmethod

class Transporte:
    __metaclass__ = ABCMeta
    def __init__(self,medio):
        self.medio=medio
#Usar el atributo "medio" para definir como avanza
    @abstractmethod
    def avanzar(self,frase): pass

    def giraIzquierda(self):
        print  "gira a la izquierda"

    def giraDerecha(self):
        print "gira a la derecha"

#De acuerdo al "medio" especificar que hace para frenar
    @abstractmethod
    def detener(self): pass


class Auto(Transporte):

    def avanzar(self,frase,*acelerar):
      self.frase=frase
      for velocidad in acelerar:
           print self.medio,";",frase,velocidad

    def detener(self,*frenar):
        for desacelera in frenar:
           print self.medio,":",desacelera


class camion (Transporte):

    def avanzar(self,frase,*acelerar):
      self.frase=frase
      for velocidad in acelerar:
           print self.medio,";",frase,velocidad

    def detener(self,*frenar):
        for desacelera in frenar:
           print self.medio,":",desacelera


porsche=Auto("En la atalaya,llendo a la costa en auto")
porsche.detener("el auto ah frenado, asi comemos algo")
porsche.avanzar("Ya estamos cerca , ","empieza a acelerar para llegar mas rapido")


MercedesBens=camion("En la montana con paisajes hermosos llendo en camion")
MercedesBens.avanzar("Nos falta poco para llegar","Empieza acelerar mas rapido")
MercedesBens.detener("Hay un restaurant arriba de la montana vamos a parar a comer")