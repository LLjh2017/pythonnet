from socket import * 

# 接受request 发送response
def handleClient(connfd):
    request=connfd.recv(4096)
    # 将request按行切割
    request_lines=request.splitlines()
    # 暂时不做过多解析
    for line in request_lines:
        print(line)
    try:
        f=open('index.html')
    except IOError:
        response="HTTP/1.1 404 Not Found\r\n"
        response+='\r\n' # 空行
        response+='===Sorry not found==='
    else:
        response="HTTP/1.1 200 OK\r\n"
        response+='\r\n' # 空行
        response+=f.read()
    finally:
        # 无论什么结果都发送给浏览器
        connfd.send(response.encode())

# 创建套接字
def main():
    sockfd=socket()
    sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    sockfd.bind(('0.0.0.0',8800))
    sockfd.listen(3)
    print('Listen to the port 8800')
    while True:
        connfd,addr=sockfd.accept()
        # 处理请求
        handleClient(connfd)
        connfd.close()
if __name__=="__main__":
    main()