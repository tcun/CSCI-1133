# Warm Up
def word_freq(fname):
    fp = open(fname)
    lines = fp.readlines()
    counts = {}
    for line in lines:
        words = line.split()
        for word in words:
          try:
            counts[word] += 1
          except KeyError:
            counts[word] = 1
    fp.close() 
    return counts
    
word_freq('sample.txt')

# Stretch
morse_dictionary={'A': '.-', 'B': '-...', 'C': '-.-.',
'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 
'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--',
'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--',
'X': '-..-', 'Y': '-.--', 'Z': '--..', ' ': '/'}

def morse_translate(message):
  print("Enter a message: ", message)
  # message = input()
  morse_message = ""
  for i in message.upper():
    morse_message += morse_dictionary[i] + " "
  return morse_message

# print(morse_translate("My TAs are amazing"))

# Workout 
costs = {'Philadelphia':{'Chicago':227, 'Dallas':289},
         'Chicago':{'Philadelphia':227, 'Dallas':105, 'Las Vegas':56},
         'Dallas':{'Philadelphia':289, 'Houston':173, 'Chicago':105,
                   'Las Vegas':44, 'San Diego':303},
         'Houston':{'Dallas':173},
         'Las Vegas':{'Chicago':56, 'Dallas':44, 'San Diego':74,
                      'Los Angeles':44, 'San Francisco':56},
         'Los Angeles':{'Las Vegas':44, 'San Diego':157,
                        'San Francisco':111},
         'San Diego':{'Las Vegas':44, 'Los Angeles':157, 'Dallas':303},
         'San Francisco':{'Las Vegas':56, 'Los Angeles':111}}

# Workout
total = costs['Chicago']['Las Vegas'] + costs['Las Vegas']['Dallas']
#print(total)

def cheapest(dict, city1, city2):
  min = float('inf')
  for price in dict[city1]:
    try:
      total = dict[city1][price] + dict[price][city2]
    except KeyError:
      try:
        total = dict[city1][city2]
      except KeyError:
        return float('inf')
    # print(price)
    # print(total)
    if total < min:
      min = total
  return min

# print(cheapest(costs, 'San Francisco', 'Philadelphia'))
# print(cheapest(costs, "Chicago", "Dallas"))
# print(cheapest(costs, 'Las Vegas', 'Los Angeles'))
# print(cheapest(costs, 'Philadelphia', 'Las Vegas'))

# Challenge
def rank_suit_count(cards):
  
  rank_dict = {}
  card_dict = {}
  card_rank = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
  card_suit = ['S', 'C', 'D', 'H']

  for i in range(len(cards)):
    try:
      print(cards[i[0]])
      if cards[i[0]] in card_rank:
        rank_dict[cards[i[0]]] += 1
      if cards[i[1]] in card_suit:
        card_dict[cards[i[1]]] += 1
    except KeyError:
      if cards[i[0]] in card_rank:
        rank_dict[cards[i[0]]] = 1
      if cards[i[1]] in card_suit:
        card_dict[cards[i[1]]] = 1

  return[rank_dict, card_dict]
print("\n\n\n\n\n")
print(rank_suit_count(['AS', 'AD', '2C', 'TH', 'TS' ]))