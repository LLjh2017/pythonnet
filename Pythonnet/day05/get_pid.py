import os 
from time import sleep

pid=os.fork()

if pid<0:
    print("Error")
elif pid==0:
    sleep(1)
    print("Child PID",os.getpid())
    # 获取父进程PID
    print("Get Parent PID",os.getppid())
else:
    print("Parent PID",os.getpid())
    # 获取子进程PID
    print("Get Child PID",pid)