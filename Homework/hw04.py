
def compute_tax(married, taxable_income):
    '''
    Purpose: Compute the amount of tax owed depending on marrital status and amount of income
    Input Parameter(s): 
    married (Boolean) - True or false value to determine if they are married
    taxable_income (Float or Int) - Amount of income inputed into function
    tax (Float) - Amount of tax owed
    Return Value: Tax is the return value for amount of tax owed 
    '''
    if (married != True) and (taxable_income > 0):
        if taxable_income <= 40000:
            tax = taxable_income * 0.1
        elif (taxable_income > 40000) and (taxable_income <= 160000):
            tax = 4000 + ((taxable_income - 40000) * 0.2)
        elif (taxable_income > 160000):
            tax = 28000 + ((taxable_income - 160000) * 0.3)
    elif taxable_income > 0:
        if taxable_income <= 40000:
            tax = taxable_income * 0.1
        elif (taxable_income > 40000) and (taxable_income <= 320000):
            tax = 8000 + ((taxable_income - 80000) * 0.2)
        elif (taxable_income > 320000):
            tax = 56000 + ((taxable_income - 320000) * 0.3)
    return round(tax, 2)

def choice(text, optionA, optionB, optionC):
    '''
    Purpose: A function that prints all the options, then asks for input to choose one of the given options
    Input Parameter(s): 
    text (String) - Introduction text phrase to describe situation for the options
    optionA, optionB, optionC (String) - Option inputs 
    Return Value: Then return the value of the input, or default 'A' if invalid input
    '''
    print(text, "\n")
    print('A.', optionA)
    print('B.', optionB)
    print('C.', optionC)

    invalid = False
    user_input = str(input())
    if (user_input == 'A'):
        resp = 'A'
    elif (user_input == 'B'):
        resp = 'B'
    elif (user_input == 'C'):
        resp = 'C'
    else:
        invalid = True
        resp = 'A'
    
    if(invalid):
        print('Invalid option, defaulting to A')
        return resp
    else:
        return resp

def adventure():
    '''
    Purpose: A function that is a user-interactive text based rpg, simplified to a small path
    Input Parameter(s): 
    state1, state2, state3, state4 (Functions) - Variables that hold the prints and return value in the choice() function
    Return Value: Return True or False depending on the route chosen
    '''
    state1 = choice("You sneak into the dragon's lair, with your comrades Wizard McBlastyFace and Stella the Bard.  The dragon is fast asleep.", "Tell your team to start stealing things", "Tickle the dragon on the nose", "Tell your team to prepare for battle")

    if state1 == 'A':
        state2 = choice("You can't carry the entire hoard of loot", "Take the pile of silk in the corner", "Take as much gold as you can carry", "Fight the dragon")
        if state2 == 'A':
            print("You sucessfully take the silk!")
            return True
        elif state2 == 'B':
            state4 = choice("Stella trips over a rock and the dragon wakes up.", "CHARGE!", "Tell Stella to sing to the dragon", "Run away")
            if state4 == 'A':
                print("The dragon is so surprised by the stupidity of your attack that it dies of laughter.")
                return True
            elif state4 == 'B':
                print("The dragon approves of the song, and lets you take whatever loot you can carry as a tip.")
                return True
            else:
                print("The dragon is dissappointed, and invinerates you instantly.")
                return False
        else:
            state3 = choice("Who will lead the attack?", "Wizard McBlastyFace", "Stella the Bard", "Me, of course")
            if state3 == 'A':
                print("Wizard McBlastyFace aims a spell and misses horribly, hitting the ceiling.  Rocks fall, everyone dies.")
                return False
            elif state3 == 'B':
                state4 = choice("Stella trips over a rock and the dragon wakes up.", "CHARGE!", "Tell Stella to sing to the dragon", "Run away")
                if state4 == 'A':
                    print("The dragon is so surprised by the stupidity of your attack that it dies of laughter.")
                    return True
                elif state4 == 'B':
                    print("The dragon approves of the song, and lets you take whatever loot you can carry as a tip.")
                    return True
                else:
                    print("The dragon is dissappointed, and invinerates you instantly.")
                    return False
            else:
                print("The dragon is so surprised by the stupidity of your attack that it dies of laughter.")
                return True
    elif state1 == 'B':
        print("The dragon sneezes out a fireball and incinerates you instantly.")
        return False
    else:
        state3 = choice("Who will lead the attack?", "Wizard McBlastyFace", "Stella the Bard", "Me, of course")
        if state3 == 'A':
            print("Wizard McBlastyFace aims a spell and misses horribly, hitting the ceiling.  Rocks fall, everyone dies.")
            return False
        elif state3 == 'B':
            state4 = choice("Stella trips over a rock and the dragon wakes up.", "CHARGE!", "Tell Stella to sing to the dragon", "Run away")
            if state4 == 'A':
                print("The dragon is so surprised by the stupidity of your attack that it dies of laughter.")
                return True
            elif state4 == 'B':
                print("The dragon approves of the song, and lets you take whatever loot you can carry as a tip.")
                return True
            else:
                print("The dragon is dissappointed, and invinerates you instantly.")
                return False
        else:
            print("The dragon is so surprised by the stupidity of your attack that it dies of laughter.")
            return True






