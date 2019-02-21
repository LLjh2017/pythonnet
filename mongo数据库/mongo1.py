from pymongo import MongoClient

conn = MongoClient('localhost',27017)
db = conn.stu 
myset = db.class0

# 创建索引
index_name = myset.create_index('name')
print(index_name)
conn.close()