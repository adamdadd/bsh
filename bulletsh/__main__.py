from pathlib import Path
from requests import ConnectionError

from bulletsh import Bulletsh

home = str(Path.home())
token_path = home + "/.bulletsh/token.txt"

try:
    with open(token_path) as f:
        lines = f.readlines()
except FileNotFoundError:
    print("Missing token in path " + token_path)

while (True):
    try:
        Bulletsh(lines[0].strip("\n"))
    except FileNotFoundError:
        print("Unrecognised Command")
    except ConnectionError:
        print("Unable to connect to server")
