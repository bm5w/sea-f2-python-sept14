#!/usr/bin/env python
"""circle class --

fill this in so it will pass all the tests.
"""
import math


class Circle(object):
    def __init__(self, radius=0):
        self._radius = radius
        self._diameter = 2.0 * radius
        self._area = math.pi * radius ** 2

    @property
    def radius(self):
        return self._radius

    @property
    def diameter(self):
        return self._diameter

    @property
    def area(self):
        return self._area

    @radius.setter
    def radius(self, radius):
        self._radius = radius
        self._diameter = 2.0 * radius
        self._area = math.pi * radius ** 2

    @diameter.setter
    def diameter(self, diameter):
        self._diameter = diameter
        self._radius = diameter / 2.0
        self._area = math.pi * self._radius ** 2

