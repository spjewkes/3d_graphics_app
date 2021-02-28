# -*- coding: utf-8 -*-

from core.vector import Vector4d


class Triangle(object):
    def __init__(self, p0, p1, p2):
        self.p = (p0, p1, p2)

    def __str__(self):
        return '({0},{1},{2})'.format(self.p[0], self.p[1], self.p[2])

    def __getitem__(self, i):
        return self.p[i]

    def iterPoints(self):
        for p in self.p:
            yield p


class Mesh(object):
    def __init__(self, triangles):
        self.data = []
        self.data.append(triangles)

    def __getitem__(self, i):
        return self.data[i]

    def iterTriangles(self):
        for triangle in self.data:
            yield triangle
