import random

def guessing_game():
    level = int(input('Level: '))
    answer = random.randint(1, level)
    while True:
        try:
            guess = int(input('Guess: '))
        except ValueError:
            continue
        if level < 1:
            level = int(input('Level: '))
            continue
        elif guess < 1:
            continue
        elif guess > answer:
            print('Too large!')
        elif guess < answer:
            print('Too small!')
        else:
            print('Just right!')
            break

guessing_game()
