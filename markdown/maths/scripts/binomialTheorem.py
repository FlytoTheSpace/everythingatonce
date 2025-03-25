from calculusFunctions import Product, ProductList
from numberTheory import factorial, power
from general import removeCommon

def fractionCoefficient(p: int, q: int, k: int)->tuple[int, int]:
    """
    n = p / q, n is the Power, k is the Column number
    """
    nominatorList: list = Product(0, k - 1, lambda x: p - (q*x), asList=True)
    dominatorList: list = factorial(k, True)
    
    QtotheK: list = power(q, k, True)

    for i in QtotheK:
        dominatorList.append(i)

    # print(nominatorList, dominatorList)
    removeCommon(nominatorList, dominatorList)

    fraction: tuple[int, int] = (ProductList(nominatorList), ProductList(dominatorList))

    return fraction
