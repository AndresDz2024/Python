import json

## Punto 1: Devolver pedidos realizados de forma que estén ordenados de más recientes a más antiguos
print("-----------------------------------------------------------------------------------------------------------------------------------------------------")
print("Punto 1")
importar1 = open('data.json')
Njson1 = json.load(importar1)

def fecha_pedido(pedido):
    return pedido["fecha"]
numero_pedidos = (Njson1["ventas"]["pedidos"])

pedidos_ordenados = sorted(numero_pedidos, key=fecha_pedido, reverse=True)

for g in pedidos_ordenados:
    print(g)



##Punto 2: Devolver los datos de los dos pedidos de mayor valor
print("-----------------------------------------------------------------------------------------------------------------------------------------------------")
print("Punto 2")
def valor_pedido(pedido):
    return pedido["total"]

pedidos_Mayores = sorted(numero_pedidos, key=valor_pedido, reverse=True)

print(pedidos_Mayores[0])
print(pedidos_Mayores[1])

##Punto 3: Devolver los identificadores de los clientes que han realizado algún pedido, sin repetirse
print("-----------------------------------------------------------------------------------------------------------------------------------------------------")
print("Punto 3")
ListaDePedidos = []
for i in Njson1["ventas"]["pedidos"]:
    ListaDePedidos.append(i["id_cliente"])
Sin_repetir = set(ListaDePedidos)
print(Sin_repetir)

##Punto 4: Devolver pedidos realizados en el 2017, cuya cantidad sea superior a 500€
print("-----------------------------------------------------------------------------------------------------------------------------------------------------")
print("Punto 4")
cont=0
Lista2017 = []
for j in Njson1["ventas"]["pedidos"]:
    if "2017" in Njson1["ventas"]["pedidos"][cont]["fecha"]:
        if Njson1["ventas"]["pedidos"][cont]["total"] > 500:
            Lista2017.append(j)
        cont += 1
    else:
        cont += 1    

for g in Lista2017:
    print(g)

##Punto 5:
print("-----------------------------------------------------------------------------------------------------------------------------------------------------")
print("Punto 5")
comerciales_C = []
for n in Njson1["ventas"]["comerciales"]:
    if 0.05 <= n["comisión"] <= 0.11:
        comerciales_C.append(n)

nombres_apellidos = set()
for comercial in comerciales_C:
    nombres_apellidos.add(f"{comercial['nombre']} {comercial['apellido1']}")
for nombre_apellido in nombres_apellidos:
    print(nombre_apellido)


##Punto 6:
print("-----------------------------------------------------------------------------------------------------------------------------------------------------")
print("Punto 6")
MaxValor=[]
for i in Njson1["ventas"]["comerciales"]:
    MaxValor.append(i["comisión"])
MaxValor.sort()
MaxValor.reverse()
print(MaxValor[0])

##Punto 7:
print("-----------------------------------------------------------------------------------------------------------------------------------------------------")
print("Punto 7")
cont1=0

ListaSevilla = []

def funcion_prueba(cliente):
    return cliente["apellido1"], cliente["nombre"]


for x in Njson1["ventas"]["clientes"]:
    if "Sevilla" in Njson1["ventas"]["clientes"][cont1]["ciudad"]:
        ListaSevilla.append(x)
        ListaSevilla = sorted(ListaSevilla, key = funcion_prueba )
        cont1 += 1
    else:
        cont1 += 1
Ordenados = []            
for comision in ListaSevilla:
    Ordenados.append(f"{comision['id']}, {comision['apellido1']}, {comision['nombre']}") 

print(Ordenados)

##Punto 8:
print("-----------------------------------------------------------------------------------------------------------------------------------------------------")
print("Punto 8")
cont2 = 0
for x in Njson1["ventas"]["clientes"]:
    if "A" or "P" in Njson1["ventas"]["clientes"][cont2]["nombre"]:
        print("zi")
        cont2 += 1
    else:
        print("no")
        cont2 += 1    