import random

#---------------------- Stretch -------------------------------------
project_scores = {'Adel':15, 'Barb':23, 'Tim':13, 'Xue':18, 'Sally':12}

def dict_practice():
  print(project_scores)

  print(project_scores['Barb'])
  project_scores['Vlad'] = 19
  project_scores.pop('Tim')
  # or del project_scores['Tim']
  project_scores['Sally'] = 13

  print(project_scores)


def assign_average_pair(score_dict, name1, name2):
    
    '''
    Purpose: Find average of two student's scores, change scores to that average
    Input Parameter(s): Names and grades of each student
    Return Value: None
    '''
    total = score_dict[name1] + score_dict[name2]
    avg = total / 2
    score_dict[name1] = avg
    score_dict[name2] = avg
    print("New dictionary:", score_dict) 

# ---------------------- WORKOUT -------------------------------------
def fill_in(responses):
  print('In the 1800s, Ada Lovelace worked with Charles Babbage on a', responses[0], 'engine.')
  print('While the machine was never', responses[1], 'her notes include an algorithm intended for it.')
  print('For this, many consider her to be the first computer', responses[2], '.')

def fill_in_input():
  responses = input('Enter an adjective: ')
  responses1 = input('Enter a past-tense verb: ')
  responses2 = input('Enter a noun: ')
  
  print('In the 1800s, Ada Lovelace worked with Charles Babbage on a', responses, 'engine.')
  print('While the machine was never', responses1, 'her notes include an algorithm intended for it.')
  print('For this, many consider her to be the first computer', responses2, '.')

# ---------------------- Challenge ------------------------------------
def roll():
  counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  # counts[i] represents how many times a total of i was rolled.
  # This means that counts[0] and counts[1] should always be 0,
  # since you can't roll a total of 0 or 1 with the sum of two
  # 6-sided dice.

  for i in range(100):
      roll_one = random.randint(1,6)
      roll_two = random.randint(1,6)
      total = roll_one + roll_two
      counts[total] += 1
      # print("Rolled a", total, " (",roll_one,"+",roll_two,")")

  print("Final list:", counts)
  print('')
  print("2s:", counts[2])
  print("3s:", counts[3])
  print("12s:", counts[-1])
  print('')

def roll_dict():
  counts = {'0s': 0, '1s': 0, '2s': 0, '3s': 0, '4s': 0, '5s': 0,'6s': 0, '7s': 0, '8s': 0, '9s': 0, '10s': 0, '11s': 0, '12s': 0}
  # counts[i] represents how many times a total of i was rolled.
  # This means that counts[0] and counts[1] should always be 0,
  # since you can't roll a total of 0 or 1 with the sum of two
  # 6-sided dice.

  for i in range(100):
      roll_one = random.randint(1,6)
      roll_two = random.randint(1,6)
      total = roll_one + roll_two
      key = str(total) + 's'
      counts[key] += 1
      # print("Rolled a", total, " (",roll_one,"+",roll_two,")")
  print('')
  print("Final list:", counts)
  print('')
  print("2s:", counts['2s'])
  print("3s:", counts['3s'])
  print("12s:", counts['12s'])
  print('')

 

# dict_practice()
# print('')
# assign_average_pair(project_scores, 'Adel', 'Sally')

# fill_in(['computational', 'constructed', 'programmer'])
# fill_in_input()
roll()
roll_dict()
