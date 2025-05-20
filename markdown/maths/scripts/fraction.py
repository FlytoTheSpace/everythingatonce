

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
        Makes the Fraction a reciprocal version of itself
        """

        a = self.p
        self.p = self.q
        self.q = a

    def __mul__(self, y: int):
        self.p *= y

    def coprimeRatio(self):
        pass
