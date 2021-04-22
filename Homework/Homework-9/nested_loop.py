def sum_values(dct):
    total = 0
    for key in dct:
        if type(dct[key]) == int or type(dct[key]) == float:
            total += dct[key]
    return total

def max_dict(d1, d2):
    out = {}
    for key in d1:
        out[key] = d1[key]
    for key in d2:
        if key not in out or d2[key] > out[key]:
            out[key] = d2[key]
    return out
    
def print_matches(d1, d2):
    for key in d1:
        if key in d2 and d2[key] == d1[key]:
            print(key,':',d1[key])
    
def get_unique_values(lst):
    out = []
    for dct in lst:
        for key in dct:
            if dct[key] not in out:
                out.append(dct[key])
    return out

def remove_keys(mydict, keylist):
    for key in keylist:
        if key in mydict:
            del mydict[key]
    return mydict

def accept_login(users, username, password):
    return username in users and users[username] == password

def count_vowels(string):
    if string == '':
        return 0
    elif string[0] in 'aeiouAEIOU':
        return 1 + count_vowels(string[1:])
    else:
        return count_vowels(string[1:])

def count_digits(num):
    if num < 10:
        return 1
    else:
        return 1 + count_digits(num//10)

def merge(lst1, lst2):
    if lst1 == []:
        return lst2
    elif lst2 == []:
        return lst1
    elif lst1[0] < lst2[0]:
        return [lst1[0]] + merge(lst1[1:], lst2)
    else:
        return [lst2[0]] + merge(lst1, lst2[1:])

def merge_sort(lst):
    if len(lst) < 2:
        return lst
    left = merge_sort(lst[:len(lst)//2])
    right = merge_sort(lst[len(lst)//2:])
    return merge(left, right)