
# Elementary Number Theory

All Numbers used within this are Integer. i.e

$$a, b, c, d, ... \in \mathbb{Z}$$

# Divisiblity

$$a \mid b \implies \exists k (b = a \cdot b)$$


### Divisibility Properites:

$$a \mid 0$$

$$0 \mid a \implies n = 0$$

$$1 \mid a$$

$$a \mid a$$

$$a \mid 1 \implies a = \pm 1$$

$$a \mid b \land b \mid c \implies a \mid c$$

$$a \mid b = ac \mid bc, c\in \mathbb{Q}$$

$$c \mid a \land c \mid b \implies c \mid am + bn, \forall m, n $$

$$a \mid b \implies |a| \leq |b|$$

**Even Numbers**:
a is even if:
$$
2 \mid a
$$
**Odd Numbers**
a is odd if:
$$
2 \nmid a
$$

**Negative Divisibility**:

if
then:

$$
a \mid b \implies \newline
- a \mid b \land  \newline
a \mid - b \land  \newline
a \mid |b| \newline
$$

### Divisibility Rules:

| Number | Rule                                          |
| ------ | --------------------------------------------- |
| $1$    | Always                                        |
| $2$    | If Even                                       |
| $3$    | Sum of All digits is Multiple of 3            |
| $4$    | with 3+ digits, last 2 digits divisible by it |
| $5$    | `0` or `5` in one's place                     |
| $6$    | Divisible by both 2 and 3                     |
| $8$    | with 4+ digits, last 3 digits divisible by it |
| $9$    | sum of all digits divisible by it             |
| $10$   | `0` in one's place                            |
| $11$   | -                                             |


# Prime Numbers

The Prime Numbers are Defined as follows:

$\mathbb{P} = \{n | n \in \mathbb{Z}, n > 1, \forall f [ 1 < f < n \land f \nmid n ]\}$

**Composite Numbers**: 
a number $n$ is composite $\iff \exists a, b [1 < a, b < n \land n \mid a, b]$


every positive number greater than 1 has a prime divisor.
$$
\forall (n > 1) \exists (p \in \mathbb{P}) [p \mid n]
$$

Proof:

define $S$
$$S := \{n | n > 1, \lnot \exists p \in \mathbb{P}[ p \mid n ]\}$$
if it's non-empty, then by Well-Ordering a smallest must $\exists m[m = \min(S)]$

$$m \notin \mathbb{P}$$

as all primes $p \mid p$, so $m$ must be composite, so there must $\exists a [a \mid m]$

$$1 < a < m$$

so $a < m \land m = \min(S) \therefore a \notin S$, meaning $a$ must have a factor of some $p$

$$p \mid a \land a \mid m$$

$$\therefore p \mid m $$

this contradicts the definition of $S$



