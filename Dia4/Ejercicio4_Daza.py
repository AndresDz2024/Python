import itertools

def calcular_longitudes_monedas(n, gruesos, alturas):
    resultados = []
    for altura in alturas:
        combinaciones = []
        for perm in itertools.permutations(range(n), 4):
            combinacion = sum(gruesos[i] for i in perm)
            combinaciones.append(combinacion)
        combinaciones.sort()
        menor_longitud = next(x for x in combinaciones if x >= altura)
        mayor_longitud = next(x for x in reversed(combinaciones) if x <= altura)
        resultados.append((mayor_longitud, menor_longitud))
    return resultados

def main():
    while True:
        n, t = map(int, input().split())
        if n == 0 and t == 0:
            break
        gruesos = [int(input()) for _ in range(n)]
        alturas = [int(input()) for _ in range(t)]
        resultados = calcular_longitudes_monedas(n, gruesos, alturas)
        for res in resultados:
            print(res[0], res[1])

if __name__ == "__main__":
    main()
    ##No funciona