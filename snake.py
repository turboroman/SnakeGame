from turtle import Turtle
INITIAL_SNAKE_SIZE = 3
MOVE_DISTANCE = 20
SEGMENT_SIZE = 0.8
SEGMENT_STEP = MOVE_DISTANCE * SEGMENT_SIZE
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_POSITIONS = [(0, 0), (-SEGMENT_STEP, 0), (-SEGMENT_STEP*2, 0)]


class Snake:
    def __init__(self):
        self.size = INITIAL_SNAKE_SIZE
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        t = Turtle()
        t.color('white')
        t.shape('square')
        t.turtlesize(SEGMENT_SIZE)
        t.penup()
        t.goto(position)
        self.segments.append(t)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(SEGMENT_STEP)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
