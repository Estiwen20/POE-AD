import tkinter as tk

class Autor():
        
    def __init__(self, ventanaPrincipal):
        self.ventanaPrincipal = ventanaPrincipal
        self.id = tk.StringVar(ventanaPrincipal)
        self.nombre = tk.StringVar(ventanaPrincipal)
        self.edad = tk.IntVar(ventanaPrincipal)
        self.nacionalidad = tk.StringVar(ventanaPrincipal)