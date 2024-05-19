import inspect
import datetime

error: str = lambda e: f"[{inspect.getfile(inspect.currentframe().f_back)}:{inspect.currentframe().f_back.f_code.co_name}:{inspect.currentframe().f_back.f_lineno}]: {e}"
error.__doc__ = "Return an error message with the file, function, and line number where the error occurred."

curr_date: str = lambda: datetime.datetime.now().strftime("%H-%M-%S_%d-%m-%Y")
curr_date.__doc__ = "Return the current date in the format 'HH-MM-SS_DD-MM-YYYY'."