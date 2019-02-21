import os 

filename = "./timg.jpg"
# 获取文件大小
size = os.path.getsize(filename)

# 上半部分
def copy1():
    f = open(filename,'rb')
    n = size // 2
    fw = open('1.jpg','wb')
    while True:
        if n < 1024:
            data = f.read(n)
            fw.write(data)
            break
        data = f.read(1024)
        fw.write(data)
        n -= 1024 
    f.close()
    fw.close()

# 下半部分
def copy2():
    f = open(filename,'rb')
    fw = open('2.jpg','wb')
    # 以开始为基准向后偏移
    f.seek(size//2,0)
    while True:
        data = f.read(1024)
        if not data:
            break
        fw.write(data)
    f.close()
    fw.close()

pid = os.fork()
if pid < 0:
    print("Create process failed")
elif pid == 0:
    copy1()
else:
    copy2()