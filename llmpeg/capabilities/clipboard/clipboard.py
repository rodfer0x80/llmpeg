from dataclasses import dataclass
import tkinter as tk


@dataclass
class CopyToClipboard:
  text: str

  def __post_init__(self) -> None:
    root = tk.Tk()
    root.withdraw()
    root.clipboard_clear()
    root.clipboard_append(self.text)
    root.update()
    root.destroy()


@dataclass
class CopyFromClipboard:
  text: str = ''

  def __post_init__(self):
    root = tk.Tk()
    root.withdraw()
    try:
      self.text = root.clipboard_get()
    except tk.TclError:
      self.text = ''
    root.destroy()


@dataclass
class Clipboard:
  def copy_to_clipboard(self, text: str) -> None:
    CopyToClipboard(text)

  def copy_from_clipboard(self) -> str:
    return CopyFromClipboard().text
