"""
Discarded, python already has support of such.
"""

from __future__ import annotations
from multipledispatch import dispatch

from numberTheory import power

class Imaginary:
    a: float
    def __init__(self, a: float):
        self.a = a
    def __mul__(self, b: float):
        return Imaginary(self.a*b)
    def __mul__(self, b: Imaginary):
        return - self.a*b.a
    def __add__(self, b: float):
        return Complex(a=b, b=self.a)
    def __add__(self, b: Imaginary):
        return Imaginary(self.a + b.a)

i = Imaginary(1) # Unit

class Complex:
    a: float
    b: float

    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def __add__(self, c: float):
        return Complex(self.a + c, self.b)
    def __add__(self, c: Imaginary):
        return Complex(self.a, self.b + c.a)
    def __add__(self, c: Complex):
        return Complex(self.a + c.a, self.b + c.b)
    
    @dispatch(int)
    def __sub__(self, c: float):
        return Complex(self.a - c, self.b)
    @dispatch(Imaginary)
    def __sub__(self, c: Imaginary):
        return Complex(self.a, self.b - c.a)
    @dispatch(complex)
    def __sub__(self, c: Complex):
        return Complex(self.a - c.a, self.b - c.b)
    

    def __mul__(self, c: float):
        return Complex(self.a * c, self.b * c)
    
    def __mul__(self, c: Imaginary):
        return Complex(- self.b * c.a, self.a * c.a)
    
    def __mul__(self, c: Complex):
        return Complex((self.a * c.a) - (self.b * c.b), (self.a * c.b) + (self.b * c.a))
    


    def __truediv__(self, c: float):
        return Complex(self.a / c, self.b / c)
    

    def print(self):
        print(f"{self.a} + {self.b}i")

    def conjugate(self):
        return Complex(self.a, - self.b)