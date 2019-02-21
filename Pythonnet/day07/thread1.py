import threading 
from time import sleep 

# 线程函数
def music():
    for i in range(5):
        sleep(2)
        print("播放学猫叫")

# 创建线程对象
t = threading.Thread(target=music)
t.start()

# 主线程运行
for i in range(3):
    sleep(3)
    print("播放卡路里")
t.join()