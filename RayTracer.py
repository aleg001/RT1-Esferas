from collections import namedtuple
from math import pi, tan
import math
import struct

from sphereUseful import *

V3 = namedtuple("PointXYZ", ["x", "y", "z"])


def color(r, g, b):
    return bytes([b, g, r])


def char(c):
    return struct.pack("=c", c.encode("ascii"))


def word(w):
    return struct.pack("=h", w)


def doubleword(d):
    return struct.pack("=l", d)


class RayTracer(object):
    def __init__(self, w, h) -> None:
        self.w = w
        self.h = h
        self.scene = []
        self.clearColor = color(0, 0, 0)
        self.currentColor = color(255, 255, 255)

    def sceneAdd(self, obj):
        self.scene.append(obj)

    def clear(self):
        self.framebuffer = [
            [self.clearColor for x in range(self.w)] for y in range(self.h)
        ]

    def point(self, x, y, color=None):
        if y >= 0 and y < self.h and x >= 0 and x < self.w:
            self.framebuffer[y][x] = color or self.currentColor

    def Render(self):
        fieldOfView = math.pi / 2
        fieldOfView = int(fieldOfView)
        ratio = self.w / self.h
        self.clear()
        for y in range(self.h):
            for x in range(self.w):
                tempOp = x + 0.5
                tempOp2 = y + 0.5
                halfFieldOfView = fieldOfView / 2
                tanFieldOfView = tan(halfFieldOfView)
                i = (2 * tempOp / self.w - 1) * ratio * tanFieldOfView
                j = (1 - 2 * tempOp2 / self.h) * tanFieldOfView

                origen = V3(0, 0, 0)
                direccion = Normalizar(V3(i, j, -1))

                c = self.RayCasting(origen, direccion)

                self.point(x, y, c)

    def RayCasting(self, origen, direccion):
        for i in self.scene:
            if i.intersectRay(origen, direccion):
                return i.coloring()
        return self.clearColor

    def write(self, filename):
        w = len(self.framebuffer)
        h = len(self.framebuffer[0])
        f = open(filename, "wb")
        f.write(char("B"))
        f.write(char("M"))
        f.write(doubleword(14 + 40 + w * h * 3))
        f.write(doubleword(0))
        f.write(doubleword(14 + 40))
        f.write(doubleword(40))
        f.write(doubleword(w))
        f.write(doubleword(h))
        f.write(word(1))
        f.write(word(24))
        f.write(doubleword(0))
        f.write(doubleword(w * h * 3))
        f.write(doubleword(0))
        f.write(doubleword(0))
        f.write(doubleword(0))
        f.write(doubleword(0))

        for y in range(0, h):
            for x in range(0, w):
                f.write(self.framebuffer[y][x])

        f.close()
