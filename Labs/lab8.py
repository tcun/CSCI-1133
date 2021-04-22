import math, turtle, random
# Warm Up

def print_matrix():
    mat = []

    for i in range(4):
        ls = [0,0,0,0]
        mat.append(ls)
        mat[i][i] = 5 
    print(mat)


# Stretch

def dist(a, b):
  return math.sqrt(((b[1] - a[1])**2) + ((b[0] - a[0])**2))

def shortest_dist(coords):
  shortest = dist(coords[0], coords[1])
  for i in range(len(coords)):
    for j in range(len(coords) - i - 1):
      distance = dist(coords[i], coords[j+i+1])
      if distance < shortest: 
        shortest = distance
  return shortest
    

print(shortest_dist([[8,-5], [0,9], [8,1], [3,4], [-10,-4]]))
print(shortest_dist([[45, -99], [24, 83], [-48, -68], [-97, 99],
		 [-8, -77], [-2, 50], [44, 41], [-48, -58], 
		 [-1, 53], [14, 86], [31, 94], [12, -91], 
		 [33, 50], [82, 72], [83, -90], [10, 78],
		 [7, -22], [90, -88], [-21, 5], [6, 23]]))

# Work-out

def turtle_race(num_turtles):
    # Make the window boundaries (0,0) and (100,100)
    turtle.setworldcoordinates(0,0,100,100)
    turtle.delay(0)
    turtle_list = []
    #Draw the finish line
    turtle.setpos(90, -100)
    turtle.setpos(90, 200)
    for i in range(num_turtles):
        tr = turtle.Turtle()
        tr.speed(0)
        tr.shape('turtle')
        r = random.random()
        g = random.random()
        b = random.random()
        tr.color(r,g,b)
        tr.penup()
        #Try to spread turtles out evenly
        y = 10 + 80*i/(num_turtles-1)
        tr.setpos(10, y)
        tr.pendown()
        turtle_list.append(tr)
        
    while(all(x.xcor() < 90 for x in turtle_list)):
      for i in range(num_turtles):
        turtle_list[i].forward(random.randint(1,5))
    for i in turtle_list:
      if i.xcor() >= 90:
        i.turtlesize(3)

turtle_race(5)
