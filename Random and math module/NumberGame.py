import random
playing = True
print('I will generate number between 1 and 10. You have to guess it.')
while playing:
    number = random.randint(1,10)
    guess = int(input('Enter the number: '))
    if guess == number:
        print('Your guess is correct! ')
        print('The random number is: ', number)
        playing = False
        break
    else:
         print('The random number is: ', number)
         print('Your guess is incorrect, try again')