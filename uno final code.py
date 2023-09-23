import random
#generating uno deck of 108 cards
colors = ["Red", "Green", "Yellow", "Blue"]
values = [0,1,2,3,4,5,6,7,8,9, "skip", "reverse", "Draw two"]
wilds = ["wild", "wild draw four"]

def deck_cards():
    deck = []
    for color in colors:
        for value in values:
            cardval = "{} {}".format(color, value)
            deck.append(cardval)
            if value != 0:
                deck.append(cardval)
    for i in range(4):
        deck.append(wilds[0])
        deck.append(wilds[1])
    return deck

deckCards = deck_cards()
length = len(deckCards)
print("Total number of cards:",length)
print(end = "\n")
print("Deck cards are:")
print(deckCards)
print(end = "\n")

#shuffling the uno deck of cards
def shuffle_cards():
    x = deck_cards()
    shuffled_cards = random.shuffle(x)
    return(x)

print("Shuffled cards are:")
x = shuffle_cards()
print(x)
print(end = "\n")


#all players drawing cards
def draw_cards(numCards):
    cards_drawn = []
    for i in range(numCards):
        cards_drawn.append(x.pop(0))
    return cards_drawn

def draw_two(player_num, widdie_cards):
    players[player_num-1] += widdie_cards[0:2]
    widdie_cards = widdie_cards[2:]
    print("Player {}: {}".format(player_num, players[player_num-1]))
    player_num = skip(player_num)
    return (widdie_cards, player_num)

def skip(player_num):
    print("Player {} chance is skipped".format(player_num))
    if(player_num == numplayers):
        player_num = 1
    else: 
        player_num +=1    
    return player_num

def reverse(player_num):
    if(player_num == 1):
        player_num = numplayers
    else:
        player_num -= 1
    return player_num

def draw_four(player_num, widdie_cards):
    players[player_num-1]+= widdie_cards[0:4]
    widdie_cards = widdie_cards[4:]
    print("Player {}: {}".format(player_num, players[player_num-1]))
    player_num = skip(player_num)
    return (widdie_cards, player_num)

i = 0
#Checking if any of the players list is empty
def check(players, numplayers):
    for i in range(numplayers):
        if(len(players[i])==0):
            print("Player {} wins!".format(i+1))
            print("Game ends!!")
            return 0
    return 1

#Action to perform when base card is a special card
def check_baseCard(base_card, players, widdie_cards, player_num):
    if(base_card.find("Draw two")!= -1):
        widdie_cards, player_num = draw_two(player_num, widdie_cards)
    elif(base_card.find("wild draw four")!= -1):
        widdie_cards, player_num = draw_four(player_num, widdie_cards)
    elif(base_card.find("skip")!= -1):
        player_num = skip(player_num)
    elif(base_card.find("reverse")!= -1):
        player_num = reverse(player_num)
    return (players, widdie_cards, player_num)

def special(base_card):
    if(base_card.find("reverse")!= -1):
        return 1
    return 0
    
#Play game
def play_game(players, widdie_cards):
    base_card = widdie_cards.pop(0)
    f = 0
    player_num = 1
    print("Base card is ",base_card)
    if(base_card == "wild"):
        color = input("Which color do you choose? ")
        base_card = color
    players, widdie_cards, player_num = check_baseCard(base_card, players, widdie_cards, player_num)
    if(base_card == "wild draw four"):
        color = input("Which color do you choose? ")
    while(check(players, numplayers)==1):
        b = base_card.split(" ")
        print("Player {}'s turn: ".format(player_num))
        print("Player {}: {}".format(player_num, players[player_num-1]))
        card_chosen = input("Which card do you want to choose?If there is no card of same color or number,Type Pick to take a card from widdie")
        if(card_chosen == "wild" or card_chosen == "wild draw four"):
            color = input("Which color do you choose? ")
            f = 1
            base_card = b[0] = color
            print("Choose a card in ",color)
            
        c = card_chosen.split(" ")
        if(card_chosen=="Pick" or (f==0 and b[0]!=c[0] and b[-1]!=c[-1])):
            if(card_chosen!="Pick"):
                print("Card does not match base card")
                card_chosen = base_card
            players[player_num-1].append(widdie_cards.pop(0))
            print("Player {}: {}".format(player_num, players[player_num-1]))
            if(card_chosen=="Pick" and base_card.find("Draw two")!= -1):
                base_card = b[0]
        
        if(card_chosen not in "Pick"):
            base_card = card_chosen
            players[player_num-1].remove(card_chosen)
            
        print("Base card is ", base_card)
        
        if(special(base_card)==0):
            if(player_num==numplayers):
                player_num = 1
            else:
                player_num +=1
        players, widdie_cards, player_num = check_baseCard(base_card, players, widdie_cards, player_num)
        


x = shuffle_cards()
#Distributing the cards
players =[]
numplayers = int(input("How many players: "))
for player in range(numplayers):
    players.append(draw_cards(7))

#WIDDIE - The cards left after distrubution of the deck are placed face down and are called "WIDDIE"
widdie_cards = x
play_game(players, widdie_cards)
