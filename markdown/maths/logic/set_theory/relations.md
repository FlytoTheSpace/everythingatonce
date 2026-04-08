
$$
\newcommand{\dom}{\text{dom}}
\newcommand{\ran}{\text{ran}}
$$

# Subset

The Axiom of Seperation

$$\forall y \exists z \forall x[(x \in z) \iff (x \in y \land \varphi(x, y))]$$

we define an a predicate:

$$z \subset y \iff \forall x[(x \in z) \iff (x \in y \land \varphi(x, y))]$$

in set-builder form we can write $z$ as:

$$z = \{x\ |\ x \in y \land \varphi(x, y)\}$$

# Ordered Pairs

Equivalence of Ordered-Pairs:

$$(a_0, a_1, a_2, ... a_n) = (b_0, b_1, b_2, ... b_n) \iff \bigwedge_{i = 0}^{n} (a_i = b_i)$$

> Notation:
> $$\bigwedge_{i = 0}^{n} (a_i = b_i) = [(a_0 = b_0) \land (a_1 = b_1) \land( a_2 = b_2) \land ... \land (a_n = b_n)]$$

$$(a, b) = \{\{a, b\}, {b}\}$$

with 

$$((a, b), c) = (a, b, c)$$

repeated nesting allows construction of all ordered pairs:

$$
(a) = a \newline
(a, b) = \{\{a, b\}, {b}\} \newline
(a, b, c) = \{\{\{\{a, b\}, b\}, c\}, {c}\} \newline
(a, b, c, d) = \{\{\{\{\{\{a, b\}, b\}, c\}, {c}\}, d\}, d\} \newline
...
$$

**Cartesian Product**:

definiton:

$$A \times B = \{(a, b)\ |\ a \in A \land b \in B\}$$

higher cartesian product:

$$A \times B \times C = (A \times B) \times C$$

$$
(A \times B) \times C = \{(k, c)\ |\ k \in (A \times B) \land c \in C\} \newline
A \times B \times C = \{((a, b), c)\ |\ (a \in A \land b \in B) \land c \in C\} \newline
A \times B \times C = \{(a, b, c)\ |\ a \in A \land b \in B \land c \in C\} \newline
$$

**Relations**:

$$R \subset A \times B$$

**Functions** $f$: are Relations such that:

$$\forall a \in A \exists ! b \in B[(a, b) \in f]$$

with:

$$\forall a,b [(a, b) \in \mathbb{f} \iff f(a) = b;]$$

a few operations on functions:

$$\dom(f) = A$$

$$\ran(f) = \{b | b \in B \land \exists a[a \in A \implies (a, b) \in f]\}$$

# Cardinality

for a well-defined predicate $\phi(x, y)$, we define equivalence of cardinality as:

$$|A| = |B| \iff \exists \phi \forall z [(z \in A \implies \exists ! y(y \in B \land \phi(z, y))) \land (z \in B \implies \exists ! x (x \in A \land \phi(x, z)))]$$

from Peano Axioms we can construct the set $\mathbb{N}$ (starting from $0$), which allows us to define cardinality for specific cases:
> Note: We are neither defining the zero $0$ value nor the Successor function as a set (like $0 = \emptyset$ or $s(0) = \{\emptyset\}$) instead we'll allow these to be arbitary, so the main goal here is to show How it interacts with the Axiom of Infinity.
$$
0 = |\emptyset| \newline
\forall x [1 = |\{x\}|] \newline
\forall x, y [ x \neq y \implies 2 = |\{x, y\}|] \newline
\forall x, y, z [ x \neq y \land x \neq z \land y \neq z \implies 3 = |\{x, y, z\}|] \newline
...
$$
the left-operand of "$\implies$" is combinatorially explosive, in plain english it's "for each distinct $x, y,z$" we may write it in shorthand as $\varphi(x, y, z)$

$$
\forall x, y, z [\varphi(x, y, z) \implies 3 = |\{x, y, z\}|] \newline
\forall x, y, z, t [\varphi(x, y, z, t) \implies 4 = |\{x, y, z, t\}|] \newline
...
$$

and it's like this for all the finite case.

by the Axiom of Infinity

$$\exists X [\emptyset \in X \forall y(y \in X \implies y \cup \{y\} \in X)]$$

and we can construct a predicate $\phi(x)$ that can 1-1 match this set $X$ to $\mathbb{N}$:

$$
0 \underset{\phi}{\longleftrightarrow} \emptyset \newline
1 \underset{\phi}{\longleftrightarrow} \{\emptyset\} \newline
2 \underset{\phi}{\longleftrightarrow} \{\{\emptyset\}, \emptyset\} \newline
3 \underset{\phi}{\longleftrightarrow} \{\{\{\emptyset\}, \emptyset\},\{\emptyset\}, \emptyset\} \newline
4 \underset{\phi}{\longleftrightarrow} \{\{\{\{\emptyset\}, \emptyset\},\{\emptyset\}, \emptyset\}, \{\{\emptyset\}, \emptyset\},\{\emptyset\}, \emptyset\} \newline
...
$$

it can also be done as a function:

$$
f: \mathbb{N} \to X \newline
f(0) = \emptyset \newline
f(n + 1) = f(n) \cup \{f(n)\} \newline
$$

so really:

$$|\mathbb{N}| = |X|$$

the cardinality of |$\mathbb{N}$|?:


assume $\exist k \in \mathbb{N}$ such that:
$$
k = |\mathbb{N}|
$$




so we define:

$$\aleph_0 = |\mathbb{N}| = |X|$$

since this number doesn't belong to $\mathbb{N}$, it has some special properties like:

$$\aleph_0 + 1 = \aleph_0$$

