#GUESSING GAME USING WHILE LOOP. USER HAS 5 TURNS AND PROGRAM PRINT MESSAGES FOR COMPLETED TURNS, HIGHER OR LOWER GUESSES
from random import randint
secret_num = randint(1,100) 
num_guesses = 0 
guess = 0
while guess != secret_num and num_guesses <= 4:
    guess = eval(input('Enter your guess (1-100): '))
    num_guesses = num_guesses + 1
    if guess < secret_num:
        if num_guesses == 4:
                print('HIGHER.', 5-num_guesses, 'guess left.\n')
        print('HIGHER.', 5-num_guesses, 'guesses left.\n') 
    elif guess > secret_num:
           print('LOWER.', 5-num_guesses, 'guesses left.\n')
           if num_guesses == 4:
               print('LOWER.', 5-num_guesses, 'guess left.\n') 
    else:
        print('You got it!')
if num_guesses==5 and guess != secret_num:
    print('You lose. The correct number is', secret_num)

