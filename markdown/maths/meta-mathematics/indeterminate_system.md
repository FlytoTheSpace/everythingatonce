
## About

This Article Does not Specifically belong at any Mathematical Field it's an independent system of Mathematics also known as Meta-Mathematics.

### me

hi, I'm the same kid as in the last article, this is the part 2 of the previous article, I highly encourage you to go read it before coming here as I'll be creating axioms for that system.

3:39 PM 20 - December - 2025

# Indeterminate-Systems

**Indeterminate**: is an object/expression with no determinate value, it can also represent object within the system $\mathbb{U}$

An **Indeterminate Form** is form of the Indeterminates $I$, often associated with the situation they arise from, it may restrict the scope of the indeterminate.

**Instance** are of Indeterminate Form, they can take any ***arbitary*** value as allowed by the system $\mathbb{U}$ and the Indeterminate Form.

described as $x \leftarrow I$

$$
\newcommand{\setform}{\text{set}}
\newcommand{\null}{\mathtt{NULL}}
\newcommand{\bangle}[1]{\langle #1 \rangle}
$$

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

- A1. **Axiom of Indeterminates**: An Indeterminate can be constructed via it's set of instances.

$$
\forall (A \subset \mathbb{D}) \exists (I \in \mathbb{I}) [\setform(I) = A]
$$

> the Domain for $A$ is meant to be consistent with $\mathbb{D}$ in the A4 axiom.

- A2. **Axiom of Instance**: An Instance of an indeterminate belongs within it's set of instances.

$$y \leftarrow I \iff \exists x [x \in \setform(I) \land y = x] \land |\setform(I)| > 0$$

- A3. **Axiom of Equality**: 2 Indeterminates are equal if they their resolved instance values are the same

$$I_1 = I_2 \iff x \leftarrow I_1 \land y \leftarrow I_2 \land x = y$$

> in This A2 axiom of Equality $x$ and $y$ are context dependent.

- A4. **Axiom of Limit**: Ensures that an Indeterminate can only have Determinate Instance values as it can introduce paradoxes.

$$\setform(I) \setminus \mathbb{D} = \emptyset$$

## Definitions

- **Set Form**: 

$$\setform(x) = \{y\ |\ y = x \}$$

- **Set of Determinates**: 

$$\mathbb{D} = \{x\ |\ \setform(x) = {x} \}$$

- **Congruence**: 2 Indeterminates are congruent if their set of instances are the same.
$$I_1 \cong I_2 \iff \setform(I_1) = \setform(I_2)$$

- **Constructive Indeterminates**: where all indeterminates in an expression/context resolve to the same value.

$$I = I$$


- **Destructive Indeterminates**: A more general version of the Constructive indeterminates where the self-equivalence is ambigious.

$$I \neq I$$

> for arbitary instances of $I$

> **Constructive Notation**: It can be hard to communicate which $I$ in an expression is constructive or not. this can be fixed via the following Notation:
>
> $n,m$ are mere labels, can be letters/numbers tec.
> 
> $$I^{\bangle{n}}_1 = I^{\bangle{n}}_2$$
>

- **Ordinary Indeterminates**: where

$$\setform(I) = \mathbb{D}$$

- **Partial Indeterminates**: where

$$\setform(I) \subsetneq \mathbb{D}$$

- **NULL Element**: a special indeterminate where:

$$\setform(\null) = \emptyset$$

> it is just here to complete the system.

## Results

**Determinism**: if there is only 1 possible indeterminate instance, then it is The Value of the Indeterminant.

$$
|\setform(I)| = 1 \implies I \in \mathbb{D}
$$
- Proof:

by A1:

$$\exists I [\setform(I) = \{a\}]$$

by $\setform()$ definition:

$$\implies I = a$$

$$\setform(I) = \{a\}$$

since $I = a$ in all contexts, we can use substitution here, as there's no ambiguity about their value.

$$\setform(I) = \{I\}$$

definition of determinates:
$$\mathbb{D} = \{x\ |\ \setform(x) = {x} \}$$

this satifies the conditionals for it to be a determinate. so:
$$
\therefore |\setform(I)| = 1 \implies I \in \mathbb{D}
$$


**Arbitary Value**:

$$
x \leftarrow I^{\bangle{n}} \iff I^{\bangle{n}} = x
$$
> where $I$ only needs to be constructive within this specific expression.

- Proof:

by A1:

$$\setform(I) = \{x, ...\}$$

by A2 & A3:

$$I = x \iff x \leftarrow I \land x \leftarrow x \land x = x$$

$$I = x \iff x \leftarrow I \land \top \land \top$$

$$I = x \iff x \leftarrow I$$

$$\therefore x \leftarrow I \iff I = x$$

**Determinates** and **Indeterminates**:

$$\{\text{A1}, \text{A4}\} \vdash |\mathbb{I}| = |\mathcal{P}(\mathbb{D})|$$

**Theorem**: any determinate number (Constant) $c \in \mathbb{D}$ that supports addition/multiplication can be represented as any of the following Indeterminate Forms:

$$\left\{ \frac{0}{0}, \frac{\infty}{\infty}, 0 \cdot \infty , 0^0 , \infty - \infty, \infty^0, 1^\infty, ... \right\}$$

Proof:

- $0/0$ case

$$ c $$

$$ = \lim_{x \to 0} c \cdot \frac{x}{x}$$

$$ = \left(\lim_{x \to 0} c \cdot x \right)\left(\lim_{x \to 0} \frac{1}{x}
\right)$$
$$ = \left(\lim_{x \to 0} x \right)\left(\lim_{x \to 0} \frac{1}{x}\right)$$

$$ = \lim_{x \to 0} \frac{x}{x}$$

$$ = \frac{0}{0}$$

- $\infty/\infty$ case

$$ c $$

$$ = \lim_{x \to \infty} c \cdot \frac{x}{x}$$

$$ = \left(\lim_{x \to \infty} c \cdot x \right)\left(\lim_{x \to \infty} \frac{1}{x}\right)$$

$$ = \left(\lim_{x \to \infty} x \right)\left(\lim_{x \to \infty} \frac{1}{x}\right)$$

$$ = \lim_{x \to \infty} \frac{x}{x}$$

$$ = \frac{\infty}{\infty}$$

- $0 \cdot \infty$ case

$$ c $$

$$ = \lim_{x \to \infty} c \cdot \frac{x}{x}$$

$$ = \left(\lim_{x \to \infty} c \cdot x \right)\left(\lim_{x \to \infty} \frac{1}{x}\right)$$

$$ = \left(\lim_{x \to \infty} x \right)\left(\lim_{x \to \infty} \frac{1}{x}\right)$$

$$ = (\infty)(0)$$

$$ = 0 \cdot \infty$$

- $0^0$ case

$$ c $$

$$ = \lim_{x \to 0} c \cdot \frac{x}{x}$$

$$ = \left(\lim_{x \to 0} c \cdot x \right)\left(\lim_{x \to 0} \frac{1}{x}\right)$$

$$ = \left(\lim_{x \to 0} x \right)\left(\lim_{x \to 0} \frac{1}{x}\right)$$

$$ = \lim_{x \to 0} \frac{x}{x} $$

$$ = \frac{0}{0} $$

- $\infty - \infty$ case

$$ c $$

$$ = \lim_{x \to \infty} c + x - x $$

$$ = \lim_{x \to \infty} (c + x) + \lim_{x \to \infty}( - x) $$

$$ = \lim_{x \to \infty} x + \lim_{x \to \infty}( - x) $$

$$ = \lim_{x \to \infty} (x - x) $$

$$ = \infty - \infty $$

- $\infty^0$ case

$$ c $$
$$ = \lim_{x \to \infty} c \cdot \frac{x}{x}$$
$$ = \left(\lim_{x \to \infty} c \cdot x \right)\left(\lim_{x \to \infty} \frac{1}{x}\right)$$
$$ = \left(\lim_{x \to \infty} x \right)\left(\lim_{x \to \infty} \frac{1}{x}\right)$$
$$ = \lim_{x \to \infty} \frac{x}{x}$$
$$ = \lim_{x \to \infty} x^{1 - 1}$$
$$ = \lim_{x \to \infty} x^0$$
$$ = \infty^0$$

- $1^\infty$ case

$$ c $$
$$ = \lim_{x \to \infty} c \cdot \frac{e^x}{e^x} $$
$$ = \left(\lim_{x \to \infty} c \cdot e^x\right)\left(\lim_{x \to \infty}\frac{1}{e^x}\right) $$
$$ = \left(\lim_{x \to \infty} e^x\right)\left(\lim_{x \to \infty}\frac{1}{e^x}\right) $$
$$ = \lim_{x \to \infty} \frac{e^x}{e^x} $$
$$ = \lim_{x \to \infty} \left(\frac{e}{e}\right)^x $$
$$ = \lim_{x \to \infty} 1^x $$
$$ = 1^\infty $$

so,

$$
\therefore \frac{0}{0}, \frac{\infty}{\infty}, 0 \cdot \infty , 0^0 , \infty - \infty, \infty^0, 1^\infty, ...  \in \mathbb{I} \setminus \mathbb{D}
$$

also since the constant $c$ had the same domain in each case, all these indeterminates are related as:

$$
\frac{0}{0} \cong \frac{\infty}{\infty} \cong 0 \cdot \infty  \cong 0^0  \cong \infty - \infty \cong \infty^0 \cong 1^\infty
$$

**Arithmetic**: The definition for arithematic with Indeterminates are as follows:
> These operations are for Destructive Indeterminates as they are a more general version and can be easily converted into Constructive cases via a simple constraint
- **Addition**:
$$\setform(I) = \{x_0, x_1, x_2, x_3, ...\}$$

$$a, x_0, x_1, x_2, x_3, ... \in \mathbb{D}$$

$$
I + a 
\begin{cases}
x_0 + a \cr
x_1 + a \cr
x_2 + a \cr
x_3 + a \cr
...
\end{cases}
$$
in a simpler form:
$$
I + a 
\begin{cases}
x \in \setform(I): a + x
\end{cases}
$$

indeterminates with indeterminates:

$$\setform(I_1) = \{x_0, x_1, x_2, x_3, ...\}$$

$$\setform(I_2) = \{y_0, y_1, y_2, y_3, ...\}$$

$$
I_1 + I_2 = \begin{cases}
x_0 + y_0 \cr
x_0 + y_1 \cr
x_0 + y_2 \cr
x_0 + ... \cr
x_1 + y_0 \cr
x_1 + y_1 \cr
x_1 + y_2 \cr
x_1 + ... \cr
x_2 + y_0 \cr
x_2 + y_1 \cr
x_2 + y_2 \cr
x_2 + ... \cr
... + ...
\end{cases}
$$

$$
I_1 + I_2 = 
\begin{cases}
x \in \setform(I_1) \land y \in \setform(I_2): x + y
\end{cases}
$$

- **Multiplication**:

$$
I \cdot a 
\begin{cases}
x \in \setform(I): a \cdot x
\end{cases}
$$

$$
I_1 \cdot I_2 = 
\begin{cases}
x \in \setform(I_1) \land y \in \setform(I_2): x \cdot y
\end{cases}
$$

- for any elementary operation on $I$ (i.e a finite combination of $+, \times, \sqrt{}, \sin(), \cos(), e^x, ... $) is defined as:

$$
f(I) = 
\begin{cases}
x \in \setform(I): f(x)
\end{cases}
$$


## Potential Internal Inconsistencies

Regarding some potential inconsistencies

**Proving Inconsistency**:

by A1:

$$\setform(I) = \{3, 5, 4\}$$

by A2:

$$3 \leftarrow I, 5 \leftarrow I$$

Arbitary Value result:

$$3 \leftarrow I \iff I = 3$$
$$5 \leftarrow I \iff I = 5$$

$$I = 3$$

$$I = 5$$

all we need is $I = I$, to show that $3 = 5$ breaking the system.

by A3.

$$I = I \iff 3 \leftarrow I \land 5 \leftarrow I \land 3 = 5$$

$$I = I \iff \top \land \top \land \bot$$

$$I = I \iff \bot$$

$$\therefore I \neq I$$

> why only 3, 5, and not 4 was used in A3? well equality is context-dependent here, equality of Indeterminates is dependent of their instances, statement like $x = x$ is valid regardless of context in $\mathbb{D}$, but in $\mathbb{I}$ that self-equality doesn't quite apply. writing down just multiple $I$ doesn't quite tell you whether they are constructive or not (i.e equal to each other). there is a specialized notation regarding this exact problem:

$$I^{\bangle{n}}_{1} = I^{\bangle{n}}_{2} \iff x \leftarrow I^{\bangle{n}}_{1} \land x \leftarrow I^{\bangle{n}}_{2} \land x = x$$

$\bangle{n}$ is just a label, it doesn't directly tell you it's instance value, but it does tell you that any Indeterminate with this same decorator/label resolves to the same value.

**Breaking Axiom of Limit**:

arbitary value result:

by A1:

$$\setform(I_1) = \{x, ...\}$$

$$\setform(I_2) = \{x, ...\}$$

Arbitary Value Result:
$$x \leftarrow I_1^{\bangle{n}} \iff I_1^{\bangle{n}} = x$$
$$x \leftarrow I_2^{\bangle{n}} \iff I_2^{\bangle{n}} = x$$

by A3:
$$I_1^{\bangle{n}} = I_2^{\bangle{n}} \iff x \leftarrow I_1^{\bangle{n}} \land x \leftarrow I_2^{\bangle{n}}\land x = x$$

$$x \leftarrow I_1^{\bangle{n}} \iff I_1^{\bangle{n}} = x$$

$$I_2^{\bangle{n}} \leftarrow I_1^{\bangle{n}} \iff I_1^{\bangle{n}} = I_2^{\bangle{n}}$$

this statement is built from the other axioms and must hold true.

but if we apply A4 to it then:

expected:
$$\setform(I_1^{\bangle{n}}) \setminus \mathbb{D} = \emptyset$$

reality:
$$\setform(I_1^{\bangle{n}}) \setminus \mathbb{D} = \{I_2^{\bangle{n}}\}$$

there is yet but a tiny problem with this argument and it comes down to ignoring the definition of $I_2^{\bangle{n}}$

it says:

$$I_2^{\bangle{n}} = I_2^{\bangle{n}}$$
and
$$I_2^{\bangle{n}} = x$$

so really:

$$I_2^{\bangle{n}} \in \mathbb{D}$$

then:

$$\therefore \setform(I_1) \setminus \mathbb{D} = \emptyset$$

as expected.

# Indeterminate-Systems (Experimental)

In this Experimental Indeterminate-System, the 4th and 5th axioms are modified to support Indeterminates as instances of Indeterminates. It's still deeply infested with paradoxes and is unrefined.

This System is denoted by:

$$\mathbb{J}$$

it related to the original systems as:

$$\mathbb{D} \subset \mathbb{I} \subset \mathbb{J} = \mathbb{U}$$

## Axioms

$\forall I, I_1, I_2, ... \in \mathbb{J}$

- A0. **Axiom of System**:

$$
\mathbb{I} \subset \mathbb{J}
$$

- A1. **Axiom of Indeterminates**: (slight change)

$$
\forall (A \subset \mathbb{J}) \exists (I \in \mathbb{J}) [\setform(I) = A]
$$

- A2-3. same as Before

- A4. **Axiom of Limit**: Ensures that an Indeterminates as Instances of Indeterminates are only ambigious and not false.

$$I_1 \leftarrow I_2 \iff x \leftarrow I_1 \land y \leftarrow I_2 \land x = y$$

- A5. **Axiom of Universal Indeterminate**: exists a Universal Indeterminate, whose set of Instances is the Universal Set.


$$\exists U \forall x \in \mathbb{U} [ x \leftarrow U]$$

> Comment from author: WILD!

## Definitions:

- **Recursive Indeterminate**:

$$\exists I_1 [ |\setform(I_1)| > 1 \land I_1 \leftarrow I_0 ]$$

- **Transcedental Indeterminate**:

$$\setform(I) \supsetneq \mathbb{D}$$

## Results


### Cardinality

we want to the cardinality of $\mathbb{J}$

let's assume we have a list of all the indeterminates in $\mathbb{I}$

$$\mathbb{I} = \{I_0, I_1, I_2, I_3, ...\}$$

with $\mathbb{I} \neq \emptyset$ which is guarantted as $\null \in \mathbb{I}$ even if $\mathbb{D} = \emptyset$

by A1, we can create Indeterminates with any $\setform()$ combination from this set. essentially the Powerset:

$$\mathcal{P}(\mathbb{I})$$

but A1 allows us to do it again,

$$\mathcal{P}(\mathcal{P}(\mathbb{I}))$$

and again, over and over again....

$$\mathcal{P}^{n}(\mathbb{I})$$

and yet A1 allows us to perform this task endlessly, sets with bigger and bigger sets for both finite and infinite size of $\mathbb{I}$.

and still then we can construct such an Indeterminate that isn't in our archieved power-sets yet.

$$\exists J \in \mathbb{J}[J \notin \{I | \setform(I) \in \mathcal{P}^{n}(I)\}]$$

so even though my exposure to higher-mathematics is low, I must deduce that $\mathbb{J}$ is atleast Uncountably Infinite:

$$|\mathbb{J}| \geq \mathfrak{c}$$

regardless of $\mathbb{D}$.
