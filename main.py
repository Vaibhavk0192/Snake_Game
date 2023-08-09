import turtle as t
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

def make_board():
    t.speed("fastest")
    t.hideturtle()
    t.penup()
    t.goto(-290,290)
    t.setheading(90)
    t.color("white")
    t.pendown()
    for _ in range(4):
        t.right(90)
        t.forward(580)


screen=t.Screen()
screen.setup(width=600,height=620)
make_board()

screen.bgcolor("black")
screen.title("Snake Game")
start_position=[(0,0),(-20,0),(-40,0)]
segment=[]
screen.tracer(0)

def main():
    scoreboard=Scoreboard()
    snake=Snake()
    food=Food()
    screen.listen()
    screen.onkey(snake.up,"Up")
    screen.onkey(snake.down,"Down")
    screen.onkey(snake.right,"Right")
    screen.onkey(snake.left,"Left") 


    game_is_on=True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        if snake.head.distance(food)<15:
            food.refresh()
            snake.extend_snake()
            scoreboard.increase_score()

        if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
            game_is_on=False
            scoreboard.game_over()
        
        for seg in snake.segment:
            if seg==snake.head:
                pass
            elif snake.head.distance(seg)<10:
                game_is_on=False
                scoreboard.game_over()
main()
def restart():
    t.resetscreen()
    make_board()
    main()

def exit():
    t.bye()
screen.onkey(restart,"g") 
screen.onkey(exit,"Escape")
screen.exitonclick()