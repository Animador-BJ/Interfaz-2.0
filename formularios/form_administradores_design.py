# form_administrador_design.py

import customtkinter as ctk
from PIL import Image, ImageTk, ImageDraw
from formularios.form_Iniciar_Secion import mostrar_ventana_inicio_sesion
from formularios.form_crear_cuenta import abrir_ventana_crear_cuenta
from formularios.form_tomar_datos import abrir_ventana_toma_de_datos
from formularios.form_salir import salir_aplicacion

# Definición de colores modernos
COLOR_BARRA_SUPERIOR = "#1a1b26"    # Azul oscuro
COLOR_MENU_LATERAL = "#2d4f7c"      # Azul medio
COLOR_CUERPO_PRINCIPAL = "#f0f5ff"  # Azul claro
COLOR_HOVER = "#1a365d"             # Azul oscuro para hover

class FormularioAdministradorDesign(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Configurar tema
        ctk.set_appearance_mode("system")
        ctk.set_default_color_theme("blue")
        
        self.logo = ImageTk.PhotoImage(Image.open("D:/USUARIO/Music/Eye_System/Interfaz_Eye_System/imagenes/Logo.png"))
        self.config_window()
        self.paneles()
        self.controles_barra_superior()
        self.controles_menu_lateral()
        self.cargar_pantalla_principal(self.cuerpo_principal)

    def config_window(self):
        self.title('Eye System - Administrador')
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        # Establecer las dimensiones de la ventana
        self.geometry(f"{screen_width}x{screen_height-40}+0+0")  # El -40 es para dejar espacio para la barra de tareas
        self.resizable(True, True)

    def paneles(self):
        # Barra superior moderna
        self.barra_superior = ctk.CTkFrame(self, fg_color=COLOR_BARRA_SUPERIOR, height=60)
        self.barra_superior.pack(side='top', fill='x')
        
        # Contenedor principal con grid
        self.contenedor_principal = ctk.CTkFrame(self, fg_color="transparent")
        self.contenedor_principal.pack(side='top', fill='both', expand=True)
        
        # Configurar grid del contenedor principal
        self.contenedor_principal.grid_columnconfigure(1, weight=1)
        self.contenedor_principal.grid_rowconfigure(0, weight=1)
        
        # Menú lateral con efecto glassmorphism usando grid
        self.menu_lateral = ctk.CTkFrame(self.contenedor_principal, fg_color=COLOR_MENU_LATERAL, width=250)
        self.menu_lateral.grid(row=0, column=0, sticky="nsew")
        self.menu_lateral.grid_propagate(False)  # Mantener el ancho fijo
        
        # Cuerpo principal usando grid
        self.cuerpo_principal = ctk.CTkFrame(self.contenedor_principal, fg_color=COLOR_CUERPO_PRINCIPAL)
        self.cuerpo_principal.grid(row=0, column=1, sticky="nsew")

    # Resto del código permanece igual
    # ...

    def controles_barra_superior(self):
        # Título moderno
        self.label_titulo = ctk.CTkLabel(
            self.barra_superior,
            text="Eye System - Administrador",
            font=("Roboto", 20, "bold"),
            text_color="white"
        )
        self.label_titulo.pack(side='left', padx=20)
        
        # Botón de menú moderno
        self.button_menu = ctk.CTkButton(
            self.barra_superior,
            text="≡",
            width=40,
            command=self.toggle_panel,
            fg_color="transparent",
            hover_color=COLOR_HOVER
        )
        self.button_menu.pack(side='left', padx=10)

    def controles_menu_lateral(self):
        # Imagen de perfil circular
        try:
            perfil_img = Image.open("D:/USUARIO/Music/Eye_System/Interfaz_Eye_System/imagenes/Perfil.png")
            perfil_img = perfil_img.resize((100, 100))
            self.perfil = ImageTk.PhotoImage(self.create_circular_image(perfil_img))
            
            label_perfil = ctk.CTkLabel(self.menu_lateral, image=self.perfil, text="")
            label_perfil.pack(pady=20)
        except Exception as e:
            print(f"Error al cargar la imagen de perfil: {e}")

        # Botones modernos
        botones_info = [
            ("Iniciar Sesión", lambda: self.abrir_pantalla(mostrar_ventana_inicio_sesion)),
            ("Crear Cuenta", lambda: self.abrir_pantalla(abrir_ventana_crear_cuenta)),
            ("Tomar Datos", lambda: self.abrir_pantalla(abrir_ventana_toma_de_datos)),
            ("Panel De Datos", lambda: self.abrir_pantalla(self.cargar_pantalla_principal)),
            ("Salir", lambda: salir_aplicacion(self))
        ]

        for texto, comando in botones_info:
            btn = ctk.CTkButton(
                self.menu_lateral,
                text=texto,
                command=comando,
                width=200,
                height=40,
                corner_radius=10,
                fg_color="transparent",
                hover_color=COLOR_HOVER,
                border_width=2,
                border_color="white"
            )
            btn.pack(pady=10, padx=20)

    def abrir_pantalla(self, funcion_pantalla):
        for widget in self.cuerpo_principal.winfo_children():
            widget.destroy()
        
        self.toggle_panel(False)
        funcion_pantalla(self.cuerpo_principal, self.cargar_pantalla_principal)

    def cargar_pantalla_principal(self, frame_principal=None):
        self.toggle_panel(True)
        if frame_principal is None:
            frame_principal = self.cuerpo_principal
            
        for widget in frame_principal.winfo_children():
            widget.destroy()
            
        label_logo = ctk.CTkLabel(frame_principal, image=self.logo, text="")
        label_logo.place(relx=0.5, rely=0.5, anchor='center')

    def toggle_panel(self, mostrar=None):
        if mostrar is None:
            mostrar = not self.menu_lateral.winfo_ismapped()
        
        if mostrar:
            self.menu_lateral.grid(row=0, column=0, sticky="nsew")
        else:
            self.menu_lateral.grid_remove()

    def create_circular_image(self, image):
        # Crear máscara circular
        mask = Image.new("L", image.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, image.size[0], image.size[1]), fill=255)
        
        # Aplicar máscara
        output = Image.new("RGBA", image.size, (0, 0, 0, 0))
        output.paste(image, (0, 0))
        output.putalpha(mask)
        
        return output

if __name__ == "__main__":
    app = FormularioAdministradorDesign()
    app.mainloop()