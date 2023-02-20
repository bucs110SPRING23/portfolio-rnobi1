import random

num = random.randint(1,11)
guess = ""
while guess != num:
  guess = int(input("What was the randomly selected number? "))
  if guess > num:
    print("Your guess is too high!")
  if guess < num:
    print("Your guess is too low!")
print("Correct!")