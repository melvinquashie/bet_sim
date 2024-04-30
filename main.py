#!/usr/bin/python3

# Import all functions from other files
import usrDataFunctions as usr
import slotMachine as slot

# an instance of the game
def spin(balance):
  lines = usr.get_number_of_lines()
  while True:
    bet = usr.get_bet()
    total_bet = bet * lines

    # Total amount bet (total_bet) cannot be more than the User's balance
    if total_bet > balance:
      print(f"Big SHAQ: You do not have the facilities for that big man. \nYour current balance is ${balance} ")
      # give user option to continue or quit
      continue_or_not = input("Press enter to continue or q to quit: ")
      if continue_or_not == 'q':
        return 0
    else:
      break

  # statement to tell user the information they've provided
  print(f"You are betting ${bet} on {lines} lines and your total bet = ${total_bet}")

  # Slot Machine
  slots = slot.get_slot_machine_spin(slot.ROWS, slot.COLS, slot.symbol_count)
  # now to print the slots (rows turned to columns = reels)
  slot.print_slot_machine(slots)
  winnings, winning_lines = slot.check_winnings(slots, lines, bet, slot.symbol_value)

  print(f"You won ${winnings}.")
  print(f"You won on lines:", *winning_lines)
  # * on winning_lines is known as the splat operator which passes every single line from the winning_lines list to the print function
  return winnings - total_bet

# main function
def main():
  # users balance
  balance = usr.deposit()
  while True:
    print(f"Current balance is ${balance}.")
    # getting the user to play the game
    answer = input("Press enter to play (q to quit): ")
    if answer == 'q':
      break
    
    # after spin returns 0 , you need to break out of this loop
    if spin(balance) == 0:
      break

    balance += spin(balance)
  
  print(f"you left with ${balance}")




# calling main function
main()