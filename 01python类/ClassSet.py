import datetime

class Rational_0:
    """定义有理数类"""

    def __init__(self, num, den=1):
        self.num = num  # 分子
        self.den = den  # 分母

    def plus(self, another):
        den = self.den * another.den
        num = self.den * another.num + self.num * another.den
        return Rational_0(num, den)

    def print(self):
        print(self.num, '/', self.den)


class Rational():
    """有理数类进阶"""
    counter = 0

    def __init__(self, num, den=1):
        if not isinstance(num, int) or not isinstance(den, int):
            raise TypeError
        if den == 0:
            raise ZeroDivisionError

        sign = 1
        if num < 0:
            sign, num = -sign, -num
        if den < 0:
            sign, den = -sign, -den

        g = Rational._gcd(num, den)  # 求最大公约数

        self._num = sign * (num // g)
        self._den = (den // g)

        Rational.counter += 1

    @classmethod
    def count(cls):
        return Rational.counter

    @staticmethod  # 为这个类服务，但是实际上和这个类无关的方法
    def _gcd(m, n):  # 求最大公约数的算法
        if n == 0:
            n, m = m, n
        while m != 0:
            m, n = n % m, m
        return n

    # def my_test(self):
    #     return Rational.num(self)

    def num(self):
        return self._num

    def den(self):
        return self._den

    def __add__(self, other):  # other 相当于处在类外，按照约定不要直接访问其属性，而是通过接口
        """定义加法运算的例子，其他运算类似"""
        if isinstance(other, Rational):
            num = self._num * other.den() + self._den * other.num()
            den = self._den * other.den()
            return Rational(num, den)
        else:
            raise TypeError

    def __gt__(self, other):
        """定义比较大小的例子，其他关系可以类似定义"""
        return self._num * other.den() > self._den * other.num()

    def __str__(self):
        return str(self._num) + '/' + str(self._den)


class Number(Rational):
    def __init__(self, num=1):
        # super(Number, self).__init__(num)  # 和下一句等价，区别在于是采用指定的基类还是默认的基类
        # super().__init__(num)
        Rational.__init__(self, num)


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


