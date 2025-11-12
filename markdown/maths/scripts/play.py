
import binomialTheorem
import experiment
import numberTheory
from fraction import Fraction

a = 1
b = -2
c = 1
d = 0

# print(f"{a}x^3 + {b}x^2 + {c}x + {d} = 0")
# print(experiment.PolynomialRoot.Cubic(a, b, c, d))

# print(f"{a}x^4 + {b}x^2 + {c}x + {d}")
# print(experiment.PolynomialRoot.QuarticDepressed(a, b, c, d))

limit = 10
for i in range(-10,10):
    n = Fraction(-1 - i, 1)
    print(n.p, binomialTheorem.coefficientLinear(n, limit=limit))

# print(binomialTheorem.coefficientLinear(Fraction(-1 , 1)))

# print(numberTheory.primeFactor(-5))
# for i in range(1, 101):
    # print(i, numberTheory.primeFactor(i))