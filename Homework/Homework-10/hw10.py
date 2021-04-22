import random
def bigram_count(phrase):
    '''
    Purpose: Creates a dictionary of lists with all bigrams within a string
    Input Parameter(s): 
        phrase (string) - String with words to find bigrams
    Return Value: 
        bigram_dict (dictionary) - a dictionary of lis
    '''
    # phrase = remove_punctation(phrase)
    word_list = phrase.split()
    bigram_dict = {}
    # print(word_list)
    for i in range(len(word_list) - 1):
        if(word_list[i] in bigram_dict):
         bigram_dict[word_list[i]].append(word_list[i+1])
        else:
            bigram_dict[word_list[i]]= []
            bigram_dict[word_list[i]].append(word_list[i+1])   
    return bigram_dict

# print(bigram_count("one fish, two fish, red fish, blue fish, blue"))


# Guess I didn't need this :[
# def remove_punctation(sentence):
#     punc = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''
#     for i in punc: 
#         if i in punc: 
#             sentence = sentence.replace(i, "") 
#     return sentence
            

def random_sentence(bigram_dict, starting_word, length):
    '''
    Purpose: Generate a random sentence using a dictionary of bigrams
    Input Parameter():
        bigram_dict (dictionary) - dictionary of lists full of wonderful bigrams
        starting_word (string) - intial starting string
        length (int) - amount of words wanted for sentence
    Return Value: 
        ran_sent (string) - string of a random assortment of words based on a dictionary of bigrams
    '''
    ran_sent = ""
    key_word_list = list(bigram_dict.keys())
    key = starting_word
    for i in range(length):
        ran_sent += key + " "
        try:
            key = random.choice(bigram_dict[key])
        except KeyError: 
            key = starting_word
        
    return ran_sent

# print(random_sentence({'One':['two'], 'two':['three'], 'three':['four']}, 'two', 20))
# print(random_sentence({'Never': ['gonna', 'gonna', 'gonna'], 'gonna': ['give', 'let', 'run'], 'give': ['you'], 'you': ['up.', 'down.'], 'up.': ['Never'], 'let': ['you'], 'down.': ['Never'], 'run': ['around'], 'around': ['and'], 'and': ['desert'], 'desert': ['you.']}, 'gonna', 20)
# )
# print(random_sentence({'You': ["can't", 'can'], "can't": ['stop', 'stop'], 'stop': ['an', 'the', 'my', 'the'], 'an': ['avalanche'], 'avalanche': ['as'], 'as': ['it'], 'it': ['races'], 'races': ['down'], 'down': ['the'], 'the': ['hill.', 'seasons', 'world', 'speed', 'drums', 'beat.'], 'hill.': ['You'], 'can': ['try', 'try'], 'try': ['to', 'to'], 'to': ['stop', 'stop', 'the'], 'seasons': ['girl'], 'girl': ['but'], 'but': ['you', 'I'], 'you': ['know', 'never', 'can', "can't"], 'know': ['you'], 'never': ['will.'], 'will.': ['And'], 'And': ['you', 'my'], 'my': ["dancin'", "heart's", 'way.'], "dancin'": ['feet'], 'feet': ['but'], 'I': ['just', 'was', 'heard', 'found'], 'just': ['cannot'], 'cannot': ['stand'], 'stand': ['still.'], 'still.': ['Cause'], 'Cause': ['the', 'you'], 'world': ['keeps'], 'keeps': ['spinning'], 'spinning': ['round'], 'round': ['and'], 'and': ['round.'], 'round.': ['And'], "heart's": ['keeping'], 'keeping': ['time'], 'time': ['to'], 'speed': ['of'], 'of': ['sound.'], 'sound.': ['I'], 'was': ['lost'], 'lost': ['til'], 'til': ['I'], 'heard': ['the'], 'drums': ['then'], 'then': ['I'], 'found': ['my'], 'way.': ['Cause']}, 'You', 30)
# )

def rand_sent_file(filename, length):
    '''
    Purpose: Reads a file a generates a random sentence from the words 
    Input Parameter(s):
        filename (string) - Name of the file
        length (int) - Number of words wanted in sentence
    Return Value: Returns a string of a random sentence using words in a file 
    '''
    with open(filename, 'r') as fp:
        words = fp.read()
        bigram_dict = bigram_count(words)
    return random_sentence(bigram_dict, random.choice(words.split()), length)

print(rand_sent_file('short3.txt', 10))
