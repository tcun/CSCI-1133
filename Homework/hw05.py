import random
# Problem A: six_tails
def six_tails():
  '''
    Purpose:
      Count the number of iterations it takes to hit 6 tails in a row
    Input Parameter(s):
      counter (Int) - Counter to count the numbr of tails in row
      flip (Int) = Random int between 0 and 1 to represent the two sides of a coin, 0 = Tails & 1 = heads
      total_iterations (Int) - Count the total number of times the loop iterates through 
    Return Value:
      returns the total number of iterations (Int)
  '''
  counter = 0
  total_iterations = 0
  while counter < 6:
    flip = random.randint(0, 1) 
    if flip == 0: 
      counter += 1
    else: 
      counter = 0
    total_iterations += 1
  return total_iterations

# Problem B: average_six
def average_six(n):
  '''
    Purpose:
      Find the estimated average value of the number of times it takes to get 6 tails in a row
    Input Parameter(s):
      total (Int) - Total sum of all the iterations from the six_tails() function
      n (Int) = Number of times to run the sequence and averaged
    Return Value:
      Returns the total iterations divided by n 
  '''
  total = 0
  for i in range(n):
    total += six_tails()
  return total / n


# Problem C: population
def population(small, middle, big):
    '''
      Purpose:
        To simulate the change of population between three different sizes in a lake 
      Input Parameter(s):
        small (Int) - Number of smallfish
        middle (Int) - Number of middlefish
        big (Int) - Number of bigfish
      Return Value:
        Returns the amount of weeks for a population to die off or 30 if simulation goes longer than 30 weeks
    '''
    week_counter = 0
    while small >= 10 and middle >= 10 and big >= 10 and week_counter < 30:
      small = int(1.1*small - 0.0002*small*middle)
      middle = int(0.95*middle + 0.0001*small*middle - 0.00025*middle*big)
      big = int(0.9*big + 0.0002*middle*big)
      print("Week", week_counter + 1, "- Small:", small, "Middle:", middle, "Big:", big)
      week_counter += 1
    return week_counter


# Problem D: find_password
def find_password(filename):
    '''
    Purpose:
      Given an encrypted file, tries every possible four letter lowercase
      password for that file until one works, and then returns the password.
    Input Parameter(s):
      filename is a string representing the name of the encrypted file.
      The file must be in the same folder as this script.
    Return Value:
      Returns the password that successfully decrypts the given file
    '''
    fp = open(filename)
    data = fp.read()

    #TODO: Try all possible four letter passwords, not just 'pwnd'
    for i in range(97, 123):
        for j in range(97, 123):
            for k in range(97, 123):
                for u in range(97, 123):
                    password = chr(i) + chr(j) + chr(k) + chr(u)
                    if decrypt(data, password):
                        return password
    return False
    

#DO NOT EDIT ANYTHING BELOW THIS LINE
#Below are helper functions used for decrypting the text files.
#You don't have to understand how any of these work.

def decrypt(data, password):
    '''
    Purpose:
      Check whether the password is correct for a given encrypted
      file, and print out the decrypted contents if it is.
    Input Parameter(s):
      data is a string, representing the contents of an encrypted file.
      password is a four letter lowercase string, representing the password
      used to encrypt/decrypt the file contents.
    Return Value:
      Returns True if the password is correct and the file contents
      were printed.  Returns False and prints nothing otherwise.
    '''
    data = data.split('\n')
    if encode(password) == int(data[0]):
        print(vigenere(data[1],password))
        return True
    return False

def encode(key):
    '''
    Purpose:
      Turn a password into a ~9 digit number
    Input Parameter(s):
      key is a four letter string representing a password
    Return Value:
      Returns a number between 0 and 547120140, using modular exponentiation
      to make it difficult to reverse engineer the password from the number.
    '''
    total = 0
    for ltr in key:
        total += ord(ltr)
        total *= 123
    return pow(total,2011,547120141)

def vigenere(msg,key):
    '''
    Purpose:
      Decipher a message using the Vigenere cipher
    Input Parameter(s):
      msg a string, representing the encrypted message
      key is a four letter string, representing the cipher key
    Return Value:
      Returns a string representing the deciphered text
    '''
    i = 0
    out_msg = ''
    for ltr in msg:
        out_msg += chr((ord(ltr)-ord(key[i]))%28 +97)
        i = (i+1)%len(key)
    return out_msg.replace('{',' ').replace('|','.')


