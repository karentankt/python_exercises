# -*- coding: utf-8 -*-
"""
@author: Karen Tan

"""
"""
Display all the perfect numbers between 2 and 1000.
Write function perfect() that determines whether parameter value is a perfect number.

An integer number is said to be a perfect number if its factors, including 1 (but not the number
itself), sum to the number. For example, 6 is a perfect number, because 6 = 1 + 2 + 3.

"""
factors = [] # Keep factors

#determine whether a value is a perfect number 
def perfect(check):
    global factors
    for j in range(1, check): # Find all factors of the number
        if check % j == 0: 
            factors.append(j)
    
    #The sum of factors equals the number, the number is a perfect number
    if sum(factors) == check: 
        print(check, "is a perfect number. Factors:", factors)
    
    #After checking the number, set the factors list to empty
    factors = [] 

        
for i in range(2, 1000):
    perfect(i)
    