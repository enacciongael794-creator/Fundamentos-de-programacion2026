from pathlib import Path
RUTA_ARCHIVO = Path(__file__).resolve().parent
RUTA_TAREAS = RUTA_ARCHIVO / "tareas.txt"
def guardar_tarea(nombre_tarea, materia, horas_estimadas):
    with open(RUTA_TAREAS, "a", encoding="utf-8") as archivo:
              archivo.write(f"{materia},{nombre_tarea},{horas_estimadas}\n")

def leer_tareas():
    tareas = []
    try:
        with open(RUTA_TAREAS, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                if not linea.strip():
                    continue
                
                materia, nombre_tarea, horas_estimadas = linea.strip().split(",")
                tareas.append((materia, nombre_tarea, float(horas_estimadas)))
    
    
    
    except FileNotFoundError:
        print("No se encontro el archivo de tareas. Asegúrese de que 'tareas.txt' exista en el directorio.")
    return tareas
                