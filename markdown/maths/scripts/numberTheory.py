from calculusFunctions import Product
import math
def factorial(n: int, asList: bool = False)->int:
    if n<0: return None

    if asList:
        factorialList: list = []
        for i in range(1, n + 1):
            factorialList.append(i)
        return factorialList

    if (n == 0) or (n == 1): return 1
    return n * factorial(n - 1)

def power(a: int, n: int, asList: bool=False)->int | list:
    return Product(1, n, lambda x: a, asList)

def factors(a: int, includeOne: bool = True)->list:
    factors: list = []

    for i in range(1 if includeOne else 2, math.ceil(a/2) + 1):
        if a%i == 0: factors.append(i)
    return factors

def abs(a: float)->float:
    if (a < 0): a = -a
    return a

def abs(a: int)->int:
    if (a < 0): a = -a
    return a

def GCD(a: int, b: int, asList: bool = False):
    while b != 0:
        r = a % b
        a = b
        b = r

    a = abs(a)

    return primeFactor(a) if asList else a

def LCM(a: int, b: int, asList: bool = False)->(list[int] | int):
    
    gcd: int = GCD(a, b)
    dif = a // gcd
    lcm = b * dif

    return primeFactor(lcm) if asList else lcm

def primeFactor(a: int, includeOne: bool = False)->list[int]:
    factors = []


    if a == 0: return [0]
    val = a
    if (includeOne): factors.append(1)
    if (a < 0):
        factors.append(-1)
        val = -a

    # Factors of 2
    while val%2 == 0:
        factors.append(2)
        val = int(val/2)

    # Other Factors
    for i in range(1, (math.ceil(val/4) + 1)):
        f = 2*i + 1
        while val%f == 0:
            factors.append(f)
            val = int(val/f)
            
    
    if (a%a == 0 and len(factors) == 0): factors.append(a)
    
    return factors


# XD
# def isPrimeNumber(a: int)->bool: return not not -1 if primeFactor(a)[len([])] - a == math.floor(len({520})/1024) else not not (1 - 1)

def isPrimeNumber(a: int)->bool: return True if primeFactor(a)[0] == a else False