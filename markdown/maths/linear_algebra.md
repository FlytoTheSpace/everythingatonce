
- [Back to Maths](./maths.md)
- [Back to Home](../../README.md)

# Linear Alegbra
**Linear Algebra**: a field of algebra about Cordinate Systems, Matrix's, and Vectors

# Axioms

The Axioms for the Vector Space are:

## Vectors Axioms

$\forall \vec{\mathbf{v}}, \vec{\mathbf{u}}, \vec{\mathbf{w}} \in V$

**Closure**: Addition of any 2 Vectors will result in a vector within the vector space
$$\vec{\mathbf{v}} + \vec{\mathbf{u}} \in V$$

**Associativity**: usage of 
$$(\vec{\mathbf{u}} + \vec{\mathbf{v}}) + \vec{\mathbf{w}} = \vec{\mathbf{v}} + (\vec{\mathbf{u}} + \vec{\mathbf{w}})$$

**Identity/Neutral**:
$$\exists \vec{\mathbf{0}} \in V(\vec{\mathbf{v}} + \vec{\mathbf{0}} = \vec{\mathbf{0}} + \vec{\mathbf{v}} = \vec{\mathbf{v}})$$
**Inverse**:

$$\exists(-\vec{\mathbf{v}}) \in V(\vec{\mathbf{v}} + (-\vec{\mathbf{v}}) = \vec{\mathbf{0}})$$

**Communicativity/Abelian**:

$$\vec{\mathbf{v}} + \vec{\mathbf{u}} = \vec{\mathbf{u}} + \vec{\mathbf{v}}$$

## Scalars Axioms:

$\forall \vec{\mathbf{v}}, \vec{\mathbf{u}} \in V$

$\forall a, b \in \mathbb{R}$

**Closure**:

$$a \vec{\mathbf{v}} \in V$$

**Associativity**:

$$(ab)\vec{\mathbf{v}} = a(b\vec{\mathbf{v}})$$

**Identity/Neutral**:

$$\exists 1 \in \mathbb{R}(1 \vec{\mathbf{v}} = \vec{\mathbf{v}} 1 = \vec{\mathbf{v}})$$

**Inverse**:

$$\exists\left(\frac{1}{a}\right) \in \mathbb{R} \left(\left(\frac{1}{a}\right) a \vec{\mathbf{v}} = \vec{\mathbf{v}}\right)$$

**Communicativity/Abelian**:

$$
a\vec{\mathbf{v}} = \vec{\mathbf{v}} a
$$

**Distributive Property**:

$$a(\vec{\mathbf{v}} + \vec{\mathbf{u}}) = a\vec{\mathbf{v}} + a\vec{\mathbf{u}}$$

**Distributive Property 2**:

$$(a + b)\vec{\mathbf{v}} = a\vec{\mathbf{v}} + b\vec{\mathbf{v}}$$

# Cordinate System

A coordinate system specifies positions in space using numerical values relative to the Origin $O$

## Cartesian Cordinate System

- **X**: The Axis of Length
- **Y**: The Axis of Width
- **Z**: The Axis of Depth

each axis is **perpendicular** to every other axis.

any point in the Cartesian Cordinate System is located by the **cordinate** of that point, each components of the cordinate corresponding to it's respective axis.

$$P = (x, y, z, ...)$$

# Scalar

A Real Number that combines with vectors

# Vectors

**Vectors**: in are vert nicely represented as a list of ordered numbers in the Cartesian Plane, where each number can be specified as a component of the cordinate.

$$
\vec{v}
= \begin{bmatrix}
v_x \cr
v_y \cr
v_z \cr
...
\end{bmatrix}

= \begin{pmatrix}
v_x \cr
v_y \cr
v_z \cr
...
\end{pmatrix} 
= < v_x, v_y, v_z, ... >
$$

all the notations above represent the same concept.

> while using the Cartesian Cordinate system's approach for vectors turns out to be very useful when dealing with vectors and matrices it should be noted that it's not the only way to represent them similar to how we use the Base 10 system for numbers but it's not the only way to represent them just that it proves useful at times for defining operations with them, so for convience purposes we'll continue to use them throughout this.

the number of entries in a vector can be denoted in the subscript.

$$
\vec{v}_n
= \begin{bmatrix}
v_1 \cr
v_2 \cr
v_3 \cr
... \cr
v_n \cr
\end{bmatrix}
$$

another way of communicating this fact is using: $\mathbb{R}^{n}$

$$\mathbb{R}^n = \left\{ \begin{bmatrix}
r_1 \cr
r_2 \cr
r_3 \cr
... \cr
r_n \cr
\end{bmatrix} \middle | \ \forall r_i \in \mathbb{R} \right\}$$

$$\vec{v} \in \mathbb{R}^n$$

**Length**: is defined as the magnitude of the Vector, a single scalar is the output
$$
|\vec{v}| = \sqrt{v_x^2 + v_y^2 + v_z^2 + ...}
$$

**Vector Addition**: 

$$
\begin{bmatrix} v_x \cr v_y \cr v_z \cr ... \end{bmatrix} + 
\begin{bmatrix} \vec{u}_x \cr \vec{u}_y \cr \vec{u}_z \cr ... \end{bmatrix} 
= \begin{bmatrix} v_x + \vec{u}_x \cr v_y + u_y \cr v_z + u_z \cr ... \end{bmatrix}
$$

**Scalar Multiplication**: 

$$
a \vec{v} = \begin{bmatrix}
a v_x \cr
a v_y \cr
a v_z \cr
...
\end{bmatrix}
$$


## Unit Vectors

**Unit/Basis Vectors**: are vectors that defines the Units in a specific axis of the Cordinate System, these are a consequence of the Cartesian Cordinate System representation of Vector.

| Vector    | Axis  | Position                                              |
| --------- | ----- | ----------------------------------------------------- |
| $\hat{i}$ | $x$   | $\begin{bmatrix} 1 \cr 0 \cr 0 \cr ... \end{bmatrix}$ |
| $\hat{j}$ | $y$   | $\begin{bmatrix} 0 \cr 1 \cr 0 \cr ... \end{bmatrix}$ |
| $\hat{k}$ | $z$   | $\begin{bmatrix} 0 \cr 0 \cr 1 \cr ... \end{bmatrix}$ |

$$
\vec{v} = \begin{bmatrix} v_x \cr v_y \cr v_z \cr ... \end{bmatrix} = v_x\hat{i} + v_y\hat{j} + v_z\hat{k} + ...
$$

## Span

**Linear Combination**: sum of 2 scaled vectors

$$\forall{v, w}$$

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

## Dot Product

A Dot product between 2 vectors is defined as:

$$$$

# Matrix

a matrix is a list of **vectors**, which can be represented as follows:

$$
M = \begin{bmatrix}
M_{1,1} & M_{1,2} & M_{1,3} & M_{1,4} & ... & M_{1,j} \cr
M_{2,1} & M_{2,2} & M_{2,3} & M_{2,4} & ... & M_{2,j} \cr
M_{3,1} & M_{3,2} & M_{3,3} & M_{3,4} & ... & M_{3,j} \cr
M_{4,1} & M_{4,2} & M_{4,3} & M_{4,4} & ... & M_{4,j} \cr
...     & ...     & ...     & ...     & ... & ...     \cr
M_{i,1} & M_{i,2} & M_{i,3} & M_{i,4} & ... & M_{i,j} \cr
\end{bmatrix}
$$

Set of Matrices:

$$
\mathbb{R}^{n \times m} = 
\left\{
\begin{bmatrix}
A_{1,1} & A_{1,2} & A_{1,3} & ... & A_{1,m} \cr
A_{2,1} & A_{2,2} & A_{2,3} & ... & A_{2,m} \cr
A_{3,1} & A_{3,2} & A_{3,3} & ... & A_{3,m} \cr
...     & ...     & ...     & ... & ...     \cr
A_{n,1} & A_{n,2} & A_{n,3} & ... & A_{n,m} \cr
\end{bmatrix}
\middle | \forall A_{ij} \in \mathbb{R}
\right\}
$$

## Linear Transformation

A Linear Transformations is defined as:

$$L: R^n \to R^n$$
$$L(\vec{v} + \vec{u}) = L(\vec{v}) + L(\vec{u})$$
$$L(c \ \vec{v}) = c\ L(\vec{v})$$

applying:

$$
L(\vec{v}) = L(v_x\hat{i} + v_y\hat{j} + v_z\hat{k} + ...) \newline
L(\vec{v}) = v_x \ L(\hat{i}) + v_y \ L(\hat{j}) + v_z \ L(\hat{k}) + ...\newline
L(\vec{v}) = v_x \ L\left(\begin{bmatrix} 1 \cr 0 \cr 0 \cr ... \end{bmatrix}\right) + v_y \ L\left(\begin{bmatrix} 0 \cr 1 \cr 0 \cr ... \end{bmatrix}\right) + v_z \ L\left(\begin{bmatrix} 0 \cr 0 \cr 1 \cr ... \end{bmatrix}\right) + ...\newline
L(\vec{v}) = v_x \begin{bmatrix} A_{1,1} \cr A_{2,1} \cr A_{3,1} \cr ... \end{bmatrix} + v_y \begin{bmatrix} A_{1,2} \cr A_{2,2} \cr A_{3,2} \cr ... \end{bmatrix} + v_z \begin{bmatrix} A_{1,3} \cr A_{2,3} \cr A_{3,3} \cr ... \end{bmatrix} + ...\newline
$$
now the Linear Transformation is solely determined by the Linear Transformation of the Unit Vectors of the cordinate system, all the information required to do that Linear Transformation can be packaged into a $m \times n$ matrix, and the Whole Transformation can be defined as a kind of "product" between a Matrix and a Vector.

$$L(\vec{v}) = \begin{bmatrix} 
A_{1,1} & A_{1,2} & A_{1,3} & ... & & A_{1,n} \cr
A_{2,1} & A_{2,2} & A_{2,3} & ... & & A_{2,n} \cr
A_{3,1} & A_{3,2} & A_{3,3} & ... & & A_{3,n} \cr
...     & ...     & ...     & ... & & ...     \cr
A_{m,1} & A_{m,2} & A_{m,3} & ... & & A_{m,n} \cr
\end{bmatrix} \begin{bmatrix} v_x \cr v_y \cr v_z \cr ... \cr v_n \end{bmatrix} $$

$$L(\vec{v}) = \vec{u}$$

$$\vec{u}_i = \sum_{k = 1}^{n} v_k A_{ik}$$

$\vec{v}, \vec{u} \in \mathbb{R}^{n}$

$A \in \mathbb{R}^{n \times m}$

similarly composition between Linear Transformations can be denoted as a single Linear Transformation via another kinda of "product" between Matrices

$$
AB = C
$$

$$
C_{ij} = \sum_{k = 1}^{n} A_{kj} B_{ik}
$$

# Tensor
