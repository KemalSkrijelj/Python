import math

def unosKordinata():
    xKordinate = list(map(float, input("Unesite x-koordinate: \n").split()))
    yKordinate = list(map(float, input("Unesite y-koordinate: \n").split()))

    if len(xKordinate) != len(yKordinate):
        print("X i Y moraju imati isti broj elemenata.")
        return None, None
    elif len(xKordinate) < 3:
        print("Poligon mora da ima bar tri temena.")
        return None, None

    return xKordinate, yKordinate

def duzinaStranice(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def obimPoligona(xKordinate, yKordinate):
    n = len(xKordinate)
    obim = 0
    for i in range(n):
        x1, y1 = xKordinate[i], yKordinate[i]
        x2, y2 = xKordinate[(i + 1) % n], yKordinate[(i + 1) % n]  
        obim += duzinaStranice(x1, y1, x2, y2)

    return obim

try:
    xKordinate, yKordinate = unosKordinata()
    obim = obimPoligona(xKordinate, yKordinate)
    print(f"Obim poligona: {obim:.2f}")
except:
    print(f"Grska")

