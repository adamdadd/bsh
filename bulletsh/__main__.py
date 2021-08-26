from pathlib import Path

from bulletsh import Bulletsh

home = str(Path.home())
token_path = home + "/.bulletsh/token.txt"

try:
    with open(token_path) as f:
        lines = f.readlines()
except FileNotFoundError:
    print("Missing token in path " + token_path)

print("\n\n\nBullet Shell ####>\n\n\n")

while (True):
    try:
        Bulletsh(lines[0].strip("\n"))
    except Exception:
        print("Unrecognised Command")
