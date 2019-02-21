from threading import Thread,currentThread
import time

def fun():
    time.sleep(0.1)
    # 获取当前线程对象
    a = currentThread().getName()
    print("执行%s线程"%a)
    print("线程属性测试")
t = Thread(target=fun,name="Tarena")
t.start()
# 设置 获取 线程名
t.setName('Tedu')
print("Thread name:",t.name)
print("Thread get name:",t.getName())
# 线程状态
print("is alive:",t.is_alive())
t.join()