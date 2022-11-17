from collections import namedtuple
from math import pi, tan


V3 = namedtuple("XYZ", ["x", "y", "z"])


def color(r, g, b):
    return bytes([b, g, r])


def RestaV3(firstV, secondV):
    tempRes1 = firstV.x - secondV.x
    tempRes2 = firstV.y - secondV.y
    tempRes3 = firstV.z - secondV.z
    returningV3 = V3(tempRes1, tempRes2, tempRes3)
    return returningV3


def ProductoPunto(firstV, secondV):
    firstProduct = firstV.x * secondV.x
    secondProduct = firstV.y * secondV.y
    thirdProduct = firstV.z * secondV.z
    result = firstProduct + secondProduct + thirdProduct
    return result


def Tamanio(firstV):
    potencia1 = firstV.x**2
    potencia2 = firstV.y**2
    potencia3 = firstV.z**2
    varPotencia = potencia1 + potencia2 + potencia3
    varPotencia = varPotencia**0.5
    return varPotencia


def Normalizar(firstV):
    l = Tamanio(firstV)
    if l == 0:
        return V3(0, 0, 0)

    else:
        calc1 = firstV.x / l
        calc2 = firstV.y / l
        calc3 = firstV.z / l
        result = V3(calc1, calc2, calc3)
        return result


class Sphere(object):
    def __init__(self, center, radio, color=color(255, 255, 255)) -> None:
        self.center = center
        self.radio = radio
        self.color = color

    def coloring(self):
        return self.color

    def intersectRay(self, origen, direccion):
        L = RestaV3(self.center, origen)
        ProductoPuntoLDireccion = ProductoPunto(L, direccion)
        ProductoPuntoL = ProductoPunto(L, L) - ProductoPuntoLDireccion**2
        radioCuadrado = self.radio**2
        if ProductoPuntoL > radioCuadrado:
            return False

        RADIOUSC = radioCuadrado - ProductoPuntoL
        firstT = ProductoPuntoLDireccion - RADIOUSC
        secondT = ProductoPuntoLDireccion + RADIOUSC

        if firstT < 0:
            firstT = secondT
            return False
        return True
