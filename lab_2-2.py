# Author: SCT (AMDG) 3/3/22

def build_house(p1, p2, p3, p4): # defines function
    # stores inputs
    color = p1
    windows = p2
    doors = p3
    bathrooms = p4
    print("Your house is {0}, has {1} windows, {2} doors, and {3} bathrooms.".format(color, windows, doors, bathrooms)) # print statements
 # input statements
q1 = input("Enter the color of your house.\n")
q2 = input("Enter the number of windows your house has.\n")
q3 = input("Enter the number of doors your house has.\n")
q4 = input("Enter the number of bathrooms your house has.\n")

print(build_house(q1, q2, q3, q4))