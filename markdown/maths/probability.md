## Probability

**Probability**: The likeliness of an event occuring given a set of Possibilities


Probability of an event is defined as a function of $P$, which returns a Real number in the range 0 to 1

$$
P(A) = \frac{\text{Favorable}}{\text{Possibilities}}
$$

- $A$ is the Event
- $\text{Favorable}$ is the amount of possibilites favors the event of $A$
- $\text{Possibilites}$ is the total acount of possible outcomes
- **Impossible**: if the outcome of the probability of an event is $0$, then it's not possible
    $$P(A) = 0$$
- **Certain**: if the outcome of the probability of an event is $1$, then it ***must*** happen
    $$P(A) = 1$$

**Terms**:

- **Experiment**: An action/process that results in a set of possible outcomes
- **Outcome**: The Possible outcome of an event
- **Sample Space**, $S$: The set of all possible outcomes of an event

    $S = \{ ...\}$

- **Event**: Subset of the sample space

    $A \subseteq S$

- **Mutually Exclusive Events**: If 2 events can't occur at the same time
- **Independent Events**: If outcome of 1 event doesn't effect the other event
- **Complementary**: All of the outcomes that are not in the Event $A$, notation:
    
    $A^c$


**Notation**

- $P(A)$: event $A$ probability
- $S$: Sample Space
- $A^c$: Complement
- $A \cup B$: **Union**, event $A$ **OR** $B$
- $A \cap B$: **Intersection**, event $A$ **AND** $B$
- $P(A | B)$: **Conditional Probability**, likelihood of the event A occuring given that 

> it is assumed that all the possible outcomes from the Sample Set are equally likely to occur

**Complementary Events**:

$$
P(A^c) = 1 - P(A)
$$

**Addition Rule**:

- Mutually Exclusive:

    $$
    P(A \cup B) = P(A) + P(B)
    $$

- Not Mutually Exclusive

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