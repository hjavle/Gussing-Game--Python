# import python's random library
import random
# declare variables to hold max no of guesses and number of guesses (counter)
number_of_guesses = 0
max_no_guesses = 5
# generate random integer between given min value max value 
computer_number = random.randint(1,10)
# prompt user to input user name
user_name = raw_input("What is your name? ")
# print message with user name
print(user_name + ",  Welcome to guessing Game !")
# prompt user to input whole number between min value max value
print(user_name + ",  Can you guess the number between 1 and 10?")
# for loop goes through iterations for the range of number_of_guesses& max_no_guesses
for Num in range(number_of_guesses,max_no_guesses): 
# user_guess will hold value of user input as string
  user_guess = raw_input("Please guess the number ")
# convert user_guess into integer number for comparision
  user_guess = int(user_guess)
# number_of_guesses will increase for each iteration as user tries to guess
  number_of_guesses = number_of_guesses + 1;
# here we check how many attempts are left for user to guess
  guesses_left = max_no_guesses - number_of_guesses;
# compare user_guess with computer_guess and give hints if guess is incorrect
  if user_guess < computer_number:
    guesses_left=str(guesses_left)
    print("Your guess is too low! You have " + guesses_left + " guesses left")
  elif user_guess > computer_number:
    guesses_left=str(guesses_left)
    print("Your guess is too high! You have " + guesses_left + " guesses left") 
# user_guess matches computer_guess and break game with message
  elif user_guess==computer_number:
    number_of_guesses=str(number_of_guesses)
    print("Good job! You guessed the number in " + number_of_guesses + " tries )")
    break;
# user_guess ran out of attempts display message that user has lost the game
# display the number computer has generated
else:
  print("You loose! The number was " + str(computer_number))