import gevent

def foo():
    print(12)
    gevent.sleep(2)
    print(34)

def bar():
    print(56)
    gevent.sleep(3)
    print(78)

f = gevent.spawn(foo)
g = gevent.spawn(bar)
gevent.joinall([f,g])