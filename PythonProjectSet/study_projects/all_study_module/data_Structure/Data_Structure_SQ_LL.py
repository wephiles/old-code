'''
Created on 2021-1-21

@author: 20866
'''
# dic = {1:3,3:2}
# 
# if "a" in dic:
#     print('okk') 
# else:
#     print('no')
# 
# if 2 in dic:
#     print('okk') 
# else:
#     print('nonono')
# from pip._vendor.requests.api import head
# from aifc import data



### 此处得出结论：字典的操作是对键进行操作的，判断也是根据键判断的，和值没有关系（有待商榷）

# D = dict.fromkeys('spam')
# C = dict.fromkeys( 'buweishi', 0)
# print(D,C)

# K = {'a':1,'b':2,'c':3}
# # for i in K.values():print(i)
# # for i in K.keys():print(i)
# 
# for key in K:print(key)
# print('-------------------------------------------------')
# for value in K:print(value)

# D = {'a':1,'b':2,'c':3,'d':4}
# print(D)
# del D['a']
# print(D)

# T = (10)
# print(T)
# T1 = (10,)
# print(T1)
# print('你好 我是卜伟仕')

### 277页
### file:///F:/python/python%E8%B5%84%E6%96%99/Python%E5%AD%A6%E4%B9%A0%E6%89%8B%E5%86%8C(%E7%AC%AC4%E7%89%88).pdf

##############################################################  Data structure - Python ##############################################################
##############################################################    数据结构 — Python     ##############################################################



### 线性表：Linear_List
### 顺序表：Sequential_List
### 单链表：Single_LinkList

### 一、顺序表

# from pickle import FALSE
# from mysqlx.protobuf.mysqlx_crud_pb2 import NONE

class SqList:
    def __init__(self): ##默认构造函数
        self.First_Add_of_List = 0
        self.MaxSize = 0
        self.True_Size = 0


    def __del__(self):  ##析构函数
        print('析构函数调用！')


    def InitList(self): ##构造一个空的顺序表
        self.SQL = []


    def CreatList(self,L): ##创建一个顺序表
        self.SQL = L
        self.True_Size = len(L)


    def DestroyList(self):  ###销毁顺序表
        del self.SQL
        print('顺序表正在被销毁！')


    def ClearList(self): ###  将顺序表重置为空表
        del self.SQL[0:len(self.SQL)]


    def ListEmpty(self): ###判断顺序表是不是非空
        if self.True_Size == 0 :
            return True
        return False


    def ListLength(self):  ###返回顺序表的元素个数
        return len(self.SQL)


    def GetElem(self,i): ###用e返回顺序表中第i个元素的值（是第几个元素，不是偏移。）
        if i >0 and i<=len(self.SQL):
            e = self.SQL[i-1]
            return e
        return False


    def LocateElem(self,e):###返顺序表中第一个与e相等的元素的位置（不是偏移），如果没有，则返回0
        for i in range(0,len(self.SQL)):
            if self.SQL[i] == e:
                return i+1
        return 0


    def PriorElem(self,cur):  ###如果num是顺序表的数据元素并且不是第一个，那么返回他的前驱
        pos = self.SQL.index(cur)
        if cur in self.SQL and pos != 0 :
            return self.SQL[pos - 1]
        return None


    def NextElem(self,cur): ###如果num是顺序表的数据元素并且不是最后一个，那么返回他的前驱
        pos = self.SQL.index(cur)
        if cur in self.SQL and cur != self.SQL[-1]:
            return self.SQL[pos + 1]
        return None


    def ListInsert(self,i,e): ###在顺序表中第i个元素位置之前插入新的元素，线性表长度加一
        if i < 1 or i > len(self.SQL) + 1:
            return False
        elif i == len(self.SQL) + 1:
            self.True_Size += 1
            self.SQL.append(e)
        else:
            self.True_Size += 1
            j = len(self.SQL)
            self.SQL.append(0)
            while j >= i:
                self.SQL[j] = self.SQL[j-1]
                j -= 1
            self.SQL[i - 1] = e


    def ListDelete(self,i): #### 删除顺序表第i个元素，长度加一
        if i < 1 or i > len(self.SQL):
            return False
        else:
            del self.SQL[i - 1]
            self.True_Size -= 1


    def DisplayList(self): ###打印顺序表
        print(self.SQL)
        print('顺序表的长度为：',end = '')
        print(len(self.SQL))


    def union(self,A,B):
        for i in B.SQL :
            if i not in A.SQL:
                A.SQL.append(i)



###测试:   
print('************************************  程序测试  *************************************')    
X = SqList()
X.InitList()
if X.ListEmpty():
    print('顺序表是空的！')
else:
    print('顺序表非空！')
    
print('-------------------------------------------------------------------------------------')  
L = [2,15,6,8,9,3,10,12,5]
X.CreatList(L)
if X.ListEmpty():
    print('顺序表是空的！')
else:
    print('顺序表非空！')
    X.DisplayList()
print('顺序表长度：',end='')
print(X.ListLength())
    
print('-------------------------------------------------------------------------------------')   
i = int(input('请输入您想查找的偏移i：'))
print('第'  + str(i) + '个对象为：' ,end='')
print(X.GetElem(i))
 
print('-------------------------------------------------------------------------------------')  
e = int(input('请输入您想查找的对象的值e：'))
if X.LocateElem(e) == 0:
    print('没有这个元素哦！')
else:
    print('您所要查找的元素是第',end='')
    print(X.LocateElem(e),end='')
    print('个元素！')
             
print('-------------------------------------------------------------------------------------')            
cur = int(input('请输入您想要查找的元素的后继元素cur：'))              
print('您所输入元素的前驱是：',end = '')               
print(X.PriorElem(cur))                
                 
cur = int(input('请输入您想要查找的元素的前驱元素cur：'))              
print('您所输入元素的后继是：',end = '')                
print(X.NextElem(cur))
 
# print(X.SQL)
# print(len(X.SQL))

print('-------------------------------------------------------------------------------------') 
i = int(input('请输入您想插入的位置：'))              
e = int(input('请输入您想插入的元素：'))               
                
X.ListInsert(i,e)      
X.DisplayList()          
                                         
i = int(input('请输入您想删除的位置：'))                
X.ListDelete(i)      
X.DisplayList()                
                
print('-------------------------------------------------------------------------------------')              
if X.ListEmpty():
    print('顺序表是空的！')
else:
    X.ClearList()
print(X.SQL)

X.DestroyList()
try:     
    print(X.SQL) 
except (IndentationError,AttributeError): 
    print('销毁成功！')   
else:
    print('销毁失败！')       

L1 = [2, 4, 6, 8, 0, 9]
L2 = [3, 6, 9, 1, 5, 7]
 
A = SqList()
A.InitList()
A.CreatList(L1)
 
B = SqList()
B.InitList()
B.CreatList(L2)
# 
# def union(A,B): ###将所有在顺序表B中但不在A中的元素插入到A中
#     for i in B.SQL:
#         if i not in A.SQL :
#             A.SQL.append(i)
SqList().union(A,B)   ###特别要注意这一点，在类名后面要加()
print(A.SQL)    
    

    
    
"""
### 二、单链表   
class LinkNode(object): ### 结点类
    def __init__(self):
        self.Data = 0
        self.Next = None
    
class SingleLinkList(object): 
    def __init__(self): ### 默认构造函数
        self.Head = LinkNode()
        self.Len = 0 
    def __del__(self):  ### 析构函数
        print('析构函数调用！！！')  
    def Init_LL(self): ### 初始化单链表
        self.Len = 0
        self.Head.Data = 0
        self.Head.Next = None
    def IsEmpty(self):###判断单链表是不是空的
        if self.Len <= 0 :
            return True
        return False 
    def LL_Length(self): ###求单链表长度
        return self.Len
    def Clear_LL(self): ### 清空单链表 
        point = self.Head
        for i in range(0,self.Len) :
            point = point.Next
            del point.Data
        self.Head.Next = None
        
    def Distroy_LL(self): ### 销毁单链表
        self.Clear_LL()
        del self.Head
    def AddElem(self,e):  ### 在单链表中添加结点(头插法)
        node = LinkNode()
        node.Next = self.Head.Next
        self.Head.Next = node
        node.Data = e
        self.Len += 1
    def AppendElem(self,e): ### 在单链表中添加结点(尾插法)
        point = self.Head
        while point.Next != None :
            point = point.Next
        node = LinkNode()
        point.Next = node
        node.Next = None 
        node.Data = e 
        self.Len += 1
    def Insert(self,i,e): ### 在单链表中添加结点(中插法，在第i个元素之前插入元素)
        if i < 1 or i > self.Len + 1 :
            return False
        elif i == 1 :
            self.AddElem(e)
        elif i == self.Len + 1 :
            self.AppendElem(e)
        else:
            node = LinkNode()
            point = self.Head 
            for i in range(1,i):
                point = point.Next
            node.Next = point.Next
            point.Next = node
            node.Data = e
            self.Len += 1
    def GetElem(self,i):  ### 返回单链表中序号为i的数据元素 (i的合法值为1≤i≤len)
        if i<1 or i>self.Len :
            return False 
        else:
            point = self.Head
            for i in range(1,i+1):
                point = point.Next
            if point != None: 
                return point.Data 
    def Creat_LL(self,L): ### 通过传入一个列表来创建一个单链表
        for e in L:
            self.AppendElem(e)
    def LocateElem(self,e): ### 从第一个位置起查找与e匹配的数据元素，若存在则返回该数据元素的位置
        if self.IsEmpty():
            return False 
        point = self.Head
        i = 0
        while point.Next != None:
            point = point.Next
            i += 1
            if point.Data == e :
                return i
        if point.Next == None:
            return 0 
    def LocatePrior(self,e): ### 从第一个位置起查找与e匹配的数据元素，若存在且不是第一个则返回该数据元素前驱的位置
        if self.IsEmpty():
            return False 
        point = self.Head
        i = 0
        while point.Next != None:
            point = point.Next
            i += 1
            if point.Data == e and i != 1:###
                return i-1
#         if point.Next == None:
        if i == 1:
            return None
    def LocateNext(self,e):  ## 从第一个位置起查找与e匹配的数据元素，若存在且不是最后一个则返回该数据元素后继的位置
        if self.IsEmpty():
            return False 
        point = self.Head
        i = 0 
        while point.Next != None:
            point = point.Next
            i += 1
            if point.Data == e and point.Next != None:
                return i + 1
        if point.Next == None :
            return None
    def DeleteElem(self,i): ###在单链表中删除第i个数据元素并用数据变量e返回其值（i的合法值为1≤i≤Len）
        if i<1 or i> self.Len :
            return False
        point = self.Head
        for j in range(1,i)  :
            point = point.Next
        q = point.Next
        point.Next = q.Next
        q.Next = None
        del q.Data
        self.Len -= 1
    def Traverse_LL(self): ### 遍历单链表
        if self.IsEmpty():
            return False
        point = self.Head
        print('Header->',end = '')
        while point.Next != None:
            point = point.Next
            print(point.Data,end = '->')
        print('None')
    def CopyFrom(self,L): ###拷贝函数
        self.Clear_LL()
        self.Head = L.Head
###测试:   
print('************************************  程序测试  *************************************')
X =  SingleLinkList()
X.Init_LL()  
if X.IsEmpty():
    print('单链表是空的！')
else:
    print('单链表不是空的！')  
L = [2,5,4,1,0,6,9,8] 
X.Creat_LL(L)
X.Traverse_LL()
print(X.LL_Length())
if X.IsEmpty():
    print('单链表是空的！')
else:
    print('单链表不是空的！')  
  
print('单链表的长度为：',end = '')
print(X.LL_Length())    
                
print('-------------------------------------------------------------------------------------')  
       
print('头插法添加元素:' )
e1 = int(input('请输入您想插入的元素e1:'))
X.AddElem(e1)
X.Traverse_LL()
 
print('尾插法添加元素：' )
e2 = int(input('请输入您想插入的元素e2:'))
X.AppendElem(e2)
X.Traverse_LL()
 
print('中插法添加元素：' )
e3 = int(input('请输入您想插入的元素e3:'))
i = int(input('请输入您想插入的元素的位置i:'))
X.Insert(i, e3)
X.Traverse_LL()
  
print('-------------------------------------------------------------------------------------') 
e4 = int(input('请输入您想要查找的元素e4:')) 
if X.LocateElem(e4) == 0:
    print('未找到该元素！')
elif X.LocateElem(e4) == False :
    print('单链表是空的！')
else:
    print(X.LocateElem(e4))  
  
e5 = int(input("请输入您想查找的元素的后继元素e5，我们将为您查找其前驱元素！"))
if X.LocatePrior(e5) == False :
    print('单链表是空的！')
print('您所输入的元素的前驱的位置为：',end = '')
print(X.LocatePrior(e5))
  
      
e6 = int(input("请输入您想查找的元素的前驱元素e6，我们将为您查找其后继元素！"))
if X.LocateNext(e6) == False :
    print('单链表是空的！')
print('您所输入的元素的后继的位置为：',end = '')
print(X.LocateNext(e6))
 
print('-------------------------------------------------------------------------------------')
i = int(input('请输入您想删除的元素的位置i:'))
X.DeleteElem(i)
X.Traverse_LL()
print(X.LL_Length())

Y =  SingleLinkList()
Y.Init_LL()  
L = [1,2,3,4,5,6] 
Y.Creat_LL(L)

# Y.CopyFrom(X)   
# Y.Traverse_LL()  
          
X.CopyFrom(Y)
X.Traverse_LL()



#### 43页  

# L = []
# L.append(1)
# L.append(2)
# L.append(3)
# 
# print(L.pop())
# print(L)

# L = [0,1,2,3,4]
# # for i in range(0,len(L)):
# #     del L[i]
# print(L)
# print(range(0,len(L)))
# for i in range(0,len(L)):
#     print(i)
               




