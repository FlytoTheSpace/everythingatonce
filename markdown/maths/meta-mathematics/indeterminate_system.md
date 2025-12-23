
## About

This Article Does not Specifically belong at any Mathematical Field it's an independent system of Mathematics also known as Meta-Mathematics.

### me

hi, I'm the same kid as in the last article, this is the part 2 of the previous article, I highly encourage you to go read it before coming here as I'll be creating axioms for that system.

3:39 PM 20 - December - 2025

# Indeterminate-Systems

**Indeterminate**: is an object/expression $U$ with no determinate value, it can also represent object within the system $\mathbb{U}$

An **Indeterminate Form** is form of the Indeterminates $I$, often associated with the situation they arise from, it may restrict the scope of the indeterminate.

**Instance** are of Indeterminate Form, they can take any ***arbitary*** value as allowed by the system $\mathbb{U}$ and the Indeterminate Form.

described as $x \leftarrow I$

$$\newcommand{\setform}{\text{set}}$$

$$\setform(I)$$

is a the set of all instances of the indeterminate form $I$

Set of All Determinate Values:

$$\mathbb{D}$$

Set of All Indeterminates:

$$\mathbb{I}$$

The Relationship between all of these are:

$$
\mathbb{D} \subset \mathbb{I} = \mathbb{U}
$$

## Axioms

$\forall I, I_1, I_2, ... \in \mathbb{I}$

- A1. **Arbitary Value**: Indeterminates are equal to every instance within their set of instances.

$$\forall x \in \setform(I) [I = x] $$

- A2. **Instance**: An Instance of an indeterminate belongs within it's set of instances.

$$y \leftarrow I \iff \exists x [x \in \setform(I) \land y = x]$$

- A3. **Equality**: 2 Indeterminates are equal if they their resolved instance values are the same

$$I_1 = I_2 \iff x \leftarrow I_1, y \leftarrow I_2 [x = y]$$

- A4. **Regularity**: Ensures that an Indeterminate can only have Determinate Instance values as it can introduce inconsistencies.

$$\setform(I) \setminus \mathbb{D} = \emptyset$$

- A5. **Universal Indeterminate**: exists a Universal Indeterminate, whose set of Instances is the set of all Determinates.

$$\exists U \forall x \in \mathbb{D} [ x \leftarrow x]$$

## Definitions

- **Set Form**: 

$$\setform(x) = \{y\ |\ y = x \}$$

- **Set of Determinates**: 

$$\mathbb{D} = \{x\ |\ \setform(x) = {x} \}$$

- **Congruence**: 2 Indeterminates are congruent if their set of instances are the same.
$$I_1 \cong I_2 \iff \setform(I_1) = \setform(I_2)$$

- **Constructive Indeterminates**: expressions where 

$$I = I$$

- **Destructive Indeterminates**: expressions where 

$$I \neq I$$

- **Ordinary Indeterminates** (requires A6): where

$$\setform(I) = \mathbb{D}$$

- **Partial Indeterminates**: where

$$\setform(I) \subsetneq \mathbb{D}$$


## Results

**Determinism**: if there is only 1 possible indeterminate instance, then it is The Value of the Indeterminant.

$$|\setform(I)| = 1 \implies \exists! x \in \setform(I) [I = x]$$

**Theorem**: any determinate number (Constant) $c \in \mathbb{D}$ that supports addition/multiplication can be represented as any of the following Indeterminate Forms:

$$\left\{ \frac{0}{0}, \frac{\infty}{\infty}, 0 \cdot \infty , 0^0 , \infty - \infty, \infty^0, 1^\infty, ... \right\}$$

Proof:

- $0/0$ case

$$
c \newline
= \lim_{x \to 0} c \cdot \frac{x}{x}\newline
= \left(\lim_{x \to 0} c \cdot x \right)\left(\lim_{x \to 0} \frac{1}{x}\right)\newline
= \left(\lim_{x \to 0} x \right)\left(\lim_{x \to 0} \frac{1}{x}\right)\newline
= \lim_{x \to 0} \frac{x}{x}\newline
= \frac{0}{0}\newline
$$

- $\infty/\infty$ case

$$
c \newline
= \lim_{x \to \infty} c \cdot \frac{x}{x}\newline
= \left(\lim_{x \to \infty} c \cdot x \right)\left(\lim_{x \to \infty} \frac{1}{x}\right)\newline
= \left(\lim_{x \to \infty} x \right)\left(\lim_{x \to \infty} \frac{1}{x}\right)\newline
= \lim_{x \to \infty} \frac{x}{x}\newline
= \frac{\infty}{\infty}\newline
$$

- $0 \cdot \infty$ case

$$
c \newline
= \lim_{x \to \infty} c \cdot \frac{x}{x}\newline
= \left(\lim_{x \to \infty} c \cdot x \right)\left(\lim_{x \to \infty} \frac{1}{x}\right)\newline
= \left(\lim_{x \to \infty} x \right)\left(\lim_{x \to \infty} \frac{1}{x}\right)\newline
= (\infty)(0)\newline
= 0 \cdot \infty\newline
$$

- $0^0$ case

$$
c \newline
= \lim_{x \to 0} c \cdot \frac{x}{x}\newline
= \left(\lim_{x \to 0} c \cdot x \right)\left(\lim_{x \to 0} \frac{1}{x}\right)\newline
= \left(\lim_{x \to 0} x \right)\left(\lim_{x \to 0} \frac{1}{x}\right)\newline
= \lim_{x \to 0} \frac{x}{x} \newline
= \frac{0}{0} \newline
$$

- $\infty - \infty$ case

$$
c \newline
= \lim_{x \to \infty} c + x - x \newline
= \lim_{x \to \infty} (c + x) + \lim_{x \to \infty}( - x) \newline
= \lim_{x \to \infty} x + \lim_{x \to \infty}( - x) \newline
= \lim_{x \to \infty} (x - x) \newline
= \infty - \infty \newline
$$

- $\infty^0$ case

$$
c \newline
= \lim_{x \to \infty} c \cdot \frac{x}{x}\newline
= \left(\lim_{x \to \infty} c \cdot x \right)\left(\lim_{x \to \infty} \frac{1}{x}\right)\newline
= \left(\lim_{x \to \infty} x \right)\left(\lim_{x \to \infty} \frac{1}{x}\right)\newline
= \lim_{x \to \infty} \frac{x}{x}\newline
= \lim_{x \to \infty} x^{1 - 1}\newline
= \lim_{x \to \infty} x^0\newline
= \infty^0\newline
$$

- $1^\infty$ case

$$
c \newline
\lim_{x \to \infty} c \cdot \frac{e^x}{e^x} \newline
\left(\lim_{x \to \infty} c \cdot e^x\right)\left(\frac{1}{e^x}\right) \newline
\left(\lim_{x \to \infty} e^x\right)\left(\frac{1}{e^x}\right) \newline
\lim_{x \to \infty} \frac{e^x}{e^x} \newline
\lim_{x \to \infty} \left(\frac{e}{e}\right)^x \newline
\lim_{x \to \infty} 1^x \newline
1^\infty \newline
$$

so,

$$
\therefore \frac{0}{0}, \frac{\infty}{\infty}, 0 \cdot \infty , 0^0 , \infty - \infty, \infty^0, 1^\infty, ...  \in \mathbb{I}
$$

# Indeterminate-Systems (Experimental)

In this Experimental Indeterminate-System, the 4th and 5th axioms are modified to support Indeterminates as instances of Indeterminates, however it makes the A1 axioms abigious (not quite true or false).

## Axioms

$\forall I, I_1, I_2, ... \in \mathbb{I}$

- A1 ....

- A2 ....

- A3 ....

- A4. **Regularity**: Ensures that an Indeterminates as Instances of Indeterminates are only ambigious and not false.

$$I_1 \leftarrow I_2 \iff x \leftarrow I_1, y \leftarrow I_2 [x = y]$$

- A5. **Universal Indeterminate**: exists a Universal Indeterminate, whose set of Instances is the Universal Set.

$$\exists U \forall x \in \mathbb{U} [ x \leftarrow x]$$

> Comment from author: WILD!

## Definitions:

- **Transcedental Indeterminate**:

$$\setform(I) \supsetneq \mathbb{D}$$

- **Referential Indeterminate**:

$$\exists I_1 [ |\setform(I_1)| > 1 \land I_1 \leftarrow I_2 ]$$
