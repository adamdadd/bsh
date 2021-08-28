import os
import subprocess
import sys
import time
from cmd import Cmd

from pushbullet import Pushbullet


class ShellWrapper(Cmd):
    intro = ""
    prompt = "bsh | " + os.getcwd() + " ###>"

    def __init__(self, token) -> None:
        super().__init__()
        self.token = token

    def push_result(self, line, process, completion_time) -> None:
        note_body = "rcode: " + str(process.returncode) + "\nSUCCESS!" + "\nCompleted in: " + str(round(completion_time/60, 3)) + "m"
        pb = Pushbullet(self.token)
        pb.push_note(line, str(process.stderr) + "\nFAILED :(") if process.returncode != 0 else pb.push_note(line, note_body)

    def default(self, line) -> None:
        start_time = time.perf_counter()
        proc = subprocess.run(line.split(' '), stderr=subprocess.PIPE, text=True)
        end_time = time.perf_counter()

        self.push_result(line, proc, end_time-start_time)

    def do_cd(self, arg) -> None:
        os.chdir(arg)
        self.prompt = "bsh | " + os.getcwd() + " ###>"

    def do_ls(self, arg) -> None:
        proc = subprocess.run(["ls", "-lah"])

    def do_q(self, arg) -> None:
        print("bye :'(")
        sys.exit()
