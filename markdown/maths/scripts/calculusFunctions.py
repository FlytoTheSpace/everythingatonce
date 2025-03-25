import math
from typing import Callable, List

def Sum(k: int, n: int, func: Callable[[int], int], asList: bool)->int | list:
    if asList:
        sumlist: list = []
        for i in range(k, math.floor(n) + 1):
            sumlist.append(func(i))
        return sumlist

    sum: int = 0
    for i in range(k, math.floor(n) + 1):
        sum += func(i)
    return sum

def Product(k: int, n: int, func: Callable[[int], int], asList: bool)->int | list:
    if asList:
        productlist: list = []
        for i in range(k, math.floor(n) + 1):
            productlist.append(func(i))
        return productlist
    
    product: int = 1
    for i in range(k, math.floor(n) + 1):
        product *= func(i)
    return product

def SumList(List: List[int])->int:
    sum: int = 0
    for i in List:
        sum += i
    return sum

def ProductList(List: List[int])->int:
    product: int = 1
    for i in List:
        product *= i
    return product