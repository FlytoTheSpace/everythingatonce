
- [Back to Maths](./maths.md)
- [Back to Home](../../README.md)

# Logic

The Foundational Field for all of mathematics

> It should be noted that there exists not 1 but many Logical Systems with their own rules and definitions, this is one of them.

# Operations

## Operations Fundamentals

An Operation takes 1 or more inputs and maps them to a value based on the inputs.

**Identity**: is an operation that leaves it's input as it is
    $$f(n) = n$$

**Truth Table**: a table that lists all possible inputs for a given operation, and all of it's corresponding outcomes in the same row.

| $x$   | $f(x)$ |
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
- $I$ : **Indeterminate**: cannot be determinated.
- $\text{N/A}$ : **Undefined**: out of scope.



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

### Therefore

$$a \therefore b$$

### Because

$$a \because b$$

### Asserted

Asserts the truthfulness of the statement $a$

$$ \dashv a$$

### Proveable

Describes the Proveability of $b$ via $a$.

$$a \vdash b$$


### Entails

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

$$\exists ! x [\varphi(x)]$$
