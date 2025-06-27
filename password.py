import random
import string
charValues=string.ascii_letters + string.digits + string.punctuation
password=""
n=int(input("Enter the length of the password: "))
for i in range(n):
    password+=random.choice(charValues)
print("Your password is:", password)
