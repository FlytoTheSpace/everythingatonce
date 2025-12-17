# Probability

**Probability**: The likeliness of an event occuring given a set of Possibilities $U$, all outcomes are assumed to be equally likely.


Probability of an event is defined as a function of $P$, which returns a Real number in the range 0 to 1

$$
P(A) = \frac{|A|}{|\mathbb{U}|}
$$
$A \in \mathbb{U}$

- $\text{Possibilites}$ is the total acount of possible outcomes

**Terminology**:
- **Event**: $A \subseteq U$
- **Experiment**: An action/process that results in a set of possible outcomes
- **Outcome**: The Possible outcome of an event, $a \in \mathbb{U}$
- **Sample Space**, $\mathbb{U}$: The set of all possible outcomes of an event
- **Impossible**: when $|A|$ = 0
    $$P(A) = 0$$
- **Certain**: when $|A| = 1$
    $$P(A) = 1$$
- **Mutually Exclusive Events**: $A \cap B = \emptyset$
- **Independent Events**: If outcome of 1 event doesn't effect the other event
- **Complementary**: $A^{c} =\mathbb{U} \setminus A $

**Notation**

- $P(A)$: event $A$ probability
- $S$: Sample Space
- $A^c$: Complement
- $A \cup B$: **Union**, event $A$ **OR** $B$
- $A \cap B$: **Intersection**, event $A$ **AND** $B$
- $P(A | B)$: **Conditional Probability**, likelihood of the event A occuring given that 

> it is assumed that all the possible outcomes from the Sample Set are equally likely to occur

**Complementary Event**:

$$
P(A^c) = 1 - P(A)
$$

**Addition Rule**:


$$
P(A \cup B) = P(A) + P(B) - P(A \cap B)
$$

**Multiplicative Rule**:

- $A$ and $B$ are Independent 

    $$
    P(A \cap B) = P(A) \cdot P(B)
    $$


**Conditional Probability**: The Probability of the event $A$ and $B$ Happening relative to the Event Probability of $B$

$$
P(A | B) = \frac{P(A \cap B)}{P(B)}
$$

- $P(A \cap B)$: The likehood of the event both $A$ ***AND*** $B$ happening
- $\div P(B)$: Shifts the Perspective from the Sample Set view, to the Event $B$ Perspective.

The Conditional Probability can also be interpreted as The Amount of area occupied by Intersection of A and B, it's ratio with B