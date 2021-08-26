import subprocess
from cmd import Cmd

from pushbullet import Pushbullet


class ShellWrapper(Cmd):
    intro = ""
    prompt = "bsh ###>"

    def __init__(self, token) -> None:
        super().__init__()
        self.token = token

    def default(self, line):
        proc = subprocess.run(line.split(' '), stderr=subprocess.PIPE, text=True)
        pb = Pushbullet(self.token)
        pb.push_note(line, proc.stderr) if proc.returncode != 0 else pb.push_note(line, "rcode: " + str(proc.returncode) + "\nSUCCESS!")
