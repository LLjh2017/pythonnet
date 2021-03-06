import pymysql
import re 

f = open('dict.txt')
db = pymysql.connect('localhost','root','123456','dict')
cursor = db.cursor()
for line in f:
    try:
        pattern = r'([-a-zA-Z]+)\s+(.+)'
        obj = re.match(pattern,line)
        word = obj.group(1)
        interpret = obj.group(2)
    except:
        continue
    sql = "insert into words (word,interpret) values ('%s','%s')"%(word,interpret)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
f.close()