#TODO Ask the user if they want to play (Y or N)
#TODO Generate two cards for the user and add the result in the form of a list that's printed
#TODO Generate the first two cards for the computer and show the user the first (put them in a list)
#TODO Ask if the user wants to draw another card (Y or N)
#TODO If Y, generate a new card and add it to the result and append the list
#TODO If Y, generate a new card for the computer and add it to their list
#TODO If N, reveal the computer's total and compare who's is higher
#TODO If an 11 is drawn and it would cause the total to exceed 11, count it as 1 instead
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

play_again = input("Do you want to play a game of Blackjack? Y/N: ").lower()

power_on = True

def player_draw():
    player_cards.append(random.choice(cards))

def dealer_draw():
    dealer_cards.append(random.choice(cards))

def card_check():
    if sum(player_cards)>21:
        if 11 in player_cards:
            if sum(player_cards)-10 > 21:
                print("Bust! You Lose!")
                return False
            elif sum(player_cards)-10 == 21:
                print("Blackjack! You Win!")
                return False
        else:
            print("Bust! You Lose!")
            return False
    elif sum(player_cards) == 21:
        print("Blackjack! You Win!")
        return False
    elif sum(dealer_cards) > 21:
        if 11 in dealer_cards:
            if sum(dealer_cards)-10 > 21:
                print("Dealer Bust! You Win!")
                return False
            elif sum(dealer_cards)-10 == 21:
                print("Dealer Blackjack! You Lose!")
                return False
        else:
            print("Dealer Bust! You Win!")
            return False
    elif sum(dealer_cards) == 21:
        print("Dealer Blackjack! You Lose!")
        return False
    else:
        return True

if play_again == "y":
    power_on = True
    player_cards = []
    dealer_cards = []
    player_draw()
    player_draw()
    dealer_draw()
    dealer_draw()
    print(f"Your cards are {player_cards} and your total is {sum(player_cards)}")
    print(f"The dealer's first card is {dealer_cards[0]}")
    while power_on:
        power_on = card_check()
        if input("Hit or Stay? ").lower() == "hit":
            player_draw()
            print(f"Your cards are {player_cards} and your total is {sum(player_cards)}")
            power_on = card_check()
            if sum(dealer_cards)<14:
                dealer_draw()
                power_on = card_check()
    if sum(dealer_cards)<14:
        dealer_draw()
        power_on = card_check()
    elif sum(player_cards)>sum(dealer_cards):
        print("You Win!")
        power_on = False
        play_again = input("Do you want to play again? Y/N: ").lower()
    else:
        print("You Lose!")
        power_on = False
        play_again = input("Do you want to play again? Y/N: ").lower()

