Algoritmo mi_primer_arreglo_de_conteo_letras_pares_MIENTRAS
	
	Definir letras como Entero
	Escribir "por favor ingrese su nombre para contar las letras";
		Leer letras;
		
		Dimension vocales(a,e,i,o,u);
		
		mientras contar < 50 Hacer
			
			escribir "conteo= ",contar;
			contar<- contar +2 ;
			
		FinMientras
		
		mientras contar > 0 Hacer
			escribir "conteo= ",contar;
			contar<- contar -2;
		
		FinMientras
		
		escribir "¡Muy bien resolviste el ejercicio! ";
		
	
FinAlgoritmo
