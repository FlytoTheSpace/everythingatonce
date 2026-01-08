
# Groups


## Axioms
A Group $G$ is a Set of objects equipped with a binary operation ($\circ$) that satisfy the following axioms:

$\forall a, b, c \in G$

(minimalist variant)

- A1. **Closure**:

$$a \circ b \in G$$

- A2. **Associativity**:

$$(a \circ b) \circ c = a \circ (b \circ c)$$

- A3. **Neutral/Identity**:

$$\exists e \in G (a \circ e = a)$$

- A4. **Inverse**:

$$\exists a^{-1} (a \circ a^{-1} = e)$$

Redudant variant (common):

- A1. **Closure**:

$$a \circ b \in G$$

- A2. **Associativity**:

$$(a \circ b) \circ c = a \circ (b \circ c)$$

- A3. **Neutral/Identity**:

$$\exists e \in G (a \circ e = e \circ a = a)$$

- A4. **Inverse**:

$$\exists a^{-1} (a \circ a^{-1} = a^{-1} \circ a = e)$$

## Proof of Redundant Axioms

Proof of the Redundant Axioms via the Minimalist axioms.

- P3: $e \circ a = a \circ e = a$

Proof:
> self-equivalence:
$$a \circ a^{-1} \circ a = a \circ a^{-1} \circ a$$
> A2:
$$(a \circ a^{-1}) \circ a = a \circ (a^{-1} \circ a)$$
> by A4 and P4:
$$e \circ a = a \circ e$$
> by A3 we get:
$$e \circ a = a \circ e = a$$

$$\therefore e \circ a = a \circ e = a$$

- P4: $a \circ a^{-1} = a^{-1} \circ a = e$

Proof:

> self-equality:
$$a \circ a^{-1} \circ (a^{-1})^{-1} = a \circ a^{-1} \circ (a^{-1})^{-1} \newline$$
> by A2, The Axiom of associativity.:
$$a \circ a^{-1} \circ (a^{-1})^{-1} = a \circ (a^{-1} \circ (a^{-1})^{-1}) \newline$$
> by A4, The Axiom of inverse:
$$a \circ a^{-1} \circ (a^{-1})^{-1} = a \circ e \newline$$
> by A3, The Axiom of Neutral
$$a \circ a^{-1} \circ (a^{-1})^{-1} = a \newline$$
> by A2:
$$(a \circ a^{-1}) \circ (a^{-1})^{-1} = a \newline$$
> by A4:
$$e \circ (a^{-1})^{-1} = a \newline$$
> Applying $a^{-1}$ to both sides on the left.:
$$a^{-1} \circ e \circ (a^{-1})^{-1} = a^{-1} \circ  a \newline$$
> A3:
$$a^{-1} \circ (a^{-1})^{-1} = a^{-1} \circ a \newline$$
> A4:
$$e = a^{-1} \circ a \newline$$

$\therefore a^{-1} \circ a = e$

## Definitions

To state that a Set is Group under some operation $\circ$ then:

$$
(G, \circ)
$$

**Sub-Group**: $H$ is a subgroup of $G$ if:

$$(H, \circ) \land (G, \circ) \land H \subset G$$


### Homomorphism

$\varphi$ is a Homomorphism if:

$$\forall (a \in G) \exists (y \in H)[\varphi(a) = y]$$


## Theorems

- T1. **Theorem**: Inverse of the Inverse is the original:

$$(a^{-1})^{-1} = a$$

Proof:

$$a^{-1} \circ (a^{-1})^{-1} = a^{-1} \circ (a^{-1})^{-1}$$
> by A4:
$$a^{-1} \circ (a^{-1})^{-1} = e$$
$$a \circ a^{-1} \circ (a^{-1})^{-1} = a \circ e$$
> by A3:
$$a \circ a^{-1} \circ (a^{-1})^{-1} = a$$
> by A2:
$$(a \circ a^{-1}) \circ (a^{-1})^{-1} = a$$
> by A4:
$$e \circ (a^{-1})^{-1} = a$$
> by P3
$$(a^{-1})^{-1} = a$$

$$\therefore (a^{-1})^{-1} = a$$

- T2. **Laws of Repeated Operations**:

$$
\underbrace{a \circ a \circ a \circ a \circ ...}_{n \text{ times}} = a^{n}
$$
for $n, m \in \mathbb{Z}$
$$
a^{n} \circ a^{m} = a^{n + m}
$$
$$
(a^{n})^{m} = a^{n \times m}
$$
with:
$$a^{0} := e$$

$+, \times$ denote Addition and Multiplication Respectively.

- T3. Any Finite Group's elements loop back to the Neutral element to some number $n$

$$a \in G \land |G| \in \mathbb{N} \implies \exists n [a^{n} = e]$$

## Some Groups:

**Cyclic**:
$$\mathbb{Z}_m = \{ n \mod m | n \in \mathbb{z} \}$$
