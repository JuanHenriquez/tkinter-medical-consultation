from Tkinter import *
from Gui import *
from Data import *

# Configurar la ventana principal.
root = Tk()
root.title("Consultorio - Dr.Mata Lozano")
root.resizable(0, 0)
root.config(bg = "#263238")

# Widgets de la ventana principal

# Variables Generales.
lista_citas       = []
nombre_paciente   = StringVar()
apellido_paciente = StringVar()
sexo_paciente     = StringVar()
edad_paciente     = IntVar()

# Ventana para crear citas.
ventana_crear_cita = Toplevel(root)
ventana_crear_cita.protocol("WM_DELETE_WINDOW", ventana_cuenta.withdraw)






root.mainloop()
