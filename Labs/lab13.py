import random, turtle, math
# Warm up
class Shape:
  '''
  Purpose: A class that defines the basic functionality of a shape
  Instance variables: 
    x (float) - x coordinate position
    y (float) - y coordinate position
    color (string) - random color 
  Methods: 
    __init__ - intializing the instance variables
    __str__ - gives an instance of the class a printable value
  '''
  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y
    self.color = random.choice(["red", "orange", "yellow",
                      "green", "blue", "purple"])
  def __str__(self):
    loc = "(x="+str(self.x)+", y="+str(self.y)+"), "
    col = self.color
    return loc + col
 
class Circle(Shape):
  '''
  Purpose: A child class of the parent class shape that describes a specific circle shape
  Instance variables: 
    x & y - previous instance variables from the Shape class
    rad - specific to the circle class, radius of the circle
  Methods: 
    __init__ - intializing the instance variables
    __str__ - gives an instance of the class a printable value
    draw - draws a circle using the turle class
  '''

  def __init__(self, x=0, y=0, rad=0):
    Shape.__init__(self,x,y)
    self.rad = rad
  def __str__(self):
    shape_str = Shape.__str__(self)
    return shape_str + ", rad="+str(self.rad)
  def draw(self,t):
    t.penup()
    t.setpos(self.x,self.y-self.rad)
    t.pendown()
    t.fillcolor(self.color)
    t.begin_fill()
    t.circle(self.rad)
    t.end_fill()
  def contains(self, x, y):
    distance = math.sqrt((self.x - x)**2 + (self.y - y)**2)
    if (distance < self.rad):
      return True
    else: 
      return False
      

# Stretch
class Rectangle(Shape):
  '''
  Purpose: A child class of the parent class shape that describes a specific circle shape
  Instance variables: 
    x & y - previous instance variables from the Shape class
    width - specific to the Rectangle class, width of the Rectangle
    height - specific to the Rectangle class, height of the Rectangle
  Methods: 
    __init__ - intializing the instance variables
    __str__ - gives an instance of the class a printable value
    draw - draws a rectangle using the turle class
  '''

  def __init__(self, x=0, y=0, width=0, height=0):
    Shape.__init__(self,x,y)
    self.width = width
    self.height = height
  def __str__(self):
    shape_str = Shape.__str__(self)
    return shape_str + ", width="+str(self.width)+ ", height="+str(self.height)
  def draw(self,t):
    t.penup()
    t.setpos(self.x,self.y)
    t.pendown()
    t.fillcolor(self.color)
    t.begin_fill()
    t.sety(t.ycor() + self.height)
    t.setx(t.xcor() + self.width)
    t.sety(t.ycor() - self.height)
    t.setx(t.xcor() - self.width)
    t.end_fill()
  def contains(self, x, y):
    if ((x > self.x) and (x < self.x+self.width)) and ((y > self.y) and (y < self.y+self.height)):
      return True
    else: 
      return False
    
 
class Display:
  '''
  Purpose: To display the the turtle class and associated actions
  Instance variables:
    shapes - list of shape or shape child objects
    t - instance of turtle class
  Methods: 
    __init__ - Intializes t and shapes, and sets up t to be displayed 
    mouse_event - takes in x and y coordinate float and listens for mouse click to get x and y coordinate to draw a shape 
  '''

  def __init__(self):
    # Player
    self.player = turtle.Turtle()
    self.player.showturtle()

    self.shapes = []
    self.t = turtle.Turtle()
    self.t.speed(0)
    self.t.hideturtle()
    turtle.delay(0)
    turtle.onscreenclick(self.mouse_event)
    turtle.onkeypress(self.move_up,'Up')
    turtle.onkeypress(self.move_down,'Down')
    turtle.onkeypress(self.move_right,'Right')
    turtle.onkeypress(self.move_left,'Left')
    turtle.listen()
    turtle.mainloop()  #Required for some IDEs
    

  def mouse_event(self,x,y):
    new_rect = Rectangle(x,y,random.randint(10,50), random.randint(10,50))
    new_circ = Circle(x,y,random.randint(10,50))
    shape_classes = [new_rect, new_circ]
    shape_choice = random.choice(shape_classes)
    can_draw = True
    for shape in self.shapes:
      if shape.contains(x, y):
        print(shape)
        self.remove(shape)
        can_draw = False
    if can_draw:
      self.shapes.append(shape_choice)
      shape_choice.draw(self.t)
  def remove(self, target):
    self.shapes.remove(target)
    self.t.clear()
    
  def move_up(self):
    self.player.seth(90)
    self.player.fd(10)
  def move_down(self):
    self.player.seth(270)
    self.player.fd(10)
  def move_right(self):
    self.player.seth(0)
    self.player.fd(10)
  def move_left(self):
    self.player.seth(180)
    self.player.fd(10) 

  def feast(self):
    return 0
    
      
    
 
Display()



# Workout
