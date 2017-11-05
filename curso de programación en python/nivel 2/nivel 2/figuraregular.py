#crear 2 subclases de figura regular
class FiguraRegular:

    def __init__(self,lado = 3):#creo el metodo o funcion constructora de objeto figuraregular
        self.lado= lado
        self.__area= 0

    def VerArea(self):#creo el metodo ver area ya que area esta oculta dentro de la funcion constructora
        return self.__area,

#Si  lado es Igual a 2; area es igual a base*altura
#si lado es igual a 3; area es igual a base*altura/2
#esta clase cambia el valor a area y subtituye el valor de el atributo Lado heredado
class CalcularCantidadLadoscuadrado(FiguraRegular):

    def CalcularAreaCuadrado(self,base,altura):
         self.lado=2
         self.base=base
         self.altura=altura
         self.__area = base * altura
         print "la cantidad de lados del area de un cuadrado es ",self.lado, 'y su area es el valor ingresado como parametro =',self.__area

class CalcularCantidadLadosTriangulo(FiguraRegular):

    def CalcularLadosTriangulo(self,base,altura):
        self.lado = 3
        self.base = base
        self.altura = altura
        self.__area = base * altura / 2
        print "la cantidad de lados del triangulo es ", self.lado, 'y su area es el valor ingresado como parametro =', self.__area


cuadrado=CalcularCantidadLadoscuadrado()
cuadrado.CalcularAreaCuadrado(10,10)


triangulo=CalcularCantidadLadosTriangulo()
triangulo.CalcularLadosTriangulo(10,10)

