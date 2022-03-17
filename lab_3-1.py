# Author: SCT (AMDG) 3/16/22

def r_max(nestedlst): # Defines function
    max = 0 # stores values
    for num in nestedlst: # specifies num in list
        if type(num) == list:
            num = r_max(num)
            if num > max: # if num > max set max = to num
                max = num
        else:
            if num > max: 
                max = num
    return max # returns output to variable

print(r_max([0,2,2,[23,60],24])) # test case