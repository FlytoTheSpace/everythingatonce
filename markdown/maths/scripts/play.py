
import binomialTheorem
import experiment
from fraction import Fraction

a = 1
b = -2
c = 1
d = 0

# print(f"{a}x^3 + {b}x^2 + {c}x + {d} = 0")
# print(experiment.PolynomialRoot.Cubic(a, b, c, d))

print(f"{a}x^4 + {b}x^2 + {c}x + {d}")
print(experiment.PolynomialRoot.QuarticDepressed(a, b, c, d))