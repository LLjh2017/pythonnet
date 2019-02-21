import os 
print("************")
a=1

pid=os.fork()

if pid<0:
    print("Create process failed")
elif pid==0:
    print("Child process")
    print("a=%d"%a)
else:
    print("Parent process")