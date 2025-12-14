import random
import turtle
# import numpy as np

pen = turtle.Pen()
# pen.speed(10)
pen.ht()

'''pen.begin_fill()
for i in range(360):
    i /= 180 / math.pi
    length = A * (1 - math.cos(i))
    x, y = length * math.cos(i), length * math.sin(i)
    pen.goto(x, y)
pen.end_fill()'''

# for i in range(360):
#     i /= math.pi
#     length = A * (1 - math.sin(i))
#     x, y = length * math.cos(i), length * math.sin(i)

random.seed(1000)
times = 1000
# X = sorted((1 - np.random.random(times)))
X = [_ / times for _ in range(times)]
d = [[x ** (2 / 3), (1 - x ** 2) ** 0.5] for x in X]
pos = [None] * times * 4
for i in range(len(X)):
    pos[i + times * 0] = [X[i], d[i][0] + d[i][1]]
    pos[i + times * 1] = [X[-i - 1], d[-i - 1][0] - d[-i - 1][1]]
    pos[i + times * 2] = [-X[i], d[i][0] - d[i][1]]
    pos[i + times * 3] = [-X[-i - 1], d[-i - 1][0] + d[-i - 1][1]]
print('begin draw')


def draw(A=100, fillcolor='red', scale=1):
    turtle.tracer(False)
    start_x, start_y = pen.pos()
    pen.seth(90)
    pen.pu()
    pen.goto(start_x, pos[0][1] * A + start_y)
    pen.fillcolor(fillcolor)
    pen.pd()
    pen.begin_fill()
    for x, y in pos:
        pen.goto(x * scale * A + start_x, y * A + start_y)
    pen.end_fill()
    turtle.update()


def draw_more():
    for i in range(100):
        pen.pu()
        pen.goto(random.randint(-900, 900), random.randint(-500, 500))
        # pen.pd()
        draw(A=random.randint(10, 100), fillcolor=random_color(), scale=1.2)


def hex_(num):
    return f'{hex(num)[2:]:0>2}'


def random_color():
    r, g, b = random.randint(200, 255), random.randint(0, 20), random.randint(0, 20)
    return f'#{hex_(r)}{hex_(g)}{hex_(b)}'


turtle.Screen().delay(False)
pen.pencolor('snow')
for i in range(100):
    draw_more()
    pen.clear()
turtle.done()

#————————————————
#版权声明：本文为CSDN博主「往后，余生」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
#原文链接：https://blog.csdn.net/qq_38700592/article/details/107834555
