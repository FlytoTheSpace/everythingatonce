
# Set Theory

The Foundational Theory for all of Mathematics all centered the idea of a Set


## Set Theory Axioms
by Zermelo-Fraenkel


- **Axiom of Extentionality**:

$$
\forall y \forall z [\forall x ((x \in y) \iff (x \in z)) \implies y = z]
$$

- **Axiom of Regularity/Foundation**:

$$
\forall x (x \neq \emptyset \implies \exists y ((y \in x) \land (y \cap x = \emptyset)))
$$

- **Axiom Schema of Specification/Seperation/Restricted Comprehension**:

$$
\forall z \forall x \exists y[x \in y \iff (x \in z \land \varphi(x))]
$$

- **Axiom of Pairing**:

$$
\forall x \forall y \exists z ( x \in y \land x \in z)
$$

- **Axiom of Union**:

$$
\forall z \forall y \exists A \forall x [(x \in y \land y \in z) \implies x \in A]
$$

- **Axiom Schema of Replacement**

$$
\forall y\exists z \forall x [ (x \in y \land \varphi(x)) \implies x \in z ]
$$