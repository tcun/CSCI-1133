
import platform

# Version Confirmation
vers = platform.python_version()
assert vers[0] == '3', "You must use Python 3, " + vers + " is not acceptable"
print("Python 3 confirmed.")

# User Input for amount of Cookies
num_cookies = input("How many cookies do you want to make?\n")
# Calculations to convert reciple multiplier (recipe_mult) into grams of individual ingredients
recipe_mult = int(num_cookies) / 12
butter = str(125*recipe_mult) + "g butter"
sugar = str(225*recipe_mult) + "g sugar"
eggs = str(max(1 , round(recipe_mult))) + " eggs"
vanilla = str(recipe_mult) + " tsp vanilla extract"
flour = str(225*recipe_mult) + "g flour"
salt = str(0.5*recipe_mult) + " tsp salt"
chips = str(200*recipe_mult) + "g chocolate chips"
# Prints above-defined ingredient variables
print(butter)
print(sugar)
print(eggs)
print(vanilla)
print(flour)
print(salt)
print(chips)

# Input for amount of loan, duration in months, and annual interest rate from the loan
amt = float(input("Enter the loan amount in dollars: \n"))
N = int(input("Enter the loan duration in months: \n"))
r = int(input("Enter the % annual interest rate: ")) / 100 / 12
# Calculates total monthly payment value (payment)
payment = (r*amt)/ (1 - ((1+r)**(-N)))
# Prints total monthly payment value (payment)
print("Your monthly payment is:", round(payment,2))


# Office Hours (leave these lines commented out, this isn't Python code)
# Name of the TA who you visited in office hours: Ahmed Shahkhan
# Above TA's favorite color: Blue
