#cuestionario para saber si comes suficientes frutas.

si=True
no=False
print("por favor contesta si o no")
frutas=input("comes frutas?")
if frutas == True:
    frutas = input("cuantas veces a la semana comes frutas?")
if frutas >= 5:
    frutas = input("cuantas frutas comes al dia?")
    #si comes mas que 5 se evaalua cuanto come por dia
    if frutas >=2:
        print ("comes saludable")
    elif frutas < 2:
        print("te recomendaria comer mas frutas")

        #si comes menos que 5 se sigue evaluando por semana
elif frutas == 3:
    print ("come mas frutas a la semana")
elif frutas <= 2:
    print ("necesitas comer frutas")

        #si es falzo hay respuesta
elif frutas==False:
    print ("Necesitas comer frutas")

"""en el caso de responder mal,luego revisarlo.
else:
    print("Disculpa pero solo puedes responder si o no")
    print ("fin del programa")
"""
