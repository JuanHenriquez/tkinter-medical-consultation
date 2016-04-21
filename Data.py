#_*_coding:UTF-8_*_
from tkinter import *


# Lista de Medicamentos:

lista_tratamientos = [
    { 'nombre': 'Vacio', ' precio': 0 },
    { 'nombre': 'Restauración en Amalgama', 'precio': 500},
    { 'nombre': 'Restauración en Resina', 'precio': 600 },
    { 'nombre': 'Endodoncia', 'precio': 800 },
    { 'nombre': 'Exodoncia Simple', 'precio': 1000 },
    { 'nombre': }
]

# Añadir nuevo paciente a la lista.
def crear_cita(lista, cedula, nombre, apellido, edad, sexo, numero_cita, medicamento):
    paciente = {
        'nombre': nombre,
        'apellido': apellido,
        'edad': edad,
        'sexo': sexo,
        'numero_cita': numero_cita
    }

    total_cita(paciente, numero_cita)

    if medicamento['nombre'] == 'Vacio':
        paciente['medicamento'] = 0
        paciente['medicamento_precio'] = 0
    else:
        paciente['medicamento'] = medicamento['nombre']
        paciente['medicamento_precio'] = medicamento['precio']


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
