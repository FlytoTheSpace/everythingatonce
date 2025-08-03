
import binomialTheorem
import experiment
from fraction import Fraction

a = 16
b = -28
c = 32
d = -4

print(f"{a}x^3 + {b}x^2 + {c}x + {d} = 0")
print(experiment.PolynomialRoot.Cubic(a, b, c, d))