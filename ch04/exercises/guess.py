import random

num = random.randint(1,1000)
guess = ""
num_of_guess = 0
while guess != num:
  num_of_guess += 1
  guess = int(input("What was the randomly selected number? "))
  if guess > num:
    print("Your guess is too high!")
  if guess < num:
    print("Your guess is too low!")
print("Correct!")
print(f"The correct answer was {num} and it took you {num_of_guess} tries.")