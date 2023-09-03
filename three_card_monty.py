# import shuffle method
from random import shuffle

# shuffle list
def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

# player guess - checks input betwen 0-2, returns guess
def player():
    guess = ''
    while guess not in ['0','1','2']:
        guess = input('Guess a number: 0, 1, or 2: ')
    return int(guess)

# checks shuffled list against player guess
#returns win or loss
def check(my_list, guess):
    if mylist[guess] == 'X':
        print('You win!')
        print(my_list)
    else:
        print('Better luck next time!')
        print(my_list)

#Game Play

# establish three cards with one winner
mylist = ['X','','']

# shuffle
mixed_list = shuffle_list(mylist)

# Player guess input and returned
guess = player()

# Player guess checked against mixed_list
# Win or loss reported
check(mixed_list, guess)
