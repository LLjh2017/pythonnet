import re 
import sys 

def get_address(port):
    f = open('1.txt')
    while True:
        data = ''
        for line in f:
            if line != '\n':
                data += line
            else:
                break
        # 说明已经读到文件结尾
        if not data:
            return 'Not found the port'
        # 匹配出首个单词
        try:
            PORT = re.match(r'\S+',data).group()
        except Exception as e:
            print(e)
            continue
        
        if port == PORT:
            pattern = r'address is (\w{4}\.\w{4}\.\w{4})'
            address = re.search(pattern,data).group(1)
            return address

if __name__ == "__main__":
    port = sys.argv[1]
    print(get_address(port))