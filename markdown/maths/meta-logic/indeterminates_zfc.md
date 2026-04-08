
$$
\newcommand{\setform}{\text{set}}
\newcommand{\null}{\mathtt{NULL}}
\newcommand{\bangle}[1]{\langle #1 \rangle}
$$

# Indeterminate Systems

All Previous usages of the $\mathbb{U}$ is to be replaced to $\mathbb{D}$ here.

Set $\mathbb{D}_{\text{zfc}}$ is the Universe that satisfies all the ZFC axioms and includes everything within context, because of the Replacement axiom we can't fully describe it as a set but $\mathbb{D}_{\text{zfc}} = V_{\alpha}$ will do.

$\mathbb{I}$ is defined as a set that satisfies the following Axioms:

> Note: These are modified as from the original article

- A1. **Axiom of Indeterminates**:

$$
\forall A [A \in \mathbb{D}_{\text{zfc}} \implies \exists I (I \in \mathbb{I} \land \setform(I) = A)]
$$

- A2. **Axiom of Instance-Equality**:

$$
\forall I_1, I_2 \in \mathbb{I}[I_1 = I_2 \iff x \leftarrow I_1 \land y \leftarrow I_2 \land x = y]
$$

- A3. **Axiom of Limit**:

$$\forall I [\setform(I) \setminus \mathbb{D}_{\text{zfc}} = \emptyset]$$

Some definitions/results:

$$\forall I \forall n [I^{\bangle{n}} \in \setform(I)]$$

$$\setform(x) = \{y | y \in \mathbb{D} \land y = x \}$$

$$I_1^{\bangle{n}} = I_2^{\bangle{n}}$$

$$y \leftarrow I \iff \exists x [x \in \setform(I) \land y = x] \land \setform(I) \neq \emptyset$$

$$\setform(\null) = \emptyset$$
