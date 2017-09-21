# encoding=utf8

def someFunction():
    a = 1
    b = 1
    # yield 搭配next做流程控制
    # 兩個yield 只能有兩個next
    yield a
    a += b
    yield a


fp1 = someFunction()
print 'first', fp1.next()
print 'second', fp1.next()

# print '???', fp1.next()

print 'any', someFunction().next()
print 'any', someFunction().next()
print 'any', someFunction().next()
print 'any', someFunction().next()