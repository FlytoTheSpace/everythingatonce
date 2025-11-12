
# Harmonics

the Harmonic Series is defined as:

$$
\displaystyle \sum_{k = 1}^{\infty} \frac{1}{k} = 1 + \frac{1}{2} + \frac{1}{3} + \frac{1}{4} + \frac{1}{5} + \frac{1}{6} + \frac{1}{7} + ...
$$

--- 
as a **function**:

$$H(n) = \sum_{k = 1}^{n} \frac{1}{k}$$

properties:

- **Sum Identity**:

$$H(n + 1) = H(n) + \frac{1}{n + 1}$$

$$H(n + m) = H(n) + \sum_{k = 1}^{m} \frac{1}{k + n}$$

- **Difference Identity**:

$$H(n - 1) = H(n) - \frac{1}{n - 1}$$

$$H(n - m) = H(n) - \sum_{k = 1}^{m} \frac{1}{n - k}$$

## Convergence/Divergence

this series grows really slowly to the point that 1 could mistake it as converging but yet it ***diverges***, 1 way of verifying this is by comparing it with the area under the graph of $1/x$

$$
\int_{1}^{\infty} \frac{1}{x} dx < \displaystyle \sum_{k = 1}^{\infty} \frac{1}{k}
$$

> (Note from author: "I would've shown a nice graph to be able to justify the above claim but sadly there appears to be some kind of problem with markdown running scripts, so they are not present as of now")

evaluating the LHS:

$$
\int_{1}^{\infty} \frac{1}{x} dx < \displaystyle \sum_{k = 1}^{\infty} \frac{1}{k} \newline
\left[ \ln(x) \right]_{1}^{\infty} < \displaystyle \sum_{k = 1}^{\infty} \frac{1}{k} \newline
\lim_{x \to \infty} \ln(x) + \underbrace{\lim_{y \to 1} \ln(y)}_{c} < \displaystyle \sum_{k = 1}^{\infty} \frac{1}{k} \newline
\infty + c < \displaystyle \sum_{k = 1}^{\infty} \frac{1}{k} \newline
\infty < \displaystyle \sum_{k = 1}^{\infty} \frac{1}{k} \newline
$$

$$\therefore \displaystyle \sum_{k = 1}^{\infty} \frac{1}{k} = \infty$$


## Extention to The Reals

The Harmonic Series is in a way, a discrete version of 

$$f(x) = \ln(x)$$

with it's deriavative/slope:

$$f'(x) = \frac{1}{x}$$

if we take the Limit as $x \to \infty$

$$
\displaystyle \lim_{x \to \infty}f'(x) = \displaystyle\lim_{x \to \infty} \frac{1}{x} \newline
\displaystyle \lim_{x \to \infty}f'(x) = 0
$$

so it should be safe to say that it's discrete version should also have a slope of $0$ at some number near infinity as both similar graphs.

also to make extention of the Harmonic Series in a senseable way, we need some rule that applies to our already known definiton of Harmonics and can be extended beyond it's defined scope, in this instance the **sum identity** makes the most sense.

$$H(x + m) = H(x) + \sum_{k = 1}^{m} \frac{1}{x + k}$$

The Replacement of `n` with an `x` denotes that it should apply beyond it's scope of Integer to the Reals.

Now we take the Limit as $m \to \infty$

$$\lim_{m \to \infty} \frac{H(x + m) - H(m)}{x} = 0 $$

(this is the discrete variant of the deriavative)

$$\lim_{m \to \infty}[ H(x + m) - H(m) ]= 0 \cdot x$$
$$\lim_{m \to \infty}\left[ H(x) + \sum_{k = 1}^{m} \frac{1}{x + k} - H(m) \right] = 0$$
$$\lim_{m \to \infty}\left[ H(x) + \sum_{k = 1}^{m} \frac{1}{x + k} - \sum_{k = 1}^{m} \frac{1}{k} \right] = 0$$
$$H(x) + \lim_{m \to \infty}\left[\sum_{k = 1}^{m} \frac{1}{x + k} - \sum_{k = 1}^{m} \frac{1}{k} \right] = 0$$
$$H(x) = \lim_{m \to \infty}\left[\sum_{k = 1}^{m} \frac{1}{k} - \sum_{k = 1}^{m} \frac{1}{x + k} \right]$$
$$H(x) = \lim_{m \to \infty}\sum_{k = 1}^{m}\left( \frac{1}{k} -  \frac{1}{x + k}\right)$$
$$H(x) = \sum_{k = 1}^{\infty}\left( \frac{1}{k} -  \frac{1}{x + k}\right)$$

now we have a Definiton of the Harmonics for The Reals:

$$x \in \mathbb{R}$$

$$H(x) = \sum_{k = 1}^{\infty}\left( \frac{1}{k} -  \frac{1}{x + k}\right)$$