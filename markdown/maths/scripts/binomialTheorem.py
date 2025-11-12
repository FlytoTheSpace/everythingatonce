from calculusFunctions import Product, ProductList
import numberTheory
import sys
from fraction import Fraction

sys.path.append("../../../modules/py")
import general

def coefficient(p: int, q: int, k: int)->tuple[int, int]:
    """
    n = p / q, n is the Power, k is the Column number
    """
    nominatorList: list = Product(0, k - 1, lambda x: p - (q*x), asList=True)
    dominatorList: list = numberTheory.factorial(k, True)
    
    QtotheK: list = numberTheory.power(q, k, asList=True)

    for i in QtotheK:
        dominatorList.append(i)
    
    general.removeCommon(nominatorList, dominatorList)

    frac: Fraction = Fraction(ProductList(nominatorList), ProductList(dominatorList))
    frac.coprimeRatio()
    return frac

def coefficientLinear(n: Fraction, limit: int = 10)->list[tuple[int, int]]:

    n.coprimeRatio()
    p = n.p
    q = n.q

    coefficents: list[tuple[int, int]] = []

    if (p > 0) and (q == 1): limit = p + 1

    for k in range(limit):
        nominator = Product(0, k - 1, lambda s: p - (q*s))
        denominator = numberTheory.factorial(k, False)*numberTheory.power(q, k, False)

        frac = Fraction(nominator, denominator)
        frac.coprimeRatio()
        coefficents.append(frac.get_symbolic())

    return coefficents


# The Standard Binomial Theorem
def standard(n: int):
    coefficients: list[tuple[int, int]] = coefficientLinear(Fraction(n, 1))

    if (n == 0): raise ValueError(f"Binomial Theorem: n is raised to {n} power")

    def function(a: float, b: float):
        result = 0
        for k in range(len(coefficients)):
            result += coefficients[k][0]*numberTheory.power(a, k)*numberTheory.power(b, n-k)/coefficients[k][1]
        return result
    
    return function

def fractional(n: Fraction, limit: int = 10):
    
    if (n.q == 0): raise ValueError(f"Binomial Theorem: n is raised to {n.p}/{n.q} power")

    coefficients: list[tuple[int, int]] = coefficientLinear(Fraction(n.p, n.q), limit)

    def function(x: float):
        if (abs(x) >= 1): print("\x1b[93m[Warning] Series will Diverge\x1b[0m")
        result = 0
        for k in range(len(coefficients)):
            result += coefficients[k][0]*numberTheory.power(x, k)/coefficients[k][1]
        return result
    
    return function
