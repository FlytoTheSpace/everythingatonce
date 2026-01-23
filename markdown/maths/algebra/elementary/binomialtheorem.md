
# Binomial Theorem

The Standard Binomial Theorem Implies that:

> $n \in \mathbb{Z}^+$
$$(a + b)^n = \sum_{k = 0}^n \begin{pmatrix}n\cr k\end{pmatrix}a^{n-k}b^k$$

it can be proven via Induction.

### Pascal's Triangle:

`n` is the Row
`k` is the Column
|       | `0`   | `1`   | `2`   | `3`   | `4`   | `5`   | `6`   | `7`   | `8`   | `9`   | `10`  | `...` |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ---- |
| `0`   | $1$   |       |       |       |       |       |       |       |       |       |       |      |
| `1`   | $1$   | $1$   |       |       |       |       |       |       |       |       |       |      |
| `2`   | $1$   | $2$   | $1$   |       |       |       |       |       |       |       |       |      |
| `3`   | $1$   | $3$   | $3$   | $1$   |       |       |       |       |       |       |       |      |
| `4`   | $1$   | $4$   | $6$   | $4$   | $1$   |       |       |       |       |       |       |      |
| `5`   | $1$   | $5$   | $10$  | $10$  | $5$   | $1$   |       |       |       |       |       |      |
| `6`   | $1$   | $6$   | $15$  | $20$  | $15$  | $6$   | $1$   |       |       |       |       |      |
| `7`   | $1$   | $7$   | $21$  | $35$  | $35$  | $21$  | $7$   | $1$   |       |       |       |      |
| `8`   | $1$   | $8$   | $28$  | $56$  | $70$  | $56$  | $28$  | $7$   | $1$   |       |       |      |
| `9`   | $1$   | $9$   | $36$  | $84$  | $126$ | $126$ | $84$  | $36$  | $9$   | $1$   |       |      |
| `10`  | $1$   | $10$  | $45$  | $120$ | $210$ | $252$ | $210$ | $120$ | $45$  | $10$  | $1$   |      |
| $...$ | $...$ | $...$ | $...$ | $...$ | $...$ | $...$ | $...$ | $...$ | $...$ | $...$ | $...$ | $...$ |

any entry within this can accessed by:

$$
C_{k}^{n} = \begin{pmatrix}n\cr k\end{pmatrix} = \frac{n!}{k!(n-k)!} = \underbrace{\frac{1}{k!}\left(\displaystyle\prod_{s=0}^{k -1}(n - s)\right)}_{n \in \mathbb{R}}
$$

some properties:

$$
\begin{pmatrix}n\cr k\end{pmatrix} = \begin{pmatrix}n - 1\cr k\end{pmatrix} + \begin{pmatrix}n - 1\cr k - 1\end{pmatrix}
$$

## Exponents Extention

This is an extention of exponent in the Standard Binomial theorem to the Reals

$$(a + b)^n = \sum_{k = 0}^n \begin{pmatrix}n\cr k\end{pmatrix}a^{n-k}b^k$$
$$(1 + x)^n = \sum_{k = 0}^n \begin{pmatrix}n\cr k\end{pmatrix}x^k$$

$$
\begin{pmatrix}n\cr k\end{pmatrix} = \frac{\Gamma(n + 1)!}{k! \cdot \Gamma(n-k + 1)!} = \frac{1}{k!}\left(\displaystyle\prod_{s=0}^{k -1}(n - s)\right)
$$

the series diverge when $|x| > 1$


# N-omial Theorem

The Binomial Theorem:

$$
(x+y)^n = \sum_{k=0}^{n} \begin{pmatrix} n \cr k \end{pmatrix} x^{n-k}y^k
$$

there lies a clear pattern to extend it beyond this point:

$$
((x + z) + y)^n = \sum_{i=0}^{n} \begin{pmatrix} n \cr i \end{pmatrix} (x + z)^{n-i}y^i \newline
(x + y + z)^n = 
\sum_{i=0}^{n} \begin{pmatrix} n \cr i \end{pmatrix} \left(
    \sum_{j = 0}^{n - i} \begin{pmatrix} n - i \cr j \end{pmatrix} x^{n - i - j}
    z^j
\right)y^i \newline
$$

**Trinomial Theorem**:

$$
(x + y + z)^n =  \sum_{i = 0}^{n} \sum_{j = 0}^{n - i} \begin{pmatrix} n \cr i \end{pmatrix} \begin{pmatrix} n - i \cr j \end{pmatrix} x^{n - i - j} y^{i} z^{j} \newline
$$

now with 4 terms:

$$
(x + y + z)^n =  \sum_{i = 0}^{n} \sum_{j = 0}^{n - i} \begin{pmatrix} n \cr i \end{pmatrix} \begin{pmatrix} n - i \cr j \end{pmatrix} x^{n - i - j} y^{i} z^{j} \newline

((x + w) + y + z)^n = 
\sum_{i = 0}^{n} \sum_{j = 0}^{n - i}
\begin{pmatrix} n \cr i \end{pmatrix} \begin{pmatrix} n - i \cr j \end{pmatrix}
(x + w)^{n - i - j} y^{i} z^{j} \newline

(x + y + z + w)^n = 
\sum_{i = 0}^{n} \sum_{j = 0}^{n - i}
\begin{pmatrix} n \cr i \end{pmatrix} \begin{pmatrix} n - i \cr j \end{pmatrix}
\left(\sum_{k=0}^{n - i - j} \begin{pmatrix} n - i - j \cr k \end{pmatrix} x^{n -i - j-k}w^k\right)
y^{i} z^{j} \newline
$$

**Quartic-nomial Theorem**:
$$
(x + y + z + w)^n = 
\sum_{i = 0}^{n} \sum_{j = 0}^{n - i} \sum_{k = 0}^{n - i - j}
\begin{pmatrix} n \cr i \end{pmatrix} \begin{pmatrix} n - i \cr j \end{pmatrix} \begin{pmatrix} n - i - j \cr k \end{pmatrix}
x^{n -i - j-k}
y^{i} z^{j} w^{k} \newline
$$

now generalize it for any arbitary number $N$

$$
(x + y + z + w)^n = 
\sum_{i = 0}^{n} \sum_{j = 0}^{n - i} \sum_{k = 0}^{n - i - j}
\begin{pmatrix} n \cr i \end{pmatrix} \begin{pmatrix} n - i \cr j \end{pmatrix} \begin{pmatrix} n - i - j \cr k \end{pmatrix}
x^{n -i - j-k}
y^{i} z^{j} w^{k} \newline

(x + y + z + w)^n = 
\sum_{i = 0}^{n} \sum_{j = 0}^{n - i} \sum_{k = 0}^{n - i - j}
\begin{pmatrix} n \cr i \end{pmatrix} \begin{pmatrix} n - i \cr j \end{pmatrix} \begin{pmatrix} n - i - j \cr k \end{pmatrix}
x^{n - (i + j +k)}
y^{i} z^{j} w^{k} \newline

(x + y + z + w)^n = 
\sum_{k_1 = 0}^{n} \sum_{k_2 = 0}^{n - k_1} \sum_{k_3 = 0}^{n - (k_1 + k_2)}
\begin{pmatrix} n \cr k_1 \end{pmatrix} \begin{pmatrix} n - k_1 \cr k_2 \end{pmatrix} \begin{pmatrix} n - k_1 - k_2 \cr k_3 \end{pmatrix}
x^{n - (k_1 + k_2 + k_3)}
y^{k_1} z^{k_2} w^{k_3} \newline
$$

$$
0 \leq k_1 \leq n \newline
0 \leq k_2 \leq n - k_1 \newline
0 \leq k_3 \leq n - (k_1 + k_2) \newline
... \newline
0 \leq k_i \leq n - \displaystyle \sum_{j = 0}^{i - 1} k_j
$$

$N$ is the count of Terms in $x + y + z + w +...$

Range:
$$
S_i = \left\{x | x \in \mathbb{Z} \land 1 \leq i \leq N - 1  \land 0 \leq k_i \leq n - \displaystyle \sum_{j = 0}^{i - 1} k_j\right\}
$$

$$
(x + y + z + w)^n = 
\sum_{\forall k_i (k_i \in S_i)}
\begin{pmatrix} n \cr k_1 \end{pmatrix} \begin{pmatrix} n - k_1 \cr k_2 \end{pmatrix} \begin{pmatrix} n - (k_1 + k_2) \cr k_3 \end{pmatrix}
x^{n - (k_1 + k_2 +k_3)}
y^{k_1} z^{k_2} w^{k_3} \newline
$$

Coefficient:

$$
C(n, k_1) = \begin{pmatrix} n \cr k_1 \end{pmatrix} \newline

C(n, k_1, k_2) = \begin{pmatrix} n \cr k_1 \end{pmatrix} \begin{pmatrix} n - k_1 \cr k_2 \end{pmatrix} \newline

C(n, k_1, k_2, k_3) = \begin{pmatrix} n \cr k_1 \end{pmatrix} \begin{pmatrix} n - k_1 \cr k_2 \end{pmatrix} \begin{pmatrix} n - (k_1 + k_2) \cr k \end{pmatrix} \newline

C(n, k_1, k_2, k_3, ..., k_{N - 1} ) = \begin{pmatrix} n \cr k_1 \end{pmatrix} \begin{pmatrix} n - k_1 \cr k_2 \end{pmatrix} \begin{pmatrix} n - (k_1 + k_2) \cr k_3 \end{pmatrix} ... \begin{pmatrix} n - \displaystyle \sum_{j = 1}^{N - 2} k_{j} \cr k_{N - 1} \end{pmatrix} \newline
C(n, k_1, k_2, k_3, ..., k_{N - 1} ) = \displaystyle \prod_{i = 1}^{N - 1} \begin{pmatrix} n - \displaystyle \sum_{j = 1}^{i - 1} k_{j} \cr k_i \end{pmatrix} \newline
$$

$$
(x + y + z + w)^n = 
\displaystyle \sum_{\forall k_i (k_i \in S_i)}
C(n, k_1, k_2, k_3) \cdot
x^{n - \displaystyle \sum_{j = 1}^{3} k_j}
y^{k_1} z^{k_2} w^{k_3} \newline
$$

**N-OMIAL THEOREM**:

$$
(x + y + z + t + w + ...)^n = \newline

\Huge \sum_{\small \forall k_i(k_i \in S_i)} \left( \normalsize
C(n, k_1, k_2, ..., k_{N-1})
\cdot x^{n - \displaystyle\sum_{j = 1}^{N-1} k_j}
y^{k_1}
z^{k_2}
t^{k_3}
w^{k_4}
...
\right)
$$

where:
$$C(n, k_1, k_2, k_3, ..., k_{N - 1} ) = \displaystyle \prod_{i = 1}^{N - 1} \begin{pmatrix} n - \displaystyle \sum_{j = 1}^{i - 1} k_{j} \cr k_i \end{pmatrix} \newline$$

$$
S_i = \left\{x | x \in \mathbb{Z} \land 1 \leq i \leq N - 1  \land 0 \leq k_i \leq n - \displaystyle \sum_{j = 0}^{i - 1} k_j\right\}
$$

**General Variation**:

$$
\left(\sum_{i = 0}^{N - 1} x_i\right)^n = \Huge \sum_{\small \forall k_i(k_i \in S_i)} \left( \normalsize
C(n, k_1, k_2, ..., k_{N-1})
\cdot x_{0}^{n - \displaystyle\sum_{j = 1}^{N-1} k_j}
\cdot \displaystyle \prod_{i = 1}^{N - 1} x_i^{k_{i}}
\right)
$$

# Infinite Series Expansion

The N-omial Theorem's exponent can be Extended past the Natural Numbers to Create not 1 but Many Infinite Series expansion:

$$
\left(1 + \sum_{i = 1}^{N - 1} x_i\right)^n = \Huge \sum_{\small \forall k_i(k_i \in S_i)} \left( \normalsize
C(n, k_1, k_2, ..., k_{N-1})
\cdot \displaystyle \prod_{i = 1}^{N - 1} x_i^{k_{i}}
\right)
$$

$$
S_i = \left\{x | x \in \mathbb{Z} \land 1 \leq i \leq N - 1  \land 0 \leq k_i \right\}
$$

an example:

$$
(1 + x + y)^{-1} = \sum_{i = 0}^{\infty} \sum_{j = 0}^{\infty} \begin{pmatrix} n \cr i \end{pmatrix} \begin{pmatrix} n - i \cr j \end{pmatrix} x^{i} y^{j} \newline
(1 + x + y)^{-1} = \sum_{i = 0}^{\infty} \begin{pmatrix} -1 \cr i \end{pmatrix} \begin{pmatrix} -1 - i \cr j \end{pmatrix} x^{i} y^{j} \newline
$$

$$
(1 + x + y)^{-1} =
1    -y      + y^2      - y^3       + y^4       - y^5        + y^6        - y^7         + y^8         - y^9         + ... \newline
x   - 2xy    + 3xy^2    - 4xy^3     + 5xy^4     - 6xy^5      + 7xy^6      - 8xy^7       + 9xy^8       - 10xy^9      + ... \newline
x^2 - 3x^2y  + 6x^2y^2  - 10x^2y^3  + 15x^2y^4  - 21x^2y^5   + 28x^2y^6   - 36x^2y^7    + 45x^2y^8    - 55x^2y^9    + ... \newline
x^3 - 4x^3y  + 10x^3y^2 - 20x^3y^3  + 35x^3y^4  - 56x^3y^5   + 84x^3y^6   - 120x^3y^7   + 165x^3y^8   - 220x^3y^9   + ... \newline
x^4 - 5x^4y  + 15x^4y^2 - 35x^4y^3  + 70x^4y^4  - 126x^4y^5  + 210x^4y^6  - 330x^4y^7   + 495x^4y^8   - 715x^4y^9   + ... \newline
x^5 - 6x^5y  + 21x^5y^2 - 56x^5y^3  + 126x^5y^4 - 252x^5y^5  + 462x^5y^6  - 792x^5y^7   + 1287x^5y^8  - 2002x^5y^9  + ... \newline
x^6 - 7x^6y  + 28x^6y^2 - 84x^6y^3  + 210x^6y^4 - 462x^6y^5  + 924x^6y^6  - 1716x^6y^7  + 3003x^6y^8  - 5005x^6y^9  + ... \newline
x^7 - 8x^7y  + 36x^7y^2 - 120x^7y^3 + 330x^7y^4 - 792x^7y^5  + 1716x^7y^6 - 3432x^7y^7  + 6435x^7y^8  - 11440x^7y^9 + ... \newline
x^8 - 9x^8y  + 45x^8y^2 - 165x^8y^3 + 495x^8y^4 - 1287x^8y^5 + 3003x^8y^6 - 6435x^8y^7  + 12870x^8y^8 - 24310x^8y^9 + ... \newline
x^9 - 10x^9y + 55x^9y^2 - 220x^9y^3 + 715x^9y^4 - 2002x^9y^5 + 5005x^9y^6 - 11440x^9y^7 + 24310x^9y^8 - 48620x^9y^9 + ... \newline
... - ...    + ...      - ...       + ...       - ...        + ...        - ...         + ...         - ...         + ... \newline
$$

> these coefficients were computed via this library's computational tools and are most likely correct but there's always a small chance for a problems to occur

This Results in an Infinite Number of Infinite series
