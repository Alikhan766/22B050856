print("Hello! What is your name?")
name = str(input())
print("Well, {0}, I am thinking of a number between 1 and 20.\nTake a guess.".format(name))
t = 1

while True:
    s = int(input())
    if s == 19:
        break
    else:
        print('Your guess is too low.\nTake a guess.')
        t += 1
print('Good job, {0}! You guessed my number in {1} guesses!'.format(name, t))
