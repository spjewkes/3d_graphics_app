# -*- coding: utf-8 -*-

import math
import copy


class Vector3d:
    def __init__(self, x, y, z):
        self.v = [x, y, z]

    def __str__(self):
        return '({0},{1},{2})'.format(v[0], v[1], v[2])

    def __getitem__(self, i):
        return self.v[i]

    def __add__(self, v):
        return Vector3d(self.v[0] + v.v[0], self.v[1] + v.v[1], self.v[2] + v.v[2])

    def __iadd__(self, v):
        self.v[0] += v.v[0]
        self.v[1] += v.v[1]
        self.v[2] += v.v[2]
        return self

    def __sub__(self, v):
        return Vector3d(self.v[0] - v.v[0], self.v[1] - v.v[1], self.v[2] - v.v[2])

    def __isub__(self, v):
        self.v[0] -= v.v[0]
        self.v[1] -= v.v[1]
        self.v[2] -= v.v[2]
        return self

    def mag(self):
        return math.sqrt((self.v[0] ^ 2) + (self.v[1] ^ 2) + (self.v[2] ^ 2))

    def normalize(self):
        length = self.mag()
        if length == 0.0:
            self.v = [0.0, 0.0, 0.0]
        else:
            self.v = [self.p[0] / length, self.v[1] /
                      length, self.v[2] / length]

    def dot(self, p):
        return (self.v[0] * p.v[0]) + (self.v[1] * p.v[1]) + (self.v[2] * p.v[2])

    def cross(self, p):
        x = (self.v[1] * p.v[2]) - (p.v[1] * self.v[2])
        y = (self.v[2] * p.v[0]) - (p.v[2] * self.v[0])
        z = (self.v[0] * p.v[1]) - (p.v[0] * self.v[1])
        return Vector3d(x, y, z)


class Vector4d:
    def __init__(self, x, y, z, w=1.0):
        self.v = [x, y, z, w]

    def __str__(self):
        return '({0},{1},{2},{3})'.format(self.v[0], self.v[1], self.v[2], self.v[3])

    def __getitem__(self, i):
        return self.v[i]

    def __add__(self, v):
        hom = self.v[3] / v[3]
        return Vector4d(self.v[0] + v.v[0] * hom, self.v[1] + v.v[1] * hom, self.v[2] + v.v[2] * hom, self.v[3])

    def __iadd__(self, v):
        if isinstance(v, Vector4d):
            hom = self.v[3] / v[3]
            self.v[0] += v.v[0] * hom
            self.v[1] += v.v[1] * hom
            self.v[2] += v.v[2] * hom
        else:
            self.v[0] += v
            self.v[1] += v
            self.v[2] += v
        return self

    def __sub__(self, v):
        hom = self.v[3] / v[3]
        return Vector4d(self.v[0] - v.v[0] * hom, self.v[1] - v.v[1] * hom, self.v[2] - v.v[2] * hom, self.v[3])

    def __isub__(self, v):
        if isinstance(v, Vector4d):
            hom = self.v[3] / v[3]
            self.v[0] -= v.v[0] * hom
            self.v[1] -= v.v[1] * hom
            self.v[2] -= v.v[2] * hom
        else:
            self.v[0] -= v
            self.v[1] -= v
            self.v[2] -= v
        return self

    def __mul__(self, scale):
        v = Vector4d(self.v[0], self.v[1], self.v[2], self.v[3])
        v[3] /= scale
        v.normalize()
        return v

    def __imul__(self, scale):
        self.v[3] *= scale
        self.normalize()
        return self

    def __div__(self, scale):
        v = Vector4d(self.v[0], self.v[1], self.v[2], self.v[3])
        v[3] *= scale
        v.normalize()
        return v

    def __idiv__(self, scale):
        self.v[3] /= scale
        self.normalize()
        return self

    def mag(self):
        val = (self.v[0] ^ 2) + (self.v[1] ^ 2) + (self.v[2] ^ 2)
        if self.v[3] == 1.0:
            return math.sqrt(val)
        else:
            return math.sqrt(val / self.v[3])

    def normalize(self):
        if self.v[3] == 0.0:
            self.v = [0.0, 0.0, 0.0, 0.0]
        elif self.v[3] != 1.0:
            self.v = [self.v[0] / self.v[3],
                      self.v[1] / self.v[3],
                      self.v[2] / self.v[3],
                      1.0]

    def unit(self):
        self.v[3] = self.mag()

    def dot(self, p):
        v1 = copy.copy(self).normalize()
        v2 = copy.copy(p).normalize()
        return (v1.v[0] * v2.v[0]) + (v1.v[1] * v2.v[1]) + (v1.v[2] * v2.v[2])

    def cross(self, p):
        v1 = copy.copy(self).normalize()
        v2 = copy.copy(p).normalize()
        x = (v1.v[1] * v2.v[2]) - (v2.v[1] * v1.v[2])
        y = (v1.v[2] * v2.v[0]) - (v2.v[2] * v1.v[0])
        z = (v1.v[0] * v2.v[1]) - (v2.v[0] * v1.v[1])
        return Vector4d(x, y, z, 1.0)
