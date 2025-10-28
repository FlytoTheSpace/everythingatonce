17/10/2025 <- Date of Knowledge Acquiry

28/10/2025 <- Date of Writing this

# Part 1 The Contradiction:

**The Axiom of Regularity** states that:
$$
\forall x (x \neq \emptyset \implies \exists y ((y \in x) \land (y \cap x = \emptyset)))
$$
which is intented to eliminate the self-reference paradoxes.
however this mathematical formulation felt "hollow" so i contructed a new set:

$x = \{y, z\}$ `(axiom of pairing)`

$y = \{3, 4\}$ `(axiom of pairing)`

$z \neq 3, 4$ `(defined as to be)`


$$x \neq \emptyset \text{ ✅ it contains y and z}$$

> $\exists y \Gamma$ <- this expression guarantees existence of atleast 1 match so we can stop after getting a single match.

if we pick the first element $y$ of the set $x$ it should satisfy the axiom:

$$y \in x \text{ ✅ it contains y}$$
$$\{3, 4\} \in \{y, z\} = \emptyset \text{ ✅ as they don't have any common elements}$$

so the set $x = \{\{3, 4\}, z\}$ should satify the axiom of regularity as long as $z \neq 3, 4$ so $z$ is a free element here, we can define it to be whatever we want it as long the above statement is satisfied.

now as for the twist we define $z = x$, so the set

$$x = \{\{3, 4\}, x\}$$

should satisfy the axiom of regularity which kills the whole point of the axiom.

# Part 2: The Resolvement

(the above definition still apply here)

define a new set 

$s = \{x\}$ `(axiom of pairing)`

the only mattering part of the axiom of regularity is this part:
$$y \cap x = \emptyset$$

now if we apply it to our set $s$

$$x \cap s = \emptyset$$
$$\{\{3, 4\}, x\} \cap s = \emptyset$$
$$\{\{3, 4\}, x\} \cap \{x\} = \emptyset$$
$$\{x\} \cap \{x\} = \emptyset$$
$$\{x\} \color{red}\ \neq \color{white} \emptyset$$

so the only possible conclusion is that it **DOES** violate the axiom of regularity putting it all end.
