import os
import subprocess
import sys
import time
from cmd import Cmd

from pushbullet import Pushbullet


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

class ShellWrapper(Cmd):
    intro = logo
    prompt = "bsh | " + os.getcwd() + " ###>"

    completions = [""]

    def __init__(self, token) -> None:
        super().__init__()
        self.token = token
        self.secret = False

    def push_result(self, line, process, completion_time) -> None:
        if not self.secret:
            note_body_failure = str(process.stderr) + "\nFAILED :("
        else:
            note_body_failure = str(process.returncode) + "\nFAILED :("
        note_body_success = "rcode: " + str(process.returncode) + "\nSUCCESS!" + "\nCompleted in: " + str(round(completion_time/60, 3)) + "m"

        pb = Pushbullet(self.token)
        pb.push_note(line, note_body_failure) if process.returncode != 0 else pb.push_note(line, note_body_success)

    def default(self, line) -> None:
        parsed_line = self.parse_line(line)
        start_time = time.perf_counter()
        proc = subprocess.run(parsed_line, stderr=subprocess.PIPE, text=True)
        end_time = time.perf_counter()
        self.push_result(line, proc, end_time-start_time)

    def parse_line(self, line) -> list:
        line_list = line.split(' ')
        secret_option = "--secret"
        if self._is_option_in_line(line_list, secret_option):
            line_list.remove(secret_option)
            self.secret = True
        return line_list

    @staticmethod
    def _is_option_in_line(line_list, option) -> bool:
        return True if option in line_list else False

    def do_cd(self, arg) -> None:
        os.chdir(arg)
        self.prompt = "bsh | " + os.getcwd() + " ###>"

    def do_ls(self, line) -> None:
        subprocess.run(["ls", "-lahS"])

    def do_gitlog(self, line) -> None:
        subprocess.run(["git", "log", "--all", "--decorate", "--graph", "--oneline"])

    def do_q(self, line) -> None:
        print("bye :'(")
        sys.exit()
