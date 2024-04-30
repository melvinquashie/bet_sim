#!/usr/bin/python3

# File for functions for User Data Collection

# global constants
# ff is the available number of lines to bet on
MAX_LINES = 3 # defining in all caps makes it a constant
# Max and Min allowed amount for bet
MAX_BET = 100
MIN_BET = 1 


# function for User's deposits
def deposit():
  # to continue asking the user to enter a deposit amount until the provide a valid amount.
  while True:

    # create a prompt to ask the user for the amount
    amount = input("What would you like to deposit? $")

    # to make sure the amount entered is a number
    # the following checks if the user's input (which is stored as a string) is a whole number. If so, it is converted into an integer
    if amount.isdigit():
      amount = int(amount)

      # now to make sure you have a positive deposit
      if amount > 0:
        break
      else:
        print("Amount must be greater than 0.")

    # if amount is not a number
    else:
      print("Please enter a valid number.")

  return amount 


# function for number of lines User would like to bet on
def get_number_of_lines():
  # similar to the deposit function, asking the user for number of lines until they provide a valid input.
  while True:

    # a prompt to ask for number of lines (input)
    lines = input("Please enter the number of lines to bet on (1 - " + str(MAX_LINES) +"): ")
    # above has some string concatenation as the MAX_LINES constant has been converted to a sting and concatenated to the prompt
  
    # to make sure the amount entered is a number
    # the following checks if the user's input (which is stored as a string) is a whole number. If so, it is converted into an integer
    if lines.isdigit():
      lines = int(lines)

      # now to make sure you have a positive deposit
      if 1 <= lines <= MAX_LINES:
        break
      else:
        print("Enter a valid number of lines.")

    # if amount is not a number
    else:
      print("Please enter a valid number.")

  return lines 


# Now to get the amount to bet on each line from User
def get_bet():
  # to continue asking the user to enter a bet amount until the provide a valid amount.
  while True:

    # create a prompt to ask the user for the amount
    amount = input("What would you like to bet on each line? $")

    # to make sure the amount entered is a number
    # the following checks if the user's input (which is stored as a string) is a whole number. If so, it is converted into an integer
    if amount.isdigit():
      amount = int(amount)

      # now to make sure amount is between max and min bet
      if MIN_BET <= amount <= MAX_BET:
        break
      else:
        print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")

    # if amount is not a number
    else:
      print("Please enter a valid number.")

  return amount 
