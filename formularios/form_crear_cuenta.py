# form_crear_cuanta.py

# form_crear_cuanta.py

import customtkinter as ctk
import pymysql
from tkinter import messagebox

# Definición de colores modernos
COLOR_PRINCIPAL = "#1a1b26"     # Azul oscuro
COLOR_SECUNDARIO = "#f0f5ff"    # Azul claro 
COLOR_ACENTO = "#2d4f7c"        # Azul medio
COLOR_HOVER = "#1a365d"         # Azul oscuro para hover
COLOR_CUERPO_PRINCIPAL = COLOR_SECUNDARIO  # Mismo color de fondo que form_tomar_datos.py

def guardar_info():
    correo = correo_entry.get()
    contrasena = contrasena_entry.get()

    try:
        # Establecer la conexión a la base de datos
        conn = pymysql.connect(host='b4qhbwwqys2nhher1vul-mysql.services.clever-cloud.com', port=3306, db='b4qhbwwqys2nhher1vul', user='upvge9afjesbmmgv', password='BS2bxJNACO1XYEmWBqA0')

        # Crear un objeto cursor
        cur = conn.cursor()

        # Preparar la consulta SQL para insertar los datos
        sql = "INSERT INTO usuario (correo, password) VALUES (%s, %s)"

        # Ejecutar la consulta SQL con los valores obtenidos de los campos de entrada
        cur.execute(sql, (correo, contrasena))

        # Confirmar los cambios en la base de datos
        conn.commit()

        # Mostrar mensaje de éxito
        messagebox.showinfo("Cuenta Creada", "Cuenta creada exitosamente.")

    except Exception as e:
        # Manejar cualquier error que ocurra durante la operación de inserción
        print(f"Ocurrió un error: {e}")
    finally:
        # Cerrar la conexión a la base de datos
        if conn.open:
            cur.close()
            conn.close()

def abrir_ventana_crear_cuenta(parent_frame, regresar_callback):
    # Limpiar frame principal
    for widget in parent_frame.winfo_children():
        widget.destroy()

    # Estilos y fuentes
    fuente_titulo = ("Roboto", 24, "bold")
    fuente_normal = ("Roboto", 14)

    # Frame principal
    main_frame = ctk.CTkFrame(parent_frame, fg_color=COLOR_CUERPO_PRINCIPAL)
    main_frame.pack(fill="both", expand=True, padx=20, pady=20)

    # Título
    titulo = ctk.CTkLabel(main_frame, text="Crear Cuenta", font=fuente_titulo, text_color=COLOR_PRINCIPAL)
    titulo.pack(pady=20)

    # Campo de correo
    correo_label = ctk.CTkLabel(main_frame, text="Correo Electrónico:", font=fuente_normal, text_color=COLOR_PRINCIPAL)
    correo_label.pack(pady=5)

    global correo_entry
    correo_entry = ctk.CTkEntry(main_frame, font=fuente_normal, height=45, width=300)
    correo_entry.pack(pady=5)

    # Campo de contraseña
    contrasena_label = ctk.CTkLabel(main_frame, text="Contraseña:", font=fuente_normal, text_color=COLOR_PRINCIPAL)
    contrasena_label.pack(pady=5)

    global contrasena_entry
    contrasena_entry = ctk.CTkEntry(main_frame, show="*", font=fuente_normal, height=45, width=300)
    contrasena_entry.pack(pady=5)

    # Botón para crear cuenta moderno
    boton_crear_cuenta = ctk.CTkButton(
        main_frame, 
        text="Crear Cuenta",
        command=guardar_info,
        width=200,
        height=40,
        corner_radius=10,
        hover_color=COLOR_HOVER
    )
    boton_crear_cuenta.pack(pady=10)

    # Botón para regresar moderno
    boton_regresar = ctk.CTkButton(
        main_frame,
        text="Regresar",
        command=regresar_callback,
        width=200,
        height=40,
        corner_radius=10,
        hover_color=COLOR_HOVER
    )
    boton_regresar.pack(pady=10)