from socket import *

# 创建套接字
s=socket(AF_INET,SOCK_STREAM)
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',9000))
s.listen(3)
c,addr=s.accept()
print('Connect from',addr) # 客户端地址

# 接收文件
f=open('recv.jpg','wb')
while True:
    data=c.recv(1024)
    if not data:
        break
    f.write(data)

f.close()
c.close()
s.close()