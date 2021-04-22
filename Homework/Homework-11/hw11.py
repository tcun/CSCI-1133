import os


def count_e_vs_t(path):
    '''
    Purpose: Find the difference between the occurences of the characters e and t in the entirety of the directory
    Input Parameter(s):
        path (string) - Name of beginning path of a directory 
    Return Value: Returns an int of the difference between the occruences of the characters e and t 
    '''

    total = 0
    
    for file in os.listdir(path): 
        if os.path.isfile(path+'/'+file):
            filepath = path+'/'+file  #This is a file, print out the pat
            with open(filepath, 'r') as fp:
                text = fp.read()
                text = text.lower()
                total += text.count("e") - text.count("t")
        else:
            count_e_vs_t(path+'/'+file)  #Go into a subdirectory
    return total
     
    

print(count_e_vs_t("docs1"))
print(count_e_vs_t('docs2'))
print(count_e_vs_t('docs3'))

def palindrome(word):
    '''
    Purpose: A function that checks whether a word or phrase is a palindrome
    Input Parameter(s):
        word (string) - the word being checked if it is a palidrome
    Return Value:
        return true or false depending on whether the word is a palindrome 
    '''
    if " " in word:
        return (palindrome(word.replace(" ", "")))
    try:
        if word[0] != word[-1]:
            return False
    except IndexError:
        return True
    if len(word) <= 1:
        return True
    return palindrome(word[1:-1])

# print(palindrome(''))
# print(palindrome('a'))
# print(palindrome('abba'))
# print(palindrome('telat'))
# print(palindrome("madam im adam"))

def collatz(num):
    '''
    Purpose: Take a single positive integer and return a list of numbers in the form of the collatz sequence from your input to 1
    Input Parameter(s):
        num (int) - Positve int that is the beginning of the sequence
    Return Value: Returns a list from num to 1 in the form of the collatz sequence
    '''
    if num == 1:
        return [1]
    elif num % 2 == 0:
        temp = num // 2
    elif num % 2 == 1:
        temp =  num * 3 + 1
    return [num] + collatz(temp)

# print(collatz(5))
# print(collatz(1))
# print(collatz(123))



