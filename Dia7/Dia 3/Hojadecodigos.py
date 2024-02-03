def The_number(number):
    #In case the user enters a negative number.
    if number < 0:
        print("The number entered is negative, please enter a positive number " )
        
    #Perform the operation
    coins_10 = number // 10
    number %= 10
    coins_5 = number // 5
    number %= 5
    coins_1 = number
    #Print the result
    Result = {
            "coins_10": coins_10, 
            "coins_5" : coins_5,
            "coins_1" : coins_1 }
            
    
    return Result