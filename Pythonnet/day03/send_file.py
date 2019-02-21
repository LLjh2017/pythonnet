from socket import *

s=socket()
addr=('127.0.0.1',9000)
s.connect(addr)

# 打开文件
f=open('timg.jpg','rb')
# 发送文件
while True:
    data=f.read(1024)
    if not data:
        break
    s.send(data)
    
f.close()
s.close()