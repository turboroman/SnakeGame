from turtle import Turtle
FONT = ('Arial', 16, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.write(f'Score = {self.score}', align='center', font=('Arial', 16, 'normal'))
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f'Score = {self.score}', align='center', font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f'GAME OVER', align='center', font=FONT)
