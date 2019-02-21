from multiprocessing import Process,Array
import time 

# 创建共享内存,将列表放入共享内存
# shm=Array('i',[1,2,3,4,5])
# 在共享内存中开辟5个整形空间
# shm=Array('i',5)
# 存入字符串
shm = Array('c',b'Hello')
def fun():
    for i in shm:
        print(i)
p = Process(target = fun)
p.start()
p.join()
print(shm.value)