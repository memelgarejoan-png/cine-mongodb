from pymongo import MongoClient
from datetime import datetime
from dotenv import load_dotenv
from datos import peliculas_iniciales
import os

# -- Conexion ------------------------------------------------------------------
load_dotenv()
client = MongoClient(os.getenv("MONGO_URI"))
db = client["cine_db"]
col = db["peliculas"]


# -- Carga de datos iniciales --------------------------------------------------
def cargar_datos_iniciales():
    if col.count_documents({}) == 0:
        col.insert_many(peliculas_iniciales)
        print("Datos iniciales cargados correctamente.")
    else:
        print(f"Base de datos lista. ({col.count_documents({})} peliculas encontradas)")


# -- Helpers -------------------------------------------------------------------
def separador(titulo=""):
    if titulo:
        print("\n" + "=" * 50)
        print(f"   {titulo.upper()}")
        print("=" * 50)
    else:
        print("=" * 50)


def mostrar_pelicula(p):
    genero = p.get("genero")
    if isinstance(genero, list):
        genero = ", ".join(genero)
    print(f"\n  Titulo      : {p.get('titulo')}")
    print(f"  Genero      : {genero}")
    print(f"  Duracion    : {p.get('duracion_min')} min")
    print(f"  Clasificac. : {p.get('clasificacion')}")
    det = p.get("detalles", {})
    print(f"  Director    : {det.get('director')}")
    print(f"  Idioma      : {det.get('idioma')}")
    print(f"  Estreno     : {p.get('fecha_estreno').strftime('%Y-%m-%d') if p.get('fecha_estreno') else 'N/A'}")
    for i, f in enumerate(p.get("funciones", []), 1):
        fecha_f = f.get("fecha").strftime("%Y-%m-%d") if f.get("fecha") else "N/A"
        print(f"  Funcion {i}   : {fecha_f} {f.get('hora')} | Sala {f.get('sala')} | ${f.get('precio'):,}")


def confirmar_accion(mensaje="  Confirmas la accion? (s/n): "):
    return input(mensaje).strip().lower() == "s"


# -- 1. LISTAR TODAS -----------------------------------------------------------
def listar_peliculas():
    separador("Todas las peliculas")
    peliculas = list(col.find())
    if not peliculas:
        print("\n  No hay peliculas en la base de datos.")
        return
    for p in peliculas:
        separador()
        mostrar_pelicula(p)
    print(f"\n  Total: {len(peliculas)} peliculas.")


# -- 2. CREAR DOCUMENTO --------------------------------------------------------
def crear_pelicula():
    separador("Agregar nueva pelicula")
    titulo = input("  Titulo: ").strip()

    # Verificar si ya existe
    if col.find_one({"titulo": {"$regex": f"^{titulo}$", "$options": "i"}}):
        print(f"\n  Ya existe una pelicula con el titulo '{titulo}'.")
        return

    genero = input("  Genero: ").strip()
    duracion = int(input("  Duracion (minutos): "))
    clasificacion = input("  Clasificacion (PG / PG-13 / R): ").strip()
    director = input("  Director: ").strip()
    idioma = input("  Idioma: ").strip()
    estreno_str = input("  Fecha de estreno (YYYY-MM-DD): ").strip()
    fecha_estreno = datetime.strptime(estreno_str, "%Y-%m-%d")
    print("\n  --- Agregar funcion ---")
    fecha_f_str = input("  Fecha de funcion (YYYY-MM-DD): ").strip()
    fecha_funcion = datetime.strptime(fecha_f_str, "%Y-%m-%d")
    hora = input("  Hora (HH:MM): ").strip()
    sala = int(input("  Sala: "))
    precio = int(input("  Precio: $"))
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
    print(f"\n  Pelicula '{titulo}' insertada correctamente. ID: {resultado.inserted_id}")


# -- 3. BUSCAR POR PRECIO ------------------------------------------------------
def buscar_por_precio():
    separador("Buscar por precio maximo")
    try:
        precio_max = int(input("  Ingresa el precio maximo: $"))
    except ValueError:
        print("\n  Error: ingresa un numero valido.")
        return
    peliculas = list(col.find({"funciones.precio": {"$lte": precio_max}}))
    if not peliculas:
        print(f"\n  No se encontraron peliculas con precio <= ${precio_max:,}.")
        return
    for p in peliculas:
        separador()
        mostrar_pelicula(p)
    print(f"\n  Total encontradas: {len(peliculas)} (precio <= ${precio_max:,})")


# -- 4. BUSCAR POR REGEX -------------------------------------------------------
def buscar_por_titulo():
    separador("Buscar por titulo")
    texto = input("  Ingresa parte del titulo: ").strip()
    peliculas = list(col.find({"titulo": {"$regex": texto, "$options": "i"}}))
    if not peliculas:
        print(f"\n  No se encontraron peliculas con '{texto}' en el titulo.")
        return
    for p in peliculas:
        separador()
        mostrar_pelicula(p)
    print(f"\n  Total encontradas: {len(peliculas)}")


# -- 5. BUSCAR POR RANGO DE FECHAS ---------------------------------------------
def buscar_por_fechas():
    separador("Buscar por rango de fecha de estreno")
    try:
        desde = datetime.strptime(input("  Fecha desde (YYYY-MM-DD): ").strip(), "%Y-%m-%d")
        hasta = datetime.strptime(input("  Fecha hasta (YYYY-MM-DD): ").strip(), "%Y-%m-%d")
    except ValueError:
        print("\n  Error: formato de fecha incorrecto. Usa YYYY-MM-DD.")
        return
    if desde > hasta:
        print("\n  Error: la fecha 'desde' no puede ser mayor que 'hasta'.")
        return
    peliculas = list(col.find({"fecha_estreno": {"$gte": desde, "$lte": hasta}}))
    if not peliculas:
        print("\n  No se encontraron peliculas en ese rango de fechas.")
        return
    for p in peliculas:
        separador()
        mostrar_pelicula(p)
    print(f"\n  Total encontradas: {len(peliculas)}")
    print(f"  Rango: {desde.strftime('%Y-%m-%d')} hasta {hasta.strftime('%Y-%m-%d')}")


# -- 6. BUSCAR EN SUBDOCUMENTO -------------------------------------------------
def buscar_por_idioma():
    separador("Buscar por idioma")
    idioma = input("  Idioma (Espanol / Ingles / Japones): ").strip()
    peliculas = list(col.find({"detalles.idioma": {"$regex": f"^{idioma}$", "$options": "i"}}))
    if not peliculas:
        print(f"\n  No se encontraron peliculas en idioma '{idioma}'.")
        return
    for p in peliculas:
        separador()
        mostrar_pelicula(p)
    print(f"\n  Total encontradas: {len(peliculas)}")


# -- 7. ACTUALIZAR CAMPO RAIZ --------------------------------------------------
def actualizar_clasificacion():
    separador("Actualizar clasificacion")
    titulo = input("  Titulo de la pelicula: ").strip()
    pelicula = col.find_one({"titulo": {"$regex": titulo, "$options": "i"}})
    if not pelicula:
        print("\n  Pelicula no encontrada.")
        return
    print("\n  Antes:")
    mostrar_pelicula(pelicula)
    nueva_clasificacion = input("\n  Nueva clasificacion: ").strip()
    if not confirmar_accion("  Confirmas el cambio? (s/n): "):
        print("  Operacion cancelada.")
        return
    col.update_one({"_id": pelicula["_id"]}, {"$set": {"clasificacion": nueva_clasificacion}})
    print("\n  Clasificacion actualizada. Despues:")
    mostrar_pelicula(col.find_one({"_id": pelicula["_id"]}))


# -- 8. ACTUALIZAR CAMPO EN SUBDOCUMENTO ---------------------------------------
def actualizar_director():
    separador("Actualizar director")
    titulo = input("  Titulo de la pelicula: ").strip()
    pelicula = col.find_one({"titulo": {"$regex": titulo, "$options": "i"}})
    if not pelicula:
        print("\n  Pelicula no encontrada.")
        return
    print("\n  Antes:")
    mostrar_pelicula(pelicula)
    nuevo_director = input("\n  Nuevo director: ").strip()
    if not confirmar_accion("  Confirmas el cambio? (s/n): "):
        print("  Operacion cancelada.")
        return
    col.update_one({"_id": pelicula["_id"]}, {"$set": {"detalles.director": nuevo_director}})
    print("\n  Director actualizado. Despues:")
    mostrar_pelicula(col.find_one({"_id": pelicula["_id"]}))


# -- 9. ELIMINAR PELICULA ------------------------------------------------------
def eliminar_pelicula():
    separador("Eliminar pelicula")
    titulo = input("  Titulo de la pelicula a eliminar: ").strip()
    pelicula = col.find_one({"titulo": {"$regex": titulo, "$options": "i"}})
    if not pelicula:
        print("\n  Pelicula no encontrada.")
        return
    print("\n  Pelicula a eliminar:")
    mostrar_pelicula(pelicula)
    if not confirmar_accion("\n  Confirmas la eliminacion? (s/n): "):
        print("  Operacion cancelada.")
        return
    col.delete_one({"_id": pelicula["_id"]})
    print(f"\n  Pelicula '{pelicula.get('titulo')}' eliminada correctamente.")


# -- MENU PRINCIPAL ------------------------------------------------------------
def menu():
    while True:
        separador("Sistema de Gestion de Cine")
        print("  1. Listar todas las peliculas")
        print("  2. Agregar nueva pelicula")
        print("  3. Buscar por precio maximo")
        print("  4. Buscar por titulo")
        print("  5. Buscar por rango de fecha de estreno")
        print("  6. Buscar por idioma")
        print("  7. Actualizar clasificacion")
        print("  8. Actualizar director")
        print("  9. Eliminar pelicula")
        print("  0. Salir")
        separador()
        opcion = input("  Selecciona una opcion: ").strip()

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
            print("\n  Hasta luego.")
            client.close()
            break
        else:
            print("\n  Opcion invalida. Intenta de nuevo.")

        input("\n  Presiona Enter para continuar...")


# -- ENTRADA -------------------------------------------------------------------
if __name__ == "__main__":
    cargar_datos_iniciales()
    menu()