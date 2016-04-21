#_*_coding:UTF-8_*_
from tkinter import *

# Lista de Tratamientos:

lista_tratamientos = [
    { 'nombre': 'Vacio', 'precio': 0 },
    { 'nombre': 'Restauración en Amalgama', 'precio': 5000},
    { 'nombre': 'Restauración en Resina', 'precio': 7000 },
    { 'nombre': 'Endodoncia', 'precio': 8000 },
    { 'nombre': 'Exodoncia Simple', 'precio': 9000 },
    { 'nombre': 'Exodoncia Compleja', 'precio': 102789 }
]

# Añadir nuevo paciente a la lista.
def crear_cita(lista, cedula, nombre, apellido, edad, sexo, numero_cita, tratamiento):
    paciente = {
        'cedula': cedula,
        'nombre': nombre,
        'apellido': apellido,
        'edad': edad,
        'sexo': sexo,
        'numero_cita': numero_cita,
        'tratamiento': tratamiento
    }

    for tratamiento_item in lista_tratamientos:
        if tr['nombre'] == tratamiento:
            paciente['costo_tratamiento'] = tratamiento_item['precio']

    total_cita(paciente, numero_cita)

    lista.append(paciente)

# Calculo del pago de la cita.
def total_cita(paciente, numero_cita):
    if numero_cita <= 3:
        paciente['total_cita'] = 6000
    elif numero_cita >= 4 and numero_cita <= 5:
        paciente['total_cita'] = 4500
    elif numero_cita > 5 and numero_cita <= 8:
        paciente['total_cita'] = 3000
    else:
        paciente['total_cita'] = 2000

# Otros Datos:

description_text = 'Puede apartar su cita ya mismo haciendo click en el menu "Paciente" '\
                    'de la parte de arriba!'
