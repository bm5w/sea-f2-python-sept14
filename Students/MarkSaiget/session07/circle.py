#!/usr/bin/env python
"""circle class --

fill this in so it will pass all the tests.
"""
import math


class Circle(object):

    def __init__(self, radius):
        self._radius = radius
        self._diameter = 2*radius
        self._area = math.pi*(radius**2)

    """a class method to make alternate constructor that takes diameter"""
    @classmethod
    def diameterConstr(self, diameter):
        return Circle(diameter/2)

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):
        self._radius = radius
        self._diameter = radius*2
        self._area = math.pi*(radius**2)

    @property
    def diameter(self):
        return self._diameter

    @diameter.setter
    def diameter(self, diameter):
        self._diameter = diameter
        self._radius = diameter/2
        self._area = math.pi*((diameter/2)**2)

    @property
    def area(self):
        return self._area

    def __str__(self):
        return 'Circle with radius: {radius:.6f}'.format(radius=self._radius)

    def __repr__(self):
        return 'Circle({radius})'.format(radius=self._radius)

    @staticmethod
    def add(a, b):
        return Circle(a+b)
