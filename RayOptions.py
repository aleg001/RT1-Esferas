# Desplegar resultado
# Referencia: https://www.geeksforgeeks.org/python-pil-image-show-method/
from PIL import Image
from RayTracer import *
from sphereUseful import *

Raytracer = None


def HombreNieve():
    black = color(0, 0, 0)
    orange = color(255, 165, 0)
    snowmanColor = color(254, 253, 254)

    hombreNieve = []

    Ojo1 = Sphere(V3(0.5, -5, -15), 2.5 / 10, black)
    Ojo2 = Sphere(V3(-0.5, -5, -15), 2.5 / 10, black)
    Nariz = Sphere(V3(0, -4, -15), 32 / 100, orange)
    Nariz2 = Sphere(V3(-0.01, -4, -15), 32 / 100, orange)

    Boca1 = Sphere(V3(0, -3, -15), 13 / 100, black)

    Boca2 = Sphere(V3(1, -3.5, -15), 13 / 100, black)
    Boca3 = Sphere(V3(-1, -3.5, -15), 13 / 100, black)

    Boca6 = Sphere(V3(1.55, -3.9, -15), 13 / 100, black)
    Boca7 = Sphere(V3(-1.55, -3.9, -15), 13 / 100, black)

    Cuerpo1 = Sphere(V3(0, 3, -15), 4, snowmanColor)
    Cuerpo2 = Sphere(V3(0, -1, -15), 4 - 1, snowmanColor)
    Cuerpo3 = Sphere(V3(0, -4.01, -15), 4 / 2, snowmanColor)
    Botoncito2 = Sphere(V3(0, -1.5, -15), 35 / 100, black)
    Botoncito1 = Sphere(V3(0, -0.5, -15), 33 / 100, black)
    Botoncito3 = Sphere(V3(0, 0.5, -15), 30 / 100, black)

    hombreNieve.append(Ojo1)
    hombreNieve.append(Ojo2)
    hombreNieve.append(Boca1)
    hombreNieve.append(Boca2)
    hombreNieve.append(Boca3)
    hombreNieve.append(Boca6)
    hombreNieve.append(Boca7)
    hombreNieve.append(Nariz)
    hombreNieve.append(Nariz2)
    hombreNieve.append(Botoncito1)
    hombreNieve.append(Botoncito2)
    hombreNieve.append(Botoncito3)
    hombreNieve.append(Cuerpo1)
    hombreNieve.append(Cuerpo2)
    hombreNieve.append(Cuerpo3)
    return hombreNieve


def __init__(tituloArchivo):
    global Raytracer
    Raytracer = RayTracer(1000, 1000)
    Raytracer.clear()
    run(tituloArchivo)


def sceneAdd(obj):
    if isinstance(obj, list):
        for i in obj:
            Raytracer.sceneAdd(i)
    else:
        Raytracer.sceneAdd(obj)


def Execution(objectUsed, filename):
    sceneAdd(objectUsed)
    Raytracer.Render()
    Raytracer.write(filename)


def run(filename):
    Execution(HombreNieve(), filename)
    im = Image.open(filename)
    im.show()
