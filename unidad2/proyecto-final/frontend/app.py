import tkinter as tk
from tkinter import messagebox
import requests
import threading
import time

API_URL = "http://127.0.0.1:8000/api"
BACKUP_INTERVAL = 60  # segundos

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión Editorial Andina S.A.S.")
        self.root.geometry("800x800")
        self.root.config(bg="#cceeff")

        # Crear frames para autores y libros
        self.frame_autores = tk.LabelFrame(root, text="Autores", padx=10, pady=10, bg="#cceeff", font=("Arial", 14, "bold"))
        self.frame_libros = tk.LabelFrame(root, text="Libros", padx=10, pady=10, bg="#cceeff", font=("Arial", 14, "bold"))
        self.frame_autores.pack(side="left", fill="both", expand=True, padx=10, pady=10)
        self.frame_libros.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        # Construir UI para autores y libros
        self.crear_seccion_autores()
        self.crear_seccion_libros()

        # Lanzar hilo para respaldo automático
        threading.Thread(target=self.respaldos_automaticos, daemon=True).start()

    def crear_seccion_autores(self):
        # Etiquetas y entradas
        tk.Label(self.frame_autores, text="Nombre:", bg="#cceeff").pack(anchor="w")
        self.ent_nombre = tk.Entry(self.frame_autores, width=30)
        self.ent_nombre.pack()

        tk.Label(self.frame_autores, text="Nacionalidad:", bg="#cceeff").pack(anchor="w")
        self.ent_nacionalidad = tk.Entry(self.frame_autores, width=30)
        self.ent_nacionalidad.pack()

        tk.Label(self.frame_autores, text="Edad:", bg="#cceeff").pack(anchor="w")
        self.ent_edad = tk.Entry(self.frame_autores, width=30)
        self.ent_edad.pack()

        tk.Label(self.frame_autores, text="ID (para consultar/actualizar/borrar):", bg="#cceeff").pack(anchor="w", pady=(10,0))
        self.ent_id_autor = tk.Entry(self.frame_autores, width=30)
        self.ent_id_autor.pack()

        # Botones
        botones = [
            ("Crear", self.agregar_autor),
            ("Consultar Todos", self.ver_autores),
            ("Consultar por ID", self.consultar_autor_por_id),
            ("Actualizar", self.actualizar_autor),
            ("Borrar", self.borrar_autor),
            ("Limpiar", self.limpiar_campos_autor)
        ]
        for texto, cmd in botones:
            tk.Button(self.frame_autores, text=texto, width=20, command=cmd).pack(pady=3)

        # Área de texto para resultados
        tk.Label(self.frame_autores, text="Resultados:", bg="#cceeff", font=("Arial", 12, "bold")).pack(pady=(10,0), anchor="w")
        self.resultados_autores = tk.Text(self.frame_autores, height=15, width=40)
        self.resultados_autores.pack(pady=5)

    def crear_seccion_libros(self):
        tk.Label(self.frame_libros, text="Título:", bg="#cceeff").pack(anchor="w")
        self.ent_titulo = tk.Entry(self.frame_libros, width=30)
        self.ent_titulo.pack()

        tk.Label(self.frame_libros, text="Género:", bg="#cceeff").pack(anchor="w")
        self.ent_genero = tk.Entry(self.frame_libros, width=30)
        self.ent_genero.pack()

        tk.Label(self.frame_libros, text="Páginas:", bg="#cceeff").pack(anchor="w")
        self.ent_paginas = tk.Entry(self.frame_libros, width=30)
        self.ent_paginas.pack()

        tk.Label(self.frame_libros, text="Año:", bg="#cceeff").pack(anchor="w")
        self.ent_anio = tk.Entry(self.frame_libros, width=30)
        self.ent_anio.pack()

        tk.Label(self.frame_libros, text="ID (para consultar/actualizar/borrar):", bg="#cceeff").pack(anchor="w", pady=(10,0))
        self.ent_id_libro = tk.Entry(self.frame_libros, width=30)
        self.ent_id_libro.pack()

        botones = [
            ("Crear", self.agregar_libro),
            ("Consultar Todos", self.ver_libros),
            ("Consultar por ID", self.consultar_libro_por_id),
            ("Actualizar", self.actualizar_libro),
            ("Borrar", self.borrar_libro),
            ("Limpiar", self.limpiar_campos_libro)
        ]
        for texto, cmd in botones:
            tk.Button(self.frame_libros, text=texto, width=20, command=cmd).pack(pady=3)

        tk.Label(self.frame_libros, text="Resultados:", bg="#cceeff", font=("Arial", 12, "bold")).pack(pady=(10,0), anchor="w")
        self.resultados_libros = tk.Text(self.frame_libros, height=15, width=40)
        self.resultados_libros.pack(pady=5)

    # --- Métodos para autores ---
    def agregar_autor(self):
        datos = {
            "nombre": self.ent_nombre.get(),
            "nacionalidad": self.ent_nacionalidad.get(),
            "edad": self.ent_edad.get()
        }
        try:
            r = requests.post(f"{API_URL}/autores/", json=datos)
            if r.status_code == 201:
                messagebox.showinfo("Éxito", "Autor agregado correctamente")
                self.limpiar_campos_autor()
                self.ver_autores()
            else:
                messagebox.showerror("Error", f"Error al agregar autor:\n{r.text}")
        except Exception as e:
            messagebox.showerror("Error", f"Error de conexión:\n{e}")

    def ver_autores(self):
        try:
            r = requests.get(f"{API_URL}/autores/")
            self.resultados_autores.delete("1.0", tk.END)
            if r.status_code == 200:
                autores = r.json()
                if autores:
                    for a in autores:
                        self.resultados_autores.insert(tk.END, f"ID: {a['id']}\nNombre: {a['nombre']}\nNacionalidad: {a['nacionalidad']}\nEdad: {a['edad']}\n\n")
                else:
                    self.resultados_autores.insert(tk.END, "No hay autores registrados.\n")
            else:
                messagebox.showerror("Error", f"Error al obtener autores:\n{r.text}")
        except Exception as e:
            messagebox.showerror("Error", f"Error de conexión:\n{e}")

    def consultar_autor_por_id(self):
        id_ = self.ent_id_autor.get().strip()
        if not id_.isdigit():
            messagebox.showwarning("Advertencia", "Ingrese un ID válido para el autor.")
            return
        try:
            r = requests.get(f"{API_URL}/autores/{id_}/")
            self.resultados_autores.delete("1.0", tk.END)
            if r.status_code == 200:
                a = r.json()
                self.resultados_autores.insert(tk.END, f"ID: {a['id']}\nNombre: {a['nombre']}\nNacionalidad: {a['nacionalidad']}\nEdad: {a['edad']}\n")
                # Rellenar campos para actualización
                self.ent_nombre.delete(0, tk.END)
                self.ent_nombre.insert(0, a['nombre'])
                self.ent_nacionalidad.delete(0, tk.END)
                self.ent_nacionalidad.insert(0, a['nacionalidad'])
                self.ent_edad.delete(0, tk.END)
                self.ent_edad.insert(0, a['edad'])
            else:
                messagebox.showerror("Error", f"No se encontró autor con ID {id_}.")
        except Exception as e:
            messagebox.showerror("Error", f"Error de conexión:\n{e}")

    def actualizar_autor(self):
        id_ = self.ent_id_autor.get().strip()
        if not id_.isdigit():
            messagebox.showwarning("Advertencia", "Ingrese un ID válido para actualizar.")
            return
        datos = {
            "nombre": self.ent_nombre.get(),
            "nacionalidad": self.ent_nacionalidad.get(),
            "edad": self.ent_edad.get()
        }
        try:
            r = requests.put(f"{API_URL}/autores/{id_}/", json=datos)
            if r.status_code == 200:
                messagebox.showinfo("Éxito", "Autor actualizado correctamente")
                self.ver_autores()
            else:
                messagebox.showerror("Error", f"Error al actualizar:\n{r.text}")
        except Exception as e:
            messagebox.showerror("Error", f"Error de conexión:\n{e}")

    def borrar_autor(self):
        id_ = self.ent_id_autor.get().strip()
        if not id_.isdigit():
            messagebox.showwarning("Advertencia", "Ingrese un ID válido para borrar.")
            return
        try:
            r = requests.delete(f"{API_URL}/autores/{id_}/")
            if r.status_code == 204:
                messagebox.showinfo("Éxito", "Autor borrado correctamente")
                self.limpiar_campos_autor()
                self.ver_autores()
            else:
                messagebox.showerror("Error", f"No se pudo borrar el autor con ID {id_}.")
        except Exception as e:
            messagebox.showerror("Error", f"Error de conexión:\n{e}")

    def limpiar_campos_autor(self):
        self.ent_nombre.delete(0, tk.END)
        self.ent_nacionalidad.delete(0, tk.END)
        self.ent_edad.delete(0, tk.END)
        self.ent_id_autor.delete(0, tk.END)
        self.resultados_autores.delete("1.0", tk.END)

    # --- Métodos para libros ---
    def agregar_libro(self):
        datos = {
            "titulo": self.ent_titulo.get(),
            "genero": self.ent_genero.get(),
            "paginas": self.ent_paginas.get(),
            "anio": self.ent_anio.get()
        }
        try:
            r = requests.post(f"{API_URL}/libros/", json=datos)
            if r.status_code == 201:
                messagebox.showinfo("Éxito", "Libro agregado correctamente")
                self.limpiar_campos_libro()
                self.ver_libros()
            else:
                messagebox.showerror("Error", f"Error al agregar libro:\n{r.text}")
        except Exception as e:
            messagebox.showerror("Error", f"Error de conexión:\n{e}")

    def ver_libros(self):
        try:
            r = requests.get(f"{API_URL}/libros/")
            self.resultados_libros.delete("1.0", tk.END)
            if r.status_code == 200:
                libros = r.json()
                if libros:
                    for l in libros:
                        self.resultados_libros.insert(tk.END, f"ID: {l['id']}\nTítulo: {l['titulo']}\nGénero: {l['genero']}\nPáginas: {l['paginas']}\nAño: {l['anio']}\n\n")
                else:
                    self.resultados_libros.insert(tk.END, "No hay libros registrados.\n")
            else:
                messagebox.showerror("Error", f"Error al obtener libros:\n{r.text}")
        except Exception as e:
            messagebox.showerror("Error", f"Error de conexión:\n{e}")

    def consultar_libro_por_id(self):
        id_ = self.ent_id_libro.get().strip()
        if not id_.isdigit():
            messagebox.showwarning("Advertencia", "Ingrese un ID válido para el libro.")
            return
        try:
            r = requests.get(f"{API_URL}/libros/{id_}/")
            self.resultados_libros.delete("1.0", tk.END)
            if r.status_code == 200:
                l = r.json()
                self.resultados_libros.insert(tk.END, f"ID: {l['id']}\nTítulo: {l['titulo']}\nGénero: {l['genero']}\nPáginas: {l['paginas']}\nAño: {l['anio']}\n")
                # Rellenar campos para actualización
                self.ent_titulo.delete(0, tk.END)
                self.ent_titulo.insert(0, l['titulo'])
                self.ent_genero.delete(0, tk.END)
                self.ent_genero.insert(0, l['genero'])
                self.ent_paginas.delete(0, tk.END)
                self.ent_paginas.insert(0, l['paginas'])
                self.ent_anio.delete(0, tk.END)
                self.ent_anio.insert(0, l['anio'])
            else:
                messagebox.showerror("Error", f"No se encontró libro con ID {id_}.")
        except Exception as e:
            messagebox.showerror("Error", f"Error de conexión:\n{e}")

    def actualizar_libro(self):
        id_ = self.ent_id_libro.get().strip()
        if not id_.isdigit():
            messagebox.showwarning("Advertencia", "Ingrese un ID válido para actualizar.")
            return
        datos = {
            "titulo": self.ent_titulo.get(),
            "genero": self.ent_genero.get(),
            "paginas": self.ent_paginas.get(),
            "anio": self.ent_anio.get()
        }
        try:
            r = requests.put(f"{API_URL}/libros/{id_}/", json=datos)
            if r.status_code == 200:
                messagebox.showinfo("Éxito", "Libro actualizado correctamente")
                self.ver_libros()
            else:
                messagebox.showerror("Error", f"Error al actualizar:\n{r.text}")
        except Exception as e:
            messagebox.showerror("Error", f"Error de conexión:\n{e}")

    def borrar_libro(self):
        id_ = self.ent_id_libro.get().strip()
        if not id_.isdigit():
            messagebox.showwarning("Advertencia", "Ingrese un ID válido para borrar.")
            return
        try:
            r = requests.delete(f"{API_URL}/libros/{id_}/")
            if r.status_code == 204:
                messagebox.showinfo("Éxito", "Libro borrado correctamente")
                self.limpiar_campos_libro()
                self.ver_libros()
            else:
                messagebox.showerror("Error", f"No se pudo borrar el libro con ID {id_}.")
        except Exception as e:
            messagebox.showerror("Error", f"Error de conexión:\n{e}")

    def limpiar_campos_libro(self):
        self.ent_titulo.delete(0, tk.END)
        self.ent_genero.delete(0, tk.END)
        self.ent_paginas.delete(0, tk.END)
        self.ent_anio.delete(0, tk.END)
        self.ent_id_libro.delete(0, tk.END)
        self.resultados_libros.delete("1.0", tk.END)

    # --- Respaldo automático ---
    def respaldos_automaticos(self):
        while True:
            time.sleep(10)
            try:
                # Obtener autores y guardar en archivo
                r_autores = requests.get(f"{API_URL}/autores/")
                if r_autores.status_code == 200:
                    with open("respaldo_autores.txt", "w", encoding="utf-8") as f:
                        for a in r_autores.json():
                            f.write(f"ID: {a['id']}\n")
                            f.write(f"Nombre: {a['nombre']}\n")
                            f.write(f"Nacionalidad: {a['nacionalidad'].capitalize()}\n")
                            f.write(f"Edad: {a['edad']}\n\n")  # línea en blanco para separar autores


                # Obtener libros y guardar en archivo
                r_libros = requests.get(f"{API_URL}/libros/")
                if r_libros.status_code == 200:
                    with open("respaldo_libros.txt", "w", encoding="utf-8") as f:
                        for l in r_libros.json():
                            f.write(f"ID: {l['id']}\n")
                            f.write(f"Título: {l['titulo']}\n")
                            f.write(f"Género: {l['genero']}\n")
                            f.write(f"Páginas: {l['paginas']}\n")
                            f.write(f"Año: {l['anio']}\n\n")


                print("Respaldo automático realizado.")
            except Exception as e:
                print(f"Error en respaldo automático: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

