"5 mini python projects, Tech with Tim"
print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
	quit()

print("Okay! Let's play:) ")
score = 0
questions = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
    questions += 1
else:
    print('Wrong! Fuck you!')
    questions += 1

answer = input("What is the meaning of life? ")
if answer == "42":
    print('Thanks for all the fish')
    score += 1
    questions += 1
else:
    print("Don't Panic")
    questions += 1

answer = input("Flat Earth or Ball Earth? ")
if answer.lower() == "ball earth":
    print('A 15 degree per hour drift...')
    score += 1
    questions += 1
else:
    print('Please die')
    questions += 1

answer = input("Is Ben Shapiro smart? ")
if answer.lower() == "no":
    print('yes')
    score += 1
    questions += 1
else:
    print('no')
    questions += 1

print("You got a score of " + str((score / questions) * 100) +"%")

