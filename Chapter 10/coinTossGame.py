import random
guess = ''

while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
toss = ('heads','tails')
correct = toss[random.randint(0, 1)]
if  correct == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    if correct == guess:
       print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
