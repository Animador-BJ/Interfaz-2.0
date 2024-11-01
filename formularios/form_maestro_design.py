# form_maestro_design.py

import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk, ImageDraw
from PIL import Image as PilImage  
from formularios.config import COLOR_BARRA_SUPERIOR, COLOR_MENU_LATERAL, COLOR_CUERPO_PRINCIPAL, COLOR_MENU_CURSOR_ENCIMA
import util.util_ventana as util_ventana
import util.util_imagenes as util_img
from formularios.form_Iniciar_Secion import mostrar_ventana_inicio_sesion
from formularios.form_salir import salir_aplicacion
from formularios.form_crear_cuenta import abrir_ventana_crear_cuenta
from formularios.form_tomar_datos import abrir_ventana_toma_de_datos 

class FormularioMaestroDesign(tk.Tk):
    
    def configurar_boton_menu(self, button, text, icon, font, ancho, alto):
        button.config(
            text=f"{icon} {text}",
            font=font,
            bg=COLOR_MENU_LATERAL,
            fg="white",
            activebackground=COLOR_MENU_CURSOR_ENCIMA,
            activeforeground="white",
            width=ancho,
            height=alto,
            bd=0,
            relief="flat",
        )
        button.pack(side=tk.TOP, fill="x", pady=5, padx=10)
    
    def __init__(self):
        super().__init__()
        self.logo = ImageTk.PhotoImage(Image.open("D:/USUARIO/Music/Eye_System/Interfaz_Eye_System/imagenes/Logo.png"))
        self.config_window()
        self.paneles()
        self.controles_barra_superior()        
        self.controles_menu_lateral()
        self.cargar_pantalla_principal(self.cuerpo_principal) 

    def config_window(self):
        self.title('Eye System')
        w, h = 1800, 900       
        util_ventana.centrar_ventana(self, w, h)        

    def paneles(self):        
        self.barra_superior = tk.Frame(self, bg=COLOR_BARRA_SUPERIOR, width=250)
        self.barra_superior.pack(side=tk.TOP, fill='both')      

        self.menu_lateral = tk.Frame(self, bg=COLOR_MENU_LATERAL, width=500)
        self.menu_lateral.pack(side=tk.LEFT, fill='both') 
        
        self.cuerpo_principal = tk.Frame(self, bg=COLOR_CUERPO_PRINCIPAL, width=150)
        self.cuerpo_principal.pack(side=tk.RIGHT, fill='both', expand=True)

    def controles_barra_superior(self):
        font_awesome = font.Font(family='FontAwesome', size=12)

        self.labelTitulo = tk.Label(self.barra_superior, text="Eye System")
        self.labelTitulo.config(fg="#fff", font=("Roboto", 15), bg=COLOR_BARRA_SUPERIOR, pady=10, width=16)
        self.labelTitulo.pack(side=tk.LEFT)

        self.buttonMenuLateral = tk.Button(self.barra_superior, text="\uf0c9", font=font_awesome,
                                           command=self.toggle_panel, bd=0, bg=COLOR_BARRA_SUPERIOR, fg="white")
        self.buttonMenuLateral.pack(side=tk.LEFT)

    def controles_menu_lateral(self):
        ancho_menu = 20
        alto_menu = 2
        font_awesome = font.Font(family='FontAwesome', size=15)
        self.perfil = self.create_circular_image("D:/USUARIO/Music/Eye_System/Interfaz_Eye_System/imagenes/Perfil.png", (100, 100))
        self.labelPerfil = tk.Label(self.menu_lateral, image=self.perfil, bg=COLOR_MENU_LATERAL)
        self.labelPerfil.pack(side=tk.TOP, pady=10)
        self.buttonIniciarSecion = tk.Button(self.menu_lateral, text="Iniciar Sesión", command=lambda: self.abrir_pantalla(mostrar_ventana_inicio_sesion))
        self.buttonCrearCuenta = tk.Button(self.menu_lateral, text="Crear Cuenta", command=lambda: self.abrir_pantalla(abrir_ventana_crear_cuenta))
        self.buttonTomarDatos = tk.Button(self.menu_lateral, text="Tomar Datos", command=lambda: self.abrir_pantalla(abrir_ventana_toma_de_datos))
        self.buttonDashBoard = tk.Button(self.menu_lateral)
        self.buttonSalir = tk.Button(self.menu_lateral, text="Salir", command=lambda: salir_aplicacion(self))

        buttons_info = [
            ("Iniciar Sesión", "\uf109", self.buttonIniciarSecion),
            ("Crear Cuenta", "\uf007", self.buttonCrearCuenta),
            ("Tomar Datos", "\uf03e", self.buttonTomarDatos),
            ("Panel De Datos", "\uf129", self.buttonDashBoard),
            ("Salir", "\uf013", self.buttonSalir),
        ]

        for text, icon, button in buttons_info:
            self.configurar_boton_menu(button, text, icon, font_awesome, ancho_menu, alto_menu)                    
    
    def abrir_pantalla(self, funcion_pantalla):
        # Limpiar el frame principal antes de abrir la nueva pantalla
        for widget in self.cuerpo_principal.winfo_children():
            widget.destroy()

        self.toggle_panel(False)  # Ocultar el menú lateral al abrir una pantalla
        funcion_pantalla(self.cuerpo_principal, self.cargar_pantalla_principal)

    def cargar_pantalla_principal(self, frame_principal=None):
        self.toggle_panel(True)  # Mostrar el menú lateral al regresar a la pantalla principal
        if frame_principal is None:
            frame_principal = self.cuerpo_principal
            
        for widget in frame_principal.winfo_children():
            widget.destroy()
        label_logo = tk.Label(frame_principal, image=self.logo, bg=COLOR_CUERPO_PRINCIPAL)
        label_logo.place(x=0, y=0, relwidth=1, relheight=1)

    def toggle_panel(self, mostrar=None):
        if mostrar is None:
            mostrar = not self.menu_lateral.winfo_ismapped()
        if mostrar:
            self.menu_lateral.pack(side=tk.LEFT, fill='y')
        else:
            self.menu_lateral.pack_forget()

    def create_circular_image(self, image_path, size):
        img = Image.open(image_path).resize(size, PilImage.Resampling.LANCZOS)
        mask = Image.new("L", size, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, size[0], size[1]), fill=255)
        img = img.convert("RGBA")
        img.putalpha(mask)

        return ImageTk.PhotoImage(img)

if __name__ == "__main__":
    app = FormularioMaestroDesign()
    app.mainloop()
