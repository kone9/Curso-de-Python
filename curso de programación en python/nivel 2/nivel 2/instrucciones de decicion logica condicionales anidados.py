#dependiendo la instruccion tengo una respuesta que tiene un resultado final

#creo una variable que va alojar mi respuesta,no olvidarme de las mayusculas verdadera(True) o falza(False)
pregunta= input('trabajas desde casa?= ')

if pregunta == True:
    print 'eres afortunado'

if pregunta == False:
    print 'trabajas fuera de casa'

#creo otra variable para determinar el tiempo que tardo en llegar al trabajo.
tiempo= input('cuantos minutos tardas en llegar al trabajo= ')
if tiempo== 0:
    print 'trabajas desde casa'

#lo mismo que antes pero calculo el tiempo y dependiendo obtengo los resultados
elif tiempo< 20:
    print 'es el tiempo ideal'
elif tiempo >=21 and tiempo<= 45:
    print 'es un tiempo razonable'
else:
    print 'busca otra ruto o otro trabajo no pierdas tu tiempo'
