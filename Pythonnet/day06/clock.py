from multiprocessing import Process
from time import * 

class ClockProcess(Process):
    def __init__(self,value):
        self.value=value
        super().__init__() # 加载父类的init
    
    def run(self):
        for i in range(5):
            print("The time is {}".format(ctime()))
            sleep(self.value)

p=ClockProcess(2)
p.start() # 会自动运行run方法
p.join()