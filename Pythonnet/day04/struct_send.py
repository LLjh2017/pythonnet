from socket import *
import struct

s=socket()
s.connect(('127.0.0.1',8000))

st=struct.Struct('i5sf')

# 将数据打包发送
data=st.pack(1,b'zhang',1.75)

s.send(data)
s.close()