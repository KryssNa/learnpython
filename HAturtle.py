# import turtle
# star = turtle.Turtle()

# for i in range(5):
#     star.forward(200)
#     star.right(144)
# star.hideturtle()
# turtle.done()


import turtle

t=turtle.Turtle()
t.fillcolor("pink")
t.begin_fill()
t.up()
t.goto(0,0)
t.down()
t.circle(60)
t.end_fill()
t.hideturtle()

t=turtle.Turtle()
t.fillcolor("orange")
t.begin_fill()
t.up()
t.goto(-250,-150)
t.down()
t.circle(50)
t.end_fill()
t.hideturtle()

t=turtle.Turtle()
t.fillcolor("blue")
t.begin_fill()
t.up()
t.goto(250,150)
t.down()
t.circle(50)
t.end_fill()
t.hideturtle()


t=turtle.Turtle()
t.fillcolor("green")
t.begin_fill()
t.up()
t.goto(-250,150)
t.down()
t.circle(50)
t.end_fill()
t.hideturtle()

t=turtle.Turtle()
t.fillcolor("red")
t.begin_fill()
t.up()
t.goto(250,-150)
t.down()
t.circle(50)
t.end_fill()
t.hideturtle()
turtle.done()

