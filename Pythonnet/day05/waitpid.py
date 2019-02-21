import os 
from time import sleep 

pid=os.fork()

if pid<0:
    print('Create process failed')
elif pid==0:
    sleep(3)
    print('child %d process exit'%os.getpid())
    os._exit(3)
else:
    # 非阻塞等待
    while True:
        p,status=os.waitpid(-1,os.WNOHANG)
        print("child pid:",p)
        # 退出状态*256
        print('child exit status:',status)
        if p!=0:
            break
        sleep(1)
    while True:
        print('Parent process...')
        sleep(2)