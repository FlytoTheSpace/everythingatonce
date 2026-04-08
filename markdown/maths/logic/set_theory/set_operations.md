
# Set Operations


## Union

The Axiom of Union of zfc:

$$
\forall z \exists A \forall y \forall x [(x \in y \land y \in z) \iff x \in A]
$$

this is written as:

$$A = \bigcup z$$

in set-builder form it can be expressed as:

$$\bigcup z = \{x\ |\ \exists y [x \in y \land y \in z]\}$$

$\exists$ can be replaced with many OR expressions for every $y_0, y_1, y_2, ... \in z$

$$\bigcup z = \{x\ |\ x \in y_0 \lor x \in y_1 \lor x \in y_2 \lor ...\}$$

if $z$ has only 2 element $y_0, y_1$ then:

$$\bigcup z = \{x\ |\ x \in y_0 \lor x \in y_1\}$$

we define it as a binary set-operation between $y_0$ and $y_1$:

$$y_0 \cup y_1 = \{x\ |\ x \in y_0 \lor x \in y_1\}$$

> we replace $y_0, y_1$ with $A, B$ respectively for our purposes

$$A \cup B = \{x\ |\ x \in A \lor x \in B\}$$

from this we prove certain properties about our binary operation:

commutativity:

$$
A \cup B = \{x\ |\ x \in A \lor x \in B\} \newline
A \cup B = \{x\ |\ x \in B \lor x \in A\} \newline
A \cup B = B \cup A \newline
$$

associativity:

$$
A \cup \underbrace{(B \cup C)}_{Y} = \{x\ |\ x \in A \lor x \in Y\} \newline
\underbrace{(A \cup B)}_{X} \cup C = \{x\ |\ x \in X \lor x \in C\} \newline
(A \cup B) \cup C = \{x\ |\ (x \in A \lor x \in B) \lor x \in C\} \newline
(A \cup B) \cup C = \{x\ |\ x \in A \lor x \in B \lor x \in C\} \newline
(A \cup B) \cup C = \{x\ |\ x \in A \lor ( x \in B \lor x \in C)\} \newline
(A \cup B) \cup C = \{x\ |\ x \in A \lor x \in Y\} \newline
(A \cup B) \cup C = A \cup \underbrace{(B \cup C)}_{Y} \newline
(A \cup B) \cup C = A \cup (B \cup C) \newline
$$

identity:

$$
A \cup \emptyset 
= \{x\ |\ x \in A \lor x \in \emptyset\} \newline
= \{x\ |\ x \in A \lor \bot\} \newline
= \{x\ |\ x \in A\} \newline
A \cup \emptyset = A \newline
$$

original big-union as multiple binary-union
for $y_0, y_1, y_2, y_3, ... \in z$
$$
\bigcup z = \{x\ |\ x \in y_0 \lor x \in y_1 \lor x \in y_2 \lor x \in y_3 \lor ...\} \newline
\bigcup z = \{x\ |\ (x \in y_0) \lor (x \in y_1 \lor x \in y_2 \lor x \in y_3 \lor ...)\} \newline
\bigcup z = \{x\ |\ x \in y_0\} \cup \{x\ |\ x \in y_1 \lor x \in y_2 \lor x \in y_3 \lor ...\} \newline
\bigcup z = y_0 \cup \{x\ |\ (x \in y_1) \lor (x \in y_2 \lor x \in y_3 \lor ...)\} \newline
\bigcup z = y_0 \cup y_1 \cup \{x\ |\ x \in y_2 \lor x \in y_3 \lor ...\} \newline
\bigcup z = y_0 \cup y_1 \cup y_2 \cup \{x\ |\ \lor x \in y_3 \lor ...\} \newline
\bigcup z = y_0 \cup y_1 \cup y_2 \cup y_3 \cup ... \newline
\bigcup_{y \in z} y = y_0 \cup y_1 \cup y_2 \cup y_3 \cup ... \newline
$$

## Intersection

by the Axiom of Seperation, we get subsets of $A$, where we choose $\varphi(x)$ to be $x \in B$ to get the intersection.

$$A \cap B = \{x\ |\ x \in A \land x \in B\}$$

some properties:

commutativity:

$$
A \cap B = \{x\ |\ x \in A \land x \in B\} \newline
= \{x\ |\ x \in B \land x \in A\} \newline
= B \cap A \newline
A \cap B = B \cap A
$$

associativity:

$$
A \cap \underbrace{(B \cap C)}_{Y} = \{x\ |\ x \in A \land x \in Y\} \newline
\underbrace{(A \cap B)}_{X} \cap C = \{x\ |\ x \in X \land x \in C\} \newline
(A \cap B) \cap C = \{x\ |\ (x \in A \land x \in B) \land x \in C\} \newline
(A \cap B) \cap C = \{x\ |\ x \in A \land x \in B \land x \in C\} \newline
(A \cap B) \cap C = \{x\ |\ x \in A \land ( x \in B \land x \in C)\} \newline
(A \cap B) \cap C = \{x\ |\ x \in A \land x \in Y\} \newline
(A \cap B) \cap C = A \cap \underbrace{(B \cap C)}_{Y} \newline
(A \cap B) \cap C = A \cap (B \cap C) \newline
$$

identity/special case:

$$
A \cap A = \{x\ |\ x \in A \land x \in A\} \newline
A \cap A = \{x\ |\ x \in A\} \newline
A \cap A = A \newline
$$

$$
A \cap \emptyset = \{x\ |\ x \in A \land x \in \emptyset\} \newline
A \cap \emptyset = \{x\ |\ x \in A \land \bot\} \newline
A \cap \emptyset = \{x\ |\ \bot\} \newline
A \cap \emptyset = \emptyset \newline
$$

big intersection:

$$
\bigcap z = \{x\ |\ x \in y_0 \land x \in y_1 \land x \in y_2 \land x \in y_3 \land ...\} \newline
\bigcap z = \{x\ |\ (x \in y_0) \land (x \in y_1 \land x \in y_2 \land x \in y_3 \land ...)\} \newline
\bigcap z = \{x\ |\ x \in y_0\} \cap \{x\ |\ x \in y_1 \land x \in y_2 \land x \in y_3 \land ...\} \newline
\bigcap z = y_0 \cap \{x\ |\ (x \in y_1) \land (x \in y_2 \land x \in y_3 \land ...)\} \newline
\bigcap z = y_0 \cap y_1 \cap \{x\ |\ x \in y_2 \land x \in y_3 \land ...\} \newline
\bigcap z = y_0 \cap y_1 \cap y_2 \cap \{x\ |\ \land x \in y_3 \land ...\} \newline
\bigcap z = y_0 \cap y_1 \cap y_2 \cap y_3 \cap ... \newline
\bigcap_{y \in z} y = y_0 \cap y_1 \cap y_2 \cap y_3 \cap ... \newline
$$

Intersection and Union:

$$
A \cap (B \cup C) = \{x\ |\ x \in A \land (x \in B \lor x \in C)\} \newline
A \cap (B \cup C) = \{x\ |\ (x \in A \land x \in B) \lor (x \in A \land x \in C)\} \newline
A \cap (B \cup C) = \{x\ |\ x \in A \land x \in B\} \cup \{x\ |\ x \in A \land x \in C\} \newline
A \cap (B \cup C) = (A \cap B) \cup (A \cap C) \newline
$$

for the sake of conversion between intersection and union declare:

$$
\mathbb{U}_{AB} = A \cup B
$$
and then proceed with our defintions/rules:

$$
A^{c} = \{x\ |\ x \notin A\}
$$

with $A^{c} \subset \mathbb{U}_{AB}$ implicitally, then:

$$
A \cup B = \{x\ |\ x \in A \lor x \in B\} \newline
A \cup B = \{x\ |\ \lnot [x \notin A \land x \notin B]\} \newline
A \cup B = \{x\ |\ x \notin A \land x \notin B\}^{c} \newline
A \cup B = [\{x\ |\ x \notin A\} \cap \{x\ |\ x \notin B\}]^{c} \newline
A \cup B = [A^{c} \cap B^{c}]^{c} \newline
$$

and also reverse:

$$
A \cap B = [A^{c} \cup B^{c}]^{c} \newline
$$

## Set-Difference

as allowed by the Axiom of Seperation, get have derived subsets, and set $\varphi(x)$ to $x \notin B$ to get the following operation.

$$A \setminus B = \{x\ |\ x \in A \land x \notin B \}$$

sometimes also written as:

$$A - B = A \setminus B$$

$$A \setminus B \subset A$$

