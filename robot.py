import turtle as t
from itertools import cycle

my_color = cycle(['red', 'blue', 'yellow'])
t.speed(35)
my_rad = 10
t.bgcolor("#D2D2D2")

for i in range(100):
    t.pencolor(next(my_color))
    t.circle(my_rad)
    t.left(5)
    my_rad = my_rad + 1

t.exitonclick()
