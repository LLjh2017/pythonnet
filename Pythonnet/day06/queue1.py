from multiprocessing import Queue
import time 

# 创建消息队列
q=Queue(3)
q.put(1)
time.sleep(0.1)
print(q.empty())
q.put(2)
q.put(3)

print(q.full())
q.put(4,False)