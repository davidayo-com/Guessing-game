import random

def play_guess_the_number():
  """A simple number guessing game."""

  print("Welcome to Guess the Number!")

  # Generate a random number between 1 and 100
  secret_number = random.randint(1, 100)

  # Set the number of guesses allowed
  guesses_allowed = 7

  # Start the guessing loop
  for i in range(guesses_allowed):
    try:
      # Get the player's guess
      guess = int(input(f"Guess a number between 1 and 100 (You have {guesses_allowed - i} guesses left): "))
    except ValueError:
      print("Invalid input. Please enter a number.")
      continue

    # Check if the guess is correct
    if guess == secret_number:
      print(f"Congratulations! You guessed the number in {i + 1} tries.")
      return

    # Provide feedback on the guess
    elif guess < secret_number:
      print("Too low! Try again.")
    else:
      print("Too high! Try again.")

  # If the player runs out of guesses
  print(f"You ran out of guesses. The number was {secret_number}.")

# Start the game
play_guess_the_number()