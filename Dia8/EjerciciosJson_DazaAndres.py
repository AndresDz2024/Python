import json

## Punto 1: Devolver pedidos realizados de forma que estén ordenados de más recientes a más antiguos
importar1 = open('data.json')
Njson1 = json.load(importar1)

def fecha_pedido(pedido):
    return pedido["fecha"]
numero_pedidos = (Njson1["ventas"]["pedidos"])

pedidos_ordenados = sorted(numero_pedidos, key=fecha_pedido, reverse=True)

print(pedidos_ordenados)



##Punto 2: Devolver los datos de los dos pedidos de mayor valor
print("-----------------------------------------------------------------------------------------------------------------------------------------------------")
def valor_pedido(pedido):
    return pedido["total"]

pedidos_ordenados = sorted(numero_pedidos, key=valor_pedido, reverse=True)

print(pedidos_ordenados[0], pedidos_ordenados[1])

##Punto 3: Devolver los identificadores de los clientes que han realizado algún pedido, sin repetirse
print("-----------------------------------------------------------------------------------------------------------------------------------------------------")
ListaDePedidos = []
for i in Njson1["ventas"]["pedidos"]:
    ListaDePedidos.append(i["id_cliente"])
Sin_repetir = set(ListaDePedidos)
print(Sin_repetir)

##Punto 4: Devolver pedidos realizados en el 2017, cuya cantidad sea superior a 500€
print("-----------------------------------------------------------------------------------------------------------------------------------------------------")
cont=0
Lista2017 = []
for j in Njson1["ventas"]["pedidos"]:
    if "2017" in Njson1["ventas"]["pedidos"][cont]["fecha"]:
        if Njson1["ventas"]["pedidos"][cont]["total"] > 500:
            Lista2017.append(j)
        cont += 1
    else:
        cont += 1    

print(Lista2017)

##Punto 5:






##Punto 6:

MaxValor=[]
for i in Njson1["ventas"]["comerciales"]:
    MaxValor.append(i["comisión"])
MaxValor.sort()
MaxValor.reverse()
print(MaxValor[0])