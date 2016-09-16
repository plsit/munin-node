#!/usr/bin/python
import os
from subprocess import Popen, PIPE
def execute(*cmd):
    p = Popen(cmd, shell=True, bufsize=1024,
              stdin=PIPE, stdout=PIPE, close_fds=True)
    (child_stdin, child_stdout) = (p.stdin, p.stdout)
    return child_stdout.read()
commands = execute("/usr/sbin/munin-node-configure --shell --remove-also").split("\n")
for command in commands:
    if not command.startswith("ln "):
        continue
    if not "/usr/share/munin/plugins/" in command:
        continue
    os.system(command)

