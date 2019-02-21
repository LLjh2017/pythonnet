from pymongo import MongoClient

# 创建数据连接
conn = MongoClient('localhost',27017)

# 创建数据库对象
db = conn.stu 

# 创建集合对象
myset = db.class5

# 数据操作
# 插入操作
# myset.insert_many([{'name':'张铁林','king':'乾隆'},
#                    {'name':'张国立','king':'康熙'}])
# myset.insert_one({'name':'任贤齐','role':'令狐冲'})
# myset.insert({'name':'古天乐','role':'杨过'})
# myset.insert([{'name':'李若彤','role':'小龙女'},
#               {'name':'刘亦菲','role':'王语嫣'}])
# myset.save({'name':'胡军','role':'萧峰'})

# 查找操作
# cursor = myset.find({'role':{'$exists':True}},{'_id':0})
# for i in cursor:
#     print(i['name'],'----',i['role'])
# print(cursor.next())
# for i in cursor.limit(3):
#     print(i)
# print(cursor[0]) 
# print(myset.find_one())  
# myset.update_one({'king':{'$exists':True}},{'$set':{
#     'name':'陈小春','king':'韦小宝'}})
myset.update_many({'king':{'$exists':True}},
                  {'$rename':{'king':'role'}})

# 关闭数据库连接
conn.close()