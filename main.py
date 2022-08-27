import math


def areaTriangulo(alt, base):
    return alt*base/2

def areaCirulo(radio):
    return radio**2 * math.pi

print("El área del triangulo es: " + str(areaTriangulo(6,5)))
print("El área del círculo es: " + str(areaCirulo(4)))