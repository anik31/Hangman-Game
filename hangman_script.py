import time
name = input('Type your name : ')
print('Hey,'+ name, 'play hangman with me !')

time.sleep(1)
print('Give your guesses..')
time.sleep(0.5)

word = ('Python')
word = word.lower()

guesses = ''

turns = 12

while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char,)
        else:
            print('_',)
            failed+=1

    if failed == 0:
        print('Congrats..!! You have successfully guessed the word.')
        break

    guess = input('Guess a letter : ')
    guesses + = guess

    if guess not in word:
        turns - = 1
        print('That is a wrong guess')
        print('You have',+ turns,'chances left')
        if turns == 0:
            print('Better luck next time..! You have lost the game.')

