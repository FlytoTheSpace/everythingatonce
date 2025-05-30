
- [Back to Maths](./maths.md)
- [Back to Home](../../README.md)

# Calculus

**Calculus**: a Branch of mathematics that involves Continuous change, Area under a curve and approximations

- [Deriavative](#deriavative)

# Deriavative

**Deriavatives** is the *Rate of change* over a *small amount of time*

The Deriavatives at their **core** are:
$$
\lim_{\Delta x \to 0} \frac{\Delta y}{\Delta x}
$$

formal definition:
$$
\lim_{h \to 0} \frac{f(x + h) - f(x)}{h}
$$

- $y$ is a function with the argument $x$

    $y(x)$

- $x$ is the argument passed to the $y$ function

- $\Delta x$ is a very small amount, it is not infinitely small but it does approach 0, it is also the difference along the X axis between both points
- $\Delta y$ difference is the difference in the function's output with the arguments $x$ and $x + dx$
    
    $\Delta y = y(x + \Delta x) - y(x)$

- [`See Notation`](#notation)

(Please turn on "Allow Scripts Execution" on your Render if the graph isn't loading)

Example: -

<script>
    document.write("Hello, World");
</script>
<script src="https://cdn.jsdelivr.net/npm/function-plot@1/dist/function-plot.min.js"></script>

<div id="quadratic"></div>

<script>
    const quadratic = functionPlot({
        target: '#quadratic',
        width: 600,
        height: 400,
        grid: true,
        data: [
            {
                fn: 'x^2',
                color: "Dodgerblue",
                derivative: {
                    fn: `2*x`,
                    updateOnMouseMove: true   
                }
            }
        ]
    });
</script>

## Notation

The Deriavatives are not usually written as their core, but rather in their own Notations

### Leibniz's Notation

- $dx$ is equivalent to $\Delta x$ as $x$ approaches $0$

- $dy$ equivalent to $\Delta y$, The Difference in the function's outputs, given *slightely* different input

$$
\frac{dy}{dx} = \lim_{\Delta x \to 0} \frac{\Delta y}{\Delta x}
$$

`n`'th Deriavative:

$$
\frac{d^ny}{dx^n}
$$

$$
df = f(x + dx) - f(x) \newline
df + f(x) = f(x + dx) \newline
f(x + dx) = df + f(x)
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

### Newton's Notation

Function Symbols with `n` count of dots above to infinite n'th deriavative
$$
\dot{f}
$$
$$
\ddot{f}
$$

## Derivative Rules

### General


**Power Rule**:
$$
f(x) = x^n
$$
$$
\frac{df}{dx} = \frac{f(x + dx) - f(x)}{dx}
$$
$$
= \frac{(x + dx)^n - x^n}{dx}
$$
$$
= \frac{x^n + nx^{n-1} \cdot dx + \frac{n(n-1)}{2!}x^{n-2} \cdot dx^2 + ... + nx \cdot dx^{n-1} + dx^n - x^n}{dx}
$$
$$
= \frac{nx^{n-1} \cdot dx + \frac{n(n-1)}{2!}x^{n-2} \cdot dx^2 + ... + nx \cdot dx^{n-1} + dx^n}{dx}
$$
$$
= \lim_{dx \to 0} (nx^{n-1} + \frac{n(n-1)}{2!}x^{n-2} \cdot dx + ... + nx \cdot dx^{n-2} + dx^{n-1})
$$
$$
= nx^{n-1} + \lim_{dx \to 0} (\frac{n(n-1)}{2!}x^{n-2} \cdot dx + ... + nx \cdot dx^{n-2} + dx^{n-1})
$$
$$
= nx^{n-1} + (0 + ... + 0 + 0) = nx^{n-1} + 0 = nx^{n-1}
$$

### Sum Rule

$$
S(x) = f(x) + g(x)\newline
\frac{dS}{dx} = \frac{df}{dx} + \frac{dg}{dx}
$$

### Product Rule

$$
\frac{d(f(x) \cdot g(x))}{dx} = \frac{f(x + dx) \cdot g(x + dx) - f(x) \cdot g(x)}{dx} \newline
= \frac{f(x + dx) \cdot g(x + dx) - f(x) \cdot g(x)}{dx} \newline
= \frac{(f(x) + df) \cdot (g(x) + dg) - f(x) \cdot g(x)}{dx} \newline
= \frac{f(x) \cdot g(x) + f(x) \cdot dg + g(x) \cdot df + df \cdot dg - f(x) \cdot g(x)}{dx} \newline
= \frac{f(x) \cdot dg + g(x) \cdot df + df \cdot dg}{dx} \newline
= f(x) \cdot \frac{dg}{dx} + g(x) \cdot \frac{df}{dx} + \frac{df \cdot dg}{dx} \newline
= f(x) \cdot g'(x) + f'(x) \cdot g(x) + \frac{f'(x) \cdot dx \cdot g(x) \cdot dx}{dx} \newline
= f(x) \cdot g'(x) + f'(x) \cdot g(x) + f'(x) \cdot g(x) \cdot dx \newline
= f(x) \cdot g'(x) + f'(x) \cdot g(x) + (\lim_{dx \to 0}{f'(x) \cdot g(x) \cdot dx}) \newline
= f(x) \cdot g'(x) + f'(x) \cdot g(x) + (0) \newline
= f(x) \cdot g'(x) + f'(x) \cdot g(x)
$$

### Composition Rule

$$
\frac{d(f(g(x)))}{dx} = \frac{f(g(x + dx)) - f(g(x))}{dx} \newline
= \frac{f(dg + g(x)) - f(g(x))}{dx} \newline
= \frac{f(g(x) + dg) - f(g(x))}{dg} \cdot \frac{dg}{dx} \newline
= \frac{df}{dg} \cdot \frac{dg}{dx} \newline
$$

# Integral

An Integral is any function that gives the area under a graph of `f(x)` under some interval

$$
\int_{a}^{b} f(x) \ {dx}
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



# Multivariable

# Limits

L'Hopital's Rule:

$$
L_1 := \left\{\frac{0}{0}, \frac{\infty}{\infty}, 0 \cdot \infty, \infty - \infty, 0^{0}, \infty^{0}, 1^{\infty} \right\}
$$
$$
L_2 := \{0, \infty\}
$$
$$
R := \lim_{x \to a} f(x) = \lim_{x \to a} g(x)
$$

$$
(R \in L_2 \land \newline 
(\exists S_1 \in \mathbb{R} (f'(a) = S_1) \land \exists S_2 \in \mathbb{R} (g'(a) = S_2)) \land \newline
(\lim_{x \to a} \frac{f(x)}{g(x)} \in L_1) \implies \newline
\lim_{x \to a} \frac{f(x)}{g(x)} = \frac{f'(a)}{g'(a)}
$$