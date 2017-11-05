#Las funciones son acciones que luego pueden ser llamadas sin tener que volver a escribirlas y ellas tienen variables(parametros).

F=3.141516

def acuadrado():

    lado = input("cual es el valor del lado")
    x=lado**2
    print "\nel area del cuadrado es ",x," unidades cuadraticas"

#Area del triangulo
def atriangulo():

    base= input("cual es el valor de la base?")
    altura= input("cual es el valor de la altura?")
    y= base*altura/2
    print "\El area del triangulo es ",y," unidades cuadraticas"

 #area del circulo
def acirculo():
    radio= input("cual es el valor de radio?")
    z=(F*radio)**2
    print "\El area del circulo es ",z," unidades cuadraticas"

i=True
while i== True:
    area= input("\Elije la figura geometrica para calcular su area \ncuadrado = 1 \ntriangulo = 2 \ncirculo = 3\n")
    if area == 1:
        acuadrado()
    elif area == 2:
        atriangulo()
    elif area == 3:
        acirculo()
    else:
        print ("Por favor ingrese una opcion valida")

        i=input("\nquieres calcular el area de otra figura? \n si=True \n no=False\n")


