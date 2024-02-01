D_productos = {'Paquete de soldados:':10000, 'Tiranosaurio rex:':6000, 'Carro Hotweels:':12000, }
print("Bienvenido usuario, por favor selescciona cual de los siguientes productos deseas: ")
for i, j in D_productos.items() :
    print(i, j) 
producto1 = input(str("ingresa el nombre del producto que deseas: "))
if producto1 == "Paquete de soldados":
    producto1 = D_productos["Paquete de soldados:"]
elif producto1 == "Tiranosaurio rex":
    producto1 = D_productos["Tiranosaurio rex:"]
elif producto1 == "Carro Hotweels":
    producto1 = D_productos["Carro Hotweels:"]
else:
    print("El producto ingresado no está registrado.")

Cantidad = int(input("Cuantas unidades deseas de este producto? "))

total = producto1 * Cantidad

print(total)
    
             
   
   
   
   
   
