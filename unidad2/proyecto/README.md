# 📚 Gestión Editorial Andina S.A.S.

Una aplicación de escritorio para la gestión de autores y libros, desarrollada con **Django** como backend y **Tkinter** como frontend. Incluye funcionalidades CRUD, búsqueda y respaldos automáticos en archivos de texto plano.

---

## 🧰 Tecnologías utilizadas

- Python 3.x
- Django
- Django REST Framework
- Tkinter
- Requests
- Threading (para respaldos automáticos)

---

## 🚀 Características principales

### ✅ Backend con Django
- Modelos: `Autor` y `Libro`.
- Endpoints REST (`/api/autores/` y `/api/libros/`) para:
  - Crear, consultar, actualizar, eliminar.
  - Filtrar por atributos y buscar por nombre/título.

### ✅ Frontend con Tkinter
- Interfaz dividida en dos secciones: Autores (izquierda) y Libros (derecha).
- Botones por sección:
  - Crear
  - Consultar todos
  - Consultar por ID
  - Actualizar
  - Borrar
  - Limpiar campos
- Estilo visual con color de fondo azul claro (`#e6f0ff`).
- Visualización de resultados en widgets `Text`.

### ✅ Respaldo automático
- Cada 60 segundos se generan:
  - `backup_autores.txt`
  - `backup_libros.txt`
- Incluyen todos los registros actuales.

---

## 📂 Estructura del proyecto

proyecto/
│
├── backend/ # Proyecto Django con modelos, views y API
│
├── frontend/
│ └── app.py # Interfaz gráfica con Tkinter
│
├── backup_autores.txt # Respaldo automático de autores
├── backup_libros.txt # Respaldo automático de libros
├── requirements.txt # Dependencias del proyecto
└── README.md # Este archivo

---

## ⚙ Instalación

1. Clona este repositorio o copia el proyecto.
2. Crea un entorno virtual:

```bash
python -m venv env
env\Scripts\activate  # En Windows

urls
127.0.0.1:8000/api/autores/
127.0.0.1:8000/api/libros/