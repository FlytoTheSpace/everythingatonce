
# Conditional Sum, Product, and Integral

**Prerequisites**:

The Reader is Expect to know the following or atleast have a fundamental understanding of them before continuing forward:

- Sum Notation
- Product Notation
- Fundamental Theorem of Calculus
- Riemann Sums
- Continuity and Discreteness
- Basic Set-Theory

Word on Notation:

$\varphi(x)$ denotes a predicate, standard in Set Theory.

notation here is heavily made up or is influenced by what is seen out in the mathematical wild.

# Conditional Sum

A Conditional Sum is a sum of $f(i)$ values where $i$ satisfies $\varphi(i)$, expressed in the following way:

$$
\displaystyle \sum_{\varphi(i)} f(i)
$$

if $\varphi(i_1), \varphi(i_2), \varphi(i_3), \varphi(i_4), ... = \top$ then:

$$
\displaystyle \sum_{\varphi(i)} f(i) = \varphi(i_1) + \varphi(i_2) + \varphi(i_3) + \varphi(i_4) + ... 
$$

you can also rewrite $\varphi(i)$ as a set $S$ in the set-build form.

$$S = \{x\ |\ \varphi(x)\}$$

$$
\displaystyle \sum_{\varphi(i)} f(i) = \displaystyle \sum_{i \in S} f(i)
$$

# Conditional Product

It is the same as the conditional sum except for product instead of sums, it is as straight forward as it gets:

$$
\displaystyle \prod_{\varphi(i)} f(i) = \varphi(i_1) \ \varphi(i_2) \ \varphi(i_3) \ \varphi(i_4) \ ... 
$$

# Conditional Integral

A Conditional Integral is expressed in the following way:

$$
\displaystyle \int_{\varphi(x)} f(x) \ dx
$$

What this is saying is to only integrate over values of $x$ if $\varphi(x)$ is satisfied at that particular point.

it's better to digest it with a few examples:

$$\displaystyle \int_{x \in [a ; b]} f(x) \ dx = \displaystyle \int_{a}^{b} f(x) \ dx$$

$$\displaystyle \int_{a \leq x \leq b} f(x) \ dx = \displaystyle \int_{a}^{b} f(x) \ dx$$

$$
\displaystyle \int_{a \leq x < b} f(x) \ dx= \lim_{n \to b} \displaystyle \int_{a}^{n} f(x) \ dx \newline
= \displaystyle \int_{a}^{b} f(x) \ dx
$$

(due to continuity)

All Continuous intervals have cardinality of $\mathfrak{c}$

$$[a;b] = \mathfrak{c}$$

(except for these which may or may-not be considered intervals: $[a;a], (a;a), ...$)

so the cardinality of the set $S$ must be $\mathfrak{c}$

$$|S| = \mathfrak{c}$$

$S$ was previous defined as the following:

$$S = \{x\ | \ \varphi(x)\}$$

## Discrete Conditional Integral

A Discrete one is a collection of disconnected points on the numberline.

this indicates that the cardinality of set $S$ must be less than $\mathfrak{c}$

$$|S| < \mathfrak{c}$$

Now back to our integral, if we assume that points $x_1, x_2, x_3, ...$ satisfy $\varphi(x)$ then

$$ \displaystyle \int_{\varphi(x)} f(x) \ dx = \int_{x_1}^{x_1} f(x)\ dx + \int_{x_2}^{x_2} f(x)\ dx + \int_{x_3}^{x_3} f(x)\ dx + ... \newline

= [F(x_1) - F(x_1)] + [F(x_2) - F(x_2)] + [F(x_3) - F(x_3)] + ... \newline
= 0 + 0 + 0 + ... $$

so here's our core result:

$$|S| < \mathfrak{c} \implies \int_{\varphi(x)} f(x) \ dx = 0$$

$$S = \{x\ |\ \varphi(x)\}$$

another way of showing this is via riemann sums of integrals:
> **Riemann Sums**:
> 
> $$\displaystyle \int_{a}^{b} f(x)\ dx = \displaystyle \lim_{\delta x \to 0} \sum_{i = 0}^{n} f(x_i) \ \delta x$$
> 
> where:
> 
> $$n = \frac{b - a}{\delta x}$$
> 
> $$x_i = a + i \cdot \delta x$$
> 

we can transform our riemann sums as such:

$$\displaystyle \int_{x \in [a;b]} f(x)\ dx = \displaystyle \lim_{\delta x \to 0} \sum_{x \in [a;b]} f(x) \ \delta x$$

if we generalize it, then we'll get our Conditional Riemann Sums (this name is made up):

$$\displaystyle \int_{\varphi(x)} f(x)\ dx = \displaystyle \lim_{\delta x \to 0} \sum_{\varphi(x)} f(x) \ \delta x$$

since we considering case where $\varphi(x)$ is discrete here, there is space on the numberline between each term which does not get filled as $\delta x$ goes to zero, so the whole expression tends toward zero.

> This can be visually verified on a graph but we can't show it here due to a reoccuring bug with our editing software when rendering.

$$ \displaystyle \int_{\varphi(x)} f(x)\ dx = \displaystyle \lim_{\delta x \to 0} \sum_{\varphi(x)} f(x) \ \delta x \newline
= \displaystyle \lim_{\delta x \to 0} \sum_{\varphi(x)} 0 \newline
= 0 $$

attaching a little more context to it, and we arrive at the same result:

$$|S| < \mathfrak{c} \implies \int_{\varphi(x)} f(x) \ dx = 0$$

$$S = \{x\ |\ \varphi(x)\}$$

END 9 - 12 - 2025
