from __future__ import annotations

import sys
import sys
import numberTheory
from typing import Type


sys.path.append("../../../modules/py")
import general

class Fraction:
    p: int
    q: int

    def __init__(self, p: int, q: int):
        
        if q == 0: print("\x1b[93m[Warning] Divisor of a Fraction is 0, proceed with caution.\x1b[0m")

        self.p = p
        self.q = q

    def get_symbolic(self, reciprocal: bool = False)->tuple[int, int]:
        return (self.p, self.q) if not reciprocal else (self.q, self.p)
    
    def get_numerical(self, reciprocal: bool = False)->float:
        return self.p/self.q if not reciprocal else self.q/self.p
    
    def reciprocal(self)->None:
        
        """
        Switches Dividend and the Divisor
        """

        a = self.p
        self.p = self.q
        self.q = a

    def scale(self, c: int):
        self.p *= c
        self.q *= c

    def __mul__(self, y: int):
        self.p *= y
        return self
    
    def __mul__(self, y: Fraction):
        self.p *= y.p
        self.q *= y.q
        return self

    def __add__(self, y: Fraction):
        
        c = self.q
        d = y.q

        cdGCD = numberTheory.GCD(c, d)
        s1 = c // cdGCD
        s2 = d // cdGCD

        self.scale(s2)
        y.scale(s1)

        a = self.p
        b = y.p
        c = self.q
        d = y.q
        if (c != d): raise ValueError(f"Fraction Multiplication Error ({c}, {d})")

        f = Fraction(a+b, c)

        return f

    def coprimeRatio(self):
        pList, qList = general.removeCommon2([numberTheory.primeFactor(self.p), numberTheory.primeFactor(self.q)])

        p = 1
        q = 1
        for i in pList:
            p *= i
        for i in qList:
            q *= i
        self.p = p
        self.q = q
        pass
