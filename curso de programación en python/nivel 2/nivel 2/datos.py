def escritura(datoa, datob ,datoc):
    ruta= "C:/Users/ariel/Desktop/datos.py"
    prueba= open(ruta, 'w')
    prueba.write(datoa)
    prueba.write(datob)
    prueba.write(datoc)
    print "\nescritura\n"
    prueba.close()


def lectura():
    ruta = "C:/Users/ariel/Desktop/datos.py"
    prueba=open(ruta,'r')
    print prueba.read()
    prueba.close()
    print prueba.read()
    prueba.close()



escritura("hola","mundo","Bonito")
lectura()