import turtle 

def squares():

  turtle.fd(100)
  turtle.left(90)
  turtle.fd(100)
  turtle.left(90)
  turtle.fd(100)
  turtle.left(90)
  turtle.fd(100)

  turtle.left(120)
  turtle.fd(200)
  turtle.left(90)
  turtle.fd(200)
  turtle.left(90)
  turtle.fd(200)
  turtle.left(90)
  turtle.fd(200)

def draw_square(length):
  turtle.fd(length)
  turtle.left(90)
  turtle.fd(length)
  turtle.left(90)
  turtle.fd(length)
  turtle.left(90)
  turtle.fd(length)
  turtle.left(90)


def draw_triangle(length):

  turtle.fd(length)
  turtle.left(120)
  turtle.fd(length)
  turtle.left(120)
  turtle.fd(length)
  turtle.left(120)

def shape_select():
  print('Enter the side length: ')
  length = int(input())
  print('Enter the shape type (S or s for square, T or t for triangle): ')
  shape = input()

  if(shape.lower() == 't'):
    draw_triangle(length)
  elif(shape.lower() == 's'):
    draw_square(length)
  else:
    print('Illegal shape type entered:', shape)

# Stretch

def round_it(value):
  if value > 0:
    value += 0.5
  else:
    value -= 0.5

  return int(value)


# Workout
def print_letters(num):
  number = {
    1: 'One',
    2: 'Two',
    3: 'Three',
    4: 'Four',
    5: 'Five',
    6: 'Six',
    7: 'Seven',
    8: 'Eight',
    9: 'Nine',
   }
  ans = len(number[num])

  print(ans)


def return_letters(num):
  number = {
    1: 'One',
    2: 'Two',
    3: 'Three',
    4: 'Four',
    5: 'Five',
    6: 'Six',
    7: 'Seven',
    8: 'Eight',
    9: 'Nine',
   }
  ans = len(number[num])

  return ans


def most_letters(an, bn, cn):
  number = {
    1: 'One',
    2: 'Two',
    3: 'Three',
    4: 'Four',
    5: 'Five',
    6: 'Six',
    7: 'Seven',
    8: 'Eight',
    9: 'Nine',
   }
  a1 = len(number[an])
  b1 = len(number[bn])
  c1 = len(number[cn])

  if (a1 > b1) and (a1 > c1):
    return number[an]
  elif (b1 > a1) and (b1 > c1):
    return number[bn]
  elif (c1 > a1) and (c1 > b1):
    return number[cn]
  else:
    print("Tie!")


  
# Challenge
def find_day():
  day_of_week_list = {
    0: 'Monday',
    1: 'Tuesday',
    2: 'Wedensday',
    3: 'Thursday',
    4: 'Friday',
    5: 'Saturday',
    6: 'Sunday',
   }
   
  print('Enter Month: ')
  month = int(input())
  print('Enter Day: ')
  day = int(input())
  print('Enter Year: ')
  year = int(input())
  
  if(month == 1):
    month = 13
    year -= 1
  elif(month == 2):
    month = 14
    year -= 1

  zeller_value = (day + 5 + ((26 * (month + 1)) // 10) + ((5 * (year % 100)) // 4) + ((21 * (year // 100)) // 4)) % 7

  day_of_week = day_of_week_list[int(zeller_value)]
  month = 13
  year -= 1
  key = str(month) + '/' + str(day) + '/' + str(year)

  print(key, 'is a', day_of_week)
  print(zeller_value)

find_day()
   