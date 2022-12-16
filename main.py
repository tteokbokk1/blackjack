from artwork import logo
import random
import os
from sys import exit

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

playGame = input("Do you want to play a game of Blackjack? Y/N ").lower()

def dealPlayerCards():
    playersCards.append(random.choice(cards))

def dealDealerCards():
    dealersCards.append(random.choice(cards))

def startGame():
    print(logo)
    dealDealerCards()
    dealDealerCards()
    dealPlayerCards()
    dealPlayerCards()
    print(f"The dealer got [{dealersCards[0]}, X]")
    print(f"You got {playersCards}")

#check if there are any aces
def aceChecker(person):
    if person == "dealer" and dealersCards.count(11) > 0:
        return True
    elif person == "dealer" and dealersCards.count(11) == 0:
        return False
    elif person == "player" and playersCards.count(11) > 0:
        return True
    elif person == "player" and playersCards.count(11) == 0:
        return False

#replace the aces with a 1 so it's easier to sum the totals
def aceFlipper(person):
    if person == "dealer":
        while dealersCards.count(11) > 0:
            dealersCards[dealersCards.index(11)] = 1
        return sum(dealersCards)
    elif person == "player":
        while playersCards.count(11) > 0:
            playersCards[playersCards.index(11)] = 1
        return sum(playersCards)
    
dealersCards = []
playersCards = []

if playGame == "y":
   startGame()
else:
    os.system("clear")

hitOrStay = input("Would you like to hit or stay?\n").lower()

while hitOrStay == "hit" and sum(playersCards) <= 21:
    dealPlayerCards()
    print(f"You now have {playersCards}")
    if sum(playersCards) > 21 and aceChecker("player") == True:
        aceFlipper("player")
        print(f"Aces can count as a 1. You now have {playersCards}")
    elif sum(playersCards) > 21 and aceChecker("player") == False:
        print("You busted. You lose.")
        os.system("clear")
        exit()
    elif sum(playersCards) > 21:
        print("You busted. You lose.")
        os.system("clear")
        exit()
    elif sum(playersCards) == 21:
        print("You got 21! You win!")
        os.system("clear")
        exit()
    else:
        hitOrStay = input("Would you like to hit or stay?\n").lower()

while sum(dealersCards) <17 or sum(dealersCards) < sum(playersCards):
    print(f"The dealer has {dealersCards}")
    dealDealerCards()
    print(f"The now dealer has {dealersCards}")
    if sum(dealersCards) > 21 and aceChecker("dealer") < 0:
        print("The dealer busted. You win!")
        replay = input("Would you like to play again? y/n ").lower()
    elif sum(dealersCards) > 21 and aceChecker("dealer") > 0:
        aceFlipper("dealer")
        print(f"Aces can count as a 1. The dealer now has {dealersCards}")
    elif sum(dealersCards) > sum(playersCards):
        print("The dealer has won. You lose.")
        replay = input("Would you like to play again? y/n ").lower()