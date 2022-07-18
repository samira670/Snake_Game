from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()

        self.goto(0, 280)
        self.color("white")
        self.hideturtle()
        self.write("score=0")



    def scorebord(self, i):
        self.clear()
        self.write(f"score= {i}")


    def game_over(self):
        self.goto(-50,0)
        self.write("GAME IS OVER", font=('Arial', 15, 'normal'))


