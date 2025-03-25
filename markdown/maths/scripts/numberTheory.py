from calculusFunctions import Product

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