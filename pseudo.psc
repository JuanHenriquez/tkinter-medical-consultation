Proceso SolicitudDeCitas
	
	// Variables.
	
	contPaciente = 0
	numConsulta = 1
	respuesta = "s"
	
	// Matriz que guarda usuarios.
	Dimension pacientes_dc[100, 4]
	Dimension pacientes_dn[100, 4]
	
	// Vector con los precios:
	Dimension precios[4]
	precios[1] = 6000
	precios[2] = 4500
	precios[3] = 3000
	precios[4] = 2000
	
	
	// Vector con tratamientos:
	Dimension  tratamientos[5]
	tratamientos[1] = "Restauración en Amalgama"
	tratamientos[2] = "Restauración en Resina"
	tratamientos[3] = "Endodoncia"
	tratamientos[4] = "Exodoncia Simple"
	tratamientos[5] = "Exodoncia Compleja"
	
	// Vector con precios de tratamientos:
	Dimension tratamientos_precio[5] 
	tratamientos_precio[1] = Aleatorio(500, 1000)
	tratamientos_precio[2] = Aleatorio(2000, 3000)
	tratamientos_precio[3] = Aleatorio(4000, 6000)
	tratamientos_precio[4] = Aleatorio(5000, 8000)
	tratamientos_precio[5] = Aleatorio(10000, 20000)
	
	Escribir "Bienvenido al consultorio del Dr. Mata Lozano"
	
	Mientras respuesta = "s" o respuesta = "S" Hacer
		
		contPaciente = contPaciente + 1
		
		Escribir "Cedula de Identidad: "
		Leer pacientes_dn[contPaciente, 1]
		Escribir "Nombre: "
		Leer pacientes_dc[contPaciente, 1]
		Escribir "Apellido: "
		Leer pacientes_dc[contPaciente, 2]
		Escribir "Edad: "
		Leer pacientes_dn[contPaciente, 2]
		Escribir "Sexo: "
		Leer pacientes_dc[contPaciente, 3]
		Escribir "Numero de la consulta: "
		Leer numeroCitas
		
		
		
		// Validar precio de la cita:
		Si ConvertirANumero(numeroCitas) <= 3 Entonces
			pacientes_dn[contPaciente, 3] = precios[1]
		Fin Si
		
		Si ConvertirANumero(numeroCitas) >= 4 y ConvertirANumero(numeroCitas) <= 5 Entonces
			pacientes_dn[contPaciente, 3] = precios[2]
		FinSi
		
		Si ConvertirANumero(numeroCitas) >= 6 y ConvertirANumero(numeroCitas) <= 8 Entonces
			pacientes_dn[contPaciente, 3] = precios[3]
		FinSi
		
		Si ConvertirANumero(numeroCitas) >= 9 Entonces
			pacientes_dn[contPaciente, 3] = precios[4]
		FinSi
		
		num_tratamiento = 1
		
		// Elegir tratamiento: 
		Mientras respuesta2 = 0 Hacer
			Escribir "Elija uno de los tratamientos: "
			Escribir "1.- " tratamientos[1]
			Escribir "2.- " tratamientos[2]
			Escribir "3.- " tratamientos[3]
			Escribir "4.- " tratamientos[4]
			Escribir "5.- " tratamientos[5]
			Leer num_tratamiento
			
			Si num_tratamiento == 1 o num_tratamiento == 2 o num_tratamiento == 3 o num_tratamiento == 4 o num_tratamiento == 5
				respuesta2 = 1
			Sino
				Escribir "Opcion invalida"
			FinSi
		Fin Mientras
		
		pacientes_dn[contPaciente, 4] = num_tratamiento 
		
		Escribir "¿Desea ingresar a otro paciente?(s/n): "
		Leer respuesta
		
		Escribir pacientes_dn[contPaciente, 4]
		
		Limpiar Pantalla
		
	Fin Mientras
	
	Escribir "Lista de clientes:"
	Escribir "----------------------------------"
	Para i = 1 Hasta contPaciente Hacer
		Escribir "Cedula de Identidad: " pacientes_dn[i, 1]
		Escribir "Nombre: " pacientes_dc[i, 1]
		Escribir "Apellido: " pacientes_dc[i, 2]
		Escribir "Edad: " pacientes_dn[i, 2]
		Escribir "Sexo: " pacientes_dc[i, 3]
		Escribir "Costo de la cita: " pacientes_dn[i, 3]
		Escribir "Tratamiento del paciente: " tratamientos[pacientes_dn[i, 4]]
		Escribir "Costo del tratamiento: " tratamientos_precio[pacientes_dn[i, 4]]
		Escribir "-------------------------------"
	Fin Para
	
FinProceso
