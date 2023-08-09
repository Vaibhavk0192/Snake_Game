from turtle import Turtle
alignment="center"
font=("courier",15,"normal")
font2=("courier",13,"normal")


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,290)
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}",align=alignment,font=font)

    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",font=font,align="center")
        self.goto(0,-20)
        self.write("press G to restart",font=font2,align="center")
        self.goto(0,-280)
        self.write("press esc to exit",font=font2,align="center")