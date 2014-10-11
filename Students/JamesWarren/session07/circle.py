#!/usr/bin/env python
"""circle class --

fill this in so it will pass all the tests.
"""
import math


class Circle(object):
    
    def __init__(self, radius):
        self._radius = radius
        self._diameter = radius * 2
        self._area = math.pi * radius**2

    @property
    def radius(self):
        return self._radius
    @radius.setter
    def radius(self, value):
        self._radius = value
        self._diameter = self._radius * 2
        self._area = math.pi * self._radius**2

    @property
    def diameter(self):
        return self._diameter
    @diameter.setter
    def diameter(self, value):
        self._diameter = value
        self._radius = self._diameter / 2.0
        self._area = math.pi * self._radius**2

    @property
    def area(self):
        return self._area

    def __str__(self):
        return "Circle with radius: %s" % format(self.radius, '.6f')

    def __repr__(self):
        return "Circle(%s)" % self.radius

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __sub__(self, other):
        return Circle(self.radius - other.radius)

    def __mul__(self, other):
        return Circle(self.radius * other)

    def __lt__(self, other):
        return self.radius < other.radius
    def __le__(self, other):
        return self.radius <= other.radius

    def __gt__(self, other):
        return self.radius > other.radius
    def __ge__(self, other):
        return self.radius >= other.radius

    def __eq__(self, other):
        return self.radius == other.radius
    def __ne__(self, other):
        return self.radius != other.radius