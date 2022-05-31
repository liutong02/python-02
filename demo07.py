#函数

def add(x,y):
    z = x + y
    return z
print(add(6,7))

def add1(x,y):
    return x + y
print(add('ll','uu'))

#打印菱形
str1 = '*'
a = [1,3,5,7,5,3,1]
for n in a:
    print((str1 * n).center(7))

#关键字参数
def student_lesson(grade,subject = '数学'):
    z = "{}年级上{}课".format(grade,subject)
    return z


print(student_lesson(grade=2,subject='语文'))
print(student_lesson(3))

#可变化参数
def uud(x,y,*args):
    z = x+y+sum(args)
    return z
print(uud(6,7,77,9,0)) #args使用元组方式调用
print(uud(6,7,*[2,34,7])) #*[]args使用列表方式调用
#可变化参数字典形式
def show_info(**kwargs):
    print(kwargs)
    return None
print(show_info(a='一',b='二'))

#实例: 创建学生类，要求有属性：姓名和年级 ; 方法有：学习的方法，打印学生的上课情况

class Student():
    name = ""
    grade = ""
    def __init__(self):
        self.name='张三'
        self.grade = '5'

    def study(self):
        print("{}年级的学生{}正在学习".format(self.name,self.grade))
    def eat(self):
        print("{}是{}年级，正在吃饭".format(self.name,self.grade))
s1 = Student()
print(s1)
print(s1.eat())
s1.name = '张三'
s1.grade = '三'
print(s1.study())

#父类-人类
class People():
    def eat(self,ids):
        print("{}吃饭".format(ids))

class Students(People):

    pass
    def study(self):
        print("学习")

class Teacher(People):

    pass
    def teach(self):
         print("教书")
s = Students()
s.eat("学生")
t = Teacher()
t.eat("老师")
## 需求-迭代1：登录功能
# 1. 定义两条用户数据 ，要求用户数据的属性包括用户角色，用户账号，密码，部门
# 2. 要求返回的格式是字典形式 ，包含两个字段，code和message ,code为0代表成功，为1代表失败 ；message给出相应的提示 ，格式如 ：{'code':0,'message':'登录成功'}
# 3. 用户通过控制台输入用户名和密码，判断用户名和密码是否和定义数据中的用户名密码相匹配，若匹配返回成功登录消息体，并把用户列表也追加到返回结果中,{'code':0,'message':'登录成功',user_list:[]}
# 4. 若用户名输入为空或密码输入为空，都给出对应的提示，如用户名不能为空
# 5. 若用户名或密码不匹配，都给出登录失败，请检查您的用户名或密码是否填写正确。提示
class user():

