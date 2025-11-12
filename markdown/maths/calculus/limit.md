# Limits

Limit is said to be definite at a given point if as you approach it from all the different possible directions and it converges to a single definitive value.


$$ \lim_{x \to a} x = a $$

$$ \lim_{x \to a} (c \cdot f(x)) = c \cdot \lim_{x \to a} f(x) $$

$$ \lim_{x \to a} (f(x))^n = (\lim_{x \to a} f(x))^n $$

$$ \lim_{x \to a} (f(x) \pm g(x)) = \lim_{x \to a} f(x) \pm \lim_{x \to a} g(x)$$

$$ \lim_{x \to a} (f(x) \cdot g(x)) = \lim_{x \to a} f(x) \cdot \lim_{x \to a} g(x)$$

**Change in Variable**:

$$ \lim_{y \to a} f(y) = \lim_{x \to g^{-1}(a)} f(g(x))$$

$$
\forall f(x)\left(\left((\delta \text{ ranges}) \land f(a \pm \delta) \in \mathbb{R} \land
\lim_{\delta \to 0} (f(a + \delta) - f(a - \delta)) = 0\right)\implies \exists h \left(h \in \mathbb{R}\land \lim_{x \to a} f(x) = h\right)\right)
$$

**L'Hôpital's Rule**:

$$
L_1 := \left\{\frac{0}{0}, \frac{\infty}{\infty}, 0 \cdot \infty, \infty - \infty, 0^{0}, \infty^{0}, 1^{\infty} \right\}
$$
$$
L_2 := \{0, \infty\}
$$
$$
h := \lim_{x \to a} f(x) = \lim_{x \to a} g(x)
$$

$$
(h \in L_2 \land \newline 
(\exists S_1(f'(a) = S_1) \land \exists S_2(g'(a) = S_2)) \land \newline
\left(\lim_{x \to a} \frac{f(x)}{g(x)} \in L_1\right) \implies
\lim_{x \to a} \frac{f(x)}{g(x)} = \frac{f'(a)}{g'(a)})
$$