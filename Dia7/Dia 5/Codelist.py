import math

def calcular_longitudes(monedas, altura):
    mcm_longitudes = monedas[0]
    mcd_longitudes = monedas[0]
    for moneda in monedas[1:]:
        mcm_longitudes = mcm_longitudes * moneda // math.gcd(mcm_longitudes, moneda)
        mcd_longitudes = math.gcd(mcd_longitudes, moneda)
   
    menor_mayor_longitud = mcm_longitudes * (altura // mcm_longitudes)
    mayor_menor_longitud = mcm_longitudes * ((altura + mcm_longitudes - 1) // mcm_longitudes)

    return menor_mayor_longitud, mayor_menor_longitud

# Lectura de la entrada
def Proceso():
    while True:
        n, t = map(int, input().split())
        if n == 0 and t == 0:
            break
        monedas = [int(input()) for _ in range(n)]
        alturas = [int(input()) for _ in range(t)]

        # Obtener las longitudes para cada mesa
        for altura in alturas:
            menor, mayor = calcular_longitudes(monedas, altura)
            print(menor, mayor)

Proceso()