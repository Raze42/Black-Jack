# Play BlackJack
import random

def pick_card():
    suit = "blank"
    value = "blank"
    set = [(random.randint (1,4)), (random.randint(1,13))]
    if (set[0] == 1) :
        suit = "♦"
    if (set[0] == 2) :
        suit = "♣"
    if (set[0] == 3) :
        suit = "♥"
    if (set[0] == 4) :
        suit = "♠"
    if (set[1] <= 10):
        value = str(set[1])
    if (set[1] == 1):
        value = "A"
    if (set[1] == 11):
        value = "J"
    if (set[1] == 12):
        value = "Q"
    if (set[1] == 13):
        value = "K"
    return value+suit

def add_cards(card):
    total = 0
    ace = "no"
    cardval = [x[:-1] for x in card]
    for i in cardval:
        if (i == "A"):
            total = total + 1
            ace = "yes"
        elif (i == "J" or i == "Q" or i == "K"):
            total = total + 10
        elif (i == "B"):
            total = total + 0
        else:
            total = total + int(i)
    if ace == "yes" and total < 12:
        total = total +10
    return total

def clrscr():
    print ("\n" * 25)

#Start of main program
play = "yes"
print("""
Welcome to Lame-o-Black Jack.
Dealer stands on 16 or more.
Good luck!
""")
input("Press any key to begin...")
while play == "yes" or play == "y" or play == "Y":
    clrscr()
    print("Shuffling the deck...")
    print("Dealing cards...")
    player_bust = "no"
    #Initial Player Cards
    player_cards = [pick_card(), pick_card()]
    while player_cards[0] == player_cards[1]:
        player_cards[1] = pick_card()
    print("Player Cards: ", player_cards)
    #Initial Dealer Cards
    dealer_cards = [pick_card(), pick_card()]
    while dealer_cards[0] == player_cards[0]:
        dealer_cards[0] = pick_card()
    while dealer_cards[0] == player_cards[1]:
        dealer_cards[0] = pick_card()
    while dealer_cards[1] == player_cards[0] or dealer_cards[1] == player_cards[1] or dealer_cards[1] == dealer_cards[0]:
        dealer_cards[1] = pick_card()
    print("Dealer Cards: ", dealer_cards)
    #Check for Initial Black Jack
    if (add_cards(dealer_cards) == 21):
        if (add_cards(player_cards) == 21):
            print("You and the dealer both have Black Jack! Push!")
        else:
            print("Dealer has Black Jack! You lose!")
    elif (add_cards(player_cards) == 21):
        print("You have Black Jack! You win!")
    else: #No initial black-jack so begin asking for action
        print("Player Card Total: " , add_cards(player_cards))
        #print("Dealer Total: " , (add_cards(dealer_cards) - int(dealer_cards[1][:-1]))) #trying to show dealer total with one card hiddedn, but doesn't work because J,Q,K,A throws an error
        action = input("Hit(h) or Stand(s)?: ")        
        while action == "h" or action == "H" or action == "hit" or action == "Hit" or action == "HIT":
            player_cards.append(pick_card())
            print(player_cards)
            print("Player Card Total: " , add_cards(player_cards))
            if add_cards(player_cards) > 21:
                print("Player busts! Dealer Wins.")
                player_bust = "yes"
                break
            action = input("Hit(h) or Stand(s)?: ")
        if player_bust == "no": #dealer actions
            print("Revealing dealer cards...")
            print("Dealer Cards: ", dealer_cards)
            print("Dealer Card Total: " , add_cards(dealer_cards))
            while (add_cards(dealer_cards) < 16):
                dealer_cards.append(pick_card())
                print("Dealer Cards: ", dealer_cards)
                print("Dealer Card Total: " , add_cards(dealer_cards))
            if add_cards(dealer_cards) > 21:
                print("Dealer busts. Player wins.")
            elif add_cards(dealer_cards) == add_cards(player_cards):
                print("Push")
            elif add_cards(dealer_cards) > add_cards(player_cards):
                print("Dealer Wins")
            elif add_cards(dealer_cards) < add_cards(player_cards):
                print ("Player Wins")

        play = input("Would you like to play again? (yes/no): ")
        