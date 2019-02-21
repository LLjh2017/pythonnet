from socket import *

# 创建tcp套接字
s=socket()
s.bind(('0.0.0.0',8000))
s.listen(3)
while True:
    c,addr=s.accept()
    print('Connect from',addr)
    data=c.recv(4096)
    print("************************")
    print(data)
    print("************************")
    c.close()
s.close()