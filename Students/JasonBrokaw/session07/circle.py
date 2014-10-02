#!/usr/bin/env python
"""circle class --

fill this in so it will pass all the tests.
"""
import math


class Circle(object):
    def __init__(self, radius=0):
        self._radius = radius

    @classmethod
    def from_diameter(klass, diameter=0):
        return klass(diameter / 2.0)

    @property
    def radius(self):
        return self._radius

    @property
    def diameter(self):
        return 2 * self.radius

    @property
    def area(self):
        return math.pi * self.radius ** 2

    @radius.setter
    def radius(self, radius):
        self._radius = radius

    @diameter.setter
    def diameter(self, diameter):
        self._radius = diameter / 2.0


