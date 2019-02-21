from socket import * 
import sys

if len(sys.argv)<3:
    print('''
    argv is error!
    run as python3 udp_client.py 127.0.0.1 8888''')
    raise
# 从命令行接收服务器地址
HOST=sys.argv[1]
PORT=int(sys.argv[2])
ADDR=(HOST,PORT)

# 创建数据报套接字
sockfd=socket(AF_INET,SOCK_DGRAM)

# 消息发收
while True:
    data=input("Msg>>")
    if not data:
        break
    sockfd.sendto(data.encode(),ADDR)
    msg,addr=sockfd.recvfrom(1024)
    print("从服务器收到:",msg.decode())

sockfd.close()
