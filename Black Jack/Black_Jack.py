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

def add_cards(card):
    total = 0
    cardval = [x[:-1] for x in card]
    for i in cardval:
        if (i == "A"):
            total = total + 11
        elif (i == "J" or i == "Q" or i == "K"):
            total = total + 10
        elif (i == "B"):
            total = total + 0
        else:
            #:-1 is supposed to return all but the last character in the string
            total = total + int(i)
    return total

#Start of main program
play = "yes"
input("Welcome to Lame-o-Black Jack. Press any key to begin...")
while play == "yes" or play == "y" or play == "Y":
    print("Shuffling the deck...")
    print("Dealing cards...")
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
        #print("Dealer Total: " , (add_cards(dealer_cards) - int(dealer_cards[1][:-1]))) #doesn't work because J,Q,K,A throw it off
        action = input("Hit(h) or Stand(s)?: ")
        
        while action == "h" or action == "H" or action == "hit" or action == "Hit" or action == "HIT":
            player_cards.append(pick_card())
            print(player_cards)
            print("Player Card Total: " , add_cards(player_cards))
            if add_cards(player_cards) > 21:
                print("Player busts! Dealer Wins.")
                break
            action = input("Hit(h) or Stand(s)?: ")
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
        