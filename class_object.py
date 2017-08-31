# 类
class Person:
    pass  # 空代码使用pass标明

p = Person()
print(p)

class Mike:
    def say_hi(self):
        print('Hello')

m = Mike()
m.say_hi()

# __init__ 方法
# __init__ 会在类的对象诶实例化时立即运行
class Jane:
     def __init__(self, name):
         self.name = name
         
     def say_hi(self):
         print('Hello, my name is', self.name)


J = Jane('Zhou')
J.say_hi()


# 类变量与对象对变量
class Robot:
    
    populations = 0  # 类变量

    def __init__(self, name):
        self.name = name  # name 为对象变量
        print('Initializing {}'.format(self.name))
        Robot.populations += 1

    def die(self):
        print('{} is being destroyed!'.format(self.name))
        Robot.populations -= 1
        if Robot.populations == 0:
            print('{} is being the last one.'.format(self.name))
        else:
            print('There are still {:d} robots working'.format(Robot.populations))
            
    def say_hi(self):
        print('Greekings, my master call me {}.'.format(self.name))

    @classmethod  # 类方法
    def how_many(cls):
        print('We have {:d} robots.'.format(cls.populations))


droid1 = Robot('D1')
droid1.say_hi()
Robot.how_many()

droid2 = Robot('D2')
droid1.say_hi()
Robot.how_many()

droid1.die()
droid2.die()
Robot.how_many()

# 继承 inheritance
# SchoolMember类 ： 基类Base Class 或 超类 Superclass
# Teacher类 ： 派生类Derived Class 或 子类 Subclass
class SchoolMember:

    # 学校任何成员的共有信息
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('Initialized SchoolMember : {}'.format(self.name))

    # 打印信息
    def tell(self):
        print('Name : {} Age : {}'.format(self.name, self.age), end = ' ')
        
class Teachers(SchoolMember):

    # 学校中老师的信息
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('Initialized Teacher : {}'.format(self.name))

    # 打印信息
    def tell(self):
        SchoolMember.tell(self)
        print('Salary : {:d}'.format(self.salary))

class Students(SchoolMember):

    # 学校中学生的信息
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('Initialized Stuedent : {}'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Marks : {}'.format(self.marks))


t = Teachers('chris', 40, 5000)
s = Students('zhou', 20, 90)

members = [t, s]
for member in members:
    member.tell()

























































        
   
     
