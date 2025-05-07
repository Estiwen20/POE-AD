import tkinter as tk
from tkinter import messagebox
import requests

API_URL = "http://localhost:8000/loros/"

def buscar():
    loro_id = entry_id.get()
    if loro_id:
        response = requests.get(API_URL + loro_id + "/")
        if response.status_code == 200:
            data = response.json()
            entry_nombre.delete(0, tk.END)
            entry_nombre.insert(0, data['nombre'])
            entry_tamaño.delete(0, tk.END)
            entry_tamaño.insert(0, data['tamaño'])
            entry_edad.delete(0, tk.END)
            entry_edad.insert(0, data['edad'])
            entry_color.delete(0, tk.END)
            entry_color.insert(0, data['color'])
        else:
            messagebox.showerror("Error", "loro no encontrado")

def guardar():
    data = {
        "nombre": entry_nombre.get(),
        "tamaño": entry_tamaño.get(),
        "edad": int(entry_edad.get()),
        "color": entry_color.get()
    }
    response = requests.post(API_URL, json=data)
    if response.status_code in (200, 201):
        messagebox.showinfo("Éxito", "Cliente guardado")
    limpiar_campos()

def actualizar():
    cliente_id = entry_id.get()
    if cliente_id:
        data = {
            "nombre": entry_nombre.get(),
            "tamaño": entry_tamaño.get(),
            "edad": int(entry_edad.get()),
            "color": entry_color.get()
        }
        response = requests.put(API_URL + cliente_id + "/", json=data)
        if response.status_code == 200:
            messagebox.showinfo("Éxito", "loro actualizado")
    limpiar_campos()

def eliminar():
    loro_id = entry_id.get()
    if loro_id:
        response = requests.delete(API_URL + loro_id + "/")
        if response.status_code == 204:
            messagebox.showinfo("Éxito", "Cliente eliminado")
    limpiar_campos()

def limpiar_campos():
    entry_id.delete(0, tk.END)
    entry_nombre.delete(0, tk.END)
    entry_tamaño.delete(0, tk.END)
    entry_edad.delete(0, tk.END)
    entry_color.delete(0, tk.END)


root = tk.Tk()
root.title("Gestión de Clientes")

tk.Label(root, text="ID").grid(row=0, column=0)
entry_id = tk.Entry(root)
entry_id.grid(row=0, column=1)
tk.Button(root, text="Buscar", command=buscar).grid(row=0, column=2)

tk.Label(root, text="Nombre").grid(row=1, column=0)
entry_nombre = tk.Entry(root)
entry_nombre.grid(row=1, column=1)

tk.Label(root, text="tamaño").grid(row=2, column=0)
entry_tamaño = tk.Entry(root)
entry_tamaño.grid(row=2, column=1)

tk.Label(root, text="Edad").grid(row=3, column=0)
entry_edad = tk.Entry(root)
entry_edad.grid(row=3, column=1)

tk.Label(root, text="color").grid(row=4, column=0)
entry_color = tk.Entry(root)
entry_color.grid(row=4, column=1)

tk.Button(root, text="Guardar", command=guardar).grid(row=5, column=0)
tk.Button(root, text="Actualizar", command=actualizar).grid(row=5, column=1)
tk.Button(root, text="Eliminar", command=eliminar).grid(row=5, column=2)

root.mainloop()
