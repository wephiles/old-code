'''
Created on 2021-1-28

@author: 20866
'''
##############################################################  Data structure - Python ##############################################################
##############################################################    数据结构 — Python     ##############################################################
### 循环链表 :Circular_Linked_List 
### 双向链表 :Double_Linked_List
class Stack():
    def __init__(self):
        self.Top = None
        self.Bottom = None
        self.Len = 0
    def __del__(self):
        print("析构函数调用！")
    def Initialize(self):  ###初始化栈
        self.Stack_List = []
        self.Len = 0
        self.Top = None
        self.Bottom = None
    def Create_Stack(self,L):
        for i in L:
            self.Stack_List.append(i)
            self.Len += 1
        self.Top = self.Stack_List[self.Len - 1]
        self.Bottom = self.Stack_List[0]
    def Is_Empty(self):
        if self.Len == 0:
            return True
        return False
    def Push_Stack(self,e): ###一个元素入栈
        self.Stack_List.append(e)
        self.Len += 1
        self.Top = self.Stack_List[self.Len - 1]
    def Pop_Stack(self):
        if self.Is_Empty() == False :
            self.Stack_List.pop()
            self.Len -= 1
            if self.Is_Empty() == True:
                self.Top = None
                self.Bottom = None
            else:
                self.Bottom = self.Stack_List[0]
                self.Top = self.Stack_List[self.Len - 1]
        else:
            print('栈是空的，请停止出栈操作！')
            return False
    def Traverse_Stack(self): ### 遍历
        if self.Is_Empty() != True :
            print(self.Stack_List)
            return True
        return False
    def Get_Top(self):
        return self.Top
    def Get_Bottom(self):
        return self.Bottom
    def Get_Length(self):
        return self.Len
    def Clear_Stack(self):
        del self.Stack_List[0:len(self.Stack_List)]
        self.Len = 0
        self.Top = None
        self.Bottom = None
    def Distroy_Stack(self):
        del self.Stack_List
    def Conversion_ten_to_two(self,e):
        if self.Is_Empty() != True :
            self.Clear_Stack()
        if e == 0:
            return False
        if type(e) == int:
            while e != 0 :
                n = e % 2
                self.Push_Stack(n)
                e = e // 2
            print('0b',end = '')
            for i in range(0,self.Len) :
                print(self.Stack_List.pop(),end = '')
            print()
        if type(e) == float:
            e = str(e)
            for i in range(-1,-len(e),-1):
                if e[i] == '.':
                    num = abs(i+1)  ## 求出小数点的位数 num
                    break
            e = float(e)
            integer = e*(10**num) // (10**num)
            decimal = e - integer
            integer = int(integer)
            if integer == 0 and decimal != 0:
                for i in range(0,4): ### 保留四位小数
                    result = 2 * decimal ### 乘2
                    result1 = int(result) ### 取整入栈
                    self.Push_Stack(result1)
                    decimal = result - result1
                    if decimal == 0 :
                        result = int(result) ###注意：添加此条语句的原因是：result = 2 * decimal 是float类型的，
                        ###入栈的如果是result不转换类型的话那么就会以float显示，就会出现输出格式错误的情况
                        self.Push_Stack(result)
                        break
                print('0b',end = '')
                print('0.',end = '')
                for i in self.Stack_List :
                    print(i,end = '')
                print()
            elif integer != 0 and decimal != 0:
                while integer != 0:
                    p = integer % 2
                    self.Push_Stack(p)
                    integer = integer // 2
                print('0b',end = '')
                for i in range(0,self.Len):
                    print(self.Stack_List.pop(),end = '')
                self.Clear_Stack() ## 要清空栈，否则会出现输出错误！
                print('.',end='') 
                for i in range(0,4): ### 保留四位小数
                    result = 2 * decimal ### 乘2
                    if result == 1 :
                        result = int(result) 
                        self.Push_Stack(result)
                        break
                    result1 = int(result) ### 取整入栈
                    self.Push_Stack(result1)
                    decimal = result - result1 
                for i in self.Stack_List :
                    print(i,end = '')
                print()    
            else :
                while integer != 0:
                    p = integer % 2
                    self.Push_Stack(p)
                    integer = integer // 2
                print('0b',end = '')
                for i in range(0,self.Len):
                    print(self.Stack_List.pop(),end = '')
                self.Clear_Stack()
                print('.0',end='')
                print()            
    def Conversion_ten_to_eight(self,e):
        if self.Is_Empty() != True :
            self.Clear_Stack()
        if e == 0:
            return False
        if type(e) == int:
            while e != 0 :
                n = e % 8
                self.Push_Stack(n)
                e = e // 8
            print('0o',end = '')
            for i in range(0,self.Len) :
                print(self.Stack_List.pop(),end = '')
            print()
        if type(e) == float:
            e = str(e)
            for i in range(-1,-len(e),-1):
                if e[i] == '.':
                    num = abs(i+1)  ## 求出小数点的位数 num
                    break
            e = float(e)
            integer = e*(10**num) // (10**num)
            decimal = e - integer
            integer = int(integer)
            if integer == 0 and decimal != 0:
                for i in range(0,4): ### 保留四位小数
                    result = 8 * decimal ### 乘2
                    result1 = int(result) ### 取整入栈
                    self.Push_Stack(result1)
                    decimal = result - result1
                    if decimal == 0 :
                        result = int(result) ###注意：添加此条语句的原因是：result = 2 * decimal 是float类型的，
                        ###入栈的如果是result不转换类型的话那么就会以float显示，就会出现输出格式错误的情况
                        self.Push_Stack(result)
                        break
                print('0o',end = '')
                print('0.',end = '')
                for i in self.Stack_List :
                    print(i,end = '')
                print()
            elif integer != 0 and decimal != 0:
                while integer != 0:
                    p = integer % 8
                    self.Push_Stack(p)
                    integer = integer // 8
                print('0o',end = '')
                for i in range(0,self.Len):
                    print(self.Stack_List.pop(),end = '')
                self.Clear_Stack() ## 要清空栈，否则会出现输出错误！
                print('.',end='') 
                for i in range(0,4): ### 保留四位小数
                    result = 8 * decimal ### 乘2
                    if result == 1 :
                        result = int(result) 
                        self.Push_Stack(result)
                        break
                    result1 = int(result) ### 取整入栈
                    self.Push_Stack(result1)
                    decimal = result - result1 
                for i in self.Stack_List :
                    print(i,end = '')
                print()    
            else :
                while integer != 0:
                    p = integer % 8
                    self.Push_Stack(p)
                    integer = integer // 8
                print('0o',end = '')
                for i in range(0,self.Len):
                    print(self.Stack_List.pop(),end = '')
                self.Clear_Stack()
                print('.0',end='')
                print()
    def Conversion_ten_to_sixteen(self,e):
        W = [0,1,2,3,4,5,6,7,8,9,'a','b','c','d','e','f']
        if self.Is_Empty() != True :
            self.Clear_Stack()
        if e == 0:
            return False
        if type(e) == int:
            while e != 0 :
                n = e % 16
                self.Push_Stack(W[n])
                e = e // 16
            print('0x',end = '')
            for i in range(0,self.Len) :
                print(self.Stack_List.pop(),end = '')
            print()
        if type(e) == float:
            e = str(e)
            for i in range(-1,-len(e),-1):
                if e[i] == '.':
                    num = abs(i+1)  ## 求出小数点的位数 num
                    break
            e = float(e)
            integer = e*(10**num) // (10**num)
            decimal = e - integer
            integer = int(integer)
            if integer == 0 and decimal != 0:
                for i in range(0,4): ### 保留四位小数
                    result = 16 * decimal ### 乘2
                    result1 = int(result) ### 取整入栈
                    self.Push_Stack(W[result1])
                    decimal = result - result1
                    if decimal == 0 :
                        result = int(result) ###注意：添加此条语句的原因是：result = 2 * decimal 是float类型的，
                        ###入栈的如果是result不转换类型的话那么就会以float显示，就会出现输出格式错误的情况
                        self.Push_Stack(W[result])
                        break
                print('0x',end = '')
                print('0.',end = '')
                for i in self.Stack_List :
                    print(i,end = '')
                print()
            elif integer != 0 and decimal != 0:
                while integer != 0:
                    p = integer % 16
                    self.Push_Stack(W[p])
                    integer = integer // 16
                print('0x',end = '')
                for i in range(0,self.Len):
                    print(self.Stack_List.pop(),end = '')
                self.Clear_Stack() ## 要清空栈，否则会出现输出错误！
                print('.',end='') 
                for i in range(0,4): ### 保留四位小数
                    result = 16 * decimal ### 乘2
                    if result == 1 :
                        result = int(result) 
                        self.Push_Stack(W[result])
                        break
                    result1 = int(result) ### 取整入栈
                    self.Push_Stack(W[result1])
                    decimal = result - result1 
                for i in self.Stack_List :
                    print(i,end = '')
                print()    
            else :
                while integer != 0:
                    p = integer % 16
                    self.Push_Stack(W[p])
                    integer = integer // 16
                print('0x',end = '')
                for i in range(0,self.Len):
                    print(self.Stack_List.pop(),end = '')
                self.Clear_Stack()
                print('.0',end='')
                print()
    def Conversion_two_to_ten(self,e):
        if self.Is_Empty() != True :
            self.Clear_Stack()
        if e == 0:
            return False
        if type(e) == int :
            e = str(e)
            len_e = len(e) - 1
            add = 0
            for i in range(0,len(e)):
                add = add + int(e[i]) * (2 ** (len_e-i))
            print('0d'+str(add))
        if type(e) == float:
            e = str(e)
            for i in range(-1,-len(e),-1):
                if e[i] == '.':
                    num = abs(i+1)  ## 求出小数点的位数 num
                    break
            e = float(e)
            integer = e*(10**num) // (10**num)
            decimal = e - integer
            integer = int(integer)
            decimal = int(decimal * (10 ** num))
            if integer != 0 and decimal != 0:
                integer = str(integer)
                decimal = str(decimal)
                len_integer = len(integer) - 1
                add = 0
                for i in range(0,len(integer)):
                    add += int(integer[i]) * (2 ** (len_integer-i))
                for i in range(0,len(decimal)):
                    add +=  int(decimal[i]) * (2 ** -(i + 1))
                print('0d' + str(add)) 
            if integer != 0 and decimal == 0 :
                integer = str(integer)
                len_integer = len(integer) - 1
                add = 0
                for i in range(0,len(integer)):
                    add += int(integer[i]) * (2 ** (len_integer-i))
                print('0d'+str(add),end = '.')
                print(0)
            if integer == 0 and decimal != 0 :
                decimal = str(decimal)
                add = 0
                for i in range(0,len(decimal)):
                    add +=  int(decimal[i]) * (2 ** -(i + 1))
                print('0d'+str(add))
    def Conversion_eight_to_ten(self,e):
        if self.Is_Empty() != True :
            self.Clear_Stack()
        if e == 0:
            return False
        if type(e) == int :
            e = str(e)
            len_e = len(e) - 1
            add = 0
            for i in range(0,len(e)):
                add = add + int(e[i]) * (8 ** (len_e-i))
            print('0d'+str(add))
        if type(e) == float:
            e = str(e)
            for i in range(-1,-len(e),-1):
                if e[i] == '.':
                    num = abs(i+1)  ## 求出小数点的位数 num
                    break
            e = float(e)
            integer = e*(10**num) // (10**num)
            decimal = e - integer
            integer = int(integer)
            decimal = int(decimal * (10 ** num))
            if integer != 0 and decimal != 0:
                integer = str(integer)
                decimal = str(decimal)
                len_integer = len(integer) - 1
                add = 0
                for i in range(0,len(integer)):
                    add += int(integer[i]) * (8 ** (len_integer-i))
                for i in range(0,len(decimal)):
                    add +=  int(decimal[i]) * (8 ** -(i + 1))
                print('0d' + str(add)) 
            if integer != 0 and decimal == 0 :
                integer = str(integer)
                len_integer = len(integer) - 1
                add = 0
                for i in range(0,len(integer)):
                    add += int(integer[i]) * (8 ** (len_integer-i))
                print('0d'+str(add),end = '.')
                print(0)
            if integer == 0 and decimal != 0 :
                decimal = str(decimal)
                add = 0
                for i in range(0,len(decimal)):
                    add +=  int(decimal[i]) * (8 ** -(i + 1))
                print('0d'+str(add))  
    def Conversion_sixteen_to_ten(self,e): 
        if self.Is_Empty() != True :
            self.Clear_Stack()
        if e == 0:
            return False
        if type(e) == int :
            e = str(e)
            len_e = len(e) - 1
            add = 0
            for i in range(0,len(e)):
                add = add + int(e[i]) * (16 ** (len_e-i))
            print('0d'+str(add))
        if type(e) == float:
            e = str(e)
            for i in range(-1,-len(e),-1):
                if e[i] == '.':
                    num = abs(i+1)  ## 求出小数点的位数 num
                    break
            e = float(e)
            integer = e*(10**num) // (10**num)
            decimal = e - integer
            integer = int(integer)
            decimal = int(decimal * (10 ** num))
            if integer != 0 and decimal != 0:
                integer = str(integer)
                decimal = str(decimal)
                len_integer = len(integer) - 1
                add = 0
                for i in range(0,len(integer)):
                    add += int(integer[i]) * (16 ** (len_integer-i))
                for i in range(0,len(decimal)):
                    add +=  int(decimal[i]) * (16 ** -(i + 1))
                print('0d' + str(add)) 
            if integer != 0 and decimal == 0 :
                integer = str(integer)
                len_integer = len(integer) - 1
                add = 0
                for i in range(0,len(integer)):
                    add += int(integer[i]) * (16 ** (len_integer-i))
                print('0d'+str(add),end = '.')
                print(0)
            if integer == 0 and decimal != 0 :
                decimal = str(decimal)
                add = 0
                for i in range(0,len(decimal)):
                    add +=  int(decimal[i]) * (16 ** -(i + 1))
                print('0d'+str(add))
    def Arbitrary_Sys_Convert(self,e,a,b):  ### 任意进制转换：e为要转换的数据，a为数据的本来进制，b为要转换成的数据 
        Tuple_a = (2,4,8,10,16)
        Tuple_b = (2,4,8,10,16)
        if a not in Tuple_a or b not in Tuple_b :
            print('您所要转换的数制目前还不支持，请重新选择哦。')
            return False
        if a == b :
            print('您所要转换的数制是相同的，不需要转换哦。')
            return False
        if a == 2 :
            if b == 8 :
                self.Conversion_two_to_ten(e)
                self.Conversion_ten_to_eight(e)
            elif b == 10:
                self.Conversion_two_to_ten(e)
            else :
                self.Conversion_two_to_ten(e)
                self.Conversion_ten_to_sixteen(e)
        elif a == 8 :
            if b == 2:
                self.Conversion_eight_to_ten(e)
                self.Conversion_ten_to_two(e)
            elif b == 10 :
                self.Conversion_eight_to_ten(e)
            else:
                self.Conversion_eight_to_ten(e)
                self.Conversion_ten_to_sixteen(e)
        elif a == 10 :
            if b == 2:
                self.Conversion_ten_to_two(e)
            elif b == 8 :
                self.Conversion_ten_to_eight(e)
            else:
                self.Conversion_ten_to_sixteen(e)
        else:
            if b == 2:
                self.Conversion_sixteen_to_ten(e)
                self.Conversion_ten_to_two(e)
            elif b == 8:
                self.Conversion_sixteen_to_ten(e)
                self.Conversion_ten_to_eight(e)
            else:
                self.Conversion_sixteen_to_ten(e)
if __name__ == '__main__' :
    print('*********************************************  程序测试  *********************************************')
    x = Stack()
    x.Initialize()
#     L = [2,4,5,6,3,9,10]
#     x.Create_Stack(L)
#     x.Traverse_Stack()
#     print('栈底：',end = '')
#     print(x.Get_Bottom())
#     print('栈顶：',end = '')
#     print(x.Get_Top())
#     print('栈的长度：',end = '')
#     print(x.Get_Length())
#     print('************************************  数制转换 —— 十进制转二进制  *************************************')
#     print()
#     print('转换后的数为：',end = '')
#     x.Conversion_ten_to_two(23)
#     x.Conversion_ten_to_two(23.8125)
#     x.Conversion_ten_to_two(23.0)
#     x.Conversion_ten_to_two(0.8125)
#     print()
#     print('''注意：第一，在进行进制转换的时候，需要把要转换的数提前转换成整形数据，否则结果不对。
#       第二，本方法在进行浮点数的进制转换的时候，把整数部分转换成二进制后，要清空栈，再次进行小数部
#     分的出栈操作，否则长度会超过列表的长度，造成错误 \n''')
#     print('************************************  数制转换 —— 十进制转八进制  *************************************')
#     print()
#     print('转换后的数为：',end = '')
#     x.Conversion_ten_to_eight(19)
#     x.Conversion_ten_to_eight(19.155)
#     x.Conversion_ten_to_eight(0.155)
#     x.Conversion_ten_to_eight(19.0) 
#     print('\n************************************  数制转换 —— 十进制转十六进制  ***********************************\n')
#     print('转换后的数为：',end = '')
#     x.Conversion_ten_to_sixteen(358.155) 
#     x.Conversion_ten_to_sixteen(0.155)
#     x.Conversion_ten_to_sixteen(358.0)
#     x.Conversion_ten_to_sixteen(358)   
#     print('\n*************************************  数制转换 —— 二进制转十进制  ************************************\n')   
#     print('转换后的结果：')
#     x.Conversion_two_to_ten(1101)
#     x.Conversion_two_to_ten(1101.1011)
#     x.Conversion_two_to_ten(1101.0)
#     x.Conversion_two_to_ten(0.1011)   
#     print('\n*************************************  数制转换 —— 八进制转十进制  ************************************\n') 
#     x.Conversion_eight_to_ten(356)
#     x.Conversion_eight_to_ten(356.673)
#     x.Conversion_eight_to_ten(356.0)
#     x.Conversion_eight_to_ten(0.673)  
#     print('\n************************************  数制转换 —— 十六进制转十进制  ***********************************\n') 
#     x.Conversion_sixteen_to_ten(356)
#     x.Conversion_sixteen_to_ten(356.673)
#     x.Conversion_sixteen_to_ten(356.0)
#     x.Conversion_sixteen_to_ten(0.673)
    while True:
        print('请选择操作：')
        A = str(input('A 数制转换    B 退出操作'))
        if A == 'A':
            e = int(input('请输入您想要转换的数据e：'))
            a = int(input('请输入您所输入的数据的进制a：'))
            b = int(input('请输入您想要转换成的进制b：'))
            e = str(e)
            flag = 1
            for i in e :
                if int(i) > a - 1 :
                    print('您所输入的数据并不是'+str(a)+'进制的数哦！请重新选择操作：')
                    flag = 0
                    break
            e = int(e)
            if flag == 1:
                x.Arbitrary_Sys_Convert(e, a, b)
        else:
            exit(0)
        
        
    
    

    
     


   

    
    
    
    
           
        
        
        
    
    























