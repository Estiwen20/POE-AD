# 📚 Gestión Editorial Andina S.A.S.

Una aplicación de escritorio para la gestión de autores y libros, desarrollada con **Django** como backend y **Tkinter** como frontend. Incluye funcionalidades CRUD, búsqueda por ID y respaldos automáticos en archivos de texto plano.

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
  - Consultar por ID.

### ✅ Frontend con Tkinter
- Interfaz dividida en dos pestañas: Autores y Libros.
- Botones por sección:
  - Crear
  - Consultar todos
  - Consultar por ID
  - Actualizar
  - Borrar
  - Limpiar 
- Estilo visual con color de fondo azul (`#e6f0ff`).
- Visualización de resultados en widgets `Text`.

### ✅ Respaldo automático
- Segun el tiempo asiganado se generan automáticamente:
  - `respaldo_autores.txt`
  - `respaldo_libros.txt`
- Incluyen todos los registros actuales del sistema.
- Se sobrescriben en cada ciclo.
- Se ejecutan en un hilo separado para no congelar la interfaz.

---

## 📂 Estructura del proyecto

proyecto/
│
├── backend/ # Proyecto Django con las api
│ ├── manage.py
│ └── ...
│
├── frontend/contiene modelos, controladores y vistas
│ └── app.py # Interfaz gráfica con Tkinter
│
├── respaldo_autores.txt # Archivo de respaldo generado automáticamente
├── respaldo_libros.txt # Archivo de respaldo generado automáticamente
├── requirements.txt # Dependencias del proyecto
└── README.md # Este archivo


---

## ⚙ Instalación y ejecución

1. Clona este repositorio o copia el proyecto.
2. Crea y activa un entorno virtual:

  ```bash
  python -m venv env
  
  # En Windows
  env\Scripts\activate
  
  # En macOS/Linux
  source env/bin/activate

## ⚙ Instala las dependencias necesarias:

  pip install -r requirements.txt

  Ejecuta el backend (desde la carpeta backend):

  cd backend
  python manage.py runserver

## ⚙ En una terminal nueva, ejecuta la interfaz gráfica (desde la carpeta frontend):

  cd ../frontend
  python main.py


## 🌐 Endpoints disponibles (API)
  http://127.0.0.1:8000/api/autores/

  http://127.0.0.1:8000/api/libros/

## 📝 Notas
  El sistema de respaldo se activa automáticamente al iniciar la interfaz Tkinter.

  Se ejecuta segun los segundos asignados en segundo plano, en este caso como demostracion se generan cada 10 segundos.

  Los respaldos se sobrescriben cada vez y están en formato legible por humanos.

## 🧑‍💻 Autor
  Desarrollado por estudiantes de Univalle para Editorial Andina S.A.S.

  David Estiwen Lozano Laverde
  Yeferson Quiroga Areiza
  Angie Katherine Jimenez Echeverry