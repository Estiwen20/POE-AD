import tkinter as tk

def validar_texto(event, campo, mensaje_error):
    """Verifica que el texto solo contenga letras y muestra el mensaje de error."""
    texto = campo.get().strip()
    if not texto.isalpha() and texto != "":
        mensaje_error.set("Solo se pueden usar letras.")
    else:
        mensaje_error.set("")

def validar_numeros(event, campo, mensaje_error):
    """Verifica que el texto solo contenga números y muestra el mensaje de error."""
    texto = campo.get().strip()
    if not texto.isdigit() and texto != "":
        mensaje_error.set("Solo se pueden usar números.")
    else:
        mensaje_error.set("")

def mostrar_datos():
    """Obtiene los datos ingresados, valida y los muestra."""
    marca = entrada_marca.get().strip()
    tamano = entrada_tamano.get().strip()
    resolucion = entrada_resolucion.get().strip()
    tipo_pantalla = entrada_tipo.get().strip()

    error_marca.set("")
    error_tamano.set("")
    error_resolucion.set("")
    error_tipo.set("")

    valido = True

    if not validar_texto(None, entrada_marca, error_marca):
        valido = False

    if not validar_numeros(None, entrada_tamano, error_tamano):
        valido = False

    if not validar_numeros(None, entrada_resolucion, error_resolucion):
        valido = False

    if not validar_texto(None, entrada_tipo, error_tipo):
        valido = False

    if valido:
        etiqueta_resultado.config(
            text=f"Marca: {marca}\nTamaño: {tamano} pulgadas\nResolución: {resolucion}p\nTipo de pantalla: {tipo_pantalla}"
        )
    else:
        etiqueta_resultado.config(text="")

ventana = tk.Tk()
ventana.title("Datos del Televisor")
ventana.geometry("350x300")

tk.Label(ventana, text="Marca:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
entrada_marca = tk.Entry(ventana)
entrada_marca.grid(row=0, column=1, padx=10, pady=5)

error_marca = tk.StringVar()
tk.Label(ventana, textvariable=error_marca, fg="red", font=("Arial", 8)).grid(row=1, column=1, padx=10, pady=0, sticky="w")

entrada_marca.bind("<KeyRelease>", lambda event: validar_texto(event, entrada_marca, error_marca))

tk.Label(ventana, text="Tamaño (pulgadas):").grid(row=2, column=0, padx=10, pady=5, sticky="w")
entrada_tamano = tk.Entry(ventana)
entrada_tamano.grid(row=2, column=1, padx=10, pady=5)

error_tamano = tk.StringVar()
tk.Label(ventana, textvariable=error_tamano, fg="red", font=("Arial", 8)).grid(row=3, column=1, padx=10, pady=0, sticky="w")

entrada_tamano.bind("<KeyRelease>", lambda event: validar_numeros(event, entrada_tamano, error_tamano))

tk.Label(ventana, text="Resolución (p):").grid(row=4, column=0, padx=10, pady=5, sticky="w")
entrada_resolucion = tk.Entry(ventana)
entrada_resolucion.grid(row=4, column=1, padx=10, pady=5)

error_resolucion = tk.StringVar()
tk.Label(ventana, textvariable=error_resolucion, fg="red", font=("Arial", 8)).grid(row=5, column=1, padx=10, pady=0, sticky="w")

entrada_resolucion.bind("<KeyRelease>", lambda event: validar_numeros(event, entrada_resolucion, error_resolucion))

tk.Label(ventana, text="Tipo de pantalla:").grid(row=6, column=0, padx=10, pady=5, sticky="w")
entrada_tipo = tk.Entry(ventana)
entrada_tipo.grid(row=6, column=1, padx=10, pady=5)

error_tipo = tk.StringVar()
tk.Label(ventana, textvariable=error_tipo, fg="red", font=("Arial", 8)).grid(row=7, column=1, padx=10, pady=0, sticky="w")

entrada_tipo.bind("<KeyRelease>", lambda event: validar_texto(event, entrada_tipo, error_tipo))


etiqueta_resultado = tk.Label(ventana, text="", font=("Arial", 10), justify="left")
etiqueta_resultado.grid(row=9, column=0, columnspan=2, padx=10, pady=5)

ventana.mainloop()