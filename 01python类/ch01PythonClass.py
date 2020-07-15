from ClassSet import *

a = Rational(3, 4)
b = Rational(4, 5)
c = Number(num=1)


import traceback
# print(a + b)
print(a > b)
print(Rational._gcd(5, 10))
print('创建了：{} 个对象。'.format(Rational.count()))
print(c.den())


try:
    # v
    print('hello')
except Exception as e:
    # traceback.print_exc()
    print(e)