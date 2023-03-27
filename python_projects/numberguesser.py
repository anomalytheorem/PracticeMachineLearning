import random

top = input("Type a number: ")

if top.isdigit():
    top = int(top)

    if top <= 0:
        print("Please type a number larger than 0. ")
        quit()
else:
    print("Please type a number. ")
    quit()

r = random.randint(0, top)
print((r*random.randint(1,top))+random.randint(-12,12))
a = 0

while True:
    a += 1
    guess = input("Make a guess: ")
    if guess.isdigit():
        guess = int(guess)
    else:
        print("Please type a number: ")
        continue

    if guess == r:
        if a == 1:
            print("You got it in " + str(a) + " attempt")
            print("Wow, only", a, "guess")
        else:
            print("You got it in " + str(a) + " attempts")
            if a < 5:
                print("Wow, only", a, "guesses")
            else:
                print("Congratulations. You have Autism.")
        break
    elif guess > r:
        print("Over")
        print((r*random.randint(1,top))+random.randint(-12,12))
    else:
        print("Under")
        print((r*random.randint(1,top))+random.randint(-12,12))
