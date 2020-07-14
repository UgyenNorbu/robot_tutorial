import turtle
import random as rn

t_1 = turtle.Turtle()
t_2 = turtle.Turtle()
t_3 = turtle.Turtle()
t_4 = turtle.Turtle()

t_1.speed(15)
t_2.speed(15)
t_3.speed(15)
t_4.speed(15)

t_1.pensize(2)
t_2.pensize(2)
t_3.pensize(2)
t_4.pensize(2)

t_1.pencolor("#F1C40F")
t_2.pencolor("#5DADE2")
t_3.pencolor("#E74C3C")
t_4.pencolor("#239B56")

turtle.bgcolor("#CFCFCF")

for i in range(50):
    t_1.right(rn.randint(0, 360))
    t_1.forward(rn.randrange(10, 30, 2))
    t_2.right(rn.randint(0, 360))
    t_2.forward(rn.randrange(10, 30, 3))
    t_3.right(rn.randint(0, 360))
    t_3.forward(rn.randrange(10, 50, 5))
    t_4.right(rn.randint(0,360))
    t_4.forward(rn.randrange(10, 50, 6))

turtle.exitonclick()
