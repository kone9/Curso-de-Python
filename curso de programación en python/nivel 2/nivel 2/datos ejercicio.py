def escritura(datoa,datob,datoc,datod,datoe):
    archivo= "C:/Users/ariel/Desktop/datos.py"
    abrirarchivo= open(archivo,'w')
    abrirarchivo.write(datoa)
    abrirarchivo.write(datob)
    abrirarchivo.write(datoc)
    abrirarchivo.write(datod)
    abrirarchivo.write(datoe)
    print "con esta funcion pruevo la escritura pero no veo lo que escribo"
    abrirarchivo.close()

def lectura():
    archivo = "C:/Users/ariel/Desktop/datos.py"
    abrirarchivo= open(archivo,'r')
    print "estos son los datos escritos en el archivo: ",abrirarchivo.read()
    abrirarchivo.close()

escritura ("\nescuela\n","cuaderno\n","lapices\n","maestro\n","livertad\n")
lectura()