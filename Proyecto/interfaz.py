import tkinter as tk
import almacenamiento
from tkinter import simpledialog

# PALETA VISUAL: puedes cambiar los colores aquí sin tocar la lógica.
COLORES = {
    "fondo": "#0D1526",         # Fondo principal azul muy oscuro
    "panel": "#17243A",         # Tarjeta central
    "barra": "#111E32",         # Franja de botones inferior
    "borde": "#2A3B53",         # Bordes discretos
    "texto": "#F3F7FF",         # Blanco suave
    "secundario": "#A7B8CE",    # Texto secundario
    "azul": "#357DF6",          # Botón principal
    "azul_hover": "#5898FF",    # Botón principal al señalarlo
    "rojo": "#B93D57",          # Botón de eliminar
    "rojo_hover": "#D44E6B",    # Botón de eliminar al señalarlo
    "boton_sec": "#2A3B53",    # Botón secundario
    "boton_sec_hover": "#38516F", # Botón secundario al señalarlo
    "lista": "#22324B",         # Recuadro de tareas
    "seleccion": "#357DF6",     # Fila seleccionada
}

ventana_principal = tk.Tk()
menu_principal = tk.Frame(ventana_principal, bg=COLORES["barra"])
menu_principal.pack(side="bottom", fill="x")
ventana_principal.title("QuestAcademy")
ventana_principal.geometry("950x650")
ventana_principal.configure(bg=COLORES["fondo"])


#TITULO
titulo = tk.Label(
    ventana_principal, text="Bienvenido a QuestAcademy",
    font=("Segoe UI Semibold", 25),
    bg=COLORES["fondo"], fg=COLORES["texto"],
)
titulo.pack(pady=(24, 16))

#Texto de tareas
frame_tareas = tk.Frame(
    ventana_principal, bg=COLORES["panel"],
    highlightbackground=COLORES["borde"], highlightthickness=1,
)
frame_tareas.pack(pady=(0, 22), padx=35, fill="both", expand=True)
tareas = tk.Label(
    frame_tareas, text="Elije una de las opciones",
    font=("Segoe UI", 20), bg=COLORES["panel"], fg=COLORES["secundario"],
)
tareas.pack(pady=28)
tareas_pendientes = tk.Label(
    frame_tareas, text="Tareas pendientes",
    font=("Segoe UI Semibold", 20), bg=COLORES["panel"], fg=COLORES["texto"],
)


#Botones de tareas 
boton_tareas = tk.Button(
    menu_principal, text="Tareas", font=("Segoe UI Semibold", 12),
    command=lambda: mostrar_tareas(),
    bg=COLORES["azul"], fg=COLORES["texto"],
    activebackground=COLORES["azul_hover"], activeforeground=COLORES["texto"],
    bd=0, relief="flat", padx=19, pady=10, cursor="hand2",
)
boton_tareas.pack(side="left", padx=14, pady=18)
boton_cerrar_tareas = tk.Button(
    menu_principal, text="Cerrar Tareas", font=("Segoe UI Semibold", 12),
    command=lambda: cerrar_tareas(),
    bg=COLORES["boton_sec"], fg=COLORES["texto"],
    activebackground=COLORES["boton_sec_hover"], activeforeground=COLORES["texto"],
    bd=0, relief="flat", padx=16, pady=10, cursor="hand2",
)
#Boton para agregar tarea
boton_agregar_tarea = tk.Button(
    menu_principal, text="Agregar Tarea", font=("Segoe UI Semibold", 12),
    command=lambda: agregar_tarea(),
    bg=COLORES["azul"], fg=COLORES["texto"],
    activebackground=COLORES["azul_hover"], activeforeground=COLORES["texto"],
    bd=0, relief="flat", padx=19, pady=10, cursor="hand2",
)
boton_agregar_tarea.pack(side="right", padx=14, pady=18)
#boton para eliminar tarea
boton_eliminar_tarea = tk.Button(
    menu_principal, text="Eliminar Tarea", font=("Segoe UI Semibold", 12),
    command=lambda: eliminar_tarea(),
    bg=COLORES["rojo"], fg=COLORES["texto"],
    activebackground=COLORES["rojo_hover"], activeforeground=COLORES["texto"],
    bd=0, relief="flat", padx=19, pady=10, cursor="hand2",
)
boton_eliminar_tarea.pack(side="right", padx=8, pady=18)







# Solo cambia el color cuando el cursor pasa por encima de un botón.
def _color_al_pasar(boton, normal, al_pasar):
    boton.bind("<Enter>", lambda evento: boton.configure(bg=al_pasar))
    boton.bind("<Leave>", lambda evento: boton.configure(bg=normal))

_color_al_pasar(boton_tareas, COLORES["azul"], COLORES["azul_hover"])
_color_al_pasar(boton_cerrar_tareas, COLORES["boton_sec"], COLORES["boton_sec_hover"])
_color_al_pasar(boton_agregar_tarea, COLORES["azul"], COLORES["azul_hover"])
_color_al_pasar(boton_eliminar_tarea, COLORES["rojo"], COLORES["rojo_hover"])


#Recuadro de tareas
cuadro = tk.Listbox(
    frame_tareas, width=80, height=15, font=("Segoe UI", 12),
    bg=COLORES["lista"], fg=COLORES["texto"],
    selectbackground=COLORES["seleccion"], selectforeground=COLORES["texto"],
    relief="flat", bd=0, highlightthickness=0, activestyle="none",
)

lista_tareas = almacenamiento.leer_tareas()
for tarea in lista_tareas:
    materia, nombre_tarea, horas_estimadas = tarea
    cuadro.insert(tk.END, f"{materia} {nombre_tarea} {horas_estimadas}",)




def mostrar_tareas():
    tareas_pendientes.pack()
    cuadro.pack(pady=12)
    boton_cerrar_tareas.pack(side="left", padx=10, pady=10)
    
    tareas.pack_forget()
    
    
def cerrar_tareas():
    cuadro.pack_forget()
    boton_cerrar_tareas.pack_forget()
    tareas_pendientes.pack_forget()
    tareas.pack()
    
    
def agregar_tarea():
    materia = simpledialog.askstring("Nueva tarea", "¿Qué materia es?", parent=ventana_principal)
    if materia is None:
        return 
    tarea_materia = simpledialog.askstring("Nueva tarea", "¿Cuál es el nombre de la tarea?", parent=ventana_principal)
    if tarea_materia is None:
        return
    horas_estimadas = simpledialog.askfloat("Nueva tarea", "¿Cuántas horas estimadas para completarla?", parent=ventana_principal)
    if horas_estimadas is None:
        return
    almacenamiento.guardar_tarea(tarea_materia, materia, horas_estimadas)
    actualizar_lista_tareas()
    
    
def actualizar_lista_tareas():
    (cuadro.delete(0, tk.END))
    for tarea in almacenamiento.leer_tareas():
        materia, nombre_tarea, horas_estimadas = tarea
        cuadro.insert(tk.END, f"{materia} {nombre_tarea} {horas_estimadas}")


def eliminar_tarea():
    seleccion = cuadro.curselection()
    if seleccion:
        indice = seleccion[0]
        cuadro.delete(indice)
        lista_tareas = almacenamiento.leer_tareas()
        lista_tareas.pop(indice)
        with open(almacenamiento.RUTA_TAREAS, "w", encoding="utf-8")  as archivo:
            for tarea in lista_tareas:
                materia, nombre_tarea, horas_estimadas = tarea
                archivo.write(f"{materia},{nombre_tarea},{horas_estimadas}\n")   




ventana_principal.mainloop()