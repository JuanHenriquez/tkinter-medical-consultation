from tkinter import *
import Gui
import Data

# Configurar la ventana principal.
root = Tk()
root.title("Consultorio - Dr.Mata Lozano")
root.resizable(0, 0)
root.config(bg = "#263238")

# Variables Generales.
lista_pacientes = []
cedula_paciente = StringVar()
nombre_paciente = StringVar()
apellido_paciente = StringVar()
sexo_paciente = StringVar()
edad_paciente = IntVar()
numero_cita_cliente = IntVar()
medicamento = StringVar()

# Ventana para crear citas.
ventana_registro = Toplevel(root)

# Widgets de la ventana principal.
menu = Menu(root)
menuOpciones = Menu(menu)
menuOpciones.add_command(label = "Añadir Paciente", command =lambda: (Gui.mostrar(ventana_registro)))
menuOpciones.add_command(label = "Salir", command = root.destroy)
menu.add_cascade(label = "Opciones", menu = menuOpciones)
root.config(menu = menu)
Gui.mostrar_lista_espera(lista_pacientes, root)

# Widgets de la ventana para registrar.

# Apellido:
frame_cedula = Frame(ventana_registro)
frame_cedula.grid(row = 1, column = 1, padx = 20, pady = 5)
label_cedula = Label(frame_cedula, text = "Cedula: ")
label_cedula.grid(row = 1, column = 1)
input_cedula = Entry(frame_cedula, textvariable = cedula_paciente)
input_cedula.grid(row = 1, column = 2)

# Nombre:
frame_nombre = Frame(ventana_registro)
frame_nombre.grid(row = 2, column = 1, padx = 20, pady = 5)
label_nombre = Label(frame_nombre, text = "Nombre: ")
label_nombre.grid(row = 1, column = 1)
input_nombre = Entry(frame_nombre, textvariable = nombre_paciente)
input_nombre.grid(row = 1, column = 2)

# Apellido:
frame_apellido = Frame(ventana_registro)
frame_apellido.grid(row = 3, column = 1, padx = 20, pady = 5)
label_apellido = Label(frame_apellido, text = "Apellido: ")
label_apellido.grid(row = 1, column = 1)
input_apellido = Entry(frame_apellido, textvariable = apellido_paciente)
input_apellido.grid(row = 1, column = 2)

# Genero:
frame_genero = Frame(ventana_registro)
frame_genero.grid(row = 4, column = 1, padx = 20, pady = 5)
label_genero = Label(frame_genero, text = "Sexo: ")
label_genero.grid(row = 1, column = 1)
input_genero = Entry(frame_genero, textvariable = sexo_paciente)
input_genero.grid(row = 1, column = 2)

# Edad:
frame_edad = Frame(ventana_registro)
frame_edad.grid(row = 5, column = 1, padx = 20, pady = 5)
label_edad = Label(frame_edad, text = "Edad: ")
label_edad.grid(row = 1, column = 1)
input_edad = Entry(frame_edad, textvariable = edad_paciente)
input_edad.grid(row = 1, column = 2)

# Numero de cita:
frame_cita = Frame(ventana_registro)
frame_cita.grid(row = 6, column = 1, padx = 20, pady = 5)
label_cita = Label(frame_cita, text = "Numero de la cita: ")
label_cita.grid(row = 1, column = 1)
input_cita = Entry(frame_cita, textvariable = numero_cita_cliente)
input_cita.grid(row = 1, column = 2)

# Numero de cita:
frame_medicamento = Frame(ventana_registro)
frame_medicamento.grid(row = 7, column = 1, padx = 20, pady = 5)
label_medicamento = Label(frame_medicamento, text = "Seleccione un medicamento si es necesario")
label_medicamento.grid(row = 1, column = 1, pady = 20, padx = 20)











ventana_registro.withdraw()
root.mainloop()

