

# Deriavative

**Deriavatives** is the *Rate of change* of a function over a small amount of tweak in the input $\Delta x$

Formal Definition:

$$
\frac{dy}{dx} = \lim_{h \to 0} \frac{f(x + h) - f(x)}{h} = \lim_{(x_1 - x_0) \to 0} \frac{y_1 - y_0}{x_1 - x_0} 
$$

$
y = f(x) \newline
h = \Delta x = x_1 - x_0 \newline
\Delta y = f(x + \Delta x) - f(x) = y_1 - y_0
$

## Notation

The Deriavatives are usually written in their own notation, so they can be treated as an "Operation" that takes a function and returns another function.

### Newton's Notation

Function Symbols with `n` count of dots above to denote n'th deriavative
$$
\dot{f}
$$
$$
\ddot{f}
$$

### Langrange's Notation

The functions are suffixed with a quote `'`, and the `n` count of quotes suffixed represented `n`'th Deriavative

$$
f'(x)
$$
2nd Deriavative:
$$
f''(x)
$$


### Leibniz's Notation


$
dx = \Delta x \newline
df = f(x + dx) - f(x)
$

$$
\frac{dy}{dx} = \lim_{\Delta x \to 0} \frac{\Delta y}{\Delta x}
$$

`n`'th Deriavative:

$$
\frac{d^ny}{dx^n}
$$

### Differential Operator Notation
represents Deriavative as an Operation with respect to `x`

$$
D_x^n f(x)
$$

$n$ represents the n'th deriavative

## 1st Derivative


Rules:
---

### Special Cases:

**Constant:**
$$ \frac{d}{dx}(a) = 0 $$
**Power Rule:**
$n \neq 0$
$$ \frac{d}{dx}(x^n) = nx^{n-1} $$
**Exponential:**
$$ \frac{d}{dx}(a^x) = \ln(a)\cdot a^x $$
**Trignometric:**
$$ \frac{d}{dx}(\sin(x)) = \cos(x)$$
$$ \frac{d}{dx}(\cos(x)) = - \sin(x)$$

### General:

$$ \frac{d}{dx}(c \cdot f(x)) = c \cdot \frac{df}{dx}$$

**Sum Rule:**
$$ \frac{d}{dx}(f(x) + g(x)) = \frac{df}{dx} + \frac{dg}{dx} $$
$$ \frac{d}{dx}\left(\displaystyle \sum_{i = 1}^mf_i(x)\right) = \displaystyle \sum_{i = 1}^m\frac{d}{dx}f_i(x)$$

**Product Rule:**
$$ \frac{d}{dx}(f(x) \cdot g(x)) = f(x) \cdot g'(x) + f'(x) \cdot g(x) $$
$$ \frac{d}{dx}\left(\displaystyle \prod_{i = 1}^m f_i(x) \right) = \displaystyle \LARGE \sum_{\small k_1 + k_2 + ... = 1} \normalsize \left(\displaystyle \prod_{i = 1}^m \frac{d^{k_i}}{dx^{k_i}}(f_i(x)) \right) $$

**Chain Rule:**
$$ \frac{d}{dx}(f(g(x))) = \frac{df}{dg} \cdot \frac{dg}{dx} \newline $$
$$ \frac{d}{dx}(f_1 \circ f_2 \circ f_3 \circ ... f_m) = \left(\displaystyle \prod_{i = 1}^{m - 1} \frac{df_i}{df_{i +1}}\right) \frac{df_m}{dx} $$

## `n`'th Derivative
n'th Derivative are the Repeated Application of Deriavative on a given function n times

$$
\frac{d^n}{dx^n}f(x) = \underbrace{\frac{d}{dx}(\frac{d}{dx}(...\frac{d}{dx}(f(x))))}_{n \text{ times}}
$$

Rules:
---

### Special Cases:

**Power Rule:**
$n \leq m$

$$ \frac{d^n}{dx^n}(x^m) = \frac{m!}{(m - n)!} x^{m - n} $$

**Exponential:**

$$ \frac{d^n}{dx^n}(a^x) = \ln(a)^n \cdot a^x$$

**Trignometric:**

$$ \frac{d^{n}}{dx^{n}}(\sin(x)) =
\begin{cases}
n \mod 4 = 0: \sin(x) \cr
n \mod 4 = 1: \cos(x) \cr
n \mod 4 = 2: - \sin(x) \cr
n \mod 4 = 3: - \cos(x) \cr
\end{cases}$$

$$ \frac{d^{n}}{dx^{n}}(\cos(x)) =
\begin{cases}
n \mod 4 = 0: \cos(x) \cr
n \mod 4 = 1: - \sin(x) \cr
n \mod 4 = 2: - \cos(x) \cr
n \mod 4 = 3: \sin(x) \cr
\end{cases}$$

### General:

**Sum Rule**:
$$ \frac{d^n}{dx^n}(f + g) = \frac{d^nf}{dx^n} + \frac{d^ng}{dx^n} $$
$$ \frac{d^n}{dx^n}\left(\displaystyle \sum_{i = 1}^mf_i(x)\right) = \displaystyle \sum_{i = 1}^m\frac{d^n}{dx^n}\left(f_i(x)\right)$$

**Product Rule**:
$$ \frac{d^n}{dx^n}(f \cdot g) = \sum_{k = 0}^n \begin{pmatrix} n \cr k \end{pmatrix} \frac{d^{n - k}f}{dx^{n - k}} \cdot \frac{d^kg}{dx^k} $$

**n'th Deriavative of the product of m count of functions**:

> 
> Coefficient:
> $$ C(n,k_1, k_3, k_4, ...,, k_{m - 1}) = \prod_{i = 1}^{m - 1} \begin{pmatrix} n - \displaystyle \sum_{j=1}^{i - 1}k_j \cr k_i \end{pmatrix} $$
> 

Main Expression:

$$ \frac{d^n}{dx^n}\left(\displaystyle \prod_{i = 1}^m f_i(x) \right) = \newline
\Huge \sum_{\small k_1 + k_2 + ... + k_m = n} \left( \normalsize
C(n, k_1, k_2, ..., k_{m-1}) \cdot \prod_{i = 1}^{m}\frac{d^{k_i}f_i}{dx^{k_i}}
\right) $$

**Chain Rule**:
$$ \frac{d^n}{dx^n}(f(g(x))) = \sum_{k = 0}^{n - 1} \begin{pmatrix} n - 1 \cr k \end{pmatrix} \frac{d^{n - 1 - k}}{dx^{n - 1 - k}}(\frac{df}{dg}) \cdot \frac{d^{k+1}g}{dx^{k+1}} $$

$$ \frac{d^n}{dx^n}(f_1 \circ f_2 \circ f_3 \circ ... f_m) = \newline
\Huge \sum_{\small k_1 + k_2 + ... + k_m = n} \left( \normalsize
C(n - 1, k_1, k_2, ..., k_{m-1}) \cdot 
\prod_{i = 1}^{m -1}\frac{d^{k_i}}{dx^{k_i}}\left(\frac{df_i}{df_{i + 1}}\right) \cdot \frac{d^{k_m + 1}f_m}{dx^{k_m + 1}}
\right) $$

## Partial Deriavatives:

These are idental to Regular Deriavatives expect they act on function with more than 1 inputs but only take the deriavative with respect to any 1 variable

$$ z = f(x, y, ...) $$

$$ \frac{\partial f}{\partial x} = \frac{df}{dx} $$
$$ \frac{\partial f}{\partial y} = \frac{dh}{dy} $$

$g(x) = f(x, y)$

$h(y) = f(x, y)$

# Fractional Deriavatives:

$$D^{\alpha}_xf$$
(pending...)


# Directional Deriavative

Generalization of The Deriavative in a scalar field with any direction of $\mathbf{\vec{u}}$

Formal Definition:

$\mathbf{\vec{u}} = <u_x, u_y, u_z, ...>$

$|\mathbf{\vec{u}}| = 1$

$$ D_{\mathbf{\vec{u}}} f(x, y, z, ...) = \lim_{h \to 0} \frac{f(x + hu_x, y + hu_y, z + hu_z, ...) - f(x,y,z,...)}{h} $$

$$ D_{\mathbf{\vec{u}}} f(x, y, z, ...) = \frac{d}{dt}f(tu_x, tu_y, tu_z, ...) $$

## 1st Directional Deriavative

Rules:
---

### Special Cases:

$$ D_{\mathbf{\vec{u}}} (a) = 0 $$

**Power Rule**:
$$ D_{\mathbf{\vec{u}}} (x^n) = nx^{n - 1} u_x $$

> $S = \left[\displaystyle \sum_{i = 1}^m k_i = 1 \land \forall k_i (k_i \in \mathbb{W}) \right]$
$$ D_{\mathbf{\vec{u}}} \left(\displaystyle \prod_{i = 1}^{m} x_{i}^{n_i}\right) = \sum_{S} \left( \displaystyle \prod_{i = 1}^{m} \begin{pmatrix}n_i \cr k_i \end{pmatrix} x_{i}^{n_i - k_i} u_{x_{i}}^{k_i} \right) $$

**Exponential**:
$$ D_{\mathbf{\vec{u}}} (a^x) = a^x \ln(a) \cdot u_x $$

### General:

$$D_{\mathbf{\vec{u}}}(c \cdot f) = c \cdot D_{\mathbf{\vec{u}}}f$$

**Sum Rule**:
$$ D_{\mathbf{\vec{u}}}(f + g) = D_{\mathbf{\vec{u}}}f + D_{\mathbf{\vec{u}}}g $$
$$ D_{\mathbf{\vec{u}}}\left(\displaystyle \sum_{i = 1}^mf_i(x)\right) = \displaystyle \sum_{i = 1}^mD_{\mathbf{\vec{u}}}f_i$$

**Product Rule**:
$$ D_{\mathbf{\vec{u}}}(f \cdot g) = (D_{\mathbf{\vec{u}}}f) \cdot g + f \cdot (D_{\mathbf{\vec{u}}} g) $$
$$ D_{\mathbf{\vec{u}}}\left(\displaystyle \prod_{i = 1}^m f_i(x) \right) = \displaystyle \LARGE \sum_{\small k_1 + k_2 + ... = 1} \normalsize \left(\displaystyle \prod_{i = 1}^m D_{\mathbf{\vec{u}}}^{k_i}(f_i(x)) \right) $$

**Chain Rule**:
$$ D_{\mathbf{\vec{u}}}(f(g(x, y, z, ...))) = \frac{df}{dg} \cdot D_{\mathbf{\vec{u}}}g $$
$$ D_{\mathbf{\vec{u}}}(f_1 \circ f_2 \circ f_3 \circ ... f_n) = \left(\displaystyle \prod_{i = 1}^{n - 1} \frac{df_i}{df_{i +1}}\right) D_{\mathbf{\vec{u}}}f_n $$

## `n`'th Directional Deriavative

Repeated Application of The Directional Deriavative n times:
$$
D_{\mathbf{\vec{u}}}^{n} f = \underbrace{D_{\mathbf{\vec{u}}}(D_{\mathbf{\vec{u}}}(...D_{\mathbf{\vec{u}}}f))}_{n \text{ times}}
$$

Rules:
---

### Special Cases:

**Power Rule:**
$n \leq m$

$$ D_{\mathbf{\vec{u}}}^n(x^m) = \frac{m!}{(m - n)!} x^{m - n} u_x^n$$

(pending)


**Exponential**:

$$ D_{\mathbf{\vec{u}}}^n(a^x) = (\ln(a) \cdot u_x)^n \cdot a^x$$

### General:

**Sum Rule**:
$$ D_{\mathbf{\vec{u}}}^n(f + g) = D_{\mathbf{\vec{u}}}^nf + D_{\mathbf{\vec{u}}}^ng $$
$$ D_{\mathbf{\vec{u}}}^n\left(\displaystyle \sum_{i = 1}^mf_i(x)\right) = \displaystyle \sum_{i = 1}^mD_{\mathbf{\vec{u}}}^nf_i$$

**Product Rule**:
$$ D_{\mathbf{\vec{u}}}^{n}(f \cdot g) = \sum_{k = 0}^n \begin{pmatrix} n \cr k \end{pmatrix} D_{\mathbf{\vec{u}}}^{n - k}f \cdot D_{\mathbf{\vec{u}}}^kg $$


$$ D_{\mathbf{\vec{u}}}^n\left(\displaystyle \prod_{i = 1}^m f_i(x) \right) = \newline
\Huge \sum_{\small k_1 + k_2 + ... + k_m = n} \left( \normalsize
C(n, k_1, k_2, ..., k_{m-1}) \cdot \prod_{i = 1}^{m}D_{\mathbf{\vec{u}}}^{k_i}f_i
\right) $$

**Chain Rule**:
$$ D_{\mathbf{\vec{u}}}^n(f(g(x))) = \sum_{k = 0}^{n - 1} \begin{pmatrix} n - 1 \cr k \end{pmatrix} \frac{d^{n - 1 - k}}{dx^{n - 1 - k}}\left(\frac{df}{dg}\right) \cdot D_{\mathbf{\vec{u}}}^{k + 1}g $$

$$ D_{\mathbf{\vec{u}}}^n(f_1 \circ f_2 \circ f_3 \circ ... f_m) = \newline
\Huge \sum_{\small k_1 + k_2 + ... + k_m = n} \left( \normalsize
C(n - 1, k_1, k_2, ..., k_{m-1}) \cdot 
\prod_{i = 1}^{m -1}\frac{d^{k_i}}{dx^{k_i}}\left(\frac{df_i}{df_{i + 1}}\right) \cdot D_{\mathbf{\vec{u}}}^{k_m + 1}f_m
\right) $$

# Tangent Vectors

The Generalization of the Deriavative into a Vector Field with Scalar Inputs

$\vec{f}(x) = <f_x(x), f_y(x), f_z(x), ...>$

$$ \frac{d}{dx} \vec{f} = <\frac{df_x}{dx}, \frac{df_y}{dx}, \frac{df_z}{dx}, ...> $$


**n'th Tangent Vector**:
$$ \frac{d^n}{dx^n} \vec{f} = <\frac{d^nf_x}{dx^n}, \frac{d^nf_y}{dx^n}, \frac{d^nf_z}{dx^n}, ...> $$

**Partial Tangent Vector**:

$$ \frac{\partial}{\partial x} \vec{f} = <\frac{\partial f_x}{\partial x}, \frac{\partial f_y}{\partial x}, \frac{\partial f_z}{\partial x}, ...> $$

## Directional Tangent Vector:

$\vec{f}(x, y, z, ...) = <f_x(x, y, z, ...), f_y(x, y, z, ...), f_z(x, y, z, ...), ...>$

$$D_{\mathbf{\vec{u}}} \vec{f} = <D_{\mathbf{\vec{u}}} f_x, D_{\mathbf{\vec{u}}} f_y, D_{\mathbf{\vec{u}}} f_z, ...>$$

**n'th Directional Tangent Vector**:

$$D_{\mathbf{\vec{u}}}^n \vec{f} = <D_{\mathbf{\vec{u}}}^n f_x, D_{\mathbf{\vec{u}}}^n f_y, D_{\mathbf{\vec{u}}}^n f_z, ...>$$
