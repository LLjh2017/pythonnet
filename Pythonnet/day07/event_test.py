from threading import Event

# 创建事件对象
e = Event()
e.set() # 设置e

e.wait() # 此时不阻塞

e.clear()
print(e.is_set())  # 判断当前状态
print("*******************")