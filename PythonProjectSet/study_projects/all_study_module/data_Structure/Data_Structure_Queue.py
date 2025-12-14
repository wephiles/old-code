'''
Created on 2021年2月3日

@author: 20866
'''
##############################################################  Data structure - Python ##############################################################
##############################################################    数据结构 — Python     ###############################################################
class Queue():
    def __init__(self):
        self.MaxLen = 10
        self.TrueLen = 0
        self.Front = None
        self.Tail = None
    def __del__(self):
        print('析构函数调用！')
    def Initialize_Queue(self):
        self.Queue = []
    def Create_Queue(self,L):
        if self.Queue_is_Empty() == True :
            if len(L) > self.MaxLen:
                print('空间不够！')
                return False
            else:
                self.Queue = L 
                self.TrueLen = len(L)
                self.Front = self.Queue[0]
                self.Tail = self.Queue[self.TrueLen - 1]
        else:
            return False
    def Destroy_Queue(self):
        del self.Queue
    def Clear_Queue(self):
        del self.Queue[0:len(self.Queue)]
        self.TrueLen = 0
    def Queue_is_Empty(self):
        if self.TrueLen == 0 :
            return True 
        return False
    def Queue_is_Full(self):
        if self.TrueLen == self.MaxLen :
            return True 
        return False
    def Get_Queue_Length(self):
        return self.TrueLen
    def Get_Queue_Front(self):
        return self.Front
    def Get_Queue_Tail(self):
        return self.Tail
    def En_Queue(self,e): ### 入队列
        if self.Queue_is_Full() == True :
            print('队列是满的，无法添加！')
            return False
        else:
            self.Queue.append(e)
            self.TrueLen += 1
            self.Tail = self.Queue[self.TrueLen - 1]
    def De_Queue(self):  ### 出队
        if self.Queue_is_Empty():
            print('队列是空的哦！')
            return False
        else:
            del self.Queue[0]
            self.TrueLen -= 1
            self.Front = self.Queue[0]
    def Traverse_Queue(self):
        for i in self.Queue :
            print(i,end = ' ')
def main():
    X = Queue()
    X.Initialize_Queue()
    L = [2,5,8,9,7,1,3,0]
    X.Create_Queue(L)
    if X.Queue_is_Empty() != True:
        print('队列非空！')
    else:
        print('队列是空滴！')
        
    if X.Queue_is_Full() != True:
        print('队列不是满的！')
    else:
        print('队列是满的！')
        
    print('队列的长度为：',end = '')
    print(X.Get_Queue_Length())
    
    print('队列的头元素为：',end = '')
    print(X.Get_Queue_Front())
    
    print('队列的尾元素为：',end = '')
    print(X.Get_Queue_Tail())
    
    X.En_Queue(10)
    X.Traverse_Queue()
    print()
    X.De_Queue()
    X.Traverse_Queue()
    print()

if __name__ == '__main__':
    main()   
    
    
    
    
    





























