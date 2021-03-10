import random
def rps_game(rounds):
    '''
    Purpose: Plays multiple rounds of Rock-Paper-Scissors
    Input Parameter(s):
        rounds - an integer representing the number of rounds to play
    Return Value: A dictionary representing the computer's win
        differential for each of the three possible choices
    '''
    win_differ = {'R':0, 'S':0, 'P':0}
    computer_choices = ["R", "P", "S"]
    for i in range(rounds):
        print("Enter R, P, or S: ")
        user = input()
        
        temp_sorted_win = sorted(win_differ, key=win_differ.get, reverse=True)
        comp = temp_sorted_win[0]

       
        win_differ = calculate_differ(win_differ, rps_round(user, comp), comp)
    return win_differ
        
def calculate_differ(win_dict, result, comp_choice):
    '''
    Purpose: Determine a winner and add or subtract to a win differential dictionary 
    Input Parameter(s):
        win_dict (Dict) - the dictionary being manipulated
        result (String) - result of the current round
        user_choice (String) - The user inputted choice
    Return Value: A dictionary representing the computer's win
        differential for the round
    '''
    if comp_choice == result:
        print("Comp Wins")
        if result == "R":
            win_dict["R"] += 1
        elif result == "P":
            win_dict["P"] += 1
        elif result == "S":
            win_dict["S"] += 1
        else:
            win_dict["S"] += 0
    else:
        print("User Wins", result)
        if result == "R":
            win_dict["S"] -= 1
        elif result == "S":
            win_dict["P"] -= 1
        elif result == "P" :
            win_dict["R"] -= 1 
        else:
            win_dict["S"] += 0
    return win_dict
        

def rps_round(user_choice, comp_choice):
    '''
    Purpose: Determine a winner and add or subtract to a win differential dictionary 
    Input Parameter(s):
        user_choice (String) - The user inputted choice
        comp_choice (String) - The computer inputted choice
    Return Value: A dictionary representing the computer's win
        differential for the round
    '''
    if((user_choice == "R") and (comp_choice == "S")) or ((user_choice == "S") and (comp_choice == "R")):
        print("Player selects", user_choice, "\nComputer selects", comp_choice)
        return "R"
    elif ((user_choice == "P") and (comp_choice == "S")) or ((user_choice == "S") and (comp_choice == "P")):
        print("Player selects", user_choice, "\nComputer selects", comp_choice)
        return "S"
    elif ((user_choice == "P") and (comp_choice == "R")) or ((user_choice == "R") and (comp_choice == "P")):
        print("Player selects", user_choice, "\nComputer selects", comp_choice)
        return "P"
    elif (((user_choice == "P") and (comp_choice == "P")) or ((user_choice == "R") and (comp_choice == "R")) or ((user_choice == "S") and (comp_choice == "S"))):
        print("Tie!")
        return None
    else:
        print("Invalid Input\nTry Again")
        print("Enter R, P, or S: ", end='')
        user_choice = input()
        return rps_round(user_choice, comp_choice)


    


def print_104():
    '''
    Purpose: Prints "Who needs loops?" 104 times
    Input Parameter(s): None
    Return Value: None
    '''
    call_5()
    call_5() 
    call_5() 
    call_5() 
    print("Who needs loops?")
    print("Who needs loops?")
    print("Who needs loops?")
    print("Who needs loops?")

def print_5():
    '''
    Purpose: Prints "Who needs loops?" 5 Times
    Input Parameter(s): None
    Return Value: None
    '''
    print("Who needs loops?")
    print("Who needs loops?")
    print("Who needs loops?")
    print("Who needs loops?")
    print("Who needs loops?")
    
def call_5(): 
    '''
    Purpose: Prints Calls print_5() 5 times, Prints "Who needs loops?" 25 Times
    Input Parameter(s): None
    Return Value: None
    '''
    print_5()
    print_5()
    print_5()
    print_5()
    print_5()




if __name__ == '__main__':

    #TODO: Write test cases for your Problem A Helper functions here
    #Make sure you include Expected Return and Input Sequence (if applicable)
    
    #Input sequence: {'R':0, 'S':0, 'P':0}, "R", "P"
    #Expected Return: {'R': 1, 'S': 0, 'P': 1}
    # print(calculate_differ({'R':0, 'S':0, 'P':0}, "R", "P"))

    # #Input sequence: "R", "P"
    # #Expected Return: "P"
    # print(rps_round("R", "P"))

    #Input sequence: S
    #Expected Return: {'R': 1, 'S': 0, 'P': 0}
    print(rps_game(1))

    #Input sequence: Scissors, P, r, 4, P, P
    #Expected Return: {'R': -1, 'S': 2, 'P': 0}
    print(rps_game(3))

    #Input sequence: R, P, P, R, R, S, P, P, P, S
    #Expected Return: {'R': -2, 'S': 1, 'P': -1}
    print(rps_game(10))

    #No return value, but should print "Who needs loops" 104 times
    print_104() 
