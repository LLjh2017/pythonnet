from socketserver import * 

# 创建服务器类
class Server(ThreadingMixIn,UDPServer):
    pass 

class Handler(DatagramRequestHandler):
    def handle(self):
        while True:
            data = self.rfile.readline()
            if not data:
                break
            print(data.decode())
            self.wfile.write(b'Receive')

if __name__ == "__main__":
    server = Server(('0.0.0.0',8888),Handler)
    server.serve_forever()