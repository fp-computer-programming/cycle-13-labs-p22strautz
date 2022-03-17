# Author: SCT (AMDG) 3/16/22

def factorial(num): # defines function
    if num != 0: # test if number is 0
        total = 1 # base values
        counter = 1
        while counter <= num: # stop when counter is = to num
            total *= counter # equation for factorial
            counter += 1 # add one for each interval
        return total
    else:
        print("This function cannot handle zero as an input") 

print(factorial(0)) # test cases
print(factorial(5))