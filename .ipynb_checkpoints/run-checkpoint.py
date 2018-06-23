"""
This file will run pikachu volleyball directly
You need to install wine if you use OSX or Linux
"""
import os
import platform
import subprocess
import time

class Pika:
    """
    Class for control operations
    """
    # TODO: Send keyboard input to subprocess
    def __init__(self):
        self.os_name = platform.system()
        self.command = "pika.exe"
        if self.os_name != "Windows":
            self.command = "wine " + self.command
        self.process = None
    def run(self):
        self.process = subprocess.Popen(self.command.split(), preexec_fn=os.setsid)

    def terminate(self):
        self.process.terminate()

if __name__ == '__main__':
    pika = Pika()
    pika.run()
    time.sleep(10)
    pika.terminate()
