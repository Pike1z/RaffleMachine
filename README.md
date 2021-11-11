# RaffleMachine
The raffle machine used for The Backpack Fund's giveaways

This code is simple, it reads in data from a CSV file containing raffle information. This file's path was hardcoded in and is found in a directory in the local repo. For the privacy of others this CSV file is not included in the online repository.

The format of this file is as follows:
`entrants name`, `number of entries`, `donated amount`

The donated amount was used to calculate the number of entries. For the 2021 summer raffle
every $15 donated resulted in 1 entry. 

The raffle machine places each entrants name into a list *n*-times, where *n* is the number of entries they have.
It then shuffles the list and pulls out the first 10 entrants, each time an entrant is selected their name is removed from the list.
We choose 10 names just in case a winner does not want the prize and we can move onto the next.