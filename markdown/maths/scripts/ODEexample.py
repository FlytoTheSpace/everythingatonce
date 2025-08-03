import sys

sys.path.append("../../../modules/py")
import numpy as np
import math

# Physical Constants
mu = 0.1
g = 9.8
L = 5

# Position, Angular Velocity
theta0 = math.pi/2
thetaDot0 = 3

# Measurement
t = 60
delta_t = 0.01 # An Arbitary number, closer to 0 for better approximation

x = [theta0]
y = [thetaDot0]

theta = theta0
thetaDot = thetaDot0

# Computation:
def thetaDoubleDotFunc(theta, thetaDot):
    return - (mu * thetaDot) - (g/L * np.sin(theta))

limit = math.ceil(t/delta_t)
for i in range(limit):
    
    thetaDoubleDot = thetaDoubleDotFunc(x[i], y[i])
    thetaDot += thetaDoubleDot * delta_t
    theta += thetaDot * delta_t

    x.append(theta)
    y.append(thetaDot)

import plotly_setup

plotly_setup.graph(x=x,y=y)
plotly_setup.show()