import random, turtle, math

turtle.speed(0)
turtle.delay(0)


# Warm Up
def div27(num):
    for i in range(2,8):
        if num % i == 0:
          return True

    return False

def filled_square(side):
    r = random.random()
    g = random.random()
    b = random.random()
    turtle.color(r,g,b)
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(side)
        turtle.left(90)
    turtle.end_fill()
        
def spiro(num, side):
  i = 0
  while i < num:
    filled_square(side)
    turtle.left(360/num)
    i += 1



#Stretch
def mul1(a,b):
  answer = 0
  for i in range(b):
    answer += a
    i += 1
  return answer

def mul2(a,b):
  i = 0
  answer = 0
  while i < b:
    answer += a
    i += 1
  return answer

def exp(x,y):
  answer = 0
  for i in range(y):
    answer = mul1(x,x) 
  return answer

#Workout
def random_walk():
  for i in range(200):
    ran_num = random.randint(1,4)
    turtle.setheading(90 * ran_num)
    turtle.forward(20)

# def escape():
#   bounds = 150.0
#   for i in range(200):
#     if (turtle.xcor() <= -bounds) or (turtle.xcor() >= bounds) or (turtle.ycor() <= -bounds) or (turtle.ycor() >= bounds):
#       turtle.pu()
#       turtle.setpos(0,0)
#       turtle.write(i, font=("Arial", 20, "normal"))
#       break
#     ran_num = random.randint(1,4)
#     turtle.setheading(90 * ran_num)
#     turtle.forward(20)

def escape():
  bounds = 150.0
  i = 0
  while (turtle.xcor() >= -bounds) and (turtle.xcor() <= bounds) and (turtle.ycor() >= -bounds) and (turtle.ycor() <= bounds):
    ran_num = random.randint(1,4)
    turtle.setheading(90 * ran_num)
    turtle.forward(20)
    i += 1
  turtle.pu()
  turtle.setpos(0,0)
  turtle.write(i, font=("Arial", 20, "normal"))
  
turtle.hideturtle
def slice_of_pi(num):
  counter = 0
  
  for i in range(num):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    

    if math.sqrt(x*x + y*y) < 1.0:
      turtle.pu()
      turtle.goto(x * 150, y * 150)
      turtle.pd()
      turtle.color("green")
      turtle.dot(5)
      counter += 1
    else:
      turtle.pu()
      turtle.goto(x * 150, y * 150)
      turtle.pd()
      turtle.color("red")
      turtle.dot(5)
    
  print((counter/num) * 4)
  
slice_of_pi(1000)