
## About

This Article Does not Specifically belong at any Mathematical Field it's an independent system of Mathematics also known as Meta-Mathematics.

This Specific Mathematical system is meant to explore Indeterminates to their fullest extent, to the points some properties about them which I thought of as universal, were not actually universal at all.

### Who Am I

Hi I'm a 14-15y/o 9th grader from India I have many online names such as "FlytoTheSpace" or "farlandunknown", so you are free to take this article with $0$ weight if you'd like to as I'm just a kid, I'm not the smartest person in the word not even the most knowledgeable, I shouldn't even be here to begin with, but yeah You can't trip away my love for mathematics, I'll be doing it till the day I die.

8:52 AM 20 - December - 2025

# Indeterminates

**Indeterminates**: are symbols/variables with no determinate value.

The Indeterminates Forms:

$$\{ \frac{0}{0}, \frac{\infty}{\infty}, 0 \cdot \infty , 0^0 , \infty - \infty, \infty^0, 1^\infty, ... \} $$

we build from a simple case:

$$a \cdot 0 = 0 $$

with $a$ here is arbitary

subtitute $b = 0$

$$a \cdot b = b$$

our standard algebra would tell us to divide by $b$ in order to solve for $a$, as long as $b \neq 0$

This is Where We Diverge from our Standard Mathematics:

# Indeterminates (Diverged)

Here in this specific instance if we allow for divison by $0$ in the VERY specific case that the Nominator is also $0$

$$a \cdot b = b$$

$$a \cdot \frac{b}{b} = \frac{b}{b}$$

$$a = \frac{b}{b}$$

This is Our result:

$$a = \frac{0}{0}$$

The Previous steps were questionable to say the least let's go over them:

## Verification

$$a \cdot b = b$$

Dividing by $b$ part:

### Associativity:

$$\frac{(a \cdot b)}{b} = \frac{b}{b}$$

$$\frac{b}{b} = \frac{b}{b}$$

$$\frac{0}{0} = \frac{0}{0}$$

nothing interesting here.
if we take $b/b = 1$ then:

- Case 1:

    $$\frac{0}{0} = 1$$

    a specific instance of an indeterminate taking a determinate form

- Case 2:

    $$1 = 1$$


### Commutativity:

$$\frac{a}{b} \cdot b = \frac{b}{b}$$

$$\underbrace{\frac{a}{0}}_{\text{undefined}} \cdot 0 = \frac{0}{0}$$

Division for by zero for $a \neq 0$ is still undefined at this point $a/0$

### Associativity 2:

$$a \cdot \frac{b}{b} = \frac{b}{b}$$

- Case 1: if we take $b/b = 1$ for each then:

    $$a \cdot 1 = 1$$
    $$a = 1$$
    FALSE, as $a$ is arbitary.

- Case 2: if we take $b/b = 1$ for the RHS case then:

    $$a \cdot \frac{b}{b} = 1$$

    $$a \cdot \frac{0}{0} = 1$$

    well this is a weird case, in this instance $0/0 = 1/a$ for it to hold true.

- Case 3: if we take $b/b = 1$ for the LHS case then:

    $$a \cdot 1 = \frac{b}{b}$$

    $$a = \frac{0}{0}$$

    look, this is our result here $a$ is any Arbitary Number we want and it's an instance of an Indeterminate.

## Instances of Indeterminates

Indeterminates from our previous result say that they can take any Determinate Value, which we call an "instance" of an indeterminate, some examples:

$$\frac{0}{0} = 5$$

or

$$\frac{0}{0} = 3$$

$$\newcommand{\random}{\text{random}}$$

ok Now This doesn't mean that $5 \neq 3$, it would be False by any means, $\frac{0}{0}$ is no longer just a simple expression, it's much more similar to the $\random()$ functions, which is not guaranteed to match it's last output, However it must be clarified that it is NOT RANDOM, it's ARBITARY.

we're gonna bring the concept of variables from programming, as they can store any given value, It'll allows of us reason more much effectively about a specific instance of an indeterminate.

$$x \leftarrow \frac{0}{0}$$

This is saying "store the instance value of $0/0$ in x", now $x$ here is a regular old variable, we can use it in expressions as we like:

$$ax^2 + bx + c$$

if we instead set $x = 0/0$ then it'd be, just another way of writing $0/0$ at every place $x$ appear and worst of all they can resolve to different values.

$$x = \frac{0}{0}$$

$$ax^2 + bx + c$$

$$a\left(\frac{0}{0}\right)^2 + b\left(\frac{0}{0}\right) + c$$

## Constructive Indeterminates

is a sitatution where all indeterminates resolve to a single value, in such cases our standard algebra can help there. e.g:

$$a\left(\frac{0}{0}\right)^2 + b\left(\frac{0}{0}\right) + c$$

$$a\left(2\right)^2 + b\left(2\right) + c$$

here both $0/0$ resolved to the value $2$.

## Destructive Indeterminates

are all cases where the instances of indeterminates resolve  to different values, can be modeled as multiple variables within a single expression:

$$a\left(\frac{0}{0}\right)^2 + b\left(\frac{0}{0}\right) + c$$

$$ax^2 + by + c$$

in here the 2 $0/0$ cases resolve to values $x$ and $y$ respectively.

## Ordinary Indeterminates

The above cases such as $0/0$ are **Ordinary Indeterminates** as they can take any arbitary value they like, they're the one's we looked at so far.

Ordinary Indeterminates occurance:

say when a function $f$ causes data/information loss to it's entire input space, consider:

| $a$ | $f(a)$ |
| --- | ------ |
| $1$ | $0$    |
| $0$ | $0$    |

here function $f$ maps both inputs to $0$ now we define a new function $f^{-1}$ which was beyond our rules, it must represent both $1$ and $0$ simultaneously, as any of them is just as valid as the other so, $f^{-1}(a)$ must be an Indeterminate

$$f^{-1}(a) = 0, 1$$

$$f^{-1}(a) \in I$$

## Partial Indeterminates

**Partial/Restrictive Indeterminates** are cases where there's only a few specific values that it can take but still has freedom to choose any one of them. e.g.

$$x^2 = 25$$
now x here is
$$x = 5, -5$$
it is a **Partial Indeterminate** as it can map either to $5$, or $-5$ as per will but is not that strong enough map to any values like **Ordinary Indeterminates**.

## Undecidability

a classic case of it is:

$$\varphi(x) \land \lnot \varphi(x) = \top$$

the statement $\varphi(x)$ is undecidable, because any output it may choose it will be wrong.

but via Destructive Indeterminates this Expression can hold true:


$$\varphi(x) = 1, 0$$

$$\varphi(x) \land \lnot \varphi(x) = \top$$

$$1 \land \lnot 0 = \top$$

$$1 \land 1 = \top$$

$$\top = \top$$


