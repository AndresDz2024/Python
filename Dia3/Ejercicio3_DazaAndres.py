##-----------------------------------------------
##-----------------------------------------------
##------------- Ejercicio 3 ---------------------
##-----------------------------------------------
#Define the function
def The_number(number):
    #In case the user enters a negative number.
    if number < 0:
        print("The number entered is negative, please enter a positive number " )
        return
    #Perform the operation
    coins_10 = number // 10
    number %= 10
    coins_5 = number // 5
    number %= 5
    coins_1 = number
    #Print the result
    print(f"{coins_10} coins of 10 are used" )
    print(f"{coins_5} coins of 5 are used" )
    print(f"{coins_1} coins of 1 are used" )
#ask the number
number = int(input("Write the number: "))
#call the function
The_number(number)

## Programa desarrollado por Andres Santiago Daza Daza --- 1095916023
