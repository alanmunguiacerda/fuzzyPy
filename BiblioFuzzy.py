#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

class BiblioFuzzy():
    def __init__(self):
        pass

    @staticmethod
    def trapecio_abierto_der(u, a, b):
        if u > b:
            return 1.0
        if u < a:
            return 0.0
        if a <= u and u <= b:
            return (float)(u - a)/(b - a)

    @staticmethod
    def trapecio_abierto_izq(u, a, b):
        if u > b:
            return 0.0
        if u < a:
            return 1.0
        if a <= u and u <= b:
            return (float)(b - u) / (b - a)

    @staticmethod
    def triangular(u, a, b, c):
        if u < a or u > c:
            return 0.0
        if a <= u and u < b:
            return (u - a)/(b - a)
        if b <= u and u <= c:
            return (float)(c - u) / (c - b)

    @staticmethod
    def trapezoidal(u, a, b, c, d):
        if u < a or u > c:
            return 0.0
        if b <= u and u <= c:
            return 1.0
        if a <= u and u < b:
            return (float)(u - a)/(b - a)
        if c < u and u <= d:
            return (float)(d - u) / (d - c)

    @staticmethod
    def curva_s(u, a, b):
        if u > b:
            return 1.0
        if u < a:
            return 0.0
        if a <= u and u <= b:
            return (float)(1+math.cos(((u - b)/(b - a))*math.pi))/2.0

    @staticmethod
    def curva_z(u, a, b):
        if u > b:
            return 0.0
        if u < a:
            return 1.0
        if a <= u and u <= b:
            return (float)(1+math.cos(((u - a)/(b - a))*math.pi))/2.0

    @staticmethod
    def triangular_suave(u, a, b, c):
        if u < a or u > c:
            return 0.0
        if a <= u and u < b:
            return (float)(1 + math.cos(((u - b) / (b - a)) * math.pi)) / 2.0
        if b <= u and u <= c:
            return (float)(1 + math.cos(((b - u) / (c - b)) * math.pi)) / 2.0

    @staticmethod
    def trapezoidal_suave(u, a, b, c, d):
        if u < a or u > d:
            return 0.0
        if b <= u and u <= c:
            return 1.0
        if a <= u and u < b:
            return (float)(1 + math.cos(((u - b) / (b - a)) * math.pi)) / 2.0
        if c < u and u <= d:
            return (float)(1 + math.cos(((c - u) / (d - c)) * math.pi)) / 2.0

    @staticmethod
    def min(a, b):
        return (a, b)[a < b]

    @staticmethod
    def max(a, b):
        return (a, b)[a > b]

    @staticmethod
    def comp_and(ma_u, mb_u):
        return BiblioFuzzy.min(ma_u, mb_u)

    @staticmethod
    def comp_or(ma_u, mb_u):
        return BiblioFuzzy.max(ma_u, mb_u)

    @staticmethod
    def niega(ma_u):
        return 1 - ma_u

    @staticmethod
    def implica_zadeh(ma_x, mb_y):
        return BiblioFuzzy.max(BiblioFuzzy.min(ma_x, mb_y), BiblioFuzzy.niega(ma_x))

    @staticmethod
    def implica_mamdani(ma_x, mb_y):
        return min(ma_x, mb_y)

    @staticmethod
    def implica_godel(ma_x, mb_y):
        if ma_x <= mb_y:
            return 1.0
        return mb_y

print BiblioFuzzy.trapecio_abierto_der(5, 4, 15)