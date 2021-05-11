import turtle, math, random
'''
Inital Notes:
Controls:
    - P - Player 1 Hit
    - Q - Player 2 Hit
    - Up Arrow - Add Strength
    - Down Arrow - Remove Strength
Three Features I added:
    - Controllable strength through the up and down arrow keys, Max is 3, minimum is 1 
    - Local Multiplayer - Key to hit starts with P and is followed by Q, repeating
    - Scores are added above each side when the opposing side lets the ball bounce twice

'''
class Ball(turtle.Turtle):
    '''
    Purpose: Simulate a moving ball through the turtle class that is affected by gravity and can be interacted with
    Instance variables: 
        _xPos = Intial X Position
        _yPos = Intial Y Position
        _xVel = Intial X Velocity / Change in X Position
        _yVel = Intial y Velocity / Change in y Position
    Methods: 
        __init__() = intializes instance variables 
        move() = Cause the ball to be moved based on the X and Y Velocities, simulate gravity, and to count bounces
        hit() = Reverse the balls x Velocity and reset ball counter
        reset() = reset the balls position and velocity to random numbers 
        addStrength() = increase balls hit velocity 
        removeStrength() = decrease balls hit velocity 
    '''
    def __init__(self, _xPos, _yPos, _xVel, _yVel):
        turtle.Turtle.__init__(self)
        self.penup()
        self.x_pos = _xPos
        self.y_pos = _yPos
        self.x_vel = _xVel
        self.y_vel = _yVel
        self.bounceCounter = 0
        self.shape('circle')
        self.turtlesize(0.3)
        self.strength = 1
        self.setpos(self.x_pos, self.y_pos)
        self.hasScored = False
        self.coordBeforeBounce = self.xcor() 

    def move(self):
        gravity = 0.981
        self.y_vel -= gravity
        self.x_pos = self.xcor() + self.x_vel
        if self.y_pos > 0:
            self.y_pos = self.ycor() + self.y_vel
        else:
            self.y_pos *= 0.75
            self.y_vel *= -0.75
            self.y_pos = self.ycor() + self.y_vel
            self.bounceCounter += 1
            self.coordBeforeBounce = self.xcor() 
            if self.bounceCounter > 1:
                self.reset()
                self.bounceCounter = 0
                self.hasScored = True;
        self.goto(self.x_pos,  self.y_pos)
    def hit(self):
        self.x_vel *= -1
        self.y_vel = 5 + (5 * self.strength)
        self.bounceCounter = 0
    def reset(self):
        self.x_pos = random.randint(-100, 100)
        self.y_pos = random.randint(90, 200)
        self.goto(self.x_pos,  self.y_pos)
        self.x_vel = random.randint(6, 12)
        self.y_vel = random.randint(4, 10)
    def addStrength(self):
        self.strength = self.strength + 1 if self.strength < 3 else 3
    def removeStrength(self):
        self.strength = self.strength - 1 if self.strength > 1 else 1

        
class Game():
    '''
    Purpose: A game structure that allows interacting with the ball class to simulate a game of tennis 
    Instance variables: 
        None, just self
    Methods: 
        __init__() = intializes instance variables 
        gameloop() = a loop that constantly moves the ball, checks for score updates, checks for control inputs, and determiens if ball hit net
        drawcourt() = intial function that draws the court
        hitTurn() = Alternates the hitKey for Player 1 and Player 2
        updateScore() = Clears the current score, and writes the new score depending on where the ball landed
    '''
    def __init__(self):
        self.rightScore = 1
        self.leftScore = 1

        self.rightref = turtle.Turtle()
        self.leftref = turtle.Turtle()

        self.hitkey = "p"
        self.screen = turtle.Screen()
        turtle.delay(0)
        turtle.tracer(0,0)
        turtle.setworldcoordinates(-500, -500, 500, 500)
        self.drawCourt()
        self.ball = Ball(random.randint(-100, 100), random.randint(30, 100), random.randint(6, 12), random.randint(4, 10))
        
        turtle.update()
        self.gameloop()
        turtle.mainloop()

        
    def gameloop(self):
        self.ball.move()
        self.screen.onkey(self.hitTurn, self.hitkey)
        self.updateScore()
        turtle.onkeypress(self.ball.addStrength, "Up")
        turtle.onkeypress(self.ball.removeStrength, "Down")
        turtle.listen()
        if self.ball.xcor() == 0 and self.ball.ycor() < 30:
            self.ball.reset()
        turtle.update()
        turtle.ontimer(self.gameloop, 30)
    def drawCourt(self):
        ref = turtle.Turtle()
        ref.hideturtle()
        ref.sety(ref.ycor() + 30)
        ref.penup()
        ref.setpos(-400, 0)
        ref.pendown()
        ref.setpos(400, 0)
    def hitTurn(self):
        self.screen.onkey(None, self.hitkey)
        self.ball.hit()
        self.hitkey = "p" if self.hitkey != "p" else "q"
        self.screen.onkey(self.hitTurn, self.hitkey)
    def updateScore(self):
        self.rightref.hideturtle()
        self.rightref.penup()
        self.leftref.hideturtle()
        self.leftref.penup()
        if self.ball.hasScored:
            if self.ball.coordBeforeBounce > 0:
                self.leftref.clear()
                self.leftref.setpos(-200, 200)
                self.leftref.write(self.leftScore)
                self.leftScore += 1
            else:
                self.rightref.clear()
                self.rightref.setpos(200, 200)
                self.rightref.write(self.rightScore)
                self.rightScore += 1
        self.ball.hasScored = False
        

def main():
    game = Game()


if __name__ == '__main__':
    main()
