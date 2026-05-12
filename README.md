# 🎬 Sistema de Gestión de Cine — MongoDB + Python

Sistema de gestión de una cartelera de cine desarrollado en Python con PyMongo, que permite administrar películas, funciones y detalles desde una interfaz de consola.

---

## 📋 Descripción del caso de estudio

El sistema gestiona una colección de **películas** (`peliculas`) dentro de una base de datos MongoDB llamada `cine_db`. Cada documento representa una película en cartelera e incluye:

- **Subdocumento** (`detalles`): director e idioma de la película.
- **Array de subdocumentos** (`funciones`): lista de funciones con fecha, hora, sala y precio.
- **Campo de fecha** (`fecha_estreno`): fecha oficial de estreno de la película.

La base de datos se precarga automáticamente con **12 películas** al ejecutar el sistema por primera vez.

---

## 🗂️ Estructura del documento

```json
{
  "titulo": "Oppenheimer",
  "genero": "Drama",
  "duracion_min": 180,
  "clasificacion": "R",
  "detalles": {
    "director": "Christopher Nolan",
    "idioma": "Inglés"
  },
  "funciones": [
    {
      "fecha": "2026-05-06",
      "hora": "19:30",
      "sala": 2,
      "precio": 6000
    }
  ],
  "fecha_estreno": "2023-07-21"
}
```

---

## ⚙️ Requisitos previos

- Python 3.8 o superior
- MongoDB instalado y corriendo en `localhost:27017`
- pip

---

## 🚀 Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/<tu-usuario>/<nombre-del-repo>.git
cd <nombre-del-repo>
```

### 2. Instalar dependencias

```bash
pip install pymongo python-dotenv
```

### 3. Configurar variables de entorno

Crear un archivo `.env` en la raíz del proyecto con el siguiente contenido:

```
MONGO_URI=mongodb://localhost:27017
```

### 4. Asegurarse de que MongoDB esté corriendo

```bash
# En Windows (si MongoDB está instalado como servicio)
net start MongoDB

# En Linux/macOS
sudo systemctl start mongod
```

### 5. Ejecutar el sistema

```bash
python main.py
```

Al iniciar por primera vez, el sistema cargará automáticamente los datos de prueba si la colección está vacía.

---

## 📌 Funcionalidades del menú

| Opción | Descripción | Operación MongoDB |
|--------|-------------|-------------------|
| 1 | Listar todas las películas | `find()` |
| 2 | Agregar nueva película | `insert_one()` |
| 3 | Buscar por precio máximo de función | `$lte` sobre array de subdocumentos |
| 4 | Buscar por título | `$regex` (case-insensitive) |
| 5 | Buscar por rango de fecha de estreno | `$gte` + `$lte` sobre campo fecha |
| 6 | Buscar por idioma | Consulta sobre subdocumento `detalles.idioma` |
| 7 | Actualizar clasificación | `$set` en campo raíz |
| 8 | Actualizar director | `$set` en subdocumento `detalles.director` |
| 9 | Eliminar película | `delete_one()` con confirmación previa |
| 0 | Salir | — |

---

## 🗄️ Base de datos y colección

- **Base de datos:** `cine_db`
- **Colección:** `peliculas`
- **Conexión:** `mongodb://localhost:27017` (configurable vía `.env`)

---

## 📁 Estructura del proyecto

```
📦 cine-mongodb/
 ┣ 📄 main.py        # Código principal del sistema
 ┣ 📄 .env           # Variables de entorno (no subir al repo)
 ┣ 📄 .env.example   # Ejemplo de configuración
 ┣ 📄 requirements.txt
 ┗ 📄 README.md
```

---

## 📦 requirements.txt

```
pymongo
python-dotenv
```

Para generar el archivo:

```bash
pip freeze > requirements.txt
```

---

## 👥 Integrantes del grupo

| Nombre | Rol |
|--------|-----|
| — | Desarrollo |
| — | Desarrollo |

---

## 📝 Notas

- Si la colección ya contiene datos, la carga inicial **no se ejecuta** para evitar duplicados.
- El sistema valida que la película exista antes de actualizar o eliminar.
- La eliminación solicita confirmación del usuario antes de proceder.