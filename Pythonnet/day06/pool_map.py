from multiprocessing import Pool 
import time 

def fun(n):
    time.sleep(1)
    return n*n

pool=Pool()
# 使用map将事件放进进程池
r=pool.map(fun,[1,2,3,4,5])
pool.close()
pool.join()
print(r)
# [1, 4, 9, 16, 25]


