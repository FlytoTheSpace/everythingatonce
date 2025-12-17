# Integral

An Integral is any function that gives the area under a graph of `f(x)` under some interval (a to b), the only requirement is ***Continuity***

$$
A_a^b = \int_{a}^{b} f(x) \ {dx}
$$

## Fundamental Theorem of Calculus

The **Fundamental Theorem of Calculus** implies that

$$
\int{\frac{df}{dx} \ dx} = f(x)
$$

it states that the integral and the deriavatives are opposites of each-other
and in the 2nd part it implies that:

$$
\int_{a}^{b}{f(x)\ dx} = F(b) - F(a)
$$

where 

$$
\frac{dF}{dx} = f(x)
$$

## Integral Properties/Methods:

### Special Cases:

**Constant**:

$$\int 0\ dx = C$$

where $C$ is any *Arbitary* Constant.

**Power-Rule**:

$$\int x^n\ dx = \frac{x^{n + 1}}{n + 1}$$

**Exponential Rule**:

$$\int a^x\ dx = \frac{a^x}{\ln(a)}$$

**Trignometric**:

$$\int \sin(x)\ dx = - \cos(x)$$

$$\int \cos(x)\ dx = \sin(x)$$

### General:

$$\int c \cdot f(x) \ dx = c \int f(x)\ dx$$

$$\int_{a}^{b} f(y) \ dy = \int_{g^{-1}(a)}^{g^{-1}(b)} f(g(x)) \cdot f'(x) \ dx $$

**Sum Rule**:

$$ \int f(x) + g(x)\ dx = \int f(x) \ dx + \int g(x) \ dx $$

**Change in Variable of Integration**:

$$ \int \displaystyle \sum_{i = 1}^mf_i(x) \ dx = \displaystyle \sum_{i = 1}^m\int f_i(x) \ dx$$

**Integration by Parts**:

$$ \int f \cdot g \ dx = f \cdot \int g \ dx - \int f' \cdot \int g \ dx \ dx$$

**Arc Length**:

$$
s = \int_{a}^{b} \sqrt{1 + f'(x)^2} \ dx
$$

### Trignometric Substitution

$$I = \int \sqrt{a^2 - x^2} \ dx$$

proceed:

$$
x = a \cdot \sin(\theta) \newline
\theta = \arcsin\left(\frac{x}{a}\right) \newline
\frac{dx}{d\theta} = a \cdot \cos(\theta) \newline
dx = a \cdot \cos(\theta) \ d\theta \newline
$$

$$
I = \int \sqrt{a^2 - x^2} dx \newline
I = \int \sqrt{a^2 - (a \cdot \sin(\theta))^2} \ a \cdot \cos(\theta) \ d\theta \newline
I = \int \sqrt{a^2 - a^2 \cdot \sin(\theta)^2} \ a \cdot \cos(\theta) \ d\theta \newline
I = \int a \sqrt{1 - \cdot \sin(\theta)^2} \ a \cdot \cos(\theta) \ d\theta \newline
I = \int a \sqrt{1 - \sin(\theta)^2} \ a \cdot \cos(\theta) \ d\theta \newline
$$

> Pythagorean Identity:
> 
> $\cos(\theta) = \sqrt{1 - \sin(\theta)^2}$

$$
I = \int a \sqrt{1 - \sin(\theta)^2} \ a \cdot \cos(\theta) \ d\theta \newline
I = \int a \cos(\theta) \ a \cdot \cos(\theta) \ d\theta \newline
I = \int a^2 \cos(\theta)^2 \ d\theta \newline
I = a^2 \int \cos(\theta)^2 \ d\theta \newline
$$

> Cosine Square Identity:
> 
> $$\cos(\theta)^2 = \frac{1 + \cos(2\theta)}{2}$$

$$
I = a^2 \int \cos(\theta)^2 \ d\theta \newline
I = a^2 \int \frac{1 + \cos(2\theta)}{2} \ d\theta \newline
I = \frac{1}{2}a^2 \left( \int 1 \ d\theta + \int \cos(2\theta) \ d\theta \right)\newline
I = \frac{1}{2}a^2 \left( \theta + \int \cos(2\theta) \ d\theta \right)\newline
$$

> u subtitution:
> $$u = 2\theta$$
$$\frac{du}{d\theta} = 2$$
$$d\theta = \frac{du}{2}$$

$$
I = \frac{1}{2}a^2 \left( \theta + \int \cos(2\theta) \ d\theta \right)\newline
I = \frac{1}{2}a^2 \left( \theta + \int \cos(u) \ \frac{du}{2} \right)\newline
I = \frac{1}{2}a^2 \left( \theta + \frac{1}{2} \int \cos(u) \ du \right)\newline
I = \frac{1}{2}a^2 \left( \theta + \sin(u) \right)\newline
I = \frac{1}{2}a^2 \left( \theta + \sin(2\theta) \right)\newline
I = \frac{1}{2}a^2 \left( \arcsin\left(\frac{x}{a}\right) + \sin(2 \cdot \arcsin\left(\frac{x}{a}\right)) \right)\newline
$$
final solution:
$$
\int \sqrt{a^2 - x^2} \ dx = \frac{a^2\cdot \arcsin(x/a) + a^2 \cdot \sin(2 \cdot \arcsin(x/a))}{2} + C
$$

$$I = \int \sqrt{a^2 + x^2} \ dx$$

$$x = a \cdot \tan(\theta)$$

$$\theta = \arctan\left(\frac{x}{a}\right)$$

$$\frac{dx}{d\theta} = \sec(x)^2$$

$$dx = a \cdot \sec(\theta)^2 \ d\theta$$

$$
I = \int \sqrt{a^2 + (a \cdot \tan(\theta))^2} \ (a \cdot \sec(\theta)^2 \ d\theta) \newline
I = \int \sqrt{a^2 + a^2 \cdot \tan(\theta)^2} \ a \cdot \sec(\theta)^2 \ d\theta \newline
I = \int a\sqrt{1 + \tan(\theta)^2} \ a \cdot \sec(\theta)^2 \ d\theta \newline
$$

> Pythagorean Identity:
> 
> $$\sec(\theta) = \sqrt{1 + \tan(\theta)^2}$$

$$
I = \int a\sec(\theta) a \cdot \sec(\theta)^2 \ d\theta \newline
I = a^2 \int \sec(\theta)^3 \ d\theta \newline
$$

(pending...)

# Path Integral

The Integral along some path $C$ is:

$$
\int_{C} f(x, y, z,...) \ dr = \int_{a}^{b} f(C_x(t), C_y(t), C_z(t), ...) \cdot C_r'(t) \ dt
$$

$r$ is some paramter of the function $f(x, y, z, ..., r,...)$

$$
C(t) =
\begin{bmatrix}
C_x(t) \cr
C_y(t) \cr
C_z(t) \cr
...
\end{bmatrix}
$$

$$C: [a, b] \to \mathbb{R}^{n}$$

in case of $ds$ which represents the step in the direction of $C(t)$

$ds = \sqrt{dx^2 + dy^2 + dz^2 + ...}$
$$
\int_{C} f(x, y, z,...) \ ds = \int_{a}^{b} f(C_x(t), C_y(t), C_z(t), ...) \cdot \sqrt{C_x'(t)^2 + C_y'(t)^2 + C_z'(t)^2 + ... } \ dt
$$

# Complex Integration