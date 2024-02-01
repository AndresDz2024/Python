import itertools

# Lee la entrada
while True:
    n, t = map(int, input().split())
    if n == 0 and t == 0:
        break

    coins_thickness = [int(input()) for _ in range(n)]
    table_heights = [int(input()) for _ in range(t)]

    print(coins_thickness)
    print(table_heights)

    # Itera sobre cada altura de la mesa
    for height in t:
        closest_lengths = []
       
        # Genera todas las combinaciones posibles de monedas para las patas
        for combination in itertools.product(coins_thickness, repeat=4):
            leg_lengths = [sum(x) for x in itertools.permutations(combination)]
            closest_lengths.append((max([x for x in leg_lengths if x <= height]), min([x for x in leg_lengths if x >= height])))

        # Encuentra las longitudes más cercanas a la altura deseada e imprímelas
        closest = min(closest_lengths, key=lambda x: abs(x[0] - height) + abs(x[1] - height))
        print(closest[0], closest[1])

        ##No funciona