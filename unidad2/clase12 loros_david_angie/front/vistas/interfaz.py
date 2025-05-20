import tkinter as tk
from tkinter import messagebox, ttk
from front.modelos.loro import Loro

class Interfaz:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Gestión de Loros")
        self.ventana.geometry("800x800")
        self.ventana.config(bg="#228B22")  # Verde bosque

        # Base de datos simulada
        self.loros = {}
        self.contador_id = 1

        # Campos de entrada
        campos = ["ID", "Nombre", "Edad", "Color", "Tamaño", "Tamaño de alas"]
        self.entradas = {}

        for i, campo in enumerate(campos):
            label = tk.Label(self.ventana, text=campo, bg="#228B22", fg="white", font=("Arial", 12, "bold"))
            label.grid(row=i, column=0, padx=10, pady=5, sticky="w")

            entrada = tk.Entry(self.ventana, font=("Arial", 12))
            entrada.grid(row=i, column=1, padx=10, pady=5)
            self.entradas[campo] = entrada

        # Botones
        botones = [
            ("Registrar", self.registrar_loro),
            ("Consultar por ID", self.consultar_por_id),
            ("Consultar todos", self.consultar_todos),
            ("Actualizar", self.actualizar_loro),
            ("Eliminar", self.eliminar_loro),
            ("Limpiar", self.limpiar_campos)
        ]

        for i, (texto, comando) in enumerate(botones):
            btn = tk.Button(self.ventana, text=texto, command=comando, font=("Arial", 12, "bold"), bg="#006400", fg="white")
            btn.grid(row=7 + i, column=0, columnspan=2, pady=5, sticky="ew", padx=10)

        # Tabla (Treeview) para mostrar loros
        columnas = ("ID", "Nombre", "Edad", "Color", "Tamaño", "Tamaño de alas")
        self.tabla = ttk.Treeview(self.ventana, columns=columnas, show="headings", height=15)
        for col in columnas:
            self.tabla.heading(col, text=col)
            self.tabla.column(col, anchor=tk.CENTER)

        self.tabla.grid(row=0, column=2, rowspan=13, padx=10, pady=10, sticky="nsew")

        # Configurar fila y columna para que la tabla pueda expandirse
        self.ventana.grid_rowconfigure(13, weight=1)
        self.ventana.grid_columnconfigure(2, weight=1)

        self.ventana.mainloop()

    def registrar_loro(self):
        try:
            nombre = self.entradas["Nombre"].get()
            edad = int(self.entradas["Edad"].get())
            color = self.entradas["Color"].get()
            tamaño = self.entradas["Tamaño"].get()
            alas = float(self.entradas["Tamaño de alas"].get())

            loro = Loro(nombre, edad, color, tamaño, alas)
            self.loros[self.contador_id] = loro
            self.contador_id += 1

            messagebox.showinfo("Éxito", f"Loro registrado con ID {self.contador_id - 1}")
            self.limpiar_campos()
            self.actualizar_tabla()
        except ValueError:
            messagebox.showerror("Error", "Por favor ingresa datos válidos")

    def consultar_por_id(self):
        try:
            id_loro = int(self.entradas["ID"].get())
            loro = self.loros.get(id_loro)
            if loro:
                self.entradas["Nombre"].delete(0, tk.END)
                self.entradas["Nombre"].insert(0, loro.nombre)
                self.entradas["Edad"].delete(0, tk.END)
                self.entradas["Edad"].insert(0, loro.edad)
                self.entradas["Color"].delete(0, tk.END)
                self.entradas["Color"].insert(0, loro.color)
                self.entradas["Tamaño"].delete(0, tk.END)
                self.entradas["Tamaño"].insert(0, loro.tamaño)
                self.entradas["Tamaño de alas"].delete(0, tk.END)
                self.entradas["Tamaño de alas"].insert(0, loro.tamaño_alas)

                # Mostrar solo ese loro en la tabla
                self.actualizar_tabla([ (id_loro, loro) ])
            else:
                messagebox.showwarning("No encontrado", "No se encontró un loro con ese ID")
                self.actualizar_tabla()
        except ValueError:
            messagebox.showerror("Error", "ID inválido")

    def consultar_todos(self):
        if self.loros:
            self.actualizar_tabla()
        else:
            messagebox.showinfo("Vacío", "No hay loros registrados")
            self.actualizar_tabla([])

    def actualizar_loro(self):
        try:
            id_loro = int(self.entradas["ID"].get())
            if id_loro in self.loros:
                nombre = self.entradas["Nombre"].get()
                edad = int(self.entradas["Edad"].get())
                color = self.entradas["Color"].get()
                tamaño = self.entradas["Tamaño"].get()
                alas = float(self.entradas["Tamaño de alas"].get())

                self.loros[id_loro] = Loro(nombre, edad, color, tamaño, alas)
                messagebox.showinfo("Actualizado", f"Loro ID {id_loro} actualizado")
                self.actualizar_tabla()
            else:
                messagebox.showwarning("No encontrado", "No existe un loro con ese ID")
        except ValueError:
            messagebox.showerror("Error", "Datos inválidos")

    def eliminar_loro(self):
        try:
            id_loro = int(self.entradas["ID"].get())
            if id_loro in self.loros:
                del self.loros[id_loro]
                messagebox.showinfo("Eliminado", f"Loro ID {id_loro} eliminado")
                self.limpiar_campos()
                self.actualizar_tabla()
            else:
                messagebox.showwarning("No encontrado", "No existe un loro con ese ID")
        except ValueError:
            messagebox.showerror("Error", "ID inválido")

    def limpiar_campos(self):
        for entrada in self.entradas.values():
            entrada.delete(0, tk.END)
        # Mostrar todos los loros al limpiar
        self.actualizar_tabla()

    def actualizar_tabla(self, lista=None):
        # Limpiar tabla actual
        for item in self.tabla.get_children():
            self.tabla.delete(item)

        # Si no se pasa lista, mostramos todos
        if lista is None:
            lista = self.loros.items()

        for id_loro, loro in lista:
            self.tabla.insert("", "end", values=(
                id_loro,
                loro.nombre,
                loro.edad,
                loro.color,
                loro.tamaño,
                loro.tamaño_alas
            ))
