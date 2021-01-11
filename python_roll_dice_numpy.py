# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 09:18:52 2020

@author: Karen Tan
"""
"""
Write a module that simulates the rolling of 1 or more dice, 
then compare the theoretical with the actual results.
Use NumPy Array and NumPy Library to do this task.
"""
import numpy as np

#Get the input number of dice from user
def getInputNumber():
    while True:
        input_number = input("Enter the number of dice: ")
        #Check whether the input number is between 1 and 8 inclusive
        if input_number.isdigit():
            number = int(input_number)
            if 1 <= number <= 8:
                return number   #return the valid number
            else:
                 print("Invalid entry, enter an integer between 1 and 8.")
                 continue
        else:
            print("Invalid entry, enter an integer between 1 and 8.")

#Get the input rolls from user
def getInputRolls():
    while True:
        input_rolls = input("Enter the number of rolls: ")
        #Check whether the input rolls is valid
        if input_rolls.isdigit() :
            rolls = int(input_rolls)
            if rolls > 0:
                return rolls   #return the valid rolls
            else:
                print("Invalid entry, enter a positive integer.")
                continue
        else:
            print("Invalid entry, enter a positive integer.")

#Calculate the count of sum
def getSumCount(n, sum): # n:the number fo dice, sum: the probability sum of n dices for per roll
    global sumCount 
    if n < 1 or sum < n or sum > 6 * n:
        return 0
    
    elif n == 1:
        return 1

    else:
        sumCount = getSumCount(n-1, sum-1) + getSumCount(n-1, sum-2) + getSumCount(n-1, sum-3) + getSumCount(n-1, sum-4) + getSumCount(n-1, sum-5) + getSumCount(n-1, sum-6)
        return sumCount      

#Get the input number of dice from user
dice_number = getInputNumber() # the number of dices

#Get the input rolls from user
rolls_number = getInputRolls()  # the rolls of dices

# Record the simulation process
dice_records = np.zeros([dice_number , rolls_number], dtype = int)

total_combination = pow(6, dice_number) #The total combinations for n dices
 
# Simulate the dices rolling
for roll in range(rolls_number):
    for dice in range(dice_number): #Calculate the points of one roll
        each_num = np.random.randint(1 , 7)
        dice_records[dice][roll] = each_num

# Points of each roll
sum_roll = np.sum(dice_records, axis = 0)
unique,count=np.unique(sum_roll,return_counts=True)
# Points of each roll and its counts
data_count = dict(zip(unique,count))


# output the statistic results
print("[Total of Dice]  [Time appears]    [Appear %age]    [Likelihood]  [Percentage Error]")
for sum in range(dice_number, dice_number * 6 + 1):
    #The times of sum
    times_appear = data_count[sum] if sum in data_count else 0 
    appear_percent = times_appear / rolls_number
    sum_count = getSumCount(dice_number, sum) # probability of the count of each sum
    probability = sum_count / total_combination  # likelihoood
    error_percent = abs(appear_percent - probability)
    
    print("\t{0}\t\t{1}\t\t{2:.2f}%\t\t{3:.2f}%\t\t{4:.2f}%".
          format(sum, times_appear, appear_percent * 100, probability * 100, error_percent * 100))

