"""
Ventana principal de la aplicación
"""
import tkinter as tk
from tkinter import messagebox


class MainView:
    """Ventana principal de la aplicación"""

    def __init__(self, root):
        self.root = root
        self.root.title("M I S   A C U A R I O S")
        self._build_form()

        # Configurar el tamaño mínimo de la ventana
        self.root.minsize(800, 600)

    def _build_form(self):
        """
        Construye el formulario con paneles correctamente dimensionados
        """
        # Configurar pesos para la ventana principal
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        # Frame principal (contiene menu y dashboard)
        frame_principal = tk.Frame(self.root, padx=0, pady=0)
        frame_principal.grid(row=0, column=0, sticky="nsew")

        # Configurar pesos para frame_principal
        frame_principal.grid_rowconfigure(0, weight=1)
        frame_principal.grid_columnconfigure(1, weight=1)  # La columna del dashboard tiene prioridad

        # Frame del menú (barra lateral izquierda)
        frame_menu = tk.Frame(frame_principal, padx=5, pady=5, bg="blue")
        frame_menu.grid(row=0, column=0, sticky="ns")
        frame_menu.grid_propagate(False)  # Fija el tamaño
        frame_menu.config(width=350, height=600)  # Altura fija pero se expandirá verticalmente

        # Frame del dashboard (área principal)
        frame_dashboard = tk.Frame(frame_principal, padx=5, pady=5, bg="green")
        frame_dashboard.grid(row=0, column=1, sticky="nsew")
        frame_dashboard.grid_propagate(False)
        frame_dashboard.config(width=600, height=600)  # Tamaño inicial

        # Añadir contenido de ejemplo para visualización
        label_acuarios = tk.Label(
            frame_menu,
            text="MIS ACUARIOS",
            bg="blue",
            fg="white",
            font=('Arial', 12, 'bold'),
            cursor="hand2"
        )
        label_acuarios.pack(pady=5)  # Primero pack
        label_acuarios.bind("<Button-1>", on_click)  # Luego bind

        tk.Label(frame_dashboard, text="DASHBOARD PRINCIPAL", bg="green",
                 fg="white", font=('Arial', 16, 'bold')).pack(expand=True)

def on_click(self):
    messagebox.showinfo("Información", "Etiqueta clickada.....")

"""
import tkinter as tk
from tkinter import messagebox


class MainView:

    def __init__(self, root):

        self.root = root
        self.root.title("M I S   A C U A R I O S")
        self._build_form()

    def _build_form(self):

       # Construye los paneles
       frame_principal = tk.Frame(self.root, padx=0, pady=0)
       frame_principal.grid(row=0, column=0)
       frame_menu = tk.Frame(frame_principal, padx=5, pady=5)
       frame_menu.grid(row=0, column=0, sticky="ns")
       frame_menu.config(
           width=200,
           height=500,
           bg="blue"
       )
       frame_dashboard = tk.Frame(frame_principal, padx=5, pady=5)
       frame_dashboard.grid(row=0, column=1)
       frame_dashboard.config(
           width=500,
           height=500,
           bg="green"
       )
"""