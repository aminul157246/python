secret_number = 9
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input('Guess : '))
    guess_count += 1                # if you are not use it loop will continue infinitely.

    if (guess == secret_number):
        print('You Won!')
        break

else:
    print('You Lose !')
