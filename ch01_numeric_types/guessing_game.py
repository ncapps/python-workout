import random


def guessing_game():
    answer = random.randint(0, 100)

    while True:
        user_guess = int(input('Guess a number between 0 and 100 (inclusive): '))

        if user_guess == answer:
            print(f'Correct. The number is {user_guess}.')
            break

        if user_guess < answer:
            print(f'{user_guess} is too low.')
        else:
            print(f'{user_guess} is too high.')

guessing_game()
