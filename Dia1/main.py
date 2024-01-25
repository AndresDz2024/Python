## ------------------------------------------------
## ---------------- Ejercicio 1 -------------------
## ------------------------------------------------
#-------------------- arreglos --------------------

from array import array
numeros = array("i", [2, 3, 5, 7])

print("array")
print(numeros[0])
print(numeros[1])
print(numeros[2])
print(numeros[3])

# funcion sin y sin
def saludo():
    print("Hola mundo") 
#funcion con y sin
def okey():
    a = 1
    b = 2
    c = 3
    return (a + b + c)
sumatoria = okey()
#funcion con y con
def test(N1, N2):
    return N1 + N2
#funcion sin y con
def resta(num1, num2, num3):
    print("La resta da como resultado", num1 - num2 - num3 )
# impresión en consola funcion sin y sin
saludo()
# impresion en consola funcion con y sin
print("La suma de 1, 2 y 3 da como resultado" , sumatoria )
# impresion en consola funcion con y con
print("El resultado de la suma entre 20 y 80 es:", test(20,80) )
# impresion en consola funcion sin y con
resta(20,10,5)
#----- Datos Primitivos ---------------------------
#1. string
texto = "hola mundo"
print(texto)
print(type(texto))
#2. Int
numeroEntero = 1
print(numeroEntero)
#3. Float
numeroDecimal = 3.1
print(numeroDecimal)
#4. Double
NumeroDecimalLargo = 3.1416970598796984
print(NumeroDecimalLargo)
#5. Boolean
boolean = True
print(boolean)
#------ Entradas parte del usuario -------------
entradausuario = input("ingresa tu nombre: ")
print ("tu nombre es: ", entradausuario) 
#------ Entradas parte del usuario cin definicion tipo de dato primitivo -------------
entradausuarioedadusuario = int(input("ingresa tu edad: "))
print ("tu edad es: ", entradausuarioedadusuario) 
# ---- Ciclos ----
#Ciclo for
for i in range(5,10,2):#for contador in range (desde, hasta, pasos):
    print(i)
#Ciclo while    
booleanito = True
while booleanito == True: #while condicion_a_cumplir :
    print("sigo vivo")
    booleanito = False
# ---- condicionales -----
texto1 = "campus"
if texto1 == "campus":
    print("soy campus")
else:
    print("no soy campus")     
## Desarrollado por: ANDRES SANTIAGO DAZA DAZA - 1095916023