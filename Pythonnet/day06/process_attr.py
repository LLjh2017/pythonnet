from multiprocessing import Process 
from time import sleep,ctime

def tm():
    for i in range(2):
        sleep(2)
        print(ctime())
p=Process(target=tm)
p.start()

print("Process name:",p.name)
print("Process PID:",p.pid)
print("Process alive:",p.is_alive())
p.join()
print("Process alive:",p.is_alive())


