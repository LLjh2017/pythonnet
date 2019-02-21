import re 

pattern1 = r"\w+:\d+"
pattern2 = r"(\w+):(\d+)"
s = "zhang:1994 li:1993"

# re直接调用 
l1 = re.findall(pattern1,s)
l2 = re.findall(pattern2,s)
print(l1)  # ['zhang:1994', 'li:1993']
print(l2)  # [('zhang', '1994'), ('li', '1993')]

# compile对象调用
regex = re.compile(pattern1)
l3 = regex.findall(s)
print(l3)   # ['zhang:1994', 'li:1993']