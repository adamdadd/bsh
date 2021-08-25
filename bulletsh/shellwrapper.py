import subprocess
from cmd import Cmd


from pushbullet import Pushbullet


class ShellWrapper(Cmd):
    intro = "\n\n\nBullet Shell ####>\n\n\n"
    prompt = "bsh ###>"

    def __init__(self, token) -> None:
        super().__init__()
        self.token = token

    def default(self, line):
        proc = subprocess.run(line.split(' '))
        pb = Pushbullet(self.token)
        pb.push_note(line, str(proc.returncode))
