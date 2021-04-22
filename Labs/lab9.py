# Warm-Up
import random, turtle

def wordcount(fname):
  try:
    with open(fname) as fp:
      text = fp.read()
      ln = text.split()
    return len(ln)
  except FileNotFoundError:
    return -1

# print(wordcount("no.py"))
# print(wordcount("test.txt"))
# print(wordcount("asdf.txt"))

def warmup_example():
  try:
    x = int(input("Enter a number"))
    z = 2/x
    print("Good job, no errors")
  except ValueError:
    print("Input was not an integer, setting z to -1")
    z = -1
  except ZeroDivisionError:
    print("Can't divide by 0, setting z to -2")
    z = -2
  print(z)

# Stretch
def make_data(fname):
  with open(fname, 'w') as fp:
    for i in range(1, 101):
      ln = str(i) + "," + str(random.randint(-1000,1000)) + "\n"
      fp.write(ln)

def read_data(fname):
  with open(fname) as fp:
    text = fp.readlines()

    minimum = 1000
    maximum = 0

    for ln in text:
      data = ln.split(",")
      if minimum > int(data[1]):
        minimum = int(data[1])
      if maximum < int(data[1]):
        maximum = int(data[1])
  print("Minimum: " + str(minimum) + " Maximum: " + str(maximum))

# read_data('text.csv')

# Workout
def stock_data(fname):
  with open(fname) as fp:
    text = fp.readlines()

    minimum = 1000
    maximum = 0
    lst = []
    for ln in range(1, len(text)):
      data = text[ln].split(",")
      lst.append(data[4])
      if minimum > float(data[4]):
        minimum = float(data[4])
      if maximum < float(data[4]):
        maximum = float(data[4])

    x = len(lst)/2
    if (len(lst) % 2) == 0:
      median = lst[int(x)]
    else:
      median = (float(lst[int(x)]) + float(lst[int(x+1)])) / 2
    total = 0
    for num in range(len(lst)):
      total += float(lst[num])
    mean = total / (len(lst))

  print("Minimum: " + str(minimum) + " Maximum: " + str(maximum))
  print("Mean: " + str(mean) + " Median: " + str(median))

# stock_data('MDT.csv')

# Challenge

def graph_data(fname):
  turtle.setworldcoordinates(0,0, 100,200)
  turtle.penup()
  r = random.random()
  g = random.random()
  b = random.random()
  turtle.color(r,g,b)
  with open(fname) as fp:
    text = fp.readlines()
    day = 0.0
    for ln in range(1, len(text)):
      if day != 100:
        data = text[ln].split(",")
        turtle.sety(float(data[4]))
        turtle.setx(day)
        turtle.pendown()
      else:
        break
      day += 1

graph_data("MDT.csv")
graph_data("MMM.csv")
graph_data("TGT.csv")


def eq():
  with open('2.5_day.csv', "r") as fp:
    text = fp.readlines()
  total = []
  for i,line in enumerate(text):
    words = line.split(',')
    result = []

    if i == 0:
      for j, v in enumerate(words):
        print(j, v.rstrip())
      print()
    else:
      for j in range(len(words)):
        if '' == words[j]:
          result.append(words[j])
        elif '"' == words[j][0]:
          result.append(words[j] + "," + words[j+1])
        elif '"' == words[j][-1]:
          pass
        else:
          result.append(words[j].rstrip())
      v = result[13].strip('\"')
      x = v.find(" of ")
      if x == -1:
          x = -4
      item = result[4] + " " +result[13][x+4:].strip('\"')
      total.append(item)
  total.sort()
  for i in range(len(total)):
    print(total[i])

eq()
