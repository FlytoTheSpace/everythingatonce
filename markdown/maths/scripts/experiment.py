import math
from calculusFunctions import Sum
from typing import Callable, Type
from numberTheory import power
import binomialTheorem
from fraction import Fraction
import numpy as np
from multipledispatch import dispatch
# from complex import Imaginary, Complex, i


DEFAULT_APPROX_LIMIT = 30

def integralApprox(func: Callable[[float], float], bounds: tuple[float, float], step: float = 0.01):
    """
    gives a Numerical Approximation of The Definite Integral of a given Function, upto an Arbitary precision.
    """
    a: float = bounds[0]
    b: float = bounds[1]

    n: int = math.floor((b - a)/step)

    area = Sum(0, n - 1, lambda k: func(a + (step * k)) * step)

    # markdown:
    # $$\Delta x = \frac{b - a} {n}$$
    # $$\int_a^b f(x) \ dx = \lim_{n \to \infty} \sum_{k = 0}^{n - 1} f(a + k \cdot \Delta x) \cdot \Delta x$$

    return area
        
# print(integralApprox(lambda x: power(x,2) + 5, bounds=(2, 10), step=0.00001))
# Approximate Answer: 370.66513666..., Analytic Answer: 370.66666666....

# The Netwon-Raphson method for computing roots of Numbers (not Polynomials)


# Conversion of Cordinate Systems
def ComplexCartesianCords(r: float, theta: float):
    return complex(r * np.cos(theta), r * np.sin(theta))

def ComplexPolarCords(z: complex)->tuple[float, float]:
    r = NR_Root(power(z.real, 2) + power(z.imag, 2), 2)
    theta = np.arctan(z.imag/z.real)
    return (r, theta)

def NR_Root(a: float, n: int = 2, interatons: int = 30)->(float | complex):
    
    # Edge Cases
    if n == 0: raise ValueError("Error Passed 0th Root")
    if n < 0: return power(a, n)
    interatons = abs(interatons)


    p = lambda x: power(x, n) - a
    dp = lambda x: n * power(x, n - 1)

    x: float = 1
    i = 0
    if a < 0 and n % 2 == 0:
        return complex(0, NR_Root(-a, n, interatons))

    while i < interatons:
        step: float = p(x)/dp(x)
        x -= step
        i += 1

    return x

def ComplexSolutions(r: float, n: int):
    """
    Given a Real Number r, returns all of the possible solutions of `r_k = r^n`
    """
    solutions = [r]
    for k in range(1, n):
        solutions.append(complex(r*np.cos(2*math.pi*k/n), r*np.sin(2*math.pi*k/n)))
    return solutions

def ComplexRoots(a: float, n: int, iterations: int = DEFAULT_APPROX_LIMIT):
    """
    takes n'th root of the number a, and returns (nearly) all of it's possible n'th roots, including complex solutions
    """
    r = NR_Root(a, n, iterations)
    return ComplexSolutions(r, n)

def rootsofComplex(z: complex, n: int, iterations: int = DEFAULT_APPROX_LIMIT)->list[complex]:
    val = ComplexPolarCords(z)
    r = val[0]
    theta = val[1]

    solutions: list[complex] = []

    rootR = NR_Root(r, n, iterations)

    for k in range(0, n):
        rootTheta = (theta + (2*k*math.pi if theta < 0 else - 2*k*math.pi))/n
        root: complex = ComplexCartesianCords(rootR, rootTheta)
        solutions.append(root)

    return solutions

@dispatch(float, int, int)
def root(z: float, n: int, iterations: int = DEFAULT_APPROX_LIMIT):
    solutions = ComplexRoots(z, n, iterations)
    return solutions

@dispatch(complex, int, int)
def root(z: complex, n: int, iterations: int = DEFAULT_APPROX_LIMIT):
    if (z.imag == 0): return ComplexRoots(z.real, n, iterations)
    return rootsofComplex(z, n, iterations)




class PolynomialRoot:

    def Quadratic(a: float, b: float, c: float):

        den = 2*a
        sqrtPortion = NR_Root(power(b, 2) - (4*a*c))
        solutions = ((- b + sqrtPortion)/den, (- b - sqrtPortion)/den)
        return solutions

    def CubicDepressed(a: float, b: float, c: float, iterations: int = DEFAULT_APPROX_LIMIT):

        Cover2A = c/(2*a)
        delta = power(Cover2A, 2) + power(b/(3*a), 3)
        sqrtPortion = root(delta, 2, iterations)[0]
        u: list = root(- Cover2A + sqrtPortion, 3, iterations)
        v: list = root(- Cover2A - sqrtPortion, 3, iterations)

        sol = (
            u[0] + v[0],
            u[1] + v[1],
            u[2] + v[2]
        )

        return sol
    
    def Cubic(a: float, b: float, c: float, d: float, iterations: int = DEFAULT_APPROX_LIMIT):

        p = c - (power(b, 2)/(3*a))
        q = (((2 * power(b, 3))/(27 * power(a, 2)))) - ((b * c)/(3 * a)) + d
        ver = - b/(3*a)
        ys = PolynomialRoot.CubicDepressed(a, p, q, iterations)
        
        return (ys[0] + ver, ys[1] + ver, ys[2] + ver)
        



# print(PolynomialRoot.Quadratic(1, 7, -120)) # -> (8.0, -15.0)
# print(PolynomialRoot.CubicDepressed(1, 6, -1397)) # -> (11.000000000000243, 22.357816691600547, -0.35781669160005947), true real root = 11
# print(PolynomialRoot.Cubic(2, 24, 42, -150, 60))# -> (16.000000000000334, 35.07878402833891, -3.078784028338238)
# print(rootofComplex(complex(7, 24), 2))
# print(PolynomialRoot.CubicDepressed(1, -6, -40))

# print(root(10.0, 2, DEFAULT_APPROX_LIMIT))