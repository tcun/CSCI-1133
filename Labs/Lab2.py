import math
import turtle

def warm_up():
  x = math.tan(math.radians(25)) * 10
  print(x)

def stretch():
  num = int(input('Enter a 4 digit number: ', ))
  ones = num % 10
  tens = (num // 10) % 10  
  hunds = (num // 100) % 10
  thous = num // 1000
  rev = str(ones) + str(tens) + str(hunds) + str(thous)

  print("Ones digit is", ones)
  print ("Tens digit is", tens)
  print("Hundreds digit is", hunds)
  print("Thousands digit is", thous)
  print("Original number reversed is", rev)

def windChill():
  
  t = float(input('Enter temperature in degrees Fahrenheit: ', ))
  v = float(input('Enter wind velocity in miles/hour: '))
  windChill = 35.74 + (0.6215 * t) - (35.75 * (v ** .16)) + 0.4275 * t * (v ** .16)
  
  print('Wind Chill Temperature: ', windChill)

def changeConverter():
  dollars = int(input("Enter dollars: ",))
  cents = int(input("Enter cents: ",))
  total = (dollars * 100) + cents

  quarter_amt = (total // 25) % 10
  dime_amt = (total // 10) % 10
  nickel_amt = (total // 5) % 10
  penny_amt = (total % 10)

  print(quarter_amt, "Quarters")
  print(nickel_amt, "Nickels")
  print(dime_amt, "Dimes")
  print(penny_amt, "Pennies")

def Olympics():
  ydownchange = 25
  xchange = 28
  turtle.pensize(3)
  turtle.showturtle()
  turtle.penup()
  turtle.setpos(turtle.xcor() - 60, turtle.ycor())
  turtle.pendown()
  turtle.color('blue')
  turtle.circle(25)
  turtle.penup()
  turtle.setpos(turtle.xcor() + xchange, turtle.ycor() - ydownchange)
  turtle.pendown()
  turtle.color('yellow')
  turtle.circle(25)
  turtle.penup()
  turtle.setpos(turtle.xcor() + xchange, turtle.ycor() + ydownchange)
  turtle.pendown()
  turtle.color('black')
  turtle.circle(25)
  turtle.penup()
  turtle.setpos(turtle.xcor() + xchange, turtle.ycor() - ydownchange)
  turtle.pendown()
  turtle.color('green')
  turtle.circle(25)
  turtle.penup()
  turtle.setpos(turtle.xcor() + xchange, turtle.ycor() + ydownchange)
  turtle.pendown()
  turtle.color('red')
  turtle.circle(25)
  turtle.penup()

Olympics()