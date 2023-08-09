import turtle as t

start_position=[(0,0),(-20,0),(-40,0)]
move_distance=20
up=90
down=270
right=0
left=180


class Snake:
    def __init__(self) -> None:
        self.segment=[]
        self.createSnake()
        self.head=self.segment[0]

    def createSnake(self):
        for position in start_position:
            self.add_segemnt(position)
            

    def add_segemnt(self,position):
        new_segment=t.Turtle("square")
        new_segment.color("White")
        new_segment.penup()
        new_segment.goto(position)
        self.segment.append(new_segment)

    def extend_snake(self):
        self.add_segemnt(self.segment[-1].position())
    
    def move(self):
        for seg_num in range(len(self.segment)-1,0,-1):
            new_x=self.segment[seg_num-1].xcor()
            new_y=self.segment[seg_num-1].ycor()
            self.segment[seg_num].goto(new_x,new_y)
        self.segment[0].forward(move_distance)

    def up(self):
        if self.head.heading()!=down:
           self.head.setheading(up)
    def right(self):
        if self.head.heading()!=left:
           self.head.setheading(right)
    def left(self):
        if self.head.heading()!=right:
           self.head.setheading(left)
    def down(self):
        if self.head.heading()!=up:
           self.head.setheading(down)   