##-----------------------------------------------
##-------------- ejercicio 6.3 ------------------
##-----------------------------------------------
import math

def Colision(bola1, bola2):
    x1, y1, r1 = bola1
    x2, y2, r2 = bola2

    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    return distance <= r1 + r2

bola1 = (1, 4, 2)
bola2 = (8, 8, 5)

print(Colision(bola1, bola2))

## Desarrollado por David Rivero, Daniel latorre, kenia hernandez, paula muñoz, joel santiago y Andres Daza.
