import Hojadecodigos

number = int(input("Write the number: "))

Result = Hojadecodigos.The_number(number)

print(f"{Result['coins_10']} monedas de 10 son utilizadas")
print(f"{Result['coins_5']} monedas de 5 son utilizadas")
print(f"{Result['coins_1']} monedas de 1 son utilizadas")
