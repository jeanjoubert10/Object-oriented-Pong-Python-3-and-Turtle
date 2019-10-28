import turtle

win = turtle.Screen()
win.setup(800, 600)
win.title('Object oriented programming Pong Python 3 and Turtle')
win.bgcolor('black')
win.tracer(0)
win.listen()

class Paddle(turtle.Turtle):
    def __init__(self, xpos):
        super().__init__(shape='square')
        self.up()
        self.shapesize(5,1)
        self.color('white')
        self.xpos = xpos
        self.goto(xpos, 0)
        

    def move_up(self):
        if self.ycor() < 250:
            self.goto(self.xcor(), self.ycor()+40)

    def move_down(self):
        if self.ycor() > -250:
            self.goto(self.xcor(), self.ycor()-40)

        
class Ball(turtle.Turtle):
    def __init__(self, paddle1, paddle2, score):
        super().__init__(shape='circle')
        self.up()
        self.color('blue')
        self.dx, self.dy = 5,5
        self.paddle1 = paddle1
        self.paddle2 = paddle2
        self.score = score
        self.score1 = 0
        self.score2 = 0
        
    def move(self):
        self.goto(self.xcor()+self.dx, self.ycor()+self.dy)

        # Score player 2
        if self.xcor()<-400:
            self.goto(0,0)
            self.dx *= -1
            self.score2 += 1
            self.score.clear()
            self.score.write(f'Player 1: {self.score1}  Player 2: {self.score2}', align='center',
                             font=('Courier', 24, 'normal'))
        # Score player 1
        if self.xcor()>400:
            self.goto(0,0)
            self.dx *= -1
            self.score1 += 1
            self.score.clear()
            self.score.write(f'Player 1: {self.score1}  Player 2: {self.score2}', align='center',
                             font=('Courier', 24, 'normal'))
            
                     
        if self.ycor()<-280 or self.ycor()>280:
            self.dy *= -1
            
    def bounce_paddle(self):

        # Paddle2
        if self.xcor()+10 >= 340 and self.dx > 0:
            if self.ycor()+10 >= self.paddle2.ycor()-50 and self.ycor()-10<= self.paddle2.ycor()+50:
                self.dx *= -1
                
        # Paddle1
        if self.xcor()-10 <= -340 and self.dx < 0:
            if self.ycor()+10 >= self.paddle1.ycor()-50 and self.ycor()-10<= self.paddle1.ycor()+50:
                self.dx *= -1

        
class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.up()
        self.hideturtle()
        self.color('red')
        self.goto(0, 260)
        self.write(f'Player 1: 0  Player 2: 0', align='center', font=('Courier', 24, 'normal'))

           
score = Scoreboard()               
paddle1 = Paddle(-350)
paddle2 = Paddle(350)
ball = Ball(paddle1, paddle2, score)


win.onkey(paddle1.move_up, 'w')
win.onkey(paddle1.move_down, 's')
win.onkey(paddle2.move_up, 'Up')
win.onkey(paddle2.move_down, 'Down')

while True:
    win.update()
    ball.move()
    ball.bounce_paddle()
    
    
 
