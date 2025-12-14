'''
Created on 2020-9-1

@author: 20866
'''

# #Python面向对象
# class Worker:
#     def __init__(self):#默认构造函数
#         self.name = 'buweishi'
#         self.pay = 1000
#     def Pay(self):
#         print(self.pay * 30)
#     def DisPlay(self):
#         print(self.name + ' 应得:' + str(self.pay * 30) + '元 ' + '2020.12.29 ' )
#
# x = Worker()
# x.Pay()
# x.DisPlay()
# class Student:
#     name = ''
#     num = ''
#     __age = 0
#     __high = 0
#     __weight = 0
#     score = 0
#     def __init__(self):#默认构造函数，初始化
#         self.name = 'XXX'
#         self.num = '1930090000'
#         self.__age = 0
#         self.__high = 0
#         self.__weight = 0
#         self.score = 0
#     def Set(self):
#         self.name = input("请输入学生姓名：\n")
#         self.num = input("请输入学生学号：\n")
#         self.score = input("请输入学生成绩：\n")
#     def Get(self):
#         print("{0}，学号： {1} 成绩：{2} ." .format(self.name,self.num,self.score))
#     def PeText(self,n,num,age,high,weight,s):
#         self.name = n
#         self.num = num
#         self.__age = age
#         self.__high = high
#         self.__weight = weight
#         self.score = s
#     def Study(self):
#         for x in [1,2,3,4,5,6,7,8,9,10]:
#             self.score += 0.5
#         if self.score>=100:
#             self.score = 100
# X = Student()#实例
# X.Get()
#
# X.Set()
# X.Get()
#
# X.PeText('BuWeishi', '1930090102', 18, 180, 60, 98)
# X.Get()
#
# X.Study()
# X.Get()

# #类的继承:
# class People:
#     Name = ''
#     ID_Num = ''
#     __Age = 0
#     __High = 0
#     __Weight = 0
#     Sex = ''
#     Home_Position = ''
#     Parent_Father = ''
#     Parent_Mother = ''
#     Friend_Best = ''
#     def __init__(self):
#         self.Name = 'XXX'
#         self.ID_Num = 'XXXXXXXXXXXXXXXXXX'
#         self.__Age = 0
#         self.__High = 0
#         self.__Weight = 0
#         self.Sex = 'X'
#         self.Home_Position = 'XXX'
#         self.Parent_Father = 'XXX'
#         self.Parent_Mother = 'XXX'
#         self.Friend_Best = 'XXX'
#     def Set(self):
#         self.Name = input("请输入姓名：\n")
#         self.ID_Num = input("请输入身份证号：\n")
#         self.Sex = input("请输入性别：\n")
#         self.Home_Position = input("请输入家庭住址：\n")
#         self.Parent_Father = input("请输入父亲姓名：\n")
#         self.Parent_Mother = input("请输入母亲姓名：\n")
#         self.Friend_Best = input("请输入最好的朋友的姓名：\n")
#         self.__High = input("请输入身高： \n")
#         self.__Weight = input("请输入体重： \n")
#         self.__Age = input("请输入年龄： \n")
#     def Get(self):
#         print("""姓名:{0}
#         性别:{1}
#         身份证号:{2}
#         家庭住址:{3}
#         父亲姓名:{4}
#         母亲姓名:{5}
#         最好的朋友:{6}
#          """.format(self.Name,self.Sex,self.ID_Num,self.Home_Position,self.Parent_Father,self.Parent_Mother,self.Friend_Best))
#     def Speak(self):
#         print("hello! i am {0} i come from {1} , i am {2} years old ,my father is {3} ,my mother is {4} !".format(self.Name,self.Home_Position,self.__Age,self.Parent_Father,self.Parent_Mother))
#     def Do_In_Oneday(self):
#         import random
#         x = random.randint(0,23)
#         if x>7 & x<23:
#             print("Now is {0} o'clock".format(x))
#             print("work/study,very important!!! \n")
#         else :
#             print("Now is {0} o'clock".format(x))
#             print("Sleep!very important !!! \n")
#
# X = People()
# X.Get()
# print('-------------------------------------------')
#
# X.Set()
# X.Get()
# print('-------------------------------------------')
#
# X.Speak()
# X.Do_In_Oneday()
#
#
# #单继承
# class Student(People):
#     Num = ''
#     Score = 0
#     __Grade = ''
#     def __init__(self):
#         People.__init__(self)#调用父类的构造函数
#         self.Num = 'XXXXXXXXXX'
#         self.Score = 99
#         self.__Grade = 'XX'
#     def Speak(self):
# #         People.Speak(self)
#         print("hello! i am {0} i come from {1} , my father is {2} ,my mother is {3} ! i am a student! my grade is :{4}".format(self.Name,self.Home_Position,self.Parent_Father,self.Parent_Mother,self.__Grade))
# Y = Student()
# Y.Set()
# Y.Get()
# Y.Speak()
#
# print("总结：父类的私有数据，只能在本类中引用，而不能在子类中引用")
#
# #多继承
# class Speaker:
#     name = ''
#     topic = ''
#     def __init__(self):
#         self.name = "XXX"
#         self.topic = "XXXXXX"
#     def Speak(self):
#         print("i am %s,my topic is :%s"%(self.name,self.topic))
#
# class StudentSpeaker(Student,Speaker):
#     clothes = ''
#     def __init__(self):
#         Student.__init__(self)
#         Speaker.__init__(self)
#         self.clothes = "xifu"
#
# Z =  StudentSpeaker()
# Z.Speak()

#运算符重载     
# """Python同样支持运算符重载，我们可以对类的专有方法进行重载"""  
# class Vector:#向量
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#     def __str__(self):  
#         return 'Vector(%d,%d)'%(self.a,self.b)  
#     def __add__(self,other):
#         return Vector(self.a+other.a,self.b+other.b)
# V1 = Vector(1,2)
# V2 = Vector(5,6)
# V = V1.__add__(V2) 
# print(V)
# 
# print(V1 + V2)
