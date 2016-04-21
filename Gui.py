from tkinter import *

# Colores:
color_text           = "#FFFFFF"
color_dark_primary   = "#455A64"
color_primary        = "#607D8B"
color_accent         = "#00BCD4"
color_primary_text   = "#212121"
color_secundary_text = "#727272"

def mostrar(ventana):
    ventana.deiconify()

def esconder(ventana):
    ventana.withdraw()

def mostrar_lista_espera(lista, ventana):

    datos = ""

    if len(lista) == 0:
        datos = "No hay ningun paciente en espera."
    else:
        datos = "Lista de Espera: \n ------------------------------ \n"
        for usuario in lista:
            datos += "Cedula: " + usuario['cedula'] + "\n"
            datos += "Nombre: " +usuario['nombre'] + "\n"
            datos += "Apellido: " + usuario['apellido'] + "\n"
            datos += "Edad: " + str(usuario['edad']) + "\n"
            datos += "Sexo: " + usuario['sexo'] + "\n"
            datos += "Numero de la cita: " + str(usuario['numero_cita']) + "\n"
            datos += "Precio de la cita: " + str(usuario['total_cita']) + "\n"
            datos += "Tratamiento: " + usuario['tratamiento'] + "\n"
            datos += "Costo del tratamiento: " + str(usuario['costo_tratamiento']) + "\n---------------------- \n"

    label_nombre = Label(ventana, text = datos)
    label_nombre.grid(row = 3, column = 1, padx = 100, pady = 20)
