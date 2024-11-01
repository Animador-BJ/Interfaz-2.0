# form_principal.py

import customtkinter as ctk
from formularios.form_maestro_design import FormularioMaestroDesign
from formularios.form_administradores_design import FormularioAdministradorDesign

# Definición de colores (tema moderno)
COLOR_MITAD_IZQUIERDA = "#1a1b26"  # Azul oscuro
COLOR_MITAD_DERECHA = "#f0f5ff"    # Azul claro

class FormCrearIniciarSesion(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Configurar tema
        ctk.set_appearance_mode("system")  # Modes: system (default), light, dark
        ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green
        
        self.config_window()
        self.paneles()
        self.controles_botones()

        # Frames modernos
        self.frame_administrador = ctk.CTkFrame(self.izquierda, fg_color=COLOR_MITAD_IZQUIERDA)
        self.frame_administrador.pack(fill='both', expand=True)

        self.frame_usuario = ctk.CTkFrame(self.derecha, fg_color=COLOR_MITAD_DERECHA)
        self.frame_usuario.pack(fill='both', expand=True)

        self.ocultar_formularios()

    def config_window(self):
        self.title('Sistema de Inicio de Sesión')
    
    # Obtener las dimensiones de la pantalla
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
    
    # Establecer las dimensiones de la ventana
        self.geometry(f"{screen_width}x{screen_height-40}+0+0")  # El -40 es para dejar espacio para la barra de tareas
        self.resizable(True, True)

    def paneles(self):
        self.cuerpo_principal = ctk.CTkFrame(self)
        self.cuerpo_principal.pack(fill='both', expand=True)

        # Mitades con efecto de glassmorphism
        self.izquierda = ctk.CTkFrame(self.cuerpo_principal, fg_color=COLOR_MITAD_IZQUIERDA)
        self.izquierda.pack(side='left', fill='both', expand=True)

        self.derecha = ctk.CTkFrame(self.cuerpo_principal, fg_color=COLOR_MITAD_DERECHA)
        self.derecha.pack(side='right', fill='both', expand=True)

    def controles_botones(self):
        # Botones modernos con hover effect
        self.button_administrador = ctk.CTkButton(
            self.izquierda,
            text="Iniciar Como Administrador",
            command=self.mostrar_formulario_administrador,
            width=200,
            height=40,
            corner_radius=10,
            hover_color="#2d4f7c"
        )
        self.button_administrador.pack(expand=True, padx=50, pady=20)

        self.button_usuario = ctk.CTkButton(
            self.derecha,
            text="Iniciar Como Usuario",
            command=self.mostrar_formulario_usuario,
            width=200,
            height=40,
            corner_radius=10,
            fg_color="#2d4f7c",
            hover_color="#1a365d"
        )
        self.button_usuario.pack(expand=True, padx=50, pady=20)

    def mostrar_formulario_administrador(self):
        self.ocultar_formularios()
        self.frame_administrador.pack(fill='both', expand=True)
        
        for widget in self.frame_administrador.winfo_children():
            widget.destroy()

        # Título con estilo
        ctk.CTkLabel(
            self.frame_administrador,
            text="Iniciar Como Administrador",
            font=("Helvetica", 24, "bold"),
            text_color="white"
        ).pack(pady=(40, 20))

        # Campo de correo con icono
        ctk.CTkLabel(
            self.frame_administrador,
            text="Correo Electrónico:",
            font=("Helvetica", 14),
            text_color="white"
        ).pack(pady=(10, 0))
        
        self.entry_admin_correo = ctk.CTkEntry(
            self.frame_administrador,
            width=300,
            height=40,
            placeholder_text="correo@ejemplo.com",
            corner_radius=10
        )
        self.entry_admin_correo.pack(pady=(5, 15))

        # Campo de contraseña con icono
        ctk.CTkLabel(
            self.frame_administrador,
            text="Contraseña:",
            font=("Helvetica", 14),
            text_color="white"
        ).pack(pady=(10, 0))
        
        self.entry_admin_contraseña = ctk.CTkEntry(
            self.frame_administrador,
            width=300,
            height=40,
            placeholder_text="Contraseña",
            show="•",
            corner_radius=10
        )
        self.entry_admin_contraseña.pack(pady=(5, 20))

        # Botón de inicio de sesión moderno
        self.button_iniciar_admin = ctk.CTkButton(
            self.frame_administrador,
            text="Iniciar Sesión",
            command=self.iniciar_sesion_administrador,
            width=200,
            height=40,
            corner_radius=10,
            hover_color="#2d4f7c"
        )
        self.button_iniciar_admin.pack(pady=20)

    def mostrar_formulario_usuario(self):
        self.ocultar_formularios()
        self.frame_usuario.pack(fill='both', expand=True)
        
        for widget in self.frame_usuario.winfo_children():
            widget.destroy()

        # Título con estilo
        ctk.CTkLabel(
            self.frame_usuario,
            text="Iniciar Como Usuario",
            font=("Helvetica", 24, "bold"),
            text_color="#1a1b26"
        ).pack(pady=(40, 20))

        # Campo de correo con estilo
        ctk.CTkLabel(
            self.frame_usuario,
            text="Correo Electrónico:",
            font=("Helvetica", 14),
            text_color="#1a1b26"
        ).pack(pady=(10, 0))
        
        self.entry_usuario_correo = ctk.CTkEntry(
            self.frame_usuario,
            width=300,
            height=40,
            placeholder_text="correo@ejemplo.com",
            corner_radius=10
        )
        self.entry_usuario_correo.pack(pady=(5, 15))

        # Campo de contraseña con estilo
        ctk.CTkLabel(
            self.frame_usuario,
            text="Contraseña:",
            font=("Helvetica", 14),
            text_color="#1a1b26"
        ).pack(pady=(10, 0))
        
        self.entry_usuario_contraseña = ctk.CTkEntry(
            self.frame_usuario,
            width=300,
            height=40,
            placeholder_text="Contraseña",
            show="•",
            corner_radius=10
        )
        self.entry_usuario_contraseña.pack(pady=(5, 20))

        # Botón de inicio de sesión moderno
        self.button_iniciar_usuario = ctk.CTkButton(
            self.frame_usuario,
            text="Iniciar Sesión",
            command=self.iniciar_sesion_usuario,
            width=200,
            height=40,
            corner_radius=10,
            fg_color="#2d4f7c",
            hover_color="#1a365d"
        )
        self.button_iniciar_usuario.pack(pady=20)

    def ocultar_formularios(self):
        self.frame_administrador.pack_forget()
        self.frame_usuario.pack_forget()

    def iniciar_sesion_usuario(self):
        self.destroy()
        app = FormularioMaestroDesign()
        app.mainloop()

    def iniciar_sesion_administrador(self):
        self.destroy()
        admin_app = FormularioAdministradorDesign()
        admin_app.mainloop()

if __name__ == "__main__":
    app = FormCrearIniciarSesion()
    app.mainloop()