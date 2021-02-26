# -*- coding: utf-8 -*-

from core.vector import Vector4d


class Matrix:
    def __init__(self):
        self.m = [0.0] * 16
        self.m[0] = 1.0
        self.m[5] = 1.0
        self.m[10] = 1.0
        self.m[15] = 1.0

    def __str__(self):
        val = '[{0},{1},{2},{3}]'.format(
            self.m[0], self.m[1], self.m[2], self.m[3])
        val += '[{0},{1},{2},{3}]'.format(self.m[4],
                                          self.m[5], self.m[6], self.m[7])
        val += '[{0},{1},{2},{3}]'.format(self.m[8],
                                          self.m[9], self.m[10], self.m[11])
        val += '[{0},{1},{2},{3}]'.format(self.m[12],
                                          self.m[13], self.m[14], self.m[15])
        return val

    def __getitem__(self, i):
        return self.m[i]

    def __setitem__(self, i, v):
        self.m[i] = v

    def mult(self, m):
        tmp = [0.0] * 16
        tmp[0] = self.m[0] * m[0] + self.m[1] * \
            m[4] + self.m[2] * m[8] + self.m[3] * m[12]
        tmp[1] = self.m[0] * m[1] + self.m[1] * \
            m[5] + self.m[2] * m[9] + self.m[3] * m[13]
        tmp[2] = self.m[0] * m[2] + self.m[1] * \
            m[6] + self.m[2] * m[10] + self.m[3] * m[14]
        tmp[3] = self.m[0] * m[3] + self.m[1] * \
            m[7] + self.m[2] * m[11] + self.m[3] * m[15]
        tmp[4] = self.m[4] * m[0] + self.m[5] * \
            m[4] + self.m[6] * m[8] + self.m[7] * m[12]
        tmp[5] = self.m[4] * m[1] + self.m[5] * \
            m[5] + self.m[6] * m[9] + self.m[7] * m[13]
        tmp[6] = self.m[4] * m[2] + self.m[5] * \
            m[6] + self.m[6] * m[10] + self.m[7] * m[14]
        tmp[7] = self.m[4] * m[3] + self.m[5] * \
            m[7] + self.m[6] * m[11] + self.m[7] * m[15]
        tmp[8] = self.m[8] * m[0] + self.m[9] * m[4] + \
            self.m[10] * m[8] + self.m[11] * m[12]
        tmp[9] = self.m[8] * m[1] + self.m[9] * m[5] + \
            self.m[10] * m[9] + self.m[11] * m[13]
        tmp[10] = self.m[8] * m[2] + self.m[9] * m[6] + \
            self.m[10] * m[10] + self.m[11] * m[14]
        tmp[11] = self.m[8] * m[3] + self.m[9] * m[7] + \
            self.m[10] * m[11] + self.m[11] * m[15]
        tmp[12] = self.m[12] * m[0] + self.m[13] * \
            m[4] + self.m[14] * m[8] + self.m[15] * m[12]
        tmp[13] = self.m[12] * m[1] + self.m[13] * \
            m[5] + self.m[14] * m[9] + self.m[15] * m[13]
        tmp[14] = self.m[12] * m[2] + self.m[13] * \
            m[6] + self.m[14] * m[10] + self.m[15] * m[14]
        tmp[15] = self.m[12] * m[3] + self.m[13] * \
            m[7] + self.m[14] * m[11] + self.m[15] * m[15]
        self.m = tmp

    def multvec4d(self, v):
        v.normalize()
        x = self.m[0] * v[0] + self.m[1] * v[1] + \
            self.m[2] * v[2] + self.m[3] * v[3]
        y = self.m[4] * v[0] + self.m[5] * v[1] + \
            self.m[6] * v[2] + self.m[7] * v[3]
        z = self.m[8] * v[0] + self.m[9] * v[1] + \
            self.m[10] * v[2] + self.m[11] * v[3]
        w = self.m[12] * v[0] + self.m[13] * v[1] + \
            self.m[14] * v[2] + self.m[15] * v[3]
        return Vector4d(x, y, z, w)
