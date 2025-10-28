
**Binomial Theorem**:

$$
(x+y)^n =
\sum_{k=0}^{n} \begin{pmatrix} n \cr k \end{pmatrix} x^{n-k}y^k
$$

$$
\begin{pmatrix} n \cr k \end{pmatrix} = \left( \prod_{s=0}^{k -1}(n - s) \right)\frac{1}{k!}
$$

---

# **Extended**

**TRINOMIAL**:

$$
(x + y + z)^n = 
\sum_{i=0}^{n}\left(\sum_{k=0}^{n - i}

\begin{pmatrix} n \cr i \end{pmatrix}
\begin{pmatrix} n - i \cr k \end{pmatrix}

x^{n-i-k}y^{k}z^{i}

\right)
$$

**QUARTIC-NOMIAL**:

$$
(x + y + z + w)^n = 
\sum_{j = 0}^{n}\left(\sum_{i=0}^{n - j}\left(\sum_{k=0}^{n - (j + i)}

\begin{pmatrix} n \cr j \end{pmatrix}
\begin{pmatrix} n - j \cr i \end{pmatrix}
\begin{pmatrix} n - (j +i) \cr i \end{pmatrix}

x^{n - (j + i + k)} y^{k} z^{i} w^{j}

\right)\right)
$$

**N-OMIAL**:

$$
s = \#(x, y, z, t, w, ...)
$$

`s` is the count of terms


Coefficient:
$$
C(n,k_1, k_3, k_4, ...,, k_{s - 1}) = \prod_{i = 1}^{s - 1} \begin{pmatrix} n - \displaystyle \sum_{j=1}^{i - 1}k_j \cr k_i \end{pmatrix}
\newline =
\begin{pmatrix} n \cr k_1 \end{pmatrix}
\begin{pmatrix} n - k_1 \cr k_2 \end{pmatrix}
\begin{pmatrix} n - (k_1 + k_2) \cr k_3 \end{pmatrix}
\begin{pmatrix} n - (k_1 + k_2 + k_3) \cr k_4 \end{pmatrix}
...
\begin{pmatrix} n - \left(\displaystyle \sum_{j = 1}^{s-2}k_j \right) \cr k_{s-1} \end{pmatrix}
$$

Range:

$$
S_i = \left\{r| r \in \mathbb{N} \land 0 \leq r \leq n - \sum_{j=1}^{i - 1}k_j \right\}
$$

Main Expression:

$$
(x + y + z + t + w + ...)^n = \newline

\Huge \sum_{\small \forall k_i(k_i\!\! \in \!\! S_i)} \left( \normalsize

C(n, k_1, k_2, ..., k_{s-1})

\cdot x^{n - \displaystyle\sum_{j = 1}^{s-1} k_j}
y^{k_1}
z^{k_2}
t^{k_3}
w^{k_4}

...

\right)

$$