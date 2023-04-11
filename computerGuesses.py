#Computer Guess the Number
#
import random
print("Think of a number between 0 and 100")
input("Press enter when ready")
myGuess = random.randint(0,100)
lowGuess = None
highGuess = None
count = 1
while True:
    print("My guess is " + str(myGuess))
    guess = int(input("1 if too high \n2 if too low \n3 if correct \n:"))
    if guess == 1:
        highGuess = myGuess - 1
        count = count + 1
        if lowGuess == None:
            myGuess = random.randint(0,highGuess)
        else:
            myGuess = random.randint(lowGuess,highGuess)
    elif guess == 2:
        lowGuess = myGuess + 1
        count = count + 1
        if highGuess == None:
            myGuess = random.randint(lowGuess,100)
        else:
            myGuess = random.randint(lowGuess,highGuess)
    elif guess == 3:
        print("I WIN! It only took me " + str(count) + " guesses!")
        input("Press Enter to exit")
        break
    else:
        print("I don't play with cheaters")
        input("Press Enter to exit")
        break
