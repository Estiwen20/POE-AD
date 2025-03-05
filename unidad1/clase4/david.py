import tkinter as tk
import re

def validar_letras(texto):
    return bool(re.match("^[A-Za-z\u00f1\u00d1 ]*$", texto))

def validar_numeros(texto):
    return bool(re.match("^[0-9]*$", texto))

def evento_presionar_tecla_nombre(event):
    if validar_letras(nombre_var.get()):
        label_validacion_nombre.config(text="")
    else:
        label_validacion_nombre.config(text="Solo se permiten letras", fg="red")

def evento_presionar_tecla_color(event):
    if validar_letras(color_var.get()):
        label_validacion_color.config(text="")
    else:
        label_validacion_color.config(text="Solo se permiten letras", fg="red")

def evento_presionar_tecla_alas(event):
    if validar_letras(alas_var.get()):
        label_validacion_alas.config(text="")
    else:
        label_validacion_alas.config(text="Solo se permiten letras", fg="red")

def evento_presionar_tecla_edad(event):
    if validar_numeros(edad_var.get()):
        label_validacion_edad.config(text="")
    else:
        label_validacion_edad.config(text="Solo se permiten números", fg="red")

def salir():
    root.quit()

root = tk.Tk()
root.title("Loro")
root.geometry("500x700")

# Campo: Alas
alas_var = tk.StringVar()
label_alas = tk.Label(root, text="Alas", font=("Arial", 10))
label_alas.pack(pady=5)
entry_alas = tk.Entry(root, font=("Arial", 14), textvariable=alas_var)
entry_alas.pack(pady=10)
entry_alas.bind("<KeyRelease>", evento_presionar_tecla_alas)
label_validacion_alas = tk.Label(root, text="", font=("Arial", 10), fg="red")
label_validacion_alas.pack()

# Campo: Color (Solo letras)
color_var = tk.StringVar()
label_color = tk.Label(root, text="Color", font=("Arial", 10))
label_color.pack(pady=15)
entry_color = tk.Entry(root, font=("Arial", 14), textvariable=color_var)
entry_color.pack(pady=20)
entry_color.bind("<KeyRelease>", evento_presionar_tecla_color)
label_validacion_color = tk.Label(root, text="", font=("Arial", 10), fg="red")
label_validacion_color.pack()

# Campo: Nombre (Solo letras)
nombre_var = tk.StringVar()
label_nombre = tk.Label(root, text="Nombre", font=("Arial", 10))
label_nombre.pack(pady=25)
entry_nombre = tk.Entry(root, font=("Arial", 14), textvariable=nombre_var)
entry_nombre.pack(pady=30)
entry_nombre.bind("<KeyRelease>", evento_presionar_tecla_nombre)
label_validacion_nombre = tk.Label(root, text="", font=("Arial", 10), fg="red")
label_validacion_nombre.pack()

# Campo: Edad (Solo números)
edad_var = tk.StringVar()
label_edad = tk.Label(root, text="Edad", font=("Arial", 10))
label_edad.pack(pady=35)
entry_edad = tk.Entry(root, font=("Arial", 14), textvariable=edad_var)
entry_edad.pack(pady=40)
entry_edad.bind("<KeyRelease>", evento_presionar_tecla_edad)
label_validacion_edad = tk.Label(root, text="", font=("Arial", 10), fg="red")
label_validacion_edad.pack()

boton_salir = tk.Button(root, text="Salir", font=("Arial", 14), command=salir)
boton_salir.pack(pady=20)

root.mainloop()