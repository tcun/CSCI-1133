# Warm up
'''
mystery([5, 3, 7]) returns [5-5] + mystery([3, 7] )
  mystery[3, 7] returns [3-5] + mystery([7])
   mystery([7]) return [7-5] + mystery[]
    mystery[] returns []
   mystery([7]) return [2] + [empty]
  mystery[3, 7] returns [-2] + [2]
mystery([5, 3, 7]) returns [0] + [-2] + [2]
This is all returned in a list so [0, -2, 2]
'''
# Subtracts 5 from each index in list
# Base case is : if lst == []: return []
# No, because after hits base case it moves towards the first function call

def mystery(lst):
  if lst == []:
    return []
  else:
    return [lst[0]-5] + mystery(lst[1:])

def mystery_loop(lst):
  for i in range(len(lst)):
    lst[i] -= 5
  return lst

# print(mystery([5, 3, 7]))
# print(mystery_loop([5, 3, 7]))

def sum_list(lst):
  if lst == []:
    return 0
  else:
    return lst[0] + sum_list(lst[1:])

# print(sum_list([1,2,3,4,5]))

def reverse_string(word):
  if word == "":
    return ""
  else:
    return word[-1] + reverse_string(word[:-1])

# print(reverse_string("word"))

# Stretch
def fib(n):
  if n <= 1:
    return n
  else:
    return fib(n-1) + fib(n-2)

# print(fib(20))

def double_reverse(str_lst):
  if str_lst == []:
    return []
  else:
    return [reverse_string(str_lst[-1])] + double_reverse(str_lst[:-1])

# print(double_reverse(['these', 'words', 'will', 'be', 'reversed']))


# Workout
def flat_square(lst):
  if lst == []:
    return lst
  if type(lst[0]) == int:
    lst[0] = lst[0]**2
  else:
    return flat_square(lst[0]) + flat_square(lst[1:])
  return lst[:1] + flat_square(lst[1:])
  
print(flat_square([-7, [2, 5, [-3], [], [[5, 7], 1]], -7]))


