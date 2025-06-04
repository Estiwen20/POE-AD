import tkinter as tk
from tkinter import ttk

class Tabla():
    def __init__(self, ventanaPrincipal, titulos, columnas, data):
        # Contenedor con borde y color de fondo elegante
        contenedor = tk.Frame(ventanaPrincipal, bg="#28044D", bd=2, relief="groove")
        contenedor.pack(expand=True, fill='both', padx=15, pady=15)

        # Estilo personalizado
        estilo = ttk.Style()
        estilo.theme_use("clam")  # permite personalizar mejor

        # Estilo general de la tabla
        estilo.configure("Treeview",
                         background="#f0f0ff",
                         foreground="black",
                         rowheight=32,
                         fieldbackground="#f0f0ff",
                         font=('Segoe UI', 10),
                         bordercolor="#ccc",
                         borderwidth=1)

        # Color al seleccionar
        estilo.map("Treeview",
                   background=[("selected", "#6C63FF")],
                   foreground=[("selected", "white")])

        # Estilo de encabezados
        estilo.configure("Treeview.Heading",
                         background="#413F96",
                         foreground="white",
                         font=('Segoe UI', 10, 'bold'),
                         padding=(8, 10),
                         borderwidth=1)

        # Scrollbar vertical estilo
        estilo.configure("Vertical.TScrollbar",
                         gripcount=0,
                         background="#cccccc",
                         darkcolor="#aaaaaa",
                         lightcolor="#eeeeee",
                         troughcolor="#f5f5f5",
                         bordercolor="#d9d9d9",
                         arrowcolor="#413F96")

        # Crear la tabla dentro del contenedor
        self.tabla = ttk.Treeview(contenedor, columns=columnas, show='headings', cursor="hand2")

        # Configurar columnas y encabezados con comando para ordenar
        for posicion in range(len(columnas)):
            col = columnas[posicion]
            self.tabla.heading(col, text=titulos[posicion], command=lambda _col=col: self.ordenar_columna(_col, False))
            self.tabla.column(col, anchor='center', width=120, minwidth=50, stretch=True)

        # Zebra stripes
        self.tabla.tag_configure('oddrow', background='#e0e5ff')
        self.tabla.tag_configure('evenrow', background='#ffffff')

        # Insertar datos
        self.insertar_datos(data)

        # Scrollbar vertical
        scrollbar = ttk.Scrollbar(contenedor, orient="vertical", command=self.tabla.yview, style="Vertical.TScrollbar")
        self.tabla.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side='right', fill='y')

        self.tabla.pack(expand=True, fill='both')

    def insertar_datos(self, data):
        self.tabla.delete(*self.tabla.get_children())
        for i, elemento in enumerate(data):
            tag = 'evenrow' if i % 2 == 0 else 'oddrow'
            self.tabla.insert('', 'end', values=elemento, tags=(tag,))

    def refrescar(self, data):
        self.insertar_datos(data)

    def ordenar_columna(self, col, reverse):
        datos = [(self.tabla.set(k, col), k) for k in self.tabla.get_children('')]
        try:
            datos.sort(key=lambda t: float(t[0]), reverse=reverse)
        except ValueError:
            datos.sort(key=lambda t: t[0].lower(), reverse=reverse)

        for index, (val, k) in enumerate(datos):
            self.tabla.move(k, '', index)

        for i, k in enumerate(self.tabla.get_children('')):
            tag = 'evenrow' if i % 2 == 0 else 'oddrow'
            self.tabla.item(k, tags=(tag,))

        self.tabla.heading(col, command=lambda: self.ordenar_columna(col, not reverse))
