

# Zermelo-Fraenkel Set Theory Axioms


- **Axiom of Extentionality**:

$$
\forall y \forall z [\forall x ((x \in y) \iff (x \in z)) \implies y = z]
$$

- **Axiom of Regularity/Foundation**:

$$
\forall x (x \neq \emptyset \implies \exists y ((y \in x) \land (y \cap x = \emptyset)))
$$

it works alongside axiom of pairing and union.

- **Axiom Schema of Specification/Seperation/Restricted Comprehension**:

$$
\forall y \exists z \forall x[(x \in z) \iff (x \in y \land \varphi(x, y))]
$$

- **Axiom of Pairing**:

$$
\forall x \forall y \exists A \forall z[z \in A \iff (z = x \lor z = y)]
$$

- **Axiom of Union**:

$$
\forall z \exists A \forall y \forall x [(x \in y \land y \in z) \iff x \in A]
$$

- **Axiom Schema of Replacement**:

$$
\forall A [\forall x (x \in A \implies \exists! y\ \phi(x, y, A)) \implies \exists B \forall y(y \in B \iff \exists x(x \in A \land \phi(x, y, A)))]
$$

- **Axiom of Infinity**:

$$\exists x [\emptyset \in x \forall y(y \in x \implies y \cup \{y\} \in x)]$$

- **Axiom of Power Set**:

$$\forall x \exists z \forall y [y \subset x \iff y \in z]$$

a derived definition:

$$\mathcal{P}(x) = \{y\ |\ y \subset x\}$$

- **Axiom of Choice**:

(left out for now due to it's formal complexity)

