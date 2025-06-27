import random
target=random.randint(1, 100)
while True:
    userch=input("Guess a number between 1 and 100: ")
    if(userch=="Quit"):
        break
    userch=int(userch)
    if (userch==target):
        print("Congratulations! You guessed the number.")
        break
    elif (userch<target):
        print("Your guess is too low. Try again.")  
    elif (userch>target):
        print("Your guess is too high. Try again.")
print("The number was:", target)
print("----------Game over----------")
