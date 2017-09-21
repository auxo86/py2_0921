# encoding=utf8

def someFunction():
    x = 1007
    y = 70
    z = 50
    y = yield x
    yield z + y


fp1 = someFunction()
print fp1.next()
# 從剛剛中斷的地方插入77指派給y
print fp1.send(77)