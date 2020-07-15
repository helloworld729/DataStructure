import datetime
from ClassSet import *
"""测试代码
a = [2018, 5, 23]
b = {'year': 2018, 'month': 5, 'day': 10}

datetime.date(*a) == datetime.date(2018, 5, 23)
datetime.date(**b)== datetime.date(year=2018, month=5, day=10)

print(datetime.date(*a))  # 本身date的参数应该为3个int变量
print(datetime.date(**b))  # 本身date的参数应该为3个int变量
print(type(datetime.date.today().year), datetime.date.today().year)  # int 形式返回
print('2' > '3')  # 原来字符串也可以比较大小
"""


class PersonTypeError(TypeError):
    pass


class PersonValueError(ValueError):
    pass


p1 = Person(name='Knight', sex='男', birthday=[1995, 4, 28], id_num='184513')
s1 = Student(name='骑士', sex='男', birthday=[1995, 5, 27], department='Computer_Science')
s1.set_course('语文')
s1.set_score('语文', cscore=99)
print(s1)