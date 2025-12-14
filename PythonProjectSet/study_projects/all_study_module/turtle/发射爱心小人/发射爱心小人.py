from turtle import *

ht()
pensize(5)
speed(9)
penup()

goto(0,-100)
pendown()
circle(100)
#画脸
fillcolor("black")
begin_fill()
penup()
goto(-40,40)
pendown()#画左边的眼睛
circle(10)
end_fill()

begin_fill()
penup()
goto(40,40)
pendown()#画左边的眼睛
circle(10)
end_fill()

#画嘴
penup()
a = 0
goto(-40,-50)
pendown()
for i in range(95):
    seth(315 + i)
    fd(a + 1)
penup()
goto(0,-100)
pendown()
#画身体
seth(270)
fd(120)
(x,y) = pos()

seth(225)
fd(100)
#画腿
penup()
goto(x,y)
pendown()
seth(315)
fd(100)
#画胳膊
penup()
goto(0,-140)
seth(0)
pendown()
fd(80)
#画手
(x,y) = pos()
seth(45)
fd(80)
penup()
goto(x,y)
pendown()
seth(315)
fd(80)
(x,y) = pos()
seth(0)
penup()
fd(100)
(c,d) = pos()
pendown()



#画心
pensize(1)
pencolor("red")
fillcolor("red")
begin_fill()
a = 0

for i in range(12):
    seth(135 - 1.1 * i)
    fd(a + 8)

for i in range(10):
    seth(125 - i * 11 )
    fd(a + 9)

for i in range(10):
    seth(15 - i * 8 )
    fd(a + 9)



for i in range(12):
    seth(75 - i * 10.5 )
    fd(a + 9)
    
for i in range(10):
    seth(309 - i * 9 )
    fd(a + 9)

for i in range(16):
    seth(230 - 0.2 * i)
    fd(a + 8)
goto(c,d)
end_fill()

penup()
pencolor("black")
goto(-50,150)
pendown()
write("就是说，学习太累了，给你们送个爱心。", font=("宋体",15,"normal"))

done()


