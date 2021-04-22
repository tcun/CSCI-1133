import turtle

class Rational:
  def __init__(self,num=0,den=1):
    self.numerator = num
    if den == 0:
      self.denominator = 1
    else:
      self.denominator = den

  def __str__(self):
    if self.numerator >= 1:
      if self.denominator == 1:
        return str(self.numerator)
      return str(self.numerator) + '/' + str(self.denominator)
    else:
      return str(0)

# num1 = Rational(3,4) 
# num2 = Rational(1,3)
# print(num1)

# num3 = Rational()
# print(num3)

#Warm-up

num2 = Rational(5,1)
print(num2)
	

num3 = Rational(0,3)
print(num3)


num4 = Rational(4,2)
print(num4)

#Stretch
class Vec2(object):
  def __init__(self, num1=0.0, num2=0.0):
    self.x = num1
    self.y = num2

  def __str__(self):
    return "<" + str(self.x) + ", " + str(self.y) + ">"

  def __add__ (self, vec):
    return Vec2(self.x + vec.x, self.y + vec.y)

  def __mul__(self, vec):
    if isinstance(vec, Vec2):
      return Vec2(self.x * vec.x, self.y * vec.y)
    else:
      return Vec2(self.x * vec, self.y * vec)
  
  def get_values(self):
    return [self.x, self.y]
  
  def set_values(self, vecLs=list()):
    self.x = vecLs[0]
    self.y = vecLs[1]

# if __name__ == '__main__':
#     mass = 0.5
#     accel1 = Vec2(1, 2)
#     print(accel1) #should output <1, 2>
#     accel2 = Vec2(2, -2)
#     total_accel = accel1 + accel2
#     print(total_accel) #should output <3, 0>
#     force = total_accel * mass
#     flist = force.get_values()
#     print(flist) #should output [1.5, 0.0]
#     accel1.set_values(flist)
#     print(accel1) #should output <1.5, 0.0>

#Workout
class Particle:
  def __init__(self, mass, pos, vel):
    self.mass = mass #this is a float or int
    self.pos = pos #this is a Vec2 object
    self.vel = vel #this is a Vec2 object
    self.t = turtle.Turtle()
    self.t.shape("circle")
    self.t.speed(0)
    self.t.penup()
    self.move()  #uncomment this after you implement move()
    self.t.pendown()

  def __str__(self):
    return "mass:" + str(self.mass) + ", pos:<" + str(self.pos.x) + "," + str(self.pos.y) + ">" + ", vel:<" + str(self.vel.x) + "," + str(self.vel.y) + ">"
  
  def move(self):
    self.t.setpos(self.pos.x, self.pos.y)

  def accelerate(self, a, t):
    self.vel.y = self.vel.y + a.y*t
    self.vel.x = self.vel.x + a.x*t

    self.pos.y = self.pos.y + (self.vel.y * t) + a.y*((t**2) * 0.5)
    self.pos.x = self.pos.x + (self.vel.x * t) + a.x*((t**2) * 0.5)
    
    self.move()
    
if __name__ == '__main__':
    p1 = Particle(50,Vec2(-200,-50),Vec2(30,30))
    p2 = Particle(20,Vec2(100,50),Vec2(-20,0))
    print(p2) #should output mass:20, pos:<100, 50>, vel:<-20, 0>
    p2.accelerate(Vec2(0,-10),2)
    print(p2) #should output mass:20, pos:<60.0, 30.0>, vel:<-20, -20>
    p2.accelerate(Vec2(20,20),3)
    print(p2) #should output mass:20, pos:<90.0, 60.0>, vel:<40, 40>
    for i in range(100):
        p1.accelerate(Vec2(0,-10),0.1)
        p2.accelerate(Vec2(0,-10),0.1)
    print(p1) #should output mass:50, pos:<100.0, -250.0>, vel:<30.0, -70.0>
    print(p2) #should output mass:20, pos:<490.0, -40.0>, vel:<40.0, -60.0>

