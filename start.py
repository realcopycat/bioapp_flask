import os
import sys
import subprocess

# 反复执行程序
env = os.environ.copy()
env['pearppid'] = str(os.getpid())
while True:
    if subprocess.call(args=[sys.executable] + sys.argv[1:], env=env) == 1:
        break