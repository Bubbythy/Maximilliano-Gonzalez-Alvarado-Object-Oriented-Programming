import tkinter as tk
from tkinter import ttk
from abc import ABC, abstractmethod
from datetime import datetime


class SmartDevice(ABC):
    def __init__(self, name: str):
        self.name = name
        # abstract method forces every child class
        # to create its own turn_on method
        # if a child forgets to include turn_on().
        # python will throw an error
    @abstractmethod
    def turn_on(self) -> str:
        pass

    @abstractmethod
    def turn_off(self) -> str:
        pass


class SmartLight(SmartDevice):
    def __init__(self):
        super().__init__("Living Room Smart Light")

    def turn_on(self) -> str:
        return f"{self.name} set to 100% brightness"

    def turn_off(self) -> str:
        return f"{self.name} dimmed to 0% and switched off"


class SmartSpeaker(SmartDevice):
    def __init__(self):
        super().__init__("Alexa Speaker")

    def turn_on(self) -> str:
        return f"{self.name} is now playing 103.5 Dawn FM"

    def turn_off(self) -> str:
        return f"{self.name} stopped playback and went to sleep"


class SmartAC(SmartDevice):
    def __init__(self):
        super().__init__("Smart Air Conditioner")

    def turn_on(self) -> str:
        return f"{self.name} is now blowing air at 20 degrees Celsius"

    def turn_off(self) -> str:
        return f"{self.name} compressor stopped, fan shutting down"


class SmartCoffeeMaker(SmartDevice):
    def __init__(self):
        super().__init__("Kitchen Coffee Maker")

    def turn_on(self) -> str:
        return f"{self.name} is heating water and brewing 2 cups"

    def turn_off(self) -> str:
        return f"{self.name} stopped brewing and is keeping coffee warm"


class SmartHomeApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Lab 6 Polymorphism GUI")
        self.geometry("600x620")
        self.resizable(False, False)

        self.items = {
            "Smart Light": SmartLight(),
            "Smart Speaker": SmartSpeaker(),
            "Smart Air Conditioner": SmartAC(),
            "Smart Coffee Maker": SmartCoffeeMaker(),
        }

        self._build_interface()

    def _build_interface(self):
        tk.Label(
            self,
            text="SmartHome",
            font=("Arial", 15, "bold"),
            fg="#2c3e50"
        ).pack(pady=12)

        group_box = tk.LabelFrame(
            self,
            text=" Select a Device ",
            font=("Arial", 10, "bold"),
            padx=15,
            pady=10
        )
        group_box.pack(fill="x", padx=20, pady=5)

        self.selected_key = tk.StringVar(value=next(iter(self.items)))

        for key in self.items:
            ttk.Radiobutton(
                group_box,
                text=key,
                value=key,
                variable=self.selected_key
            ).pack(anchor="w", pady=3)

        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=12)

        tk.Button(
            btn_frame,
            text="TURN ON",
            command=self._handle_turn_on,
            bg="#27ae60",
            fg="white",
            font=("Arial", 10, "bold"),
            relief="raised",
            cursor="hand2",
            padx=12,
            pady=6
        ).pack(side="left", padx=8)

        tk.Button(
            btn_frame,
            text="TURN OFF",
            command=self._handle_turn_off,
            bg="#c0392b",
            fg="white",
            font=("Arial", 10, "bold"),
            relief="raised",
            cursor="hand2",
            padx=12,
            pady=6
        ).pack(side="left", padx=8)

        self.lbl_output = tk.Label(
            self,
            text="Select a device and press a button.",
            font=("Arial", 10, "italic"),
            bg="#ecf0f1",
            fg="#34495e",
            relief="groove",
            height=3,
            wraplength=420,
            justify="center"
        )
        self.lbl_output.pack(fill="x", padx=20, pady=5)

        log_frame = tk.LabelFrame(
            self,
            text=" Activity Log ",
            font=("Arial", 10, "bold"),
            padx=8,
            pady=8
        )
        log_frame.pack(fill="both", expand=True, padx=20, pady=(8, 5))

        scrollbar = ttk.Scrollbar(log_frame)
        scrollbar.pack(side="right", fill="y")

        self.txt_log = tk.Text(
            log_frame,
            height=8,
            font=("Consolas", 9),
            state="disabled",  
            wrap="word",
            yscrollcommand=scrollbar.set
        )
        self.txt_log.pack(side="left", fill="both", expand=True)
        scrollbar.config(command=self.txt_log.yview)


        self.txt_log.tag_config("on", foreground="#27ae60")
        self.txt_log.tag_config("off", foreground="#c0392b")

        tk.Button(
            self,
            text="Clear Log",
            command=self._clear_log,
            font=("Arial", 9),
            cursor="hand2"
        ).pack(pady=(0, 10))


    def _handle_turn_on(self):
        device: SmartDevice = self.items[self.selected_key.get()]
        self._show_result(device.turn_on(), "on")

    def _handle_turn_off(self):
        device: SmartDevice = self.items[self.selected_key.get()]
        self._show_result(device.turn_off(), "off")

    def _show_result(self, message: str, tag: str):
        self.lbl_output.config(text=message, font=("Arial", 10, "normal"))
        self._log(message, tag)

    def _log(self, message: str, tag: str):
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.txt_log.config(state="normal")
        self.txt_log.insert("end", f"[{timestamp}] {message}\n", tag)
        self.txt_log.see("end")          # auto-scroll to newest entry
        self.txt_log.config(state="disabled")

    def _clear_log(self):
        self.txt_log.config(state="normal")
        self.txt_log.delete("1.0", "end")
        self.txt_log.config(state="disabled")


if __name__ == "__main__":
    app = SmartHomeApp()
    app.mainloop()