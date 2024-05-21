import inspect
import datetime
import tkinter as tk

error: str = lambda msg: f"[{inspect.getfile(inspect.currentframe().f_back)}:{inspect.currentframe().f_back.f_code.co_name}:{inspect.currentframe().f_back.f_lineno}]: {msg}"
error.__annotations__ = {"return": str}
error.__doc__ = "Return an error message with the file, function, and line number where the error occurred."

curr_date: str = lambda: datetime.datetime.now().strftime("%H-%M-%S_%d-%m-%Y")
curr_date.__annotations__ = {"return": str}
curr_date.__doc__ = "Return the current date in the format 'HH-MM-SS_DD-MM-YYYY'."

get_screen_size: tuple[int, int] = lambda: (tk.Tk().winfo_screenwidth(), tk.Tk().winfo_screenheight())
get_screen_size.__annotations__ = {"return": tuple[int, int]}
get_screen_size.__doc__ = "Return the screen width and height of the current display."
