import tkinter as tk
from tkinter import messagebox
from Models.login_models import User
from Views.home_view import DashboardVentana


class LoginVentana:
    def __init__(self, root):
        self.root = root
        self.root.title("Inicio de sesión")
        self.root.minsize(380, 420)
        self.root.geometry("380x420")
        self.root.resizable(False, False)
        self.root.configure(bg="#EDF5F0")

        self._crear_interfaz()

    def _crear_interfaz(self):
        tk.Label(
            self.root,
            text="Bienvenido",
            font=("Arial", 22, "bold"),
            bg="#EDF5F0",
            fg="#245C45"
        ).pack(pady=(30, 5))

        tk.Label(
            self.root,
            text="Ingresa tus datos para continuar",
            font=("Arial", 10),
            bg="#EDF5F0",
            fg="#65756D"
        ).pack(pady=(0, 25))

        tk.Label(
            self.root,
            text="Usuario:",
            font=("Arial", 11),
            bg="#EDF5F0"
        ).pack(anchor="w", padx=40)

        self.entry_usuario = tk.Entry(
            self.root,
            font=("Arial", 12),
            relief="solid",
            bd=1
        )
        self.entry_usuario.pack(fill="x", padx=40, pady=(5, 15))

        tk.Label(
            self.root,
            text="Contraseña:",
            font=("Arial", 11),
            bg="#EDF5F0"
        ).pack(anchor="w", padx=40)

        self.entry_pass = tk.Entry(
            self.root,
            font=("Arial", 12),
            show="*",
            relief="solid",
            bd=1
        )
        self.entry_pass.pack(fill="x", padx=40, pady=(5, 25))

        tk.Button(
            self.root,
            text="Iniciar sesión",
            font=("Arial", 11, "bold"),
            bg="#378562",
            fg="white",
            activebackground="#245C45",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            pady=10,
            command=self._validar_login
        ).pack(fill="x", padx=40)

        self.entry_usuario.focus_set()

    def _validar_login(self):
        usuario = self.entry_usuario.get().strip()
        password = self.entry_pass.get()

        if not usuario or not password:
            messagebox.showwarning(
                "Campos vacíos",
                "Escribe tu usuario y contraseña."
            )
            return

        usuario_obj = User(usuario, password)
        datos = usuario_obj.auth()

        if datos is None:
            messagebox.showerror(
                "Error de conexión",
                "No se pudo consultar la base de datos. Revisa la terminal."
            )
        elif datos:
            nombre = datos[0].get("nombre", "Usuario")
            self._abrir_dashboard(nombre)
        else:
            messagebox.showerror(
                "Acceso incorrecto",
                "Usuario o contraseña incorrectos."
            )

    def _abrir_dashboard(self, nombre):
        for widget in self.root.winfo_children():
            widget.destroy()

        DashboardVentana(self.root, nombre)
