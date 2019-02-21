from socket import *
import sys 
import time 

# 将具体功能实现放在类中
class FtpClient(object):
    def __init__(self,sockfd):
        self.sockfd = sockfd

    def do_list(self):
        self.sockfd.send(b'L') # 发送请求
        # 等待回复
        data = self.sockfd.recv(128).decode()
        if data == 'OK':
            data = self.sockfd.recv(4096).decode()
            files = data.split('#')
            for file in files:
                print(file)
            print('文件列表展示完毕\n')
        else:
            # 无法执行操作
            print(data)
    
    def do_quit(self):
        self.sockfd.send(b'Q')
        self.sockfd.close()
        sys.exit('谢谢使用')

    def do_get(self,filename):
        self.sockfd.send(('G '+filename).encode())
        data = self.sockfd.recv(128).decode()
        if data == 'OK':
            fd = open(filename,'wb')
            while True:
                data = self.sockfd.recv(1024)
                # 接收结束标志
                if data == b'##':
                    break 
                fd.write(data)
            fd.close()
            print('%s下载完毕'%filename)
        else:
            print(data)
    
    def do_put(self,filename):
        try:
            fd = open(filename,'rb')
        except:
            print('没有找到文件')
            return
        self.sockfd.send(('P '+filename).encode())  
        data = self.sockfd.recv(128).decode() 
        if data == 'OK':
            while True:
                data = fd.read(1024)
                if not data:
                    time.sleep(0.1)
                    # 发送文件读取完标志
                    self.sockfd.send(b'##')
                    break
                self.sockfd.send(data)
            fd.close()
            print('%s上传完毕'%filename)
        else:
            print(data)


# 网络连接
def main():
    if len(sys.argv) < 3:
        print('argv is error')
        return
    print(type(sys.argv)) # 列表
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    ADDR = (HOST,PORT)

    sockfd = socket()
    try:
        sockfd.connect(ADDR)
    except Exception as e:
        print('连接服务器失败',e)
        return
    
    # 创建对象
    ftp = FtpClient(sockfd)

    while True:
        print('=======命令选项========')
        print('***      list       ***')
        print('***    get file     ***')
        print('***    put file     ***')
        print('***      quit       ***')
        print('=======================\n')

        cmd = input('输入命令>>')
        if cmd.strip() == 'list':
            ftp.do_list()
        elif cmd.strip() == 'quit':
            ftp.do_quit()
        elif cmd[:3] == 'get':
            filename = cmd.split()[-1]
            ftp.do_get(filename)
        elif cmd[:3] == 'put':
            filename = cmd.split()[-1]
            ftp.do_put(filename)
        else:
            print('请输入正确命令')


if __name__ == '__main__':
    main()