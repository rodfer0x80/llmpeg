from pathlib import Path
import os

a = Path(f'~/.cache/{str(Path(__file__).cwd().name).split("/")[-1]}').expanduser()

print(a)
