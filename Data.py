def crear_cita(lista, cedula, nombre, apellido, edad, sexo, numero_cita):
    paciente = {
        'nombre': nombre,
        'apellido': apellido,
        'edad': edad,
        'sexo': sexo,
        'numero_cita': numero_cita
    }
    
    lista.append(paciente)