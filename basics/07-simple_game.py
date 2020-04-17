import random
import time
import sys

def generate_feedback(guess):
    """
    Generates feedback for the codebreaker game.
    NV: input code is not valid
    Close: You've guessed a correct number but in the wrong position
    Match: guessed a correct number in the correct position
    Nope: haven't guess any of the numbers correctly
    """
    output = 'Nope'

    for index,char in enumerate(guess):
        if char not in ['0','1','2','3','4','5','6','7','8','9']:
            print('At least one character of the code is not a number.\n')
            return 'NV'
        if char in code and output == 'Nope':
            output = 'Close'
        if char == code[index]:
            output = 'Match'

    return output



playing = True
sys.stdout.write('\nGenerating random 3 digit code of numbers')
sys.stdout.flush()
time.sleep(0.5)
sys.stdout.write('.')
sys.stdout.flush()
time.sleep(0.5)
sys.stdout.write('.')
sys.stdout.flush()
time.sleep(0.5)
sys.stdout.write('.')
sys.stdout.flush()
time.sleep(0.5)
sys.stdout.write('.')
sys.stdout.flush()
time.sleep(0.5)
sys.stdout.write('.\n')

code = []
for num in range(0,3):
    code.append(str(random.randint(0,9)))

print('...code generated. Good luck guessing! \n')

while playing:
    guess = input('What is your guess (enter exit to stop playing)? ')

    if list(guess) == code:
        print('\nYOU WON!!!\n')
        break

    if guess == 'exit':
        break
    if guess == 'solve':
        print(code)
        continue

    if len(guess) != 3:
        print('Please enter a three digit code of numbers.\n')
        continue

    feedback = generate_feedback(guess)
    if feedback == 'NV':
        continue
    else:
        print("\nHere's your clue: {}\n".format(feedback))
