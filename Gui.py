from tkinter import *

def mostrar(ventana):
    ventana.deiconify()

def esconder(ventana):
    ventana.withdraw()

def mostrar_lista_espera(lista, ventana):

    if len(lista) == 0:
        label_titulo_lista = Label(ventana, text = "No hay ningun paciente esperando.")
        label_titulo_lista.grid(row = 1, column = 1, padx = 30, pady = 20)
    for usuario in lista:
        label_titulo_lista = Label(ventana, text = "Lista de Espera: \n -----------------")
        label_titulo_lista.grid(row = 1, column = 1, padx = 30, pady = 20)
        label_nombre = Label(ventana, text = "Nombre: " + usuario.nombre)
        label_nombre.grid(row = 2, column = 1, padx = 30, pady = 20)
