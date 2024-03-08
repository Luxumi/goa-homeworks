from turtle import *


#we want to paint a house
width(4)

color("black")
forward(150)
left(90)
forward(160)
left(90)
forward(150)
left(90)
forward(160)

penup()
goto(50,0)
pendown()

color("yellow")
begin_fill()
left(180)
forward(100)
right(90)
forward(50)
right(90)
forward(100)
right(90)
forward(50)
end_fill()

penup()
goto(0,161)
pendown()

right(120)
forward(150)
right(120)
forward(150)



penup()
goto(100,130)
pendown()

right(90)
forward(35)
right(90)
forward(20)
right(90)
forward(35)
right(90)
forward(20)



penup()
goto(-50,0)
pendown()

speed(50)

color("blue")
forward(150)
left(90)
forward(160)
left(90)
forward(150)
left(90)
forward(160)

penup()
goto(-150,0)
pendown()



color("black")
begin_fill()
right(90)
left(180)
forward(100)
right(90)
forward(50)
right(90)
forward(100)
right(90)
forward(50)
end_fill()

penup()
goto(-50,150)
pendown()



right(60)
forward(165)
left(120)
forward(161)

penup()
goto(-113,135)
pendown()



color("black")
left(-60)
forward(-40)
right(-90)
forward(20)
right(90)
forward(40)
right(90)
forward(20)

penup()
goto(-150,115)
pendown()



left(-90)
forward(-40)
right(-90)
forward(20)
right(90)
forward(40)
right(90)
forward(20)



penup()
goto(-400,150)
pendown()

color("black")
forward(150)
left(90)
forward(160)
left(90)
forward(150)
left(90)
forward(160)

penup()
goto(-295,100)
pendown()

color("purple")
begin_fill()
right(90)
left(180)
forward(100)
right(90)
forward(50)
right(90)
forward(100)
right(90)
forward(50)
end_fill()

penup()
goto(-238,150)
pendown()

left(120)
forward(165)
left(120)
forward(161)

penup()
goto(-310,135)
pendown()

color("purple")
left(-60)
forward(-40)
right(-90)
forward(20)
right(90)
forward(40)
right(90)
forward(20)

penup()
goto(-335,115)
pendown()

left(-90)
forward(-40)
right(-90)
forward(20)
right(90)
forward(40)
right(90)
forward(20)



exitonclick()

