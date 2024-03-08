from turtle import *


#we want to paint a house
width(4)

color("blue")
forward(250)
left(90)
forward(300)
left(90)
forward(250)
left(90)
forward(300)

penup()
goto(85,0)
pendown()

color("black")
begin_fill()
left(180)
forward(130)
right(90)
forward(80)
right(90)
forward(130)
right(90)
forward(80)
end_fill()

penup()
goto(0,300)
pendown()

right(145)
forward(155)
right(72)
forward(155)

penup()
goto(25,150)
pendown()

color("yellow")
left(127)
forward(100)
right(90)
forward(60)
right(90)
forward(100)
right(90)
forward(60)

penup()
goto(175,150)
pendown()

right(90)
forward(100)
right(90)
forward(60)
right(90)
forward(100)
right(90)
forward(60)











exitonclick()