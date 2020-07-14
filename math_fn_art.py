import turtle
import math

t_1 = turtle.Turtle()
t_1.speed(25)
t_1.pencolor("#0E934A")

for i in range(500):
    t_1.forward(math.sin(i)*45)
    t_1.right(i%12)

turtle.exitonclick()
