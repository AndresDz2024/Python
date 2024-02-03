def dia6():
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