# Play BlackJack
import random, os

def pick_card():
    suit = "blank"
    value = "blank"
    set = random.randint (1,4)
    if (set == 1) :
        suit = "♦"
    if (set == 2) :
        suit = "♣"
    if (set == 3) :
        suit = "♥"
    if (set == 4) :
        suit = "♠"
    set = random.randint (1,13)
    if (set <= 10):
        value = str(set)
    if (set == 1):
        value = "A"
    if (set == 11):
        value = "J"
    if (set == 12):
        value = "Q"
    if (set == 13):
        value = "K"
    card = value+suit    
    return card

def add_cards(card1, card2):
    value1 = 0
    value2 = 0
#Determine Value of Card 1
    if (card1[0] == "A"):
        value1 = 11
    elif (card1[0] == "J" or card1[0] == "Q" or card1[0] == "K"):
        value1 = 10
    else:
#       :-1 is supposed to return all but the last character in the string
        value1 = int(card1[:-1])
#Determine Value of Card 2
    if (card2[0] == "A"):
        value2 = 11
    elif (card2[0] == "J" or card2[0] == "Q" or card2[0] == "K"):
        value2 = 10
    else:
#       :-1 is supposed to return all but the last character in the string
        value2 = int(card2[:-1])
    return value1 + value2

def clear_screen():
    if(os.name == 'posix'):
        os.system('clear')
    # else screen will be cleared for windows
    else:
        os.system('cls')

#Start of main program
#clear_screen()
print(chr(27) + "[2J")
play = "yes"
input("Welcome to Lame-o-Black Jack. Press any key to begin...")
while play == "yes":
    #clear_screen()
    print("\033[H\033[J")
    print("Shuffling the deck...")
    print("Dealing cards...")
    #Initial Player Cards
    player_card1 = pick_card()
    player_card2 = pick_card()
    while player_card1 == player_card2:
        player_card2 = pick_card()
    print("Player Cards:")
    print("Player Card 1: " + player_card1)
    print("Player Card 2: " + player_card2)
    #Initial Dealer Cards
    dealer_card1 = pick_card()
    while dealer_card1 == player_card1:
        dealer_card1 = pick_card()
    while dealer_card1 == player_card2:
        dealer_card1 = pick_card()
    dealer_card2 = pick_card()
    while dealer_card2 == player_card1 or dealer_card2 == player_card2 or dealer_card2 == dealer_card1:
        dealer_card2 = pick_card()
    print("Dealer Cards:")
    print("Dealer Card 1: " + dealer_card1)
    print("Dealer Card 2: Hidden" + dealer_card2)

    if (add_cards(dealer_card1, dealer_card2) == 21):
        if (add_cards(player_card1, player_card2) == 21):
            print("You and the dealer both have Black Jack! Push!")
        else:
            print("Dealer has Black Jack! You lose!")
    elif (add_cards(player_card1, player_card2) == 21):
        print("You have Black Jack! You win!")
    else: #begin asking for action
        print("Player Card Total:" , add_cards(player_card1, player_card2))
        play=input("Would you like to play again? (yes/no): ")
        