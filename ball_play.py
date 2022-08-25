import turtle
import time
import random
import background as bg

################ Jumping physics ###################### 
# ball.velocity=10
bg.ball.jumpHeight = 0
bg.ball.g = 9.81
bg.ball.u = 0
bg.ball.time = 0
bg.ball.nextHeight = -1

def setVelocity(h):
    bg.ball.u = (2*(bg.ball.g)*h)**0.5    #u=root(2gh)
    bg.ball.jumpHeight = h




##################### Functionality ############################
     

def passed(x):
    y_ball=bg.ball.ycor()
    ratio=10/13
    y=10-x; x*=ratio; y*=ratio
    point1=-1*(bg.displaySize-21*x) #bottommost point of mainline1
    point2=bg.displaySize-21*y #topmost point of mainline2
    print(y_ball,point1,point2)
    return (point2<=y_ball and y_ball<=point1) or (point1<=y_ball and y_ball<=point2) 

def moveBall():

    ########## LOGIC 1 ##########
    # y = ball.ycor()
    # # -90 = current boundary of lower horizontal line
    # #  10 = currently ball only jumps 100px so (-90 + 100)
    # if y < -90 or y > -90 + ball.jumpHeight:
    #     ball.velocity*=-1
    # y+=ball.velocity
    # ball.sety(y)

    ########## LOGIC 2 ##########
    bg.ball.time+=0.5
    s = (bg.ball.u)*(bg.ball.time) - 0.5*bg.ball.g*(bg.ball.time**2)
    if s<0:
        bg.ball.time=0
        s=0
        if bg.ball.nextHeight!=-1:
            setVelocity(bg.ball.nextHeight)
            bg.ball.nextHeight=-1
        else:
            setVelocity(bg.ball.jumpHeight/3)
    bg.ball.sety(-90+s)



############################# GAME ####################################
bg.window.listen()

bg.window.onkey(bg.window.bye,'x')

#### Keypress [0-9] by user to change ball jump height ######
def setNextJump(n):
    print(f"pressed {n}")
    bg.ball.nextHeight=n*18

for num in range(10):
    bg.window.onkeypress(lambda n=num: setNextJump(n), str(num))

def showScore(score):
    turtle.clear()
    turtle.penup()
    turtle.hideturtle()
    turtle.setpos(160,130)
    turtle.pendown()
    #turtle.showturtle()
    turtle.write("Score: "+str(score), font=("Serif",20))

def gameOver(score):
    turtle.clear()
    turtle.penup()
    turtle.hideturtle()
    turtle.setpos(-100,200)
    turtle.pendown()
    #turtle.showturtle()
    turtle.write("GAME OVER !\n Your score: "+str(score), font=("Serif",40))
    time.sleep(4)
    bg.window.bye()
    
def play():
    score=0
    showScore(score)
    while True:
      bg.moveRight()
      moveBall()
      x=bg.mainLine1.xcor()
      #check if ball passed through gap or not
      if x==0:
         if passed(bg.gap): 
                print("PASSED")
                score+=1
                showScore(score)
         else: 
                print("NOT PASSED")
                gameOver(score)
                
    
      # reset the mainLine
      if x < (-bg.windowWidth):
        bg.mainLine1.speed(0)
        bg.mainLine1.setx(bg.windowWidth)
        bg.mainLine2.speed(0)
        bg.mainLine2.setx(bg.windowWidth)
        bg.gap=random.randint(1,9)
        bg.createGapInMainLine(bg.gap)