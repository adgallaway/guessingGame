#Guessing Game
#
import random
myNum = random.randint(0,100)
counter = 0
yourNum = int(input("Pick a Number from 0 to 100: "))
guess = 0
while guess == 0:
    counter = counter + 1
    if yourNum > myNum:
        print("Your guess is too high")
        yourNum = int(input("Guess again: "))
    elif yourNum < myNum:
        print("Your guess is too low")
        yourNum = int(input("Guess again: "))
    else:
        print("You are correct!")
        print("My Number was " + str(myNum))
        print("It took you " + str(counter) + " guesses.")
        input("Press Enter to exit")
        guess = 1
