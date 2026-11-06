import tkinter as tk


class DashboardVentana:
    def __init__(self, root, nombre_usuario):
        self.root = root
        self.root.title("Panel principal")
        self.root.minsize(420, 350)
        self.root.geometry("420x350")
        self.root.resizable(False, False)
        self.root.configure(bg="#EDF5F0")

        tk.Label(
            self.root,
            text="Panel principal",
            font=("Arial", 21, "bold"),
            bg="#EDF5F0",
            fg="#245C45"
        ).pack(pady=(30, 20))

        tarjeta = tk.Frame(self.root, bg="white")
        tarjeta.pack(fill="x", padx=30)

        tk.Label(
            tarjeta,
            text="¡Bienvenido al sistema!",
            font=("Arial", 13, "bold"),
            bg="white",
            fg="#245C45"
        ).pack(pady=(20, 10))

        tk.Label(
            tarjeta,
            text=f"Usuario: {nombre_usuario}",
            font=("Arial", 11),
            bg="white",
            fg="#46564E",
            wraplength=320
        ).pack(padx=10, pady=(0, 20))

        tk.Button(
            self.root,
            text="Cerrar sesión",
            font=("Arial", 11, "bold"),
            bg="#378562",
            fg="white",
            activebackground="#245C45",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            pady=10,
            command=self._cerrar_sesion
        ).pack(fill="x", padx=60, pady=25)

    def _cerrar_sesion(self):
        from Views.login_view import LoginVentana

        for widget in self.root.winfo_children():
            widget.destroy()

        LoginVentana(self.root)
