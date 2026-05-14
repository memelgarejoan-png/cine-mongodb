# Sistema de Gestion de Cine — MongoDB + Python

Sistema de gestion de una cartelera de cine desarrollado en Python con PyMongo, que permite administrar peliculas, funciones y detalles desde una interfaz de consola.

---

## Descripcion del caso de estudio

El sistema gestiona una coleccion de peliculas dentro de una base de datos MongoDB llamada `cine_db`. Cada documento representa una pelicula en cartelera e incluye:

- **Subdocumento** (`detalles`): director e idioma de la pelicula.
- **Array de subdocumentos** (`funciones`): lista de funciones con fecha, hora, sala y precio.
- **Campo de fecha** (`fecha_estreno`): fecha oficial de estreno de la pelicula.

La base de datos se precarga con **12 peliculas** ejecutando `carga_datos.py` antes de iniciar el sistema.

---

## Estructura del documento

```json
{
  "titulo": "Oppenheimer",
  "genero": "Drama",
  "duracion_min": 180,
  "clasificacion": "R",
  "detalles": {
    "director": "Christopher Nolan",
    "idioma": "Ingles"
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

## Requisitos previos

- Python 3.8 o superior
- MongoDB 7 instalado y corriendo en `localhost:27017`
- pip

---

## Instalacion y ejecucion

### 1. Clonar el repositorio

```bash
git clone https://github.com/memelgarejoan-png/cine-mongodb.git
cd cine-mongodb
```

### 2. Instalar dependencias

```bash
pip install pymongo python-dotenv
```

### 3. Configurar variables de entorno

Crear un archivo `.env` en la raiz del proyecto con el siguiente contenido:

```
MONGO_URI=mongodb://localhost:27017
```

### 4. Asegurarse de que MongoDB este corriendo

```bash
# En Windows
net start MongoDB

# En Linux/macOS
sudo systemctl start mongod
```

### 5. Cargar los datos iniciales

```bash
python carga_datos.py
```

### 6. Ejecutar el sistema

```bash
python main.py
```

---

## Funcionalidades del menu

| Opcion | Descripcion | Operacion MongoDB |
|--------|-------------|-------------------|
| 1 | Listar todas las peliculas | `find()` |
| 2 | Agregar nueva pelicula | `insert_one()` |
| 3 | Buscar por precio maximo de funcion | `$lte` sobre array de subdocumentos |
| 4 | Buscar por titulo | `$regex` (case-insensitive) |
| 5 | Buscar por rango de fecha de estreno | `$gte` + `$lte` sobre campo fecha |
| 6 | Buscar por idioma | Consulta sobre subdocumento `detalles.idioma` |
| 7 | Actualizar clasificacion | `$set` en campo raiz |
| 8 | Actualizar director | `$set` en subdocumento `detalles.director` |
| 9 | Eliminar pelicula | `delete_one()` con confirmacion previa |
| 0 | Salir | — |

---

## Base de datos y coleccion

- **Base de datos:** `cine_db`
- **Coleccion:** `peliculas`
- **Conexion:** `mongodb://localhost:27017`

---

## Estructura del proyecto

```
cine-mongodb/
 |- carga_datos.py       # Inserta los 12 documentos iniciales
 |- main.py              # Menu principal y funciones CRUD
 |- .gitignore
 |- README.md
```

---

## Integrantes del grupo

| Nombre | Rol |
|--------|-----|git status
| Mayra Melgarejo| Desarrollo |
| Javier Venegas| Desarrollo |

---

## Notas

- Ejecutar `carga_datos.py` primero antes de usar el sistema.
- Si la coleccion ya tiene datos, `carga_datos.py` no inserta nada para evitar duplicados.
- El sistema valida que la pelicula exista antes de actualizar o eliminar.
- La eliminacion solicita confirmacion del usuario antes de proceder.
- El archivo `.env` no se sube a GitHub por seguridad.
- Se cambia  la conección  de atlas  a forma local
