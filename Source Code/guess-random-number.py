import random
random_number = random.randint(1,100)
guess_attempts = 0
while True:
    try:
        guess_number = int(input('Guess which number do i have?(1 to 100): '))
        if guess_number == random_number:
            print('You guessed it')
            print('Its number',random_number)
            print('Total attempts:', guess_attempts)
            play_again = input('Do you want to play again?(y/n) ')
            play_again = play_again.lower()
            if play_again == 'yes' or play_again == 'y':
                random_number = random.randint(1,100)
                guess_attempts = 0
                pass
            elif play_again == 'no' or play_again == 'n':
                break
            else:
                break
        elif guess_number > random_number:
            print('Random number is less than your number')
            guess_attempts += 1
        elif guess_number < random_number:
            print('Random number is greater than your number')
            guess_attempts += 1
        
    except ValueError:
        print('Oops use integer numbers.')
