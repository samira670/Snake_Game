from turtle import Turtle


class Snake:
    def __init__(self):
        self.snakes = []
        self.create_snakes()
        self.head = self.snakes[0]

    def create_snakes(self):
        for _ in range(3):
            snake = Turtle("square")
            snake.color("white")
            snake.penup()
            snake.goto(0 - (_ * 20), 0)
            self.snakes.append(snake)

    def append(self):
        last_seg = self.snakes[-1]
        last_seg.position()
        snake = Turtle("square")
        snake.penup()
        snake.color("white")
        snake.goto(last_seg.position())
        self.snakes.append(snake)
        self.forward()

    def tail(self):
       for _ in self.snakes[1::]:

          if self.head.distance(_.xcor(), _.ycor())<5:
              return True






    def forward(self):

        for snake in range(len(self.snakes)-1, 0, -1):

            self.snakes[snake].goto(self.snakes[snake - 1].xcor(), self.snakes[snake - 1].ycor())
        self.snakes[0].forward(20)

    def up(self):
        #If the nake goes down it does not allow to go up
        if self.snakes[0].heading() != 270:
          self.snakes[0].setheading(90)

    def down(self):
        # If the nake goes up it does not allow to go down
      if self.snakes[0].heading() != 90:
        self.snakes[0].setheading(270)


    def right(self):
        # If the nake goes left it does not allow to go right
        if self.snakes[0].heading() != 180:
           self.snakes[0].setheading(0)

    def left(self):
        # If the nake goes right it does not allow to go  left
      if self.snakes[0].heading() != 0:
        self.snakes[0].setheading(180)



