

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
A \cup \underbrace{(B \cup C)}_{Y} = \{x | x \in A \lor x \in Y\} \newline
\underbrace{(A \cup B)}_{X} \cup C = \{x | x \in X \lor x \in C\} \newline
(A \cup B) \cup C = \{x | (x \in A \lor x \in B) \lor x \in C\} \newline
(A \cup B) \cup C = \{x | x \in A \lor x \in B \lor x \in C\} \newline
(A \cup B) \cup C = \{x | x \in A \lor ( x \in B \lor x \in C)\} \newline
(A \cup B) \cup C = \{x | x \in A \lor x \in Y\} \newline
(A \cup B) \cup C = A \cup \underbrace{(B \cup C)}_{Y} \newline
(A \cup B) \cup C = A \cup (B \cup C) \newline
$$


