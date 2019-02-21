from socket import *

# 确保两端使用同一个套接字文件
sock_file='./sock'
# 创建本地套接字
sockfd=socket(AF_UNIX,SOCK_STREAM)
# 连接套接字文件
sockfd.connect(sock_file)
while True:
    msg=input(">>")
    if not msg:
        break
    sockfd.send(msg.encode())
sockfd.close()