import turtle

my_turtle= turtle.Turtle()
my_turtle.shape("turtle")
my_turtle.screen.bgcolor("black")
my_turtle.speed(5)

my_turtle.color("#3CBBE2")
my_turtle.fillcolor("yellow")
my_turtle.pensize(5)

#Functions for different alphabets
def h():

    my_turtle.left(90)
    my_turtle.forward(100)
    my_turtle.backward(200)
    my_turtle.forward(100)
    my_turtle.right(90)
    my_turtle.forward(70)
    my_turtle.left(90)
    my_turtle.forward(100)
    my_turtle.backward(200)

def a():
    
    my_turtle.left(70)
    my_turtle.forward(200)
    my_turtle.right(140)
    my_turtle.forward(200)
    my_turtle.backward(90)
    my_turtle.left(-110)
    my_turtle.forward(75)

def p():

    my_turtle.forward(200)
    my_turtle.right(90)
    my_turtle.circle(-60,180)

def y():
    
    my_turtle.forward(120)
    my_turtle.left(30)
    my_turtle.forward(90)
    my_turtle.backward(90)
    my_turtle.right(60)
    my_turtle.forward(90)

def b():

    my_turtle.left(90)
    my_turtle.forward(200)
    my_turtle.right(90)
    my_turtle.circle(-50, 180)
    my_turtle.right(180)
    my_turtle.circle(-50, 180)

def i():

    my_turtle.left(90)
    my_turtle.forward(200)

def R():

    my_turtle.left(90)
    my_turtle.forward(200)
    my_turtle.right(90)
    my_turtle.circle(-60, 180)
    my_turtle.right(-135)
    my_turtle.forward(120)

def t():

    my_turtle.left(90)
    my_turtle.forward(200)
    my_turtle.left(90)
    my_turtle.forward(70)
    my_turtle.back(140)

def d():

    my_turtle.left(90)
    my_turtle.forward(200)
    my_turtle.right(90)
    my_turtle.circle(-100,180)

def m():

    my_turtle.left(90)
    my_turtle.forward(200)
    my_turtle.right(140)
    my_turtle.forward(80)

    my_turtle.left(105)
    my_turtle.forward(80)
    my_turtle.right(145)
    my_turtle.forward(200)

def move(x,y):
    my_turtle.penup()
    my_turtle.goto(x, y)
    my_turtle.pendown()

# HAPPY

move(-600, 220)
h()
my_turtle.penup()
my_turtle.right(90)
my_turtle.forward(50)
my_turtle.pendown()
a()
my_turtle.right(90)
move(-300,120)
p()
my_turtle.right(90)
move(-200,120)
p()
my_turtle.right(90)
move(-70,120)
y()

# BIRTHDAY

my_turtle.color("#EFAE17")
my_turtle.right(60)
move(-600,-300)
b()
my_turtle.right(180)
move(-520,-300)
i()
my_turtle.right(90)
move(-475,-300)
R()
my_turtle.left(45)
move(-340,-305)
t()
my_turtle.right(180)
move(-250,-203)
h()
my_turtle.right(90)
move(-120,-300)
d()
my_turtle.right(180)
move(0,-300)
a()
my_turtle.right(90)
move(195,-300)
y()


# FLOWER
my_turtle.color("green")
my_turtle.fillcolor("yellow")

my_turtle.left(30)
move(355,-300)
my_turtle.forward(100)

my_turtle.begin_fill()
for i in range(10):
    my_turtle.speed(4)
    my_turtle.forward(100)
    my_turtle.left(160)
my_turtle.end_fill()

turtle.done()
