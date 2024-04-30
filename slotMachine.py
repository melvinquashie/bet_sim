#!/usr/bin/python3

# File for slot machine workings.

# Import modules to be used
import random

# global constants
# let's make the slot machine a 3x3 slot machine. meaning 3 rows and 3 columns are showing on the screen.
ROWS = 3
COLS = 3

# now to specify the number of symbols on each reel.
# NB: there are 3 reels in the slot machine (thats why there are 3 columns)
# We would use a dictionary here:
symbol_count = {
	"A" : 2,
	"B" : 4,
	"C" : 6,
	"D" : 8,
}

# bet multiplier. the rarer the symbol (A is rarer than D), the higher the multiplier
symbol_value = {
	"A" : 5,
	"B" : 4,
	"C" : 3,
	"D" : 2,
}
  
def check_winnings(columns, lines, bet, values):
  # initializing winnings and winning lines:
  winnings = 0
  winning_lines = []

  # we just need to look at the rows the user bet on
  for line in range(lines):
    # we need to check if every symbol in the line (row) is the same. Easy way is to get first symbol in row and compare with rest
    symbol = columns[0][line]
    for column in columns:
      symbol_to_check = column[line]
      if symbol != symbol_to_check:
        break
    else:
      # calculate user's winnings
      winnings += values[symbol] * bet
      winning_lines.append(line + 1)

  # return user's winnings and the lines won on
  return winnings, winning_lines




# Now to generate the outcome, using the above values in the dictionary
# get the spin outcome using the rows, columns and symbols
def get_slot_machine_spin(rows, cols, symbols):
  # to get all symbols in a reel in a list to be randomly picked from
  all_symbols = [] # list

  # now to put all these items in the list, the number of times they occur:
  for symbol, symbol_count in symbols.items():
    for _ in range(symbol_count): # '_' is an anonymous variable in python. used especially when you dont care about the count or iteration value 
      all_symbols.append(symbol)


  # now that we have the list of all symbols, we need to select what values are going to go in every single column
  # we would use nested lists
  columns = []
  for _ in range(cols):
    column = []
    # we would also have to use a copy of the all_symbols list as every item picked can only be picked the number of times assigned and then removed as an option
    # ':' is the slice operator, making current_symbols a list on its own
    current_symbols = all_symbols[:]

    for _ in range(rows):
      value = random.choice(current_symbols)
      # now removing that value from the list
      current_symbols.remove(value)
      # adding the value to the column list
      column.append(value)
    
    columns.append(column) 

  return columns


def print_slot_machine(columns):
  # as now your reels are in row format:
  for row in range(len(columns[0])):
    # we loop through and only print the first or index of that row. this would cause the row to be printed vertically, making it a column
    for i, column in enumerate(columns):
      if i != len(columns) - 1:
        print (column[row], end =" | ") 
        # end tells the if statement what to end the line with, pipe operator is for separation.
      else:
        print (column[row], end ="")

    # now to go to a new line for the next symbol in the reel:
    print() 
    #this just prints nothing followed by \n



