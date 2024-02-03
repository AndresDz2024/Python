import ModuloCodigos
def fibo(N):
    fibo_secuencia = [0, 1]    
    while len(fibo_secuencia) < N:
        fibo_secuencia.append(fibo_secuencia[-1] + fibo_secuencia[-2])
    return fibo_secuencia
def Inicio():
    
    ModuloCodigos.F_secuencia()
    
    while True:
        try:
            N = int(input("ingrese hasta que valor de la secuencia fibonacci desea llegar "))
            
            if N < 0:
                print("El numero ingresado no es valido, ingrese un numero entero ")
                continue
            resultado = fibo(N)
            print(f"secuencia de fibonacci hasta el termino {N}: {resultado}")
            
            continuacion = input("¿Desea continuar? (si/no)")
            if continuacion != "si":
                print("Hasta pronto usuario")
                break
        except ValueError:
            print("por favor, ingrese un valor entero que haga referencia a el termino de la secuencia fibonacci que desea llegar")
Inicio()                
