from random import randrange

print("Welcome to the Guessing Game")
print("I am thinking of a number between 1 and 100.")

level = input("\nChoose a difficulty. Type 'easy' or 'hard' :  \n\n")

random_number = randrange(100)

if level == "easy":
	remaining_life = 10
else:
	remaining_life = 5

while not remaining_life == 0:
	print(f"\n\nYou have {remaining_life} attempts left to guess the number.")
	guess = int(input("\nMake a guess: \n "))
	if guess > random_number:
		remaining_life = remaining_life - 1
		print("\nIt is too high.")
	elif guess < random_number:
		remaining_life = remaining_life - 1
		print("\nIt is too low. ")
	else:
		remaining_life = 0
		print(f"\nWell done! You got it! The answer was {guess}.")

if remaining_life == 0 and guess != random_number:
	print("\nYou ran out of attemps. You lost and the game over")
