# This code was written by Charlie Ringler
# It is designed to be as simple and easy to follow as possible for full transparency

# Import the shuffle function
from random import shuffle

# Shuffles the list, picks a winner, and removes them from the list
def get_winner(raffle_list: list):
    # Shuffle the list
    shuffle(raffle_list)

    # Pick person from top of list
    winner = raffle_list[0]

    # Remove the winner's name
    while winner in raffle_list:
        raffle_list.remove(winner)
    
    return winner

# The list of raffle names
raffle_list = []

# Holds each entrant's info in the form of:
#   (NAME, NUMBER OF ENTRIES)
info_list = []

# Holds a list of winners. First come first served style, only need multiple winners in case someone doesn't accept the prize
num_winners = 10
winner_list = []

# Gather the donation information
with open('Data/Summer Entries.csv') as f:
    for line in f:
        info = line.split(',')
        info_list.append((info[0], int(info[1])))

# Put each name into the raffle list the appropriate number of times
for info in info_list:
    for i in range(info[1]):
        raffle_list.append(info[0])

# Get winners
for i in range(num_winners):
    winner_list.append(get_winner(raffle_list))

# Print winners
for i in range(num_winners):
    print('{}: {}'.format(i + 1, winner_list[i]))