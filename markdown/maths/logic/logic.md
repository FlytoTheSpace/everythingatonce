
- [Back to Maths](./maths.md)
- [Back to Home](../../README.md)

# Logic

The Foundational Field for all of mathematics

> It should be noted that there exists not 1 but many Logical Systems with their own rules and definitions, this is a general framework that works to define certain operations and objects that all the other's use.

# Axioms

These are Axiom of certain "relations" defined in mathematics:

**Equality**:

Reflexitivity:

$$\forall x [x = x]$$

Symmetry:

$$\forall x \forall y [x = y \iff y = x]$$

Transitivity:

$$\forall x \forall y \forall z[x = y \land y = z \implies x = z]$$

**Predicate**:

for any well-defined $\varphi$:

$$[x = y] \implies [\varphi(x) \iff \varphi(y)]$$

# Propositional Logic
Propositional Logic (0'th Order Logic)

**Truth Table**: a table that lists all possible inputs for a given operation, and all of it's corresponding outcomes in the same row.

| $x$   | $\phi(x)$ |
| ----- | ------ |
| $a$   | $p$    |
| $b$   | $q$    |
| $c$   | $r$    |
| $...$ | $...$  |

## Logical Operations

These are operations that can only take boolean inputs (i.e $0, 1$) and an outcome that is it's **validity**

**Validity**: These describe the truthfulness of logical expressions, these are:
- $1, \top$ : **True**
- $0, \bot$ : **False**
- $I$ : **Indeterminate** cannot be determinated.
- $\text{N/A}$ : **Undefined** out of scope.

### AND

The **And** operator tells whether both inputs are true or not

$$a \land b$$

truth table:

| a   | b   | $a \land b$    |
| --- | --- | -------------- |
| $1$ | $1$ | $1$            |
| $1$ | $0$ | $0$            |
| $0$ | $1$ | $0$            |
| $0$ | $0$ | $0$            |

### OR

The **OR** operator tells whether either of the both inputs are true or not

$$a \lor b$$

truth table:

| a   | b   | $a \lor b$     |
| --- | --- | -------------- |
| $1$ | $1$ | $1$            |
| $1$ | $0$ | $1$            |
| $0$ | $1$ | $1$            |
| $0$ | $0$ | $0$            |

### NOT

The **NOT** operator inverts the given input

$$\lnot a$$

truth table:

| a   | $\lnot a$      |
| --- | -------------- |
| $1$ | $0$            |
| $0$ | $1$            |

### X-OR

The **Exclusive-OR** operator tells whether if only 1 of the inputs is true:

$$a \oplus b$$

truth table:

| a   | b   | $a \oplus b$     |
| --- | --- | ---------------- |
| $1$ | $1$ | $0$              |
| $1$ | $0$ | $1$              |
| $0$ | $1$ | $1$              |
| $0$ | $0$ | $0$              |

### Implies

The **Implies** operator tells whether $a$ implies $b$

$$a \implies b$$

truth table:

| a   | b   | $a \implies b$   |
| --- | --- | ---------------- |
| $1$ | $1$ | $1$              |
| $1$ | $0$ | $0$              |
| $0$ | $1$ | $1$              |
| $0$ | $0$ | $1$              |

the last 2 entries are tricky for the most, in $a \implies b$ if $a$ true then $b$ must also be true, if $a$ is false then it should not imply anything about $b$

### If-and-Only-If

The **If-and-Only-If** operator describes that both of the expressions must be equivalent.

$$a \iff b$$

truth table:

| a   | b   | $a \iff b$   |
| --- | --- | ---------------- |
| $1$ | $1$ | $1$              |
| $1$ | $0$ | $0$              |
| $0$ | $1$ | $0$              |
| $0$ | $0$ | $1$              |


## Identities

ORDER OF EVALUATION
> 1. $\land$ Logical And
> 2. $\lor$ Logical Or
> 3. $\lnot$ Logical Not.

AND:

$$a \land b = b \land a$$

$$(a \land b) \land c = a \land (b \land c)$$

$$a \land b = \lnot[(\lnot a) \lor (\lnot b)]$$

OR:

$$a \lor b = b \lor a$$

$$(a \lor b) \lor c = a \lor (b \lor c)$$

$$a \lor b = \lnot[(\lnot a) \land (\lnot b)]$$

$$a \land (b \lor c) = (a \land b) \lor (a \land c)$$

NOT:

$$\lnot(\lnot a) = a$$

Any Binary Predicate Operation that maps to $r_1, r_2, r_3, r_4$ in it's truth table written in terms of $\land, \lor, \lnot$.

$$\phi(a, b) = [a \land b \land r_1] \lor [a \land (\lnot b) \land r_2] \lor [(\lnot a) \land b \land r_3] \lor [(\lnot a) \land (\lnot b) \land r_r]$$

any predicate operation that maps to $r_1, r_2, r_3, ... , r_{2^{n}}$ with $n$ count of inputs:

$$
\phi(..., a, b, c) =\newline
[... \land a \land b \land c \land r_1] \lor \newline
[... \land a \land b \land (\lnot c) \land r_1] \lor \newline
[... \land a \land (\lnot b) \land c \land r_1] \lor \newline
[... \land a \land (\lnot b) \land (\lnot c) \land r_1] \lor \newline
[... \land (\lnot a) \land b \land c \land r_1] \lor \newline
[... \land (\lnot a) \land b \land c \land r_1] \lor \newline
[... \land (\lnot a) \land b \land (\lnot c) \land r_1] \lor \newline
[... \land (\lnot a) \land (\lnot b) \land c \land r_1] \lor \newline
[... \land (\lnot a) \land (\lnot b) \land (\lnot c) \land r_1] \lor \newline
...
$$
the pattern of $\lnot$ here is the same as counting in Base 2 representation of numbers.

# Predicate Logic

Predicate Logic (1st Order Logic)

## Quantifiers

### Universal Quantifier

The **Universal Quantifier** tells that all possible values of $x$ must satisfy that following $\varphi$ statement.

$$\forall x [\varphi(x)]$$

"for all $x$ satisfies $\varphi(x)$"

### Existential Quantifier

The **Existential Quantifier** implies the existence of atleast 1 $x$ such that the following statement $\varphi$ is true:

$$\exists x [ \varphi(x)]$$

Variantions:

**Not Exists Quantifier** implies the non-existence of any $x$ such that the following statement $\varphi$ is true:

$$\nexists x [ \varphi(x) ] = \lnot \exists x [ \varphi (x) ]$$

**Uniqueness Quantifier** implies the existence of only 1 Unique $x$, such that the following statement $\varphi$ is true:

$$\exists ! x [\varphi(x)] = \exists x [\varphi(x) \land \nexists y (x \neq y \land \varphi(y))]$$

## Identities

$$\forall x [\varphi(x)] = \lnot \exists x [\lnot \varphi(x)]$$

$$\exists x [\varphi(x)] = \lnot \forall x [\lnot \varphi(x)]$$

