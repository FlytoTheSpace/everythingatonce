from calculusFunctions import Product
import math
import fraction
def factorial(n: int, asList: bool)->int:
    if n<0: return None

    if asList:
        factorialList: list = []
        for i in range(1, n + 1):
            factorialList.append(i)
        return factorialList

    if (n == 0) or (n == 1): return 1
    return n * factorial(n - 1)

def power(a: int, n: int, asList: bool)->int | list:
    return Product(1, n, lambda x: a, asList)

def factors(a: int, includeOne: bool = True)->list:
    factors: list = []

    for i in range(1 if includeOne else 2, math.ceil(a/2) + 1):
        if a%i == 0: factors.append(i)
    return factors

def primeFactor(a: int)->list:
    factors = []
    val = a

    if a == 0: return 0

    # Factors of 2
    while val%2 == 0:
        factors.append(2)
        val = int(val/2)

    # Other Factors
    for i in range(1, (math.ceil(val/4))):
        f = 2*i + 1
        # print(i, f)
        while val%f == 0:
            factors.append(f)
            val = int(val/f)
            
    
    if (a%a == 0 and len(factors) == 0): factors.append(a)
    
    return factors


def isPrimeNumber(a: int)->bool:
    """
    use Prime Factorization to find out if the Input is a Prime Number
    """
    factors = primeFactor(a)
    return True if (factors[0] == a) else False