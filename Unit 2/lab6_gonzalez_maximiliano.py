import os
from tkinter import *
from tkinter import ttk
import tkinter as tk
from abc import ABC, abstractmethod


class SmartDevice(ABC):
    def __init__(self, name: str):
        self.name = name

        # abstract method forces every child class
        # to create its own turn_on method
        # if a child forgets to include turn_on().
        # python will throw an error

        @abstractmethod
        def turn_on(self):
            pass

# All next classes inherit from Superclass "SmartDevice"
# they share the samem method Turn_on() but each
# provides its own unique immplementation (polymorphism)


class SmartLight(SmartDevice):
    def __init__(self):
        super().__init__("Living Room Smart Light")

    def turn_on(self):
        return f"{self.name} Set to 100% brightness"


class SmartSpeaker(SmartDevice):
    def __init__(self):
        super().__init__("Alexa speaker")

    def turn_on(self):
        return f"{self.name} is now playing 103.5 Dawn FM"


class SmartAC(SmartDevice):
    def __init__(self):
        super().__init__("Smart Air Conditioner")

    def turn_on(self):
        return f"{self.name} is now blowing air at 20 degrees celsius"

# GUI with tkinter


class SmartDevice(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def turn_on(self):
        pass


class SmartLight(SmartDevice):
    def __init__(self):
        super().__init__("Living Room Smart Light")

    def turn_on(self):
        return f"{self.name} set to 100% brightness"


class SmartSpeaker(SmartDevice):
    def __init__(self):
        super().__init__("Alexa speaker")

    def turn_on(self):
        return f"{self.name} is now playing 103.5 Dawn FM"


class SmartAC(SmartDevice):
    def __init__(self):
        super().__init__("Smart Air Conditioner")

    def turn_on(self):
        return f"{self.name} is now blowing air at 20 degrees celsius"


class SmartHomeApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Lab 6 Polymorphism GUI Template")
        self.geometry("600x450")
        self.resizable(False, False)

        self.items = {
            "Smart Light": SmartLight(),
            "Smart Speaker": SmartSpeaker(),
            "Smart Air Conditioner": SmartAC(),
        }

        self._build_interface()

    def _build_interface(self):
        lbl_header = tk.Label(
            self,
            text="SmartHome",
            font=("Arial", 15, "bold"),
            fg="#2c3e50"
        )
        lbl_header.pack(pady=12)

        group_box = tk.LabelFrame(
            self,
            text=" Select an Option ",
            font=("Arial", 10, "bold"),
            padx=15,
            pady=10
        )
        group_box.pack(fill="x", padx=20, pady=5)

        first_key = list(self.items.keys())[0]
        self.selected_key = tk.StringVar(value=first_key)

        for key in self.items.keys():
            rb = ttk.Radiobutton(
                group_box,
                text=key,
                value=key,
                variable=self.selected_key
            )
            rb.pack(anchor="w", pady=3)

        btn_action = tk.Button(
            self,
            text="EXECUTE ACTION",
            command=self._handle_action,
            bg="#2980b9",
            fg="white",
            font=("Arial", 10, "bold"),
            relief="raised",
            cursor="hand2",
            padx=12,
            pady=6
        )
        btn_action.pack(pady=15)

        self.lbl_output = tk.Label(
            self,
            text="Turn on device'.",
            font=("Arial", 10, "italic"),
            bg="#ecf0f1",
            fg="#34495e",
            relief="groove",
            height=3,
            wraplength=420,
            justify="center"
        )
        self.lbl_output.pack(fill="x", padx=20, pady=5)

    def _handle_action(self):
        chosen_key = self.selected_key.get()

        active_object: SmartDevice = self.items[chosen_key]

        result_message = active_object.turn_on()

        self.lbl_output.config(
            text=result_message,
            font=("Arial", 10, "normal")
        )


if __name__ == "__main__":
    app = SmartHomeApp()
    app.mainloop()