from pathlib import Path

from bulletsh import Bulletsh


if __name__ == '__main__':

    home = str(Path.home())
    token_path = home + "/.bulletsh/token.txt"
    
    try:
        with open(token_path) as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("Missing token in path " + token_path)
    
    print("\n\n\nBullet Shell ####>\n\n\n")
    
    Bulletsh(lines[0].strip("\n"))
