import time

from turtle import Screen
from snake import Snake
from food import Food
from score import Score

screen = Screen()
#Turn off the screen
screen.tracer(0)
screen.setup(width=600, height=600)
screen.title("Funny Snake Game")
screen.bgcolor("black")



timmy = Snake()
food = Food()






#Control screen by keywords og device
screen.listen()
screen.onkey(timmy.up, "Up")
screen.onkey(timmy.down, "Down")
screen.onkey(timmy.right, "Right")
screen.onkey(timmy.left, "Left")
i= 0
#Turn on score by using score class
score = Score()

game_is_on = True
while game_is_on == True:
    #Updating screen every to 0.2 seconds to be continuous
    screen.update()
    time.sleep(0.2)
    timmy.forward()

    # Detect colision with food
    if timmy.head.distance(food.xcor(), food.ycor())<15:
    #Putting food in the random place
        food.random()
    #Increasing the scores
        i+=1
        score.scorebord(i)
        timmy.append()

    #Detect colision with body




    #Detect colision with wall
    if timmy.head.xcor() >= 280 or timmy.head.xcor() <= -280 or timmy.head.ycor() >= 280 or timmy.head.ycor() <= -280:
        game_is_on = False
        score.game_over()


    #Detect colision with tail
    if timmy.tail() == True :
        game_is_on= False
        score.game_over()




























screen.exitonclick()