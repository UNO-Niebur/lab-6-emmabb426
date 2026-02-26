#DiceRoll.py
#Name: Emma Barnes
#Date: 02/26/2026
#Assignment: Dice Roll
import random

def main():
  #Create an empty list with possible roll values
  rolls = [0,0,0,0,0,0,0,0,0,0,0,0]
  #Create two dice values ranging from 1 - 6 each
  number_rolls = int(input("How many rolls do you want to simulate? "))
  for r in range(number_rolls):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)

    #find the sum total of the two dice
    sum = dice1 + dice2
    rolls[sum - 1] = rolls[sum -1] +1
  #print statictics for dice rolls
  dice = 1
  for count in rolls:
    print(dice, ":", count, ":", round(count/number_rolls*100, 2), "%")
    dice = dice + 1

if __name__ == '__main__':
  main()
