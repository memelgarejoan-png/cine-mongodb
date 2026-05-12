from pymongo import MongoClient
from datetime import datetime
from dotenv import load_dotenv
import os

# -- Conexion ------------------------------------------------------------------
load_dotenv()
client = MongoClient(os.getenv("MONGO_URI"))
db = client["cine_db"]
col = db["peliculas"]

# -- Datos iniciales -----------------------------------------------------------
peliculas = [
    {
        "titulo": "Avengers: Endgame",
        "genero": "Accion",
        "duracion_min": 181,
        "clasificacion": "PG-13",
        "detalles": {"director": "Anthony Russo", "idioma": "Ingles"},
        "funciones": [{"fecha": datetime(2026, 5, 1), "hora": "18:00", "sala": 1, "precio": 5000}],
        "fecha_estreno": datetime(2019, 4, 26)
    },
    {
        "titulo": "Avatar 3",
        "genero": "Ciencia ficcion",
        "duracion_min": 190,
        "clasificacion": "PG-13",
        "detalles": {"director": "James Cameron", "idioma": "Ingles"},
        "funciones": [
            {"fecha": datetime(2026, 5, 1), "hora": "18:00", "sala": 1, "precio": 7000},
            {"fecha": datetime(2026, 5, 2), "hora": "21:00", "sala": 2, "precio": 7500}
        ],
        "fecha_estreno": datetime(2025, 12, 20)
    },
    {
        "titulo": "El Mono",
        "genero": "Terror",
        "duracion_min": 100,
        "clasificacion": "R",
        "detalles": {"director": "Desconocido", "idioma": "Espanol"},
        "funciones": [{"fecha": datetime(2026, 5, 3), "hora": "22:00", "sala": 3, "precio": 5000}],
        "fecha_estreno": datetime(2024, 10, 10)
    },
    {
        "titulo": "Zootopia 2",
        "genero": "Animacion",
        "duracion_min": 110,
        "clasificacion": "PG",
        "detalles": {"director": "Disney", "idioma": "Espanol"},
        "funciones": [{"fecha": datetime(2026, 5, 4), "hora": "16:00", "sala": 2, "precio": 4500}],
        "fecha_estreno": datetime(2025, 11, 26)
    },
    {
        "titulo": "Dune: Parte 2",
        "genero": "Ciencia ficcion",
        "duracion_min": 166,
        "clasificacion": "PG-13",
        "detalles": {"director": "Denis Villeneuve", "idioma": "Ingles"},
        "funciones": [{"fecha": datetime(2026, 5, 5), "hora": "20:00", "sala": 1, "precio": 6500}],
        "fecha_estreno": datetime(2024, 3, 1)
    },
    {
        "titulo": "Oppenheimer",
        "genero": "Drama",
        "duracion_min": 180,
        "clasificacion": "R",
        "detalles": {"director": "Christopher Nolan", "idioma": "Ingles"},
        "funciones": [{"fecha": datetime(2026, 5, 6), "hora": "19:30", "sala": 2, "precio": 6000}],
        "fecha_estreno": datetime(2023, 7, 21)
    },
    {
        "titulo": "Barbie",
        "genero": "Comedia",
        "duracion_min": 114,
        "clasificacion": "PG-13",
        "detalles": {"director": "Greta Gerwig", "idioma": "Espanol"},
        "funciones": [{"fecha": datetime(2026, 5, 7), "hora": "18:30", "sala": 3, "precio": 5000}],
        "fecha_estreno": datetime(2023, 7, 21)
    },
    {
        "titulo": "Deadpool 3",
        "genero": "Accion",
        "duracion_min": 130,
        "clasificacion": "R",
        "detalles": {"director": "Shawn Levy", "idioma": "Ingles"},
        "funciones": [{"fecha": datetime(2026, 5, 8), "hora": "22:30", "sala": 1, "precio": 7000}],
        "fecha_estreno": datetime(2024, 7, 26)
    },
    {
        "titulo": "Inside Out 2",
        "genero": "Animacion",
        "duracion_min": 105,
        "clasificacion": "PG",
        "detalles": {"director": "Kelsey Mann", "idioma": "Espanol"},
        "funciones": [{"fecha": datetime(2026, 5, 9), "hora": "17:00", "sala": 2, "precio": 4500}],
        "fecha_estreno": datetime(2024, 6, 14)
    },
    {
        "titulo": "Dragon Ball Z: La Batalla de los Dioses",
        "genero": ["Anime", "Animacion", "Accion"],
        "duracion_min": 105,
        "clasificacion": "PG",
        "detalles": {"director": "Masahiro Hosoda", "idioma": "Japones"},
        "funciones": [{"fecha": datetime(2015, 5, 10), "hora": "16:00", "sala": 5, "precio": 5500}],
        "fecha_estreno": datetime(2013, 10, 3)
    },
    {
        "titulo": "Kung Fu Panda",
        "genero": ["Animacion", "Cine familiar", "Accion"],
        "duracion_min": 94,
        "clasificacion": "PG",
        "detalles": {"director": "Mike Mitchell", "idioma": "Espanol"},
        "funciones": [{"fecha": datetime(2020, 7, 12), "hora": "16:00", "sala": 3, "precio": 4500}],
        "fecha_estreno": datetime(2008, 7, 10)
    },
    {
        "titulo": "Demon Slayer: Kimetsu no Yaiba - Castillo Infinito",
        "genero": ["Anime", "Animacion", "Accion"],
        "duracion_min": 155,
        "clasificacion": "B15",
        "detalles": {"director": "Haruo Sotozaki", "idioma": "Japones"},
        "funciones": [{"fecha": datetime(2026, 3, 25), "hora": "15:00", "sala": 4, "precio": 6500}],
        "fecha_estreno": datetime(2025, 7, 11)
    }
]

# -- Insertar solo si la coleccion esta vacia ---------------------------------
if col.count_documents({}) == 0:
    col.insert_many(peliculas)
    print(f"Se insertaron {len(peliculas)} peliculas correctamente.")
else:
    print("La coleccion ya tiene datos. No se inserto nada.")

client.close()