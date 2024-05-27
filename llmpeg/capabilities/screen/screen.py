from dataclasses import dataclass
import tkinter as tk


@dataclass
class ScreenSize:
    width: int = None
    height: int = None

    def __post_init__(self):
        if not self.width:
            self.width = tk.Tk().winfo_screenwidth()
        if not self.height:
            self.height = tk.Tk().winfo_screenheight()

    def __str__(self) -> tuple:
        return self.width, self.height

    def __repr__(self) -> tuple:
        return self.width, self.height
