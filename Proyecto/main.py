import tareas
import almacenamiento
import os
print(os.getcwd())

tareas.mostrar_tarea("Elaborar informe del cateto", "Cálculo Diferencial", 2.5)
almacenamiento.guardar_tarea("Elaborar informe del cateto", "Cálculo Diferencial", 2.5)
actividad = almacenamiento.leer_tareas()
for actividad in actividad:
    materia, nombre_tarea, horas_estimadas = actividad
    tareas.mostrar_tarea(nombre_tarea, materia, horas_estimadas)