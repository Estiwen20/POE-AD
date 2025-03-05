# Interfaz

import tkinter as tk
import re

texto_validar_nombre = ""

ventanaPrincipal = tk.Tk()
nombre = tk.StringVar(ventanaPrincipal)
labelNombre = tk.Label(ventanaPrincipal, text= "Nombre")
entryNombre = tk.Entry(ventanaPrincipal, textvariable= nombre)
ventanaPrincipal.title("Ventana Principal")
ventanaPrincipal.geometry("300x300")


labelValidacionNombre = tk.Label(ventanaPrincipal, text="")

def validar_letras(valor):
    patron = re.compile("^[A-Za-zñÑ ]*$")
    resultado = patron.match(valor.get()) is not None
    if not resultado:
        return False
    return True

def evento_presionar_tecla(event):
    global texto_validar_nombre
    global nombre
    if validar_letras(nombre):
        texto_validar_nombre = ""
    else:
        texto_validar_nombre = "Solo se permiten letras"
    labelValidacionNombre.config(text = texto_validar_nombre)
    print(nombre.get())



labelValidacionNombre.pack()
labelNombre.pack()
entryNombre.bind("<KeyRelease>", evento_presionar_tecla)
entryNombre.pack()
labelValidacionNombre.pack()

ventanaPrincipal.mainloop()