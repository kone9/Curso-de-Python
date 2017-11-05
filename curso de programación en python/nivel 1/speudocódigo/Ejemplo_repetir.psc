Proceso mi_proceso
//declarar una variable con el tipo de dato y el identicador
	Definir edad como Entero;
//variable que la voy a asignar a una iteración	
	Definir iteración Como Entero;
	
//Asignar un valor a la variable vectores
	Dimension edad(3);

	iteracion <-1;	
	
Repetir
		
		escribir"¿Cuál es la edad de la persona ",iteracion+1 " ?";
		leer edad(iteracion);
		iteracion<- iteracion +1;
Hasta Que iteracion<3;

	
escribir "Las edades ingresadas fueron";
	escribir "persona 1 = ",edad(1);
	escribir "persona 2 = ",edad(2);
	escribir "persona 3 = ",edad(3);
	
	
	
FinProceso

