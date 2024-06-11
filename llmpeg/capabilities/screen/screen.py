from dataclasses import dataclass
import tkinter as tk


@dataclass
class Screen:
  width: int = tk.Tk().winfo_screenwidth()
  height: int = tk.Tk().winfo_screenheight()

  def size(self):
    return self.width, self.height

  def __str__(self) -> tuple:
    return 'Screen(width={self.width}, height={self.height})'
