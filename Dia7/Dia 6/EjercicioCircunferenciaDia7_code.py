def Dey6():
    import math

    def Colision(bola1, bola2):
        x1, y1, r1 = bola1
        x2, y2, r2 = bola2

    

        distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

        print(distance)

        return distance <= r1 + r2


    bola1 = map(int, input().split())
    bola2 = map(int, input().split())

    print(Colision(bola1, bola2))
