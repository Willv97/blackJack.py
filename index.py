import random

# Define the suits and ranks of cards
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

# Function to calculate the total value of a hand
def calculate_hand_value(hand):
    total = 0
    num_aces = 0
    for card in hand:
        rank = card[0]
        if rank.isdigit():
            total += int(rank)
        elif rank in ['Jack', 'Queen', 'King']:
            total += 10
        elif rank == 'Ace':
            num_aces += 1
            total += 11
    # Adjust the value of Aces if necessary
    while total > 21 and num_aces:
        total -= 10
        num_aces -= 1
    return total

# Function to check if a hand is a blackjack (has a total value of 21)
def is_blackjack(hand):
    return len(hand) == 2 and calculate_hand_value(hand) == 21

# Function to display a hand
def display_hand(hand, player_name):
    print(f"{player_name}'s hand:", ', '.join([f"{rank} of {suit}" for rank, suit in hand]))
    print(f"Total value: {calculate_hand_value(hand)}\n")

# Create a deck of cards
deck = [(rank, suit) for rank in ranks for suit in suits]

# Shuffle the deck
random.shuffle(deck)

# Deal two cards to the player and dealer
player_hand = [deck.pop(), deck.pop()]
dealer_hand = [deck.pop(), deck.pop()]

# Print the initial hands
display_hand(player_hand, "Player")
display_hand(dealer_hand, "Dealer")

# Player's turn
while calculate_hand_value(player_hand) < 21:
    choice = input("Do you want to hit or stand? (h/s): ").lower()
    if choice == 'h':
        player_hand.append(deck.pop())
        display_hand(player_hand, "Player")
    elif choice == 's':
        break

# Dealer's turn
while calculate_hand_value(dealer_hand) < 17:
    dealer_hand.append(deck.pop())
    display_hand(dealer_hand, "Dealer")

# Determine the winner
player_total = calculate_hand_value(player_hand)
dealer_total = calculate_hand_value(dealer_hand)

if player_total > 21:
    print("Player busts! Dealer wins.")
elif dealer_total > 21:
    print("Dealer busts! Player wins.")
elif player_total == dealer_total:
    print("It's a tie!")
elif is_blackjack(player_hand) and not is_blackjack(dealer_hand):
    print("Blackjack! Player wins.")
elif is_blackjack(dealer_hand) and not is_blackjack(player_hand):
    print("Blackjack! Dealer wins.")
elif player_total > dealer_total:
    print("Player wins!")
else:
    print("Dealer wins!")

