from turtle import Turtle

FONT = ('Arial', 16, 'normal')
TOP_POSITION = (0, 270)


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color('white')
        self.penup()
        self.goto(TOP_POSITION)
        self.hideturtle()
        self.update_score()

    def reset(self):
        self.goto(TOP_POSITION)
        if self.high_score < self.score:
            self.high_score = self.score
            with open('data.txt', mode='w') as data:
                data.write(f'{self.high_score}')
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f'Score = {self.score} Highest score = {self.high_score}', align='center', font=FONT)

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f'GAME OVER', align='center', font=FONT)

    def increase_score(self):
        self.score += 1
