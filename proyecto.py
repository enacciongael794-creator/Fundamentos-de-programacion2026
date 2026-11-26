while True:
    materia = input("Ingrese una materia: ")
    materia = materia.strip()  # Eliminar espacios en blanco al inicio y al final
    if not materia:
        continue
    break
while True:
    nombre_tarea = input("Ingrese el nombre de la tarea: ")
    nombre_tarea = nombre_tarea.strip()  # Eliminar espacios en blanco al inicio y al final
    if not nombre_tarea:
        continue
    break

while True:
    try:
        horas_estimadas = float(input("Ingrese el tiempo estimado para realizar la tarea (en horas): "))
        if horas_estimadas <= 0:
            print("El tiempo estimado debe ser mayor a cero. Intente nuevamente.")
            continue
    except ValueError:
        print("Por favor, ingrese un número válido para el tiempo estimado.")
        continue
    break
with open("tareas.txt", "a") as archivo:
    archivo.write(f"{materia},{nombre_tarea},{horas_estimadas}\n")
print("La tarea de la materia", materia, "con nombre", nombre_tarea, "tiene un tiempo estimado de", horas_estimadas, "horas para completarse.")