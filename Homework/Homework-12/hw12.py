import random

# PART A (10 points)
#########################################################################

class Member:
    '''
    Purpose: Represents one singular person for the Game Class 
    Instance variables: __name is a string that identifies the person's name, and __socialStatus is default to 5 and represents current social status of individual
    Methods: 
        __init__() = intializing instances variables for class arguments 
        __repr__() = Printable representation for the member object
        updateStatus() = Randomly adds or subtracts the socialStatus variable by 1  
    '''
    def __init__(self, __name, __socialStatus=5):
        self.name = __name
        self.socialStatus = __socialStatus

    def updateStatus(self):
        ops = [lambda a: a + 1, lambda a: a - 1]
        self.socialStatus = random.choice(ops)(self.socialStatus)
        if self.socialStatus > 10:
            self.socialStatus = 10
        if self.socialStatus < 1:
            self.socialStatus = 1
    def __repr__(self):
        return "Name: " + str(self.name) + ", Social Status: " + str(self.socialStatus)
    
    
    

class Tribe:
    '''
    Purpose: Tribe is a class to be a group container for the member class
    Instance variables: __tribeName is the a string and is the name of the tribe while __playerNames is a list of player names that will turned into member objects
    Methods: 
        __init__() = intializing instances variables for class arguments 
        updateStatusForAll() = calls the updateStatus function in the member class and runs it for all members in list
        def listOfNames() = Grabs all memeber names and puts them in a list 
    '''
    def __init__(self, __tribeName, __playerNames=[]):
        self.tribeName = __tribeName
        self.members = []
        for name in __playerNames:
            self.members.append(Member(name))
    
    def updateStatusForAll(self):
        for member in self.members:
            member.updateStatus()
    
    def listOfNames(self):
        return [i.name for i in self.members]

#########################################################################


# PART B (20 points)
#########################################################################


class Game:
    '''
    Purpose: To simulate a text-game version of the game survivor and determine one winner through random chance
    Instance variables: The two instance variables are redTribe and blueTribe in which represent a list of Tribe objects
    Methods: 
        __init__() = intializes instance variables 
        challengeWinner() = randomly selects a person or tribe as winner
        getOdds(tribe) = Generates a list that represents the odds a person has of being voted off based on socialStatus in Member class
        vote(tribe, immune) = Determines a random person from a tribe to vote off except whoever won who is now immune
        playerSurvivor() = Method that generates one full game of Survivor using above methods
    '''
    def __init__(self, redTribe=[], blueTribe=[]):
        self.redTribe = redTribe
        self.blueTribe = blueTribe
        self.merge = Tribe("Merge", [])

    def challengeWinner(self): 
        if self.merge.members == []:
            tribes = [self.redTribe, self.blueTribe]
            return random.choice(tribes).tribeName
        return random.choice(self.merge.members).name

    def getOdds(self, tribe): 
        odds = []
        for member in tribe.members:
            odds += [member.name] * member.socialStatus
        return odds

    def vote(self, tribe, immune):
        odds = self.getOdds(tribe)
        randomVote = random.choice(odds)
        while randomVote == immune:
            randomVote = random.choice(odds)
        for member in tribe.members:
            if randomVote == member.name:
                tribe.members.remove(member)
        odds.remove(randomVote)
        return randomVote

    def playSurvivor(self):
        for i in range(4):
            winner = self.challengeWinner()
            print(winner, "wins the challenge!")
            loser = self.redTribe if self.redTribe == winner else self.blueTribe
            lost = self.vote(loser, "")
            print(lost, "voted out of the", loser.tribeName, "\n")
            self.redTribe.updateStatusForAll()
            self.blueTribe.updateStatusForAll()
        merged = self.redTribe.listOfNames() + self.blueTribe.listOfNames()
        self.merge = Tribe("Merged Tribe", merged)
        for i in range(6):
            soloWinner = self.challengeWinner()
            print(soloWinner, "wins the challenge!")
            soloLoser = self.vote(self.merge, soloWinner)
            print(soloLoser, "voted out of the", self.merge.tribeName, "\n")
            self.merge.updateStatusForAll()
        print("The sole survivor is", self.challengeWinner())

#########################################################################

def main():
    names = ["Isaac", "Arunima", "Nakul", "Micah", "David", "Alice", 
            "Tarik", "Ian", "Charley", "Demond", "Abdourahman", "Vin"] 
    redTribeNames = []

    while len(redTribeNames) < 6:
        randName = random.choice(names)
        redTribeNames.append(randName)
        names.remove(randName)

    blueTribeNames = names

    #UNCOMMENT THE FOLLOWING TO CREATE TRIBES AND TEST THE SIMULATION 
    redTribe = Tribe("Red Tribe", redTribeNames)
    blueTribe = Tribe("Blue Tribe", blueTribeNames)

    simulation = Game(redTribe, blueTribe)
    simulation.playSurvivor()

if __name__ == '__main__':
    main()
