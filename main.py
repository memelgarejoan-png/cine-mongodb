
from pymongo import MongoClient
from datetime import datetime
from dotenv import load_dotenv
import os
 
# ── Conexión ──────────────────────────────────────────────────────────────────
load_dotenv()
client = MongoClient(os.getenv("MONGO_URI"))
db = client["cine_db"]
col = db["peliculas"]
 
 
# ── Carga de datos iniciales ──────────────────────────────────────────────────
def cargar_datos_iniciales():
    if col.count_documents({}) == 0:
        col.insert_many([
            {
                "titulo": "Avengers: Endgame",
                "genero": "Acción",
                "duracion_min": 181,
                "clasificacion": "PG-13",
                "detalles": {"director": "Anthony Russo", "idioma": "Inglés"},
                "funciones": [{"fecha": datetime(2026, 5, 1), "hora": "18:00", "sala": 1, "precio": 5000}],
                "fecha_estreno": datetime(2019, 4, 26)
            },
            {
                "titulo": "Avatar 3",
                "genero": "Ciencia ficción",
                "duracion_min": 190,
                "clasificacion": "PG-13",
                "detalles": {"director": "James Cameron", "idioma": "Inglés"},
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
                "detalles": {"director": "Desconocido", "idioma": "Español"},
                "funciones": [{"fecha": datetime(2026, 5, 3), "hora": "22:00", "sala": 3, "precio": 5000}],
                "fecha_estreno": datetime(2024, 10, 10)
            },
            {
                "titulo": "Zootopia 2",
                "genero": "Animación",
                "duracion_min": 110,
                "clasificacion": "PG",
                "detalles": {"director": "Disney", "idioma": "Español"},
                "funciones": [{"fecha": datetime(2026, 5, 4), "hora": "16:00", "sala": 2, "precio": 4500}],
                "fecha_estreno": datetime(2025, 11, 26)
            },
            {
                "titulo": "Dune: Parte 2",
                "genero": "Ciencia ficción",
                "duracion_min": 166,
                "clasificacion": "PG-13",
                "detalles": {"director": "Denis Villeneuve", "idioma": "Inglés"},
                "funciones": [{"fecha": datetime(2026, 5, 5), "hora": "20:00", "sala": 1, "precio": 6500}],
                "fecha_estreno": datetime(2024, 3, 1)
            },
            {
                "titulo": "Oppenheimer",
                "genero": "Drama",
                "duracion_min": 180,
                "clasificacion": "R",
                "detalles": {"director": "Christopher Nolan", "idioma": "Inglés"},
                "funciones": [{"fecha": datetime(2026, 5, 6), "hora": "19:30", "sala": 2, "precio": 6000}],
                "fecha_estreno": datetime(2023, 7, 21)
            },
            {
                "titulo": "Barbie",
                "genero": "Comedia",
                "duracion_min": 114,
                "clasificacion": "PG-13",
                "detalles": {"director": "Greta Gerwig", "idioma": "Español"},
                "funciones": [{"fecha": datetime(2026, 5, 7), "hora": "18:30", "sala": 3, "precio": 5000}],
                "fecha_estreno": datetime(2023, 7, 21)
            },
            {
                "titulo": "Deadpool 3",
                "genero": "Acción",
                "duracion_min": 130,
                "clasificacion": "R",
                "detalles": {"director": "Shawn Levy", "idioma": "Inglés"},
                "funciones": [{"fecha": datetime(2026, 5, 8), "hora": "22:30", "sala": 1, "precio": 7000}],
                "fecha_estreno": datetime(2024, 7, 26)
            },
            {
                "titulo": "Inside Out 2",
                "genero": "Animación",
                "duracion_min": 105,
                "clasificacion": "PG",
                "detalles": {"director": "Kelsey Mann", "idioma": "Español"},
                "funciones": [{"fecha": datetime(2026, 5, 9), "hora": "17:00", "sala": 2, "precio": 4500}],
                "fecha_estreno": datetime(2024, 6, 14)
            },
            {
                "titulo": "Dragon Ball Z: La Batalla de los Dioses",
                "genero": ["Anime", "Animación", "Acción"],
                "duracion_min": 105,
                "clasificacion": "PG",
                "detalles": {"director": "Masahiro Hosoda", "idioma": "Japonés"},
                "funciones": [{"fecha": datetime(2015, 5, 10), "hora": "16:00", "sala": 5, "precio": 5500}],
                "fecha_estreno": datetime(2013, 10, 3)
            },
            {
                "titulo": "Kung Fu Panda",
                "genero": ["Animación", "Cine familiar", "Acción"],
                "duracion_min": 94,
                "clasificacion": "PG",
                "detalles": {"director": "Mike Mitchell", "idioma": "Español"},
                "funciones": [{"fecha": datetime(2020, 7, 12), "hora": "16:00", "sala": 3, "precio": 4500}],
                "fecha_estreno": datetime(2008, 7, 10)
            },
            {
                "titulo": "Demon Slayer: Kimetsu no Yaiba - Castillo Infinito",
                "genero": ["Anime", "Animación", "Acción"],
                "duracion_min": 155,
                "clasificacion": "B15",
                "detalles": {"director": "Haruo Sotozaki", "idioma": "Japonés"},
                "funciones": [{"fecha": datetime(2026, 3, 25), "hora": "15:00", "sala": 4, "precio": 6500}],
                "fecha_estreno": datetime(2025, 7, 11)
            }
        ])
        print("✅ Datos iniciales cargados.")
 
 
# ── Helpers ───────────────────────────────────────────────────────────────────
def separador():
    print("\n" + "=" * 50)
 
def mostrar_pelicula(p):
    print(f"\n🎬 Título     : {p.get('titulo')}")
    print(f"   Género     : {p.get('genero')}")
    print(f"   Duración   : {p.get('duracion_min')} min")
    print(f"   Clasificac.: {p.get('clasificacion')}")
    det = p.get("detalles", {})
    print(f"   Director   : {det.get('director')}")
    print(f"   Idioma     : {det.get('idioma')}")
    print(f"   Estreno    : {p.get('fecha_estreno').strftime('%Y-%m-%d') if p.get('fecha_estreno') else 'N/A'}")
    for i, f in enumerate(p.get("funciones", []), 1):
        fecha_f = f.get("fecha").strftime("%Y-%m-%d") if f.get("fecha") else "N/A"
        print(f"   Función {i}  : {fecha_f} {f.get('hora')} | Sala {f.get('sala')} | ${f.get('precio')}")
 
 
# ── 1. LISTAR TODAS ───────────────────────────────────────────────────────────
def listar_peliculas():
    separador()
    print("📋 TODAS LAS PELÍCULAS")
    separador()
    peliculas = list(col.find())
    if not peliculas:
        print("No hay películas en la base de datos.")
        return
    for p in peliculas:
        mostrar_pelicula(p)
    print(f"\nTotal: {len(peliculas)} películas.")
 
 
# ── 2. CREAR DOCUMENTO ────────────────────────────────────────────────────────
def crear_pelicula():
    separador()
    print("➕ AGREGAR NUEVA PELÍCULA")
    separador()
    titulo = input("Título: ").strip()
    genero = input("Género: ").strip()
    duracion = int(input("Duración (minutos): "))
    clasificacion = input("Clasificación (PG / PG-13 / R): ").strip()
    director = input("Director: ").strip()
    idioma = input("Idioma: ").strip()
    estreno_str = input("Fecha de estreno (YYYY-MM-DD): ").strip()
    fecha_estreno = datetime.strptime(estreno_str, "%Y-%m-%d")
    print("\n--- Agregar función ---")
    fecha_f_str = input("Fecha de función (YYYY-MM-DD): ").strip()
    fecha_funcion = datetime.strptime(fecha_f_str, "%Y-%m-%d")
    hora = input("Hora (HH:MM): ").strip()
    sala = int(input("Sala: "))
    precio = int(input("Precio: "))
    nueva = {
        "titulo": titulo,
        "genero": genero,
        "duracion_min": duracion,
        "clasificacion": clasificacion,
        "detalles": {"director": director, "idioma": idioma},
        "funciones": [{"fecha": fecha_funcion, "hora": hora, "sala": sala, "precio": precio}],
        "fecha_estreno": fecha_estreno
    }
    resultado = col.insert_one(nueva)
    print(f"\n✅ Película insertada con ID: {resultado.inserted_id}")
 
 
# ── 3. BUSCAR POR PRECIO ──────────────────────────────────────────────────────
def buscar_por_precio():
    separador()
    print("🔍 BUSCAR POR PRECIO MÁXIMO DE FUNCIÓN")
    separador()
    precio_max = int(input("Ingresa el precio máximo: $"))
    peliculas = list(col.find({"funciones.precio": {"$lte": precio_max}}))
    if not peliculas:
        print("No se encontraron películas con ese precio.")
        return
    for p in peliculas:
        mostrar_pelicula(p)
    print(f"\nTotal encontradas: {len(peliculas)}")
 
 
# ── 4. BUSCAR POR REGEX ───────────────────────────────────────────────────────
def buscar_por_titulo():
    separador()
    print("🔍 BUSCAR POR TÍTULO (expresión regular)")
    separador()
    texto = input("Ingresa parte del título a buscar: ").strip()
    peliculas = list(col.find({"titulo": {"$regex": texto, "$options": "i"}}))
    if not peliculas:
        print("No se encontraron películas con ese título.")
        return
    for p in peliculas:
        mostrar_pelicula(p)
    print(f"\nTotal encontradas: {len(peliculas)}")
 
 
# ── 5. BUSCAR POR RANGO DE FECHAS ─────────────────────────────────────────────
def buscar_por_fechas():
    separador()
    print("🔍 BUSCAR POR RANGO DE FECHA DE ESTRENO")
    separador()
    desde = datetime.strptime(input("Fecha desde (YYYY-MM-DD): ").strip(), "%Y-%m-%d")
    hasta = datetime.strptime(input("Fecha hasta (YYYY-MM-DD): ").strip(), "%Y-%m-%d")
    peliculas = list(col.find({"fecha_estreno": {"$gte": desde, "$lte": hasta}}))
    if not peliculas:
        print("No se encontraron películas en ese rango de fechas.")
        return
    for p in peliculas:
        mostrar_pelicula(p)
    print(f"\nTotal encontradas: {len(peliculas)}")
 
 
# ── 6. BUSCAR EN SUBDOCUMENTO ─────────────────────────────────────────────────
def buscar_por_idioma():
    separador()
    print("🔍 BUSCAR POR IDIOMA (campo dentro de subdocumento)")
    separador()
    idioma = input("Idioma (Español / Inglés / Japonés): ").strip()
    peliculas = list(col.find({"detalles.idioma": idioma}))
    if not peliculas:
        print("No se encontraron películas en ese idioma.")
        return
    for p in peliculas:
        mostrar_pelicula(p)
    print(f"\nTotal encontradas: {len(peliculas)}")
 
 
# ── 7. ACTUALIZAR CAMPO RAÍZ ──────────────────────────────────────────────────
def actualizar_clasificacion():
    separador()
    print("✏️  ACTUALIZAR CLASIFICACIÓN DE PELÍCULA")
    separador()
    titulo = input("Título de la película: ").strip()
    pelicula = col.find_one({"titulo": {"$regex": titulo, "$options": "i"}})
    if not pelicula:
        print("❌ Película no encontrada.")
        return
    print("\nAntes:")
    mostrar_pelicula(pelicula)
    nueva_clasificacion = input("\nNueva clasificación: ").strip()
    col.update_one({"_id": pelicula["_id"]}, {"$set": {"clasificacion": nueva_clasificacion}})
    print("\n✅ Clasificación actualizada. Después:")
    mostrar_pelicula(col.find_one({"_id": pelicula["_id"]}))
 
 
# ── 8. ACTUALIZAR CAMPO EN SUBDOCUMENTO ───────────────────────────────────────
def actualizar_director():
    separador()
    print("✏️  ACTUALIZAR DIRECTOR (dentro de subdocumento)")
    separador()
    titulo = input("Título de la película: ").strip()
    pelicula = col.find_one({"titulo": {"$regex": titulo, "$options": "i"}})
    if not pelicula:
        print("❌ Película no encontrada.")
        return
    print("\nAntes:")
    mostrar_pelicula(pelicula)
    nuevo_director = input("\nNuevo director: ").strip()
    col.update_one({"_id": pelicula["_id"]}, {"$set": {"detalles.director": nuevo_director}})
    print("\n✅ Director actualizado. Después:")
    mostrar_pelicula(col.find_one({"_id": pelicula["_id"]}))
 
 
# ── 9. ELIMINAR PELÍCULA ──────────────────────────────────────────────────────
def eliminar_pelicula():
    separador()
    print("🗑️  ELIMINAR PELÍCULA")
    separador()
    titulo = input("Título de la película a eliminar: ").strip()
    pelicula = col.find_one({"titulo": {"$regex": titulo, "$options": "i"}})
    if not pelicula:
        print("❌ Película no encontrada.")
        return
    print("\nPelícula a eliminar:")
    mostrar_pelicula(pelicula)
    confirmacion = input("\n¿Confirmas la eliminación? (s/n): ").strip().lower()
    if confirmacion == "s":
        col.delete_one({"_id": pelicula["_id"]})
        print("✅ Película eliminada correctamente.")
    else:
        print("Operación cancelada.")
 
 
# ── MENÚ PRINCIPAL ────────────────────────────────────────────────────────────
def menu():
    while True:
        separador()
        print("🎥  SISTEMA DE GESTIÓN DE CINE")
        separador()
        print("  1. Listar todas las películas")
        print("  2. Agregar nueva película")
        print("  3. Buscar por precio máximo")
        print("  4. Buscar por título")
        print("  5. Buscar por rango de fecha de estreno")
        print("  6. Buscar por idioma (subdocumento)")
        print("  7. Actualizar clasificación")
        print("  8. Actualizar director")
        print("  9. Eliminar película")
        print("  0. Salir")
        separador()
        opcion = input("Selecciona una opción: ").strip()
 
        if opcion == "1":
            listar_peliculas()
        elif opcion == "2":
            crear_pelicula()
        elif opcion == "3":
            buscar_por_precio()
        elif opcion == "4":
            buscar_por_titulo()
        elif opcion == "5":
            buscar_por_fechas()
        elif opcion == "6":
            buscar_por_idioma()
        elif opcion == "7":
            actualizar_clasificacion()
        elif opcion == "8":
            actualizar_director()
        elif opcion == "9":
            eliminar_pelicula()
        elif opcion == "0":
            print("\n👋 Hasta luego.")
            break
        else:
            print("❌ Opción inválida. Intenta de nuevo.")
 
        input("\nPresiona Enter para continuar...")
 
 
if __name__ == "__main__":
    cargar_datos_iniciales()
    menu()