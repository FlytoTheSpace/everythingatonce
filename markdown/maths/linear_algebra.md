
- [Back to Maths](./maths.md)
- [Back to Home](../../README.md)

# Linear Alegbra
**Linear Algebra**: a field of algebra about Cordinate Systems, Matrix's, and Vectors

# Cordinate System

A coordinate system specifies positions in space using numerical values relative to defined reference axes or points.

- **X**: The Plane of Length
- **Y**: The Plane of Width
- **Z**: The Plane of Depth

# Scalar

A Number that scales a Vector
$$
\color{MediumSeaGreen}a\color{white}\mathbf{\vec{v}}
$$
$$
\begin{bmatrix}\color{MediumSeaGreen}x\cr \color{MediumSeaGreen}y \end{bmatrix} = 
\color{MediumSeaGreen}x\color{white}\hat{i} + \color{MediumSeaGreen}y\color{white}\hat{j}
$$

> Assuming, $\hat{i}$ and $\hat{j}$ are both in their original cords, $\hat{i} = \begin{bmatrix}1 \cr 0 \end{bmatrix}$ and $\hat{j} = \begin{bmatrix}0 \cr 1 \end{bmatrix}$

# Vectors

**Vectors**: Arrow that point to a specific point in space

Representation:
$$
\vec{v}, \mathbf{\vec{v}}, \overline{v}, \begin{bmatrix}x\cr y \end{bmatrix}
$$

> $x\in \R$

> $y\in \R$

Properties:
- **Length**
$$
| v | = \sqrt{ x^2 + y^2}
$$
$$
| v | = \sqrt{ x^2 + y^2 + z^2}
$$
- **Pointed Space**
$$
\mathbf{\vec{v}} = \begin{bmatrix} x \cr y \end{bmatrix}
$$

**Vector Addition**:
$$
\begin{bmatrix} x_1 \cr y_1 \end{bmatrix} + \begin{bmatrix} x_2 \cr y_2 \end{bmatrix} 
= \begin{bmatrix} x_1 + x_2 \cr y_1 + y_2 \end{bmatrix}
$$

Span
---

**Linear Combination**: sum of 2 scaled vectors

$$a \color{LightCoral} \mathbf{\vec{v}} \color{white} + b \color{MediumSeaGreen} \mathbf{\vec{w}}$$

**Span**: the set of every Linear Combination of 2 Vectors

Cases:

- No Constant
    - $\mathbf{\vec{v}} \propto \mathbf{\vec{w}}$: If both vectors are Propotional, then the Linear Combination will form a straight line passing through the Origin
    - $\mathbf{\vec{v}} = \mathbf{\vec{w}} = \begin{bmatrix} 0 \cr 0 \end{bmatrix} $: stuck at the origin
    - $\lnot(\mathbf{\vec{v}} \propto \mathbf{\vec{w}}) \land (\mathbf{\vec{v}} \neq 0 \land \mathbf{\vec{w}} \neq 0)$: If both vectors are not proptional, and not equal to 0, then every point in space can be reached
- 1 Constant. every possible point in space that the Linear Combination of the 2 Vectors can reach will form a straight line

**Linearly Dependent**: when a vector can be expressed as Linear Combination of 2 scaled vectors

$$\color{Tomato} \mathbf{\vec{u}} \color{white} = a \color{LightCoral} \mathbf{\vec{v}} \color{white} + b \color{MediumSeaGreen} \mathbf{\vec{w}}$$

**Linearly Independent**: when a vector can't be expressed as another scaled vector

$$\color{Tomato} \mathbf{\vec{u}} \color{white} \neq a \color{LightCoral} \mathbf{\vec{v}} \color{white}$$

## Unit Vectors

**Unit Vectors**: are vectors that defines the Units in a specific Plane of the Cordinate System

| Vector                          | Axis  | Initial Position                                                    |
| ------------------------------- | ----- | ------------------------------------------------------------------- |
| $\color{MediumSeaGreen}\hat{i}$ | **X** | $\begin{bmatrix} \color{MediumSeaGreen}1 \cr 0 \cr 0 \end{bmatrix}$ |
| $\color{Orange}\hat{j}$         | **Y** | $\begin{bmatrix} 0 \cr \color{Orange}1 \cr 0 \end{bmatrix}$         |
| $\color{DodgerBlue}\hat{k}$     | **Z** | $\begin{bmatrix} 0 \cr 0 \cr \color{DodgerBlue}1 \end{bmatrix}$     |

**Basis Vectors**: The Unit Vectors that defines the Planes of the Cordinate System (e.g. $
\hat{i}$, $\hat{j}$)

# Matrix

# Tensor
