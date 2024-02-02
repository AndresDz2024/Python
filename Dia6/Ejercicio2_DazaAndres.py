##-------------------------------------------------------------------------------------
##-------------------------------------------------------------------------------------
##-------------------------------- Ejercicio 6.1 --------------------------------------
##-------------------------------------------------------------------------------------
def negate(num):
    return -num

def large_num(num):
    if (num > 10000):
        res = True
    else:
        res = False 
    return res    
    
num = int(input())

print(negate(num))

print(large_num(num))

##Bugs

##Bug 1

# The function "large_num"  did not return true or false as requested by the requeriments.

# To solve this bug, i applied an "if" conditional, which takes care of returning the 
# "True or False" requested in the requirements.

##Bug 2

# Functions were being called incorrectly.

# To fix this bug, i have used "print" to correctly call the function so that it prints correctly.

##Bug 3

# As of negate(b) nothing in the base code works according to the requirements.

# To solve this bug, i remove everything unnecesary from the code base and simply requestes the value
# of "num", so that the code would work correctly, fulfilling all the requirements

## Dessarrollado por Andres Santiago Daza Daza 1095916023