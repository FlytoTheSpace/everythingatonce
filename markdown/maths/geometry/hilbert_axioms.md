
# Hilbert's Geometry Axioms

# Primitives

$$\newcommand{\ray}{\text{Ray}}$$

**Primitive Objects**:

| Name  | Symbolic                      |
| ----- | ----------------------------- |
| Point | $A, B, C, D,E ...$            |
| Line  | $l, m, n, ...$                |
| Plane | $\rho, \sigma, \tau ...$      |


**Primitive Relations**:

- *Incidence*: $A \in l$, $l \in \rho$, $A \in \rho$
- *Betweenness*: $A * B * C$
- *Segment Congruence*: $\overline{AB} \cong \overline{CD}$
- *Angle Equality*: $\angle ABC = \angle XYZ$

# Axioms

## Axioms of Connection

$I_1$.

$$\forall A, B \exists l [A \neq B \implies \exist l (A \in l \land B \in l)]$$

$I_2$.

$$\forall l, A, B [(A \neq B \land A \in l \land B \in l) \implies AB = l]$$

$I_3$.

$$\forall A, B, C [(A \neq B \land A \neq C \land B \neq C) \implies \exist \rho (A \in \rho \land B \in \rho \land C \in \rho)]$$
$$\forall A, B, C [\lnot \exist l [A \in l \land B \in l \land C \in l]\implies \exist \rho (A \in \rho \land B \in \rho \land C \in \rho)]$$

$I_4$.

$$\forall \rho, A, B, C [A \in \rho \land B \in \rho \land C \in \rho \land \lnot \exist l (A \in l \land B \in l \land C \in l) \implies ABC = \rho]$$

$I_5$.

$$\forall A, B, \rho[]$$