from pathlib import Path

from bulletsh import Bulletsh

home = str(Path.home())
token_path = home + "/.bulletsh/token.txt"

try:
    with open(token_path) as f:
        lines = f.readlines()

    Bulletsh(lines[0].strip("\n"))
except Exception:
    print("Missing token in path " + token_path)

