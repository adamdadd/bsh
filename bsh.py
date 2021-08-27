from pathlib import Path

from bulletsh import Bulletsh

logo = """
Here Comes the Sun!

     ______
    /_____/\\\\
   /_____\\\\ \\\\
  /_____\ \\\\ /
 /_____/ \/ / /
/_____/ /   \//\\
\_____\//\   / /
 \_____/ / /\ /
  \_____/ \\\\ \\
   \_____\ \\\\
    \_____\/
"""


if __name__ == '__main__':

    home = str(Path.home())
    token_path = home + "/.bulletsh/token.txt"
    
    try:
        with open(token_path) as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("Missing token in path " + token_path)
    
    print(logo)
    
    Bulletsh(lines[0].strip("\n"))
