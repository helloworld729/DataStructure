import datetime
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


class Person():
    person_count = 0

    def __init__(self, name, sex, birthday, id_num):
        if not (isinstance(name, str) and sex in ('男', '女')):
            raise PersonValueError
        self._name = name
        self._sex = sex
        try:
            self._birthday = datetime.date(*birthday)
        except:
            raise PersonValueError("wrong date: ", birthday)
        self._id_num = id_num
        Person.person_count += 1

    @classmethod
    def get_personCount(cls):
        return Person.person_count

    def name(self): return self._name

    def sex(self): return self._sex

    def birthday(self): return self._birthday

    def age(self): return datetime.date.today().year - self._birthday.year

    def __lt__(self, other):
        if not isinstance(other, Person):
            raise PersonTypeError
        return self._id_num < other._id_num

    def __str__(self):
        return " {0}  {1}  {2}  {3}".format(self._name, self._sex, self._birthday, self.age())


class Student(Person):
    student_count = 0

    @classmethod
    def _id_num(cls):
        Student.student_count += 1
        year = datetime.date.today().year
        return "{:04}{:05}".format(year, Student.student_count)

    def __init__(self, name, sex, birthday, department):
        self.id_num = Student._id_num()
        super(Student, self).__init__(name, sex, birthday, self.id_num)  # self的位置必须是某个类的实例
        # super().__init__(name,sex, birthday, Student._id_num())  # 默认继承
        # Person.__init__(self, name, sex, birthday, Student._id_num())  # 指定基类
        self._depardent = department
        self._enrolldate = datetime.date.today()
        self._course = {}

    def set_course(self, cname):
        self._course[cname] = None

    def set_score(self, cname, cscore):
        if cname in self._course:
            self._course[cname] = cscore
        else:
            raise PersonValueError

    def __str__(self):
        import json
        base_info = Person.__str__(self)
        more = self.id_num + ' ' + str(self._course)
        return base_info + ' ' + more


p1 = Person(name='Knight', sex='男', birthday=[1995, 4, 28], id_num='184513')
s1 = Student(name='骑士', sex='男', birthday=[1995, 5, 27], department='Computer_Science')
s1.set_course('语文')
s1.set_score('语文', cscore=99)
print(s1)