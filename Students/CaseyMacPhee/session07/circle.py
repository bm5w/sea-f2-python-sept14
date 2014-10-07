#!/usr/bin/env python
"""circle class --

fill this in so it will pass all the tests.
"""
import math


class Circle(object):
	def __init__(self, radius):
		self.rad = radius
		self.dia = radius * 2
		self.ar = math.pi * (radius**2)
	@property
	def radius(self):
		return self.rad

	@property
	def diameter(self):
		return self.dia
	@property
	def area(self):
		return self.ar

	@radius.setter 
	def radius(self, val):
		self.rad = val
		self.dia = val * 2
		self.ar = math.pi * (val ** 2)

	@diameter.setter
	def diameter(self, val):
		self.dia= val
		self.rad = val/2
		self.ar = math.pi * ((val/2) ** 2)
	

	def __cmp__(self, other):
		if self.area > other.area:
			return 1
		elif self.area < other.area:
			return -1
		else:
			return 0
	def __str__(self):
		return "Circle with radius: {}00000".format(float(self.rad))
	def __repr__(self):
		return "Circle({})".format(int(self.rad))
	def __add__(self,other):
		val = self.radius + other.radius
		return Circle(val)
	def __mul__(self, num):
		return Circle(num * self.radius)

	# @area.setter
	# def area(self, val):
	# 	self.dia = (math.sqrt(val/math.pi)) * 2
	# 	self.rad = math.sqrt(val/math.pi)
	# 	self.ar = val





