import turtle
import random

# 速度拉满：0 是最快
turtle.speed(0)
turtle.colormode(255)
turtle.bgcolor(245, 245, 220)  # 米黄色背景

# 设置画笔
t = turtle.Turtle()
turtle.tracer(0, 0)

def draw_tree(branch_length, t):
    if branch_length < 8:
        # 随机画苹果 或 叶子
        if random.random() < 0.2:  # 20%概率画苹果
            t.pensize(1)
            t.color(255, 0, 0)  # 红色苹果
            t.begin_fill()
            t.circle(random.randint(4, 6))
            t.end_fill()
        else:  # 80%概率画叶子
            t.pensize(1)
            t.color(0, random.randint(100, 180), 0)
            t.begin_fill()
            t.circle(random.randint(3, 7))
            t.end_fill()
        
        t.color(139, 69, 19)
        return

    angle = random.randint(15, 30)
    t.pensize(branch_length / 10)
    t.color(139, 69, 19)

    t.forward(branch_length)
    t.left(angle)
    draw_tree(branch_length * random.uniform(0.7, 0.8), t)
    t.right(2 * angle)
    draw_tree(branch_length * random.uniform(0.7, 0.8), t)
    t.left(angle)
    t.backward(branch_length)

# 初始化位置
t.left(90)
t.penup()
t.backward(150)
t.pendown()

# 开始画
draw_tree(100, t)

turtle.update()
turtle.done()