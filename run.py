"""
This file will run pikachu volleyball directly
You need to install wine if you use OSX or Linux
"""
import platform
import subprocess

os_name = platform.system()
command = 'pika.exe'

if os_name != "Windows":
    command = "wine " + command
    process = subprocess.call(command, shell=True)
else:
    process = subprocess.call(command)

