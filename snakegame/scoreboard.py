from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 14, "normal")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0

        with open("highscore.txt", mode="r") as file:
            content = file.read().strip()
            try:
                self.highscore = int(content)
            except ValueError:
                self.highscore = 0

        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} HighScore: {self.highscore}", align=ALIGNMENT, font=FONT)


    def reset(self):
        if self.score>self.highscore:
            self.highscore=self.score
            with open("highscore.txt",mode="w") as file2:
                file2.write(f"{self.highscore}")
        self.score=0
        self.update_scoreboard()
        
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
