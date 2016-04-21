from tkinter import *
import Gui
import Data

# Configurar la ventana principal.
root = Tk()
root.title("Consultorio - Dr.Mata Lozano")
root.resizable(0, 0)
root.geometry("600x450+400+100")
root.config(bg = Gui.color_primary)

# Variables Generales.
lista_pacientes = []
cedula_paciente = StringVar()
nombre_paciente = StringVar()
apellido_paciente = StringVar()
sexo_paciente = StringVar()
edad_paciente = IntVar()
numero_cita_cliente = IntVar()
tratamiento = StringVar()

top_frame = Frame(root, bg = Gui.color_dark_primary, width = 600, height = 150)
top_frame.pack(side = TOP)
bottom_frame = Frame(root, bg = Gui.color_text, width = 600, height = 300)
bottom_frame.pack(side = BOTTOM)

root.mainloop()
