##-----------------------------------------------
##-----------------------------------------------
##------------- Ejercicio 3 ---------------------
##-----------------------------------------------

def The_number(number):
    if number < 0:
        print("The number entered is negative, please enter a positive number " )
        return
    coins_10 = number // 10
    number %= 10
    coins_5 = number // 5
    number %= 5
    coins_1 = number
    print(f"{coins_10} coins of 10 are used" )
    print(f"{coins_5} coins of 5 are used" )
    print(f"{coins_1} coins of 1 are used" )
number = int(input("Write the number: "))
The_number(number)