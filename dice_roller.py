import random

def main():
  playerCount = int(input('How players will be playing? '))
  for i in range(0, playerCount):
    player = input('\nWhat is your name? ')
    dice_rolls = int(input('How many dice would you like to roll? '))
    dice_size = int(input('How many sides are the dice? '))
    print(f'Here are your results {player}:')
    dice_sum = 0
    ary = [] # make array of 0 length
    for i in range(0, dice_rolls):
      roll = random.randint(1, dice_size)
      dice_sum += roll
      ary.append(roll) # add the current players rolls into it
      if roll == 1:
        print(f'You rolled a {roll}! Critical Fail')
      elif roll == dice_size:
        print(f'You rolled a {roll}! Critical Success!')
      else:
        print(f'You rolled a {roll}')


    print(f'All the numbers {player} rolled: {ary}')
    print(f'You have rolled a total of {dice_sum}')

if __name__== "__main__":

  main()