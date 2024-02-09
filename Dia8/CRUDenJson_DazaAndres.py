import json

def Crear_C():
    with open("data2.json", "r") as outfile:
        Data = json.load(outfile)

    nuevo_cliente = {}
    nuevo_cliente["id"] = int(input("Ingrese el ID del nuevo cliente: "))
    nuevo_cliente["nombre"] = input("Ingrese el nombre del nuevo cliente: ")
    nuevo_cliente["apellido1"] = input("Ingrese el primer apellido del nuevo cliente: ")
    nuevo_cliente["apellido2"] = input("Ingrese el segundo apellido del nuevo cliente (opcional): ")
    nuevo_cliente["ciudad"] = input("Ingrese la ciudad del nuevo cliente: ")
    nuevo_cliente["categoria"] = int(input("Ingrese la categoría del nuevo cliente: "))

    Data["ventas"]["clientes"].append(nuevo_cliente)

    with open("data2.json", "w") as outfile:
        json.dump(Data, outfile,indent=4) 

def Leer_C():
    with open("data2.json") as outfile:
        Data = json.load(outfile)
        clientes = Data["ventas"]["clientes"]
        for i in clientes:
            print(i)

def Actualizar_C():
    miVariable = open("data2.json")
    Data = json.load(miVariable)
    clientes = Data["ventas"]["clientes"]
    id_json = int(input("Ingresa el id del cliente que quieras actualizar: "))
    for cliente in clientes:
        if cliente["id"] == id_json:
            nombre = input("Ingresa el nuevo nombre: ") 
            apellido1 = input("Ingresa el nuevo primer apellido: ")
            apellido2 = input("Ingresa el nuevo segundo apellido (opcional): ")
            ciudad = input("Ingresa la nueva ciudad: ")
            categoria = int(input("Ingrese la nueva categoria: ")) 
            cliente["nombre"] = nombre
            cliente["apellido1"] = apellido1
            cliente["apellido2"] = apellido2 
            cliente["ciudad"] = ciudad
            cliente["categoria"] = categoria
    
    with open("data2.json", "w") as outfile:
        json.dump(Data, outfile, indent=4)
        
def Eliminar_C():
    miVariable = open("data2.json")
    Data = json.load(miVariable)
    clientes = Data["ventas"]["clientes"]
    
    id_json = int(input("Ingresa el id del cliente que quieras eliminar: "))
    
    for cliente in clientes:
        if cliente["id"] == id_json:
            clientes.remove(cliente) 
            
    with open("data2.json", "w") as outfile:
        json.dump(Data, outfile, indent=4)

def Crear_Com():
    with open("data2.json", "r") as outfile:
        Data = json.load(outfile)

    nuevo_comercial = {}
    nuevo_comercial["id"] = int(input("Ingrese el ID del nuevo comercial: "))
    nuevo_comercial["nombre"] = input("Ingrese el nombre del nuevo comercial: ")
    nuevo_comercial["apellido1"] = input("Ingrese el primer apellido del nuevo comercial: ")
    nuevo_comercial["apellido2"] = input("Ingrese el segundo apellido del nuevo comercial: ")
    nuevo_comercial["comision"] = float(input("Ingrese la comision del nuevo comercial: "))

    Data["ventas"]["comerciales"].append(nuevo_comercial)

    with open("data2.json", "w") as outfile:
        json.dump(Data, outfile,indent=4) 

def Leer_Com():
    with open("data2.json") as outfile:
        Data = json.load(outfile)
        comerciales = Data["ventas"]["comerciales"]
        for i in comerciales:
            print(i)

def Actualizar_Com():
    miVariable = open("data2.json")
    Data = json.load(miVariable)
    comerciales = Data["ventas"]["comerciales"]
    id_json = int(input("Ingresa el id del comercial que quieras actualizar: "))
    for comercial in comerciales:
        if comercial["id"] == id_json:
            nombre = input("Ingresa el nuevo nombre: ") 
            apellido1 = input("Ingresa el nuevo primer apellido: ")
            apellido2 = input("Ingresa el nuevo segundo apellido: ")
            categoria = float(input("Ingrese la nueva comision: ")) 
            comercial["nombre"] = nombre
            comercial["apellido1"] = apellido1
            comercial["apellido2"] = apellido2 
            comercial["comision"] = categoria
    
    with open("data2.json", "w") as outfile:
        json.dump(Data, outfile, indent=4)

def Eliminar_Com():
    miVariable = open("data2.json")
    Data = json.load(miVariable)
    comerciales = Data["ventas"]["comerciales"]
    
    id_json = int(input("Ingresa el id del comercial que quieras eliminar: "))
    
    for comercial in comerciales:
        if comercial["id"] == id_json:
            comerciales.remove(comercial) 
            
    with open("data2.json", "w") as outfile:
        json.dump(Data, outfile, indent=4)

def Crear_P():
    with open("data2.json", "r") as outfile:
        Data = json.load(outfile)

    nuevo_pedido = {}
    nuevo_pedido["id"] = int(input("Ingrese el ID del nuevo pedido: "))
    nuevo_pedido["total"] = float(input("Ingrese el total del nuevo pedido: "))
    nuevo_pedido["fecha"] = input("Ingrese la fecha del nuevo pedido: ")
    nuevo_pedido["id_cliente"] = int(input("Ingrese el id del cliente: "))
    nuevo_pedido["id_comercial"] = int(input("Ingrese el id del comercial: "))

    Data["ventas"]["pedidos"].append(nuevo_pedido)

    with open("data2.json", "w") as outfile:
        json.dump(Data, outfile,indent=4) 

def Leer_P():
    with open("data2.json") as outfile:
        Data = json.load(outfile)
        pedidos = Data["ventas"]["pedidos"]
        for i in pedidos:
            print(i)
            
def Actualizar_P():
    miVariable = open("data2.json")
    Data = json.load(miVariable)
    pedidos = Data["ventas"]["pedidos"]
    id_json = int(input("Ingresa el id del pedido que quieras actualizar: "))
    for pedido in pedidos:
        if pedido["id"] == id_json:
            total = float(input("Ingresa el nuevo valor total: ") )
            fecha = input("Ingresa la nueva fecha: ")
            id_cliente = int(input("Ingresa el nuevo id del cliente: "))
            id_comercial = int(input("Ingrese el nuevo id del comercial: ")) 
            pedido["total"] = total
            pedido["fecha"] = fecha
            pedido["id_cliente"] = id_cliente
            pedido["id_comercial"] = id_comercial
    
    with open("data2.json", "w") as outfile:
        json.dump(Data, outfile, indent=4)
        
def Eliminar_P():

    miVariable = open("data2.json")
    Data = json.load(miVariable)
    pedidos = Data["ventas"]["pedidos"]
    
    id_json = int(input("Ingresa el id del pedido que quieras eliminar: "))
    
    for pedido in pedidos:
        if pedido["id"] == id_json:
            pedidos.remove(pedido) 
            
    with open("data2.json", "w") as outfile:
        json.dump(Data, outfile, indent=4)


def Inicio():
  
  print("¿Que deseas hacer usuario? (ingresa el numero o escribe salir para finalizar) ")

  print("1. Crear")

  print("2. Leer")

  print("3. Actualizar")

  print("4. Eliminar")

  print("---salir---")


outfile_json = "data2.json"
while True:
  
    Inicio()
    num1 = input("¿Que opcion deseas?:  ")
    if num1 == "1":
      crear = input("clientes - comerciales - pedidos: ").lower()
      if crear == "clientes":
        Crear_C()
      elif crear == "comerciales":
        Crear_Com()
      elif crear == "pedidos":
        Crear_P()
      else:
        print("Por favor, ingresa la opcion correctamente")
    elif num1 == "2":
      leer = input("clientes - comerciales - pedidos: ").lower()
      if leer == "clientes":
        Leer_C()
      elif leer == "comerciales":
        Leer_Com()
      elif leer == "pedidos":
        Leer_P()
      else:
        print("Por favor, ingresa la opcion correctamente")
    elif num1 == "3":
      actualizar = input("clientes - comerciales - pedidos: ").lower()
      if actualizar == "clientes":
        Actualizar_C()
      elif actualizar == "comerciales":
        Actualizar_Com()
      elif actualizar == "pedidos":
        Actualizar_P()
      else:
        print("Por favor, ingresa la opcion correctamente")
    elif num1 == "4":
      eliminar = input("clientes - comerciales - pedidos: ").lower()
      if eliminar == "clientes":
        Eliminar_C()
      elif eliminar == "comerciales":
        Eliminar_Com()
      elif eliminar == "pedidos":
        Eliminar_P()
      else:
        print("Por favor, ingresa la opcion correctamente")
    elif num1 == "salir":
        print("Nos vemos en otra ocasion usuario, espero que mis servicios hayan sido de utilidad.")
        break
    else:
       print("Por favor ingresa una opcion valida")
