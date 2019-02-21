import multiprocessing as mp 

# 编写进程函数
def fun():
    print("子进程事件")

# 创建进程对象
p = mp.Process(target = fun) 

# 启动进程
p.start()

# 回收进程
p.join()