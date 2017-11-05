import sqlite3

def insertar():

    db1=sqlite3.connect("novelas2.db")
    print("estas en la funcion insertar")

    nombre1=raw_input("escribe el titulo de la novela")
    autor1=raw_input("escribe el nombre del autor")
    year1=raw_input("escribe el anio de la novela")

    consulta=db1.cursor()

    strConsulta="insert into tabla(nombre,autor,year) values
    ("""+nombre1","+autor1+","+year1+"""),""

    print(strConsulta)