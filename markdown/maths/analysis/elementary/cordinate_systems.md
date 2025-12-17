
- [Back to Maths](./../maths.md)
- [Back to Home](../../../README.md)

# Cartesian Cordinate System

## 2d

The Cartesian Plane is as follows:

$$
\vec{v} = <x, y>
$$
point:
$$
P = (x, y)
$$

with $x, y$ as parameters

$x$ is called **abscissa**
$y$ is called **ordinate**

- Magnitude:

$$|\vec{v}| = \sqrt{x^2 + y^2}$$

**Quadrants**:

- **I**:   $(+, +)$
- **II**:  $(-, +)$
- **III**: $(+, -)$
- **IV**:  $(-, -)$

## N-dimensional

The Cartesian Cordinate system for any **N** dimensions:

$$\vec{v} = <x, y, z, w, ...>$$

with $x, y, z, w, ...$ as parameters

- Magnitude:

$$|\vec{v}| = \sqrt{x^2 + y^2 + z^2 + w^2 + ...}$$

# Polar Cordinate System

## 2d

$$
\vec{v} = <r \cos(\theta), r \sin(\theta)>
$$

with $r, \theta$ as parameters.

## 3d Polar cords

$$\vec{v} = \begin{bmatrix}
r \cos(\theta) \cos (\phi) \newline
r \sin(\theta) \cos (\phi) \newline
r \sin (\phi) \newline
\end{bmatrix}
$$

with $r, \theta, \phi$ as parameters

### Derivation:
$$
x^2 + y^2 + z^2 = r^2
$$

$$
\tan(\theta) = \frac{y}{x} \newline
\theta = \arctan\left(\frac{y}{x}\right)
$$

$$
x^2 + y^2 = \rho^2 \newline
(\rho \cos(\theta))^2 + (\rho \sin(\theta))^2 = \rho^2 \newline
$$

$$
x^2 + y^2 + z^2 = r^2 \newline
\rho^2 + z^2 = r^2 \newline
$$

$$
\tan(\phi) = \frac{z}{\rho} \newline
\phi = \arctan\left(\frac{z}{\rho}\right) \newline
$$

$$
(r \cos(\phi))^2 + (r \sin(\phi))^2 = r^2 \newline
\rho = r \cos(\phi) \newline
(\rho \cos(\theta))^2 + (\rho \sin(\theta))^2 + (r \sin(\phi))^2 = r^2 \newline
(r \cos(\phi) \cos(\theta))^2 + (r \cos(\phi) \sin(\theta))^2 + (r \sin(\phi))^2 = r^2 \newline
$$

$$
x = r \cos(\theta) \cos (\phi) \newline
y = r \sin(\theta) \cos (\phi) \newline
z = r \sin (\phi) \newline
$$

## 4D Polar Cords

$$\vec{v} = 
\begin{bmatrix}
r \cos(\theta) \cos(\phi) \cos(\alpha) \newline
r \sin(\theta) \cos(\phi) \cos(\alpha) \newline
r \sin(\phi) \cos(\alpha) \newline
r \sin(\alpha) \newline
\end{bmatrix}$$

with $r, \theta, \phi, \alpha$ as paramters.

### Derivation:
$$
x^2 + y^2 + z^2 + w^2 = r^2 \newline
x^2 + y^2 + z^2 = \rho^2 \newline
(\rho \cos(\theta) \cos(\phi))^2 + (\rho \sin(\theta) \cos(\phi))^2 + (\rho \sin(\phi))^2 = \rho^2 \newline
$$
$$
\alpha = \arctan\left(\frac{w}{\rho}\right)
$$

$$
(\rho \cos(\theta) \cos(\phi))^2 + (\rho \sin(\theta) \cos(\phi))^2 + (\rho \sin(\phi))^2 = \rho^2 \newline
r \cos(\alpha) = \rho \newline
(r \cos(\theta) \cos(\phi) \cos(\alpha))^2 + (r \sin(\theta) \cos(\phi) \cos(\alpha))^2 + (r \sin(\phi) \cos(\alpha))^2 = \rho^2 \newline
(r \cos(\theta) \cos(\phi) \cos(\alpha))^2 + (r \sin(\theta) \cos(\phi) \cos(\alpha))^2 + (r \sin(\phi) \cos(\alpha))^2 + (r \sin(\alpha))^2 = r^2 \newline
$$

$$
x = r \cos(\theta) \cos(\phi) \cos(\alpha) \newline
y = r \sin(\theta) \cos(\phi) \cos(\alpha) \newline
z = r \sin(\phi) \cos(\alpha) \newline
w = r \sin(\alpha) \newline
$$

## N-Dimensional Polar Cords

$$
\sum_{i = 1}^{N} x_{i}^2 = r^2 \newline
$$

Angles:

$$
\theta_k = \arctan\left(\frac{x_{k + 1}}{\sqrt{\displaystyle\sum_{i = 1}^{k} x_i }}\right)
$$

Each Component:

$$
f(i, k)
\begin{cases}
i < k + 1 : \cos(\theta_k) \cr
i = k + 1 : \sin(\theta_k) \cr
i > k + 1 : 1 \cr
\end{cases}
$$

$$
x_i = r \prod_{k = 1}^{N - 1} f(i, k)
$$
