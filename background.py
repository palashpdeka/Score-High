import turtle
import random
import threading

##################### Window/Screen ###############################
window = turtle.Screen()
windowWidth,windowHeight = window.screensize()


##################### Main SET-UP #################################
# Two horizontal lines and working display
displaySize = 100

line1 = turtle.Turtle()
line1.speed(0)
line1.penup()
line1.sety(displaySize)
line1.shape("square")
line1.shapesize(stretch_wid=0.5,stretch_len=windowWidth/10)

line2 = turtle.Turtle()
line2.speed(0)
line2.penup()
line2.sety(-displaySize)
line2.shape("square")
line2.shapesize(stretch_wid=0.5,stretch_len=windowWidth/10)



# Vertical line with a gap in between to pass the ball
mainLine1=turtle.Turtle()
mainLine1.speed(0)
mainLine1.penup()
mainLine1.shape("square")
mainLine1.shapesize(stretch_wid=1, stretch_len= 0.5)
mainLine1.setheading(180)
mainLine1.setpos(0,0)
mainLineSpeed=20

mainLine2=turtle.Turtle()
mainLine2.speed(0)
mainLine2.penup()
mainLine2.shape("square")
mainLine2.shapesize(stretch_wid=1, stretch_len= 0.5)
mainLine2.setheading(180)
mainLine2.setpos(0,0)

# player
ball = turtle.Turtle()
ball.speed(0)
ball.penup()
ball.shape("circle")
ball.color("green")
ball.setposition(-50,-90)

def moveRight():
    mainLine1.speed(mainLineSpeed)
    mainLine2.speed(mainLineSpeed)
    mainLine1.forward(10)
    mainLine2.forward(10)

#gap height
gap=0
ratio=10/13 #mainline divided into 13 parts where 3 parts will be for a gap, why 10? read the comment below.

def createGapInMainLine(x):
    y=10-x; x*=ratio
    mainLine1.setpos(mainLine1.xcor(), -0.5*(2*displaySize-21*x)) #by default 21*21 square is formed
    mainLine1.shapesize(stretch_wid=x, stretch_len= 0.5)
    y*=ratio
    mainLine2.setpos(mainLine2.xcor(), 0.5*(2*displaySize-21*y))
    mainLine2.shapesize(stretch_wid=(10*ratio-x), stretch_len= 0.5)
    #what is 10? distance b/w two lines=200, and turtle size=21, so we get 200/21 approximately 10

# def createGapInMainLineUp(x):
#     x*=ratio
#     mainLine1.setpos(mainLine1.xcor(), -0.5*(2*displaySize-21*x)) #by default 21*21 square is formed
#     mainLine1.shapesize(stretch_wid=x, stretch_len= 0.5)
#     #what is 10? distance b/w two lines=200, and turtle size=21, so we get 200/21 approximately 10
    
# def createGapInMainLineDown(x):
#     y=10-x; y*=ratio
#     mainLine2.setpos(mainLine2.xcor(), 0.5*(2*displaySize-21*y))
#     mainLine2.shapesize(stretch_wid=(10*ratio-x), stretch_len= 0.5) 

# def createGapInMainLine(x):
#     #p1=threading.Thread(target=createGapInMainLineUp, args=(x))
#     #p2=threading.Thread(target=createGapInMainLineDown, args=(x))
#     #p1.start()
#     #p2.start()
#     #p1.join()
#     #p2.join()
#     createGapInMainLineUp(x)
#     createGapInMainLineDown(x)

gap=random.randint(1,9)
createGapInMainLine(gap)
    



# turtle.done()
