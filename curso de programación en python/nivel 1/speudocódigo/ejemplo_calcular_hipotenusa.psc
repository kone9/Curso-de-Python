Proceso Area_triaungulo
//basicos suma,resta,multiplicación,divición
//defino el tipo de dato,nombre y identificador
	Definir cateto_adyacente Como entero;
	Definir cateto_opuesto Como entero;
;
	
	//digo por consola lo que tenes que hacer
	escribir"ingrese el valor del cateto adyacente";
	//Uso leer para guardar el dato
	Leer cateto_adyacente ;
	//digo por consola lo que tenes que hacer
	escribir"ingrese el valor del cateto opuesto";
	//Uso leer para guardar el dato
	Leer cateto_opuesto;
	
//declaro la variable con los datos ingresados para la base del triangulo (RC(x) representa raiz)
	hipotenusa <- RC((cateto_opuesto)^2 + (cateto_opuesto)^2);
//muestro en pantalla el area del triangulo
	
	escribir"La hipotenusa es"," ",hipotenusa;
	
	
FinProceso

