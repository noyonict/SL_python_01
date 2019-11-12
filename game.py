import random
"""Number Guessing Game in python 3
    Made by: Md. Mohaymenul Islam (Noyon)
"""

hidden_number = random.randint(1, 101)
print('You can guess a number between 1 to 100.')
number_of_guess = 1
guess_number = int(input('Enter a guess: '))
while guess_number != hidden_number:
    if guess_number > hidden_number:
        print('Your guessing number is to high! Please try again...')
    else:
        print('Your guessing number is too short! Please try again...')
    number_of_guess += 1
    guess_number = int(input('Enter a guess: '))

print('Congratulation! You won the game. The number is {}.'.format(hidden_number))
print('You got it in {} guesses.'.format(number_of_guess))


