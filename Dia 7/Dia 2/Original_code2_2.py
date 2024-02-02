def dia2_2():
    ## -------------------------------------------------
    ## ------------------ Ejercicio2 -------------------
    ## -------------------------------------------------

    import random

    def juego():
        naleatorio = random.randint(1, 100)
    
        print("Bienvenido usuario, ahora inicia el juego de azar, tienes que adivinar un numero de 1 a 100")
        print("recuerde que solo tiene 10 intentos")
    
        vidas=0
        while vidas<10:
            try:
                Nuser = int(input("ingrese su numero: "))
                if Nuser == naleatorio:
                    print(f"Felicitaciones usuario, has acertado el numero aleatorio, el numero era: {naleatorio}")
                    break
                elif Nuser < naleatorio:
                    print("El número que ingresaste no es el numero, ingresaste un numero menor ")
                elif Nuser > naleatorio:
                    print("El número que ingresaste no es el numero, ingresaste un numero mayor al numero ")
                vidas+=1
            except ValueError:
                print("Usuario, recuerda ingresar un numero entero " )
        if vidas == 10:
            print(f"Tus vidas se han terminado, no lograste acertar el numero, el número oculto era: {naleatorio} ")
        
    juego()