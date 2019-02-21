from socket import *

s=socket()

# 设置端口可以立即重用
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

# 套接字地址族
print(s.family)
# 套接字类型
print(s.type)
# 获取套接字绑定地址
s.bind(('0.0.0.0',8888))
print(s.getsockname())
# 获取文件描述符
print(s.fileno())

s.listen(3)
c,addr=s.accept()
# 获取连接套接字连接端地址
print(c.getpeername())
# 获取套接字选项值
print(s.getsockopt(SOL_SOCKET,SO_REUSEADDR))

c.recv(1024)
c.close()
s.close()