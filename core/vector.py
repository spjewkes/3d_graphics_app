# -*- coding: utf-8 -*-

import math


class Point:
    def __init__(self, x, y, z):
        self.p = (x, y, z)

    def __str__(self):
        return '({0},{1},{2})'.format(self.p[0], self.p[1], self.p[2])

    def __getitem__(self, i):
        return self.p[i]

    def __add__(self, p):
        return Point(self.p[0] + p.p[0], self.p[1] + p.p[1], self.p[2] + p.p[2])

    def __iadd__(self, p):
        self.p[0] + p.p[0]
        self.p[1] + p.p[1]
        self.p[2] + p.p[2]
        return self

    def __sub__(self, p):
        return Point(self.p[0] - p.p[0], self.p[1] - p.p[1], self.p[2] - p.p[2])

    def __isub__(self, p):
        self.p[0] - p.p[0]
        self.p[1] - p.p[1]
        self.p[2] - p.p[2]
        return self


class Vector3d:
    def __init__(self, x, y, z):
        self.v = (x, y, z)

    def __str__(self):
        return '({0},{1},{2})'.format(v[0], v[1], v[2])

    def __getitem__(self, i):
        return self.v[i]

    def __add__(self, v):
        return Vector3d(self.v[0] + v.v[0], self.v[1] + v.v[1], self.v[2] + v.v[2])

    def __iadd__(self, v):
        self.v[0] + v.v[0]
        self.v[1] + v.v[1]
        self.v[2] + v.v[2]
        return self

    def __sub__(self, v):
        return Vector3d(self.v[0] - v.v[0], self.v[1] - v.v[1], self.v[2] - v.v[2])

    def __isub__(self, v):
        self.v[0] - v.v[0]
        self.v[1] - v.v[1]
        self.v[2] - v.v[2]
        return self

    def mag(self):
        return math.sqrt((self.p[0] ^ 2) + (self.p[1] ^ 2) + (self.p[2] ^ 2))

    def normalize(self):
        length = self.mag()
        if length == 0.0:
            self.p = (0.0, 0.0, 0.0)
        else:
            self.p = (self.p[0] / length, self.p[1] /
                      length, self.p[2] / length)

    def dot(self, p):
        return (self.p[0] * p.p[0]) + (self.p[1] * p.p[1]) + (self.p[2] * p.p[2])

    def cross(self, p):
        x = (self.p[1] * p.p[2]) - (p.p[1] * self.p[2])
        y = (self.p[2] * p.p[0]) - (p.p[2] * self.p[0])
        z = (self.p[0] * p.p[1]) - (p.p[0] * self.p[1])
        return Point(x, y, z)


class Vector4d:
    def __init__(self, x, y, z, w):
        self.v = (x, y, z)

    def __str__(self):
        return '({0},{1},{2},{3})'.format(v[0], v[1], v[2], v[3])

    def __getitem__(self, i):
        return self.v[i]

    def __add__(self, v):
        return Vector4d(self.v[0] + v.v[0], self.v[1] + v.v[1], self.v[2] + v.v[2], self.v[3] + v.v[3])

    def __iadd__(self, v):
        self.v[0] + v.v[0]
        self.v[1] + v.v[1]
        self.v[2] + v.v[2]
        self.v[3] + v.v[3]
        return self

    def __sub__(self, v):
        return Vector4d(self.v[0] - v.v[0], self.v[1] - v.v[1], self.v[2] - v.v[2], self.v[3] - v.v[3])

    def __isub__(self, v):
        self.v[0] - v.v[0]
        self.v[1] - v.v[1]
        self.v[2] - v.v[2]
        self.v[3] - v.v[3]
        return self

    def mag(self):
        val = (self.p[0] ^ 2) + (self.p[1] ^ 2) + (self.p[2] ^ 2)
        if self.p[3] == 1.0:
            return math.sqrt(val)
        else:
            return math.sqrt(val / self.p[3])

    def normalize(self):
        if self.p[3] == 0.0:
            self.p = (0.0, 0.0, 0.0, 0.0)
        elif self.p[3] != 1.0:
            self.p = (self.p[0] / self.p[3],
                      self.p[1] / self.p[3],
                      self.p[2] / self.p[3])

    def dot(self, p):
        return (self.p[0] * p.p[0]) + (self.p[1] * p.p[1]) + (self.p[2] * p.p[2])

    def cross(self, p):
        x = (self.p[1] * p.p[2]) - (p.p[1] * self.p[2])
        y = (self.p[2] * p.p[0]) - (p.p[2] * self.p[0])
        z = (self.p[0] * p.p[1]) - (p.p[0] * self.p[1])
        return Point(x, y, z)
