# -*- coding: utf-8 -*-

from core.vector import Vector4d


class Triangle(object):
    def __init__(self, p0, p1, p2):
        self.p = (p0, p1, p2)

    def __str__(self):
        return '({0},{1},{2})'.format(p[0], p[1], p[2])

    def __getitem__(self, i):
        return self.p[i]


class Mesh(object):
    def __init__(self, triangles):
        self.data = []
        self.data.append(triangles)

    def __getitem__(self, i):
        return self.data[i]
