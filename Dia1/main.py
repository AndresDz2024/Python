## ------------------------------------------------
## ---------------- Ejercicio 1 -------------------
## ------------------------------------------------

# impresión en consola
print("Hoal mundo") 

#----- Datos Primitivos ---------------------------
#1. string
texto = "campus"
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
print ("tu nombre es: ", entradausuarioedadusuario) 
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