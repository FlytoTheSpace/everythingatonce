
# Natural Numbers

## Peano Axioms

The Natural Numbers:

$\mathbb{N}$ and $s(n)$ must satisfy the following properties:

**A1**:
$$\exists 0[ 0 \in \mathbb{N}]$$
**A2**:
$$\forall n \in \mathbb{N} [s(n) \in \mathbb{N}]$$
**A3**:
$$\forall n, m \in \mathbb{N} [n = m \iff s(n) = s(m)]$$
**A4**:
$$\lnot \exists n \in \mathbb{N} [s(n) = 0]$$
**A5**: Induction.
$$
\forall A \subset \mathbb{N}[ 0 \in A \land \forall n \in A(s(n) \in A) \implies A = \mathbb{N}]
$$

---

**Definitions**:

$$
s(0) := 1 \newline
s(1) := 2 \newline
s(2) := 3 \newline
s(3) := 4 \newline
s(4) := 5 \newline
...
$$

**No Loop Proof**:

by A1:
$$0 \in \mathbb{N}$$
by A2:
$$s(0) \in \mathbb{N}$$
a definition:
$$s(0) := 1$$
if we assume:
$$1 = 0$$
then:
$$s(0) = 0$$
but by NA4
$$\lnot \exists n \in \mathbb{N} [s(n) = 0]$$
$$\therefore 1 \neq 0$$

## Theorems/Conjectures

**Conjecture 1.1**:

$$\forall n \in \mathbb{N}(s^{n}(0) = n)$$

- Proof:

we have a set $A$ here:

$$A = \{n\ |\ n \in \mathbb{N} \land s^{n}(0) = n\}$$

> syntactically $s^{n}(m)$ is another way of writing:
> $\underbrace{s(s(s(... s(m))))}_{n \text{ times}}$
a
and
$$
s^{0}(0) = 0 \newline
$$

so $0 \in A$

for any $n \in A$:
$$s^{n}(0) = n$$
then apply $s()$ to both sides:
$$
s(s^{n}(0)) = s(n) \newline
s^{s(n)}(0) = s(n) \newline
s^{s(n)}(0) = s(n) \newline
$$
abbreviate $s(n) = m$:
$$s^{m}(0) = m$$
so $s(n) \in \mathbb{N}$, 
from A5, the Axiom of Induction:
$$\therefore A = \mathbb{N}$$
in other words:
$$\forall n \in \mathbb{N}(s^{n}(0) = n) \newline$$

> Note: Use of the Set $A$ here does not persist in-between proofs, it's a buffer object.

the function $s^{0}(n)$ is by definition another equal to $n$
so:

$$\forall n \in \mathbb{N}[s^{0}(n)] = n$$

---

**Conjecture 1.2**:

$$\forall n, m \in \mathbb{N}[s^{m}(n) = s^{n}(m)]$$

- Proof:

we have another set $A$:

$$A = \{s^{m}(n)\ |\ n, m \in \mathbb{N} \land s^{m}(n) = s^{n}(m)\}$$

$$s^{0}(0) = s^{0}(0) = 0$$

implies $0 \in A$.

for any $m, n \in A$:

$$
s^{m}(n) = s^{n}(m) \newline
s(s^{m}(n)) = s(s^{n}(m)) \newline
s^{s(m)}(n) = s^{n}(s(m)) \newline
$$

abbreviate $s(m) = a$ then:

$$s^{a}(n) = s^{n}(a) \newline$$

we have:

$$s(s^{m}(n)) \in A$$

also proveable with $n$ instead:

$$
s^{m}(n) = s^{n}(m) \newline
s(s^{m}(n)) = s(s^{n}(m)) \newline
s^{m}(s(n)) = s^{s(n)}(m) \newline
$$

abbrevite $s(n) = b$:

$$s^{m}(b) = s^{b}(m)$$

we again have:

$$s(s^{m}(n)) \in A$$

for any $n, m$.

so by A5:

$$\therefore A = \mathbb{N}$$

in other words:

$$
\forall n,m \in \mathbb{N}[s^{m}(n) = s^{n}(m)]
$$

## Addition

**Addition Axioms**:

**AA1**:

$$\forall a \in \mathbb{N}[a + 0 = a]$$

**AA2**:

$$\forall a, b \in \mathbb{N}[s(a + b) = a + s(b)]$$

---

**Conjecture 2.1**:

$$\forall a, b \in \mathbb{N} [s^{b}(a) = a + s^{b}(0)]$$

we have a set $A$:

$$A = \{s^{b}(a)\ |\ a, b \in \mathbb{N} \land s^{b}(a) = a + s^{b}(0)\}$$

and
$$
s^{0}(0) = 0 + s^{0}(0) \newline
0 = 0 + 0 \newline
0 = 0 \newline
$$

so we have $0 \in A$. for any element $s^{b}(a)$ in $A$ we have:
- with $b$:
$$
s^{b}(a) = a + s^{b}(0) \newline
s(s^{b}(a)) = s(a + s^{b}(0)) \newline
s^{s(b)}(a) = a + s(s^{b}(0)) \newline
s^{s(b)}(a) = a + s^{s(b)}(0) \newline
$$

abbreviate $s(b) = n$:

$$s^{n}(a) = a + s^{n}(0)$$

so:

$$s(s^{b}(a)) \in A$$

hence:

$$\therefore A = \mathbb{N}$$

in other words:

$$\forall a, b \in \mathbb{N}[s^{b}(a) = a + s^{b}(0)]$$

- with $a$ is not proveable yet commutativity of addition also not being proved yet.

---

**Theorem 2.2**: Additive Closure


from our earlier results: $\forall a, b \in \mathbb{N}$

$$s^{b}(0) = b$$

$$s^{b}(a) = a + s^{b}(0) \newline$$

$$s^{b}(a) = a + b$$

$$s^{b}(a) \in \mathbb{N}$$

$$\therefore \forall a, b \in \mathbb{N}[a + b \in \mathbb{N}]$$

---

**Theorem 2.3**: Additive Commutativity
since:

$$s^{b}(a) = a + b$$

$$s^{a}(b) = b + a$$

$$s^{b}(a) = s^{a}(b)$$

so we have using the law of transitivity, we have:

$$a + b = b + a$$

we have proved Commutativity for addition:

$$\therefore a + b = b + a$$

---

**Theorem 2.4**: Additive Associativity
$$\forall a, b, c \in \mathbb{N}$$
$$
(a + b) + c \newline
= (a + b) + s^{c}(0) \newline
= s^{c}((a + b) + 0) \newline
= s^{c}(a + b) \newline
= a + s^{c}(b) \newline
= a + s^{c}(b + 0) \newline
= a + (b + s^{c}(0)) \newline
= a + (b + c) \newline
$$

$$\therefore (a + b) + c = a + (b + c)$$

## Multiplication

**Axioms for Multiplication:**

**MA1**:

$$\forall a \in \mathbb{N}[a \times 1 = a]$$

**MA2**:

$$\forall a, b, c \in \mathbb{N}[a \times (b + c) = (a \times b) + (a \times c)]$$

> ORDER OF OPERATION (Syntactical):
> 1. Multiplication.
> 2. Addition.
> 

---

**Theorem 3.1**: Multiplication by Zero is Zero

by MA2:

$$a \times (b + c) = (a \times b) + (a \times c)$$
$$a \times (b + 0) = (a \times b) + (a \times 0)$$
$$(a \times b) = (a \times b) + (a \times 0)$$

by what we know, the only way this equation holds if:

$$a \times 0 = 0$$

(can be proven in a better way once subtration is acquired.)

--

**Conjecture 3.1**:

$$a \times (b + c + d + e + ... + as) = ab + ac + ad + ae + ... + as$$

proof:

$$
a \times (b + c + d + e + ... + s) \newline
= a \times (b + (c + d + e + ... + s)) \newline
= (a \times b) + a \times (c + d + e + ... + s) \newline
= (a \times b) + a \times (c + (d + e + ... + s)) \newline
= (a \times b) + (a \times c) + a \times (d + e + ... + s) \newline
= ab + ac + a(d + e + ... + s) \newline
= ab + ac + a(d + (e + ... + s)) \newline
= ab + ac + ad + a(e + ... + s) \newline
= ab + ac + ad + a(e + (... + s)) \newline
= ab + ac + ad + ae + a(... + s) \newline
= ab + ac + ad + ae + a(... + (s)) \newline
= ab + ac + ad + ae + ... + as \newline
$$

$$a(b + c + d + e + ... + as) \therefore a \times (b + c + d + e + ... + s)$$

---

**Theorem 3.2**: Multiplicative Closure

$$
a \times b \newline
= a \times (s^{b}(0)) \newline
= a \times (\underbrace{1 + 1 + 1 + ...}_{b}) \newline
= \underbrace{(a \times 1) + (a \times 1) + (a \times 1) + ...}_{b} \newline
= \underbrace{a + a + a + ...}_{b} \newline
$$

$$
a + a \in \mathbb{N} \newline
(a + a) + a \in \mathbb{N} \newline
((a + a) + a) + a \in \mathbb{N} \newline
... \newline
\underbrace{((((a + a) + a) + a) + ...)}_{b} \in \mathbb{N} \newline
\underbrace{a + a + a + a + ...}_{b} \in \mathbb{N} \newline
a \times b \in \mathbb{N} \newline
$$

$$\therefore \forall a, b \in \mathbb{N}[a \times b \in \mathbb{N}]$$

---

**Theorem 3.3**: Multiplicative Associativity

$$
(a \times b) \times c \newline
= (a \times b) \times \underbrace{(1 + 1 + 1 + ...)}_{c} \newline
= \underbrace{((a \times b) + (a \times b) + (a \times b) + ...)}_{c} \newline
= a \times \underbrace{(b + b + b + ...)}_{c} \newline
= a \times (b \times \underbrace{(1 + 1 + 1 + ...)})_{c} \newline
= a \times (b \times c) \newline
$$

---

**Theorem 3.4**: Multiplicative Commutativity

$$
a \times b \newline
= a \times (s^{b}(0)) \newline
= a \times (\underbrace{1 + 1 + 1 + ...}_{b}) \newline
= \underbrace{(a \times 1) + (a \times 1) + (a \times 1) + ...}_{b} \newline
= \underbrace{a + a + a + ...}_{b} \newline
= \underbrace{s^{a}(0) + s^{a}(0) + s^{a}(0) + ...}_{b}
$$

$$
= b \underbrace{\begin{cases}
(1  +  1  +  1  + 1 + ...) + \cr
(1  +  1  +  1  + 1 + ...) + \cr
(1  +  1  +  1  + 1 + ...) + \cr
(1  +  1  +  1  + 1 + ...) + \cr
(1  +  1  +  1  + 1 + ...) + \cr
\end{cases}}_{a}
$$

$$
= b \underbrace{\begin{cases}
1  +  1  +  1  + 1 + ... + \cr
1  +  1  +  1  + 1 + ... + \cr
1  +  1  +  1  + 1 + ... + \cr
1  +  1  +  1  + 1 + ... + \cr
1  +  1  +  1  + 1 + ... + \cr
\end{cases}}_{a}
$$

switch the columns and rows
> (mostly syntactical, by `switch` it means to regoup via associativity in a certain way):

$$
= a \underbrace{\begin{cases}
1  +  1  +  1  + 1 + 1 + ... \cr
1  +  1  +  1  + 1 + 1 + ... \cr
1  +  1  +  1  + 1 + 1 + ... \cr
1  +  1  +  1  + 1 + 1 + ... \cr
\end{cases}}_{b}
$$

$$
= a \underbrace{\begin{cases}
(1  +  1  +  1  + 1 + 1 + ...) + \cr
(1  +  1  +  1  + 1 + 1 + ...) + \cr
(1  +  1  +  1  + 1 + 1 + ...) + \cr
(1  +  1  +  1  + 1 + 1 + ...) + \cr
\end{cases}}_{b}
$$

$$
= a \begin{cases}
(b) + \cr
(b) + \cr
(b) + \cr
(b) + \cr
\end{cases}
$$

$$
= a \begin{cases}
b + \cr
b + \cr
b + \cr
b + \cr
\end{cases}
$$

$$
= \underbrace{b + b + b + b +...}_{a} \newline
= \underbrace{(b \times 1) + (b \times 1) + (b \times 1) + (b \times 1) +...}_{a} \newline
= b \times \underbrace{(1 + 1 + 1 + 1 + ...)}_{a} \newline
= b \times \underbrace{(1 + 1 + 1 + 1 + ...)}_{a} \newline
= b \times (s^{a}(0)) \newline
= b \times (a) \newline
= b \times a \newline
$$

$$\therefore a \times b = b \times a$$

## Comparison

The Definitions for Comparison.

$\forall a, b \in \mathbb{N}$:

$$a < b \iff \exists k \in \mathbb{N}_{>0} [a + k = b]$$

$$a > b \iff \exists k \in \mathbb{N}_{>0} [a = b + k]$$
 
$$a \leq b \iff \exists k \in \mathbb{N} [a + k = b]$$

$$a \geq b \iff \exists k \in \mathbb{N} [a = b + k]$$

---

$$a < b \iff \exists k \in \mathbb{N}_{>0} [a + k = b]$$
$$
\exists k \in \mathbb{N}_{>0} [a + k = b] \newline
\exists k \in \mathbb{N}_{>0} [b = a + k] \newline
b > a \iff \exists k \in \mathbb{N}_{>0} [b = a + k] \newline
$$
$$\therefore a < b \iff b > a$$

---

**Theorem 4.1**: Trichotomy Law

$$\forall a, b \in \mathbb{N}[a < b \oplus a = b \oplus a > b]$$

given $a < b$ then:

$$
a + k = b \land k \neq 0\newline
\therefore \lnot (a = b)
$$
and
$$
a + k = b \land k \neq 0 \newline
a + k + (-k)= b+ (-k) \newline
a = b + (-k) \newline
$$
$$
-k \notin \mathbb{N}_{>0} \newline
\therefore \lnot (a > b)
$$

given $a = b$ then:

$$
a = b \newline
a + k = b \land k = 0 \newline
k \notin \mathbb{N}_{>0} \newline
\therefore \lnot (a < b)
$$

and

$$
a = b \newline
a = b + k \land k = 0 \newline
k \notin \mathbb{N}_{>0} \newline
\therefore \lnot (a < b)
$$

given $a > b$ then:

$$
a = b + k \land k \neq 0\newline
\therefore \lnot (a = b)
$$
and
$$
a = b + k \land k \neq 0 \newline
a + (-k) = b + k + (-k) \newline
a + (-k) = b \newline
$$
$$
-k \notin \mathbb{N}_{>0} \newline
\therefore \lnot (a < b)
$$

---

**Theorem 4.2**: Transitivity

$$a < b \iff a + k_1 = b$$
$$b < c \iff b + k_2 = c$$

$$a + k_1 = b \newline$$
$$a + k_1  + k_2 = b + k_2 \newline$$
$$a + k_1  + k_2 = c \newline$$
$$a + (k_1  + k_2) = c \newline$$

$$\therefore a < c$$

----

**Theorem 4.3**:

$$a < b \iff a + k = b$$

$$a + k = b$$
$$a + c + k = b + c$$
$$(a + c) + k = (b + c)$$
$$(a + c) < (b + c)$$

---

**Theorem 4.4**:

given:
$$a < b \iff a + k = b \newline$$

then:

$$
(a + k) \times c = b \times c \newline
(a \times c) + (k \times c) = (b \times c) \newline
$$
$$(k \times c) = 0 \iff c = 0$$
$$
(a \times c) + (k \times c) = (b \times c) \newline
$$
long as $c \in \mathbb{N}_{>0}$:
$$a \times c < b \times c $$

---

in summary:

$$\mathbb{N} = \{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...\}$$

$\forall a, b, c \in \mathbb{N}$ :

$$s^{a}(0) = a$$

$$s^{b}(a) = s^{a}(b)$$

$$a + b = s^{b}(a)$$

$$a + b \in \mathbb{N}$$

$$(a + b) + c = a + (b + c)$$

$$a + b = b + a$$

$$a + 0 = a$$

$$a \times b = \underbrace{(a + a + a + ...)}_{b}$$

$$a \times b \in \mathbb{N}$$

$$a \times b = b \times a$$

$$(a \times b) \times c = a \times (b \times c)$$

$$a \times 1 = a$$

$$a \times 0 = 0$$

$$a \times (b + c) = (a \times b) + (a \times c)$$

$$a < b \iff b > a$$

$$a < b \oplus a = b \oplus a > b$$

$$a < b \land b < c \implies a < c$$

$$a < b \implies a + c < b + c$$

$$a < b \implies a \times c < b \times c$$

long as $c \in \mathbb{N}_{>0}$

Notation:

$$\mathbb{N}_m = \{n\ |\ n \in \mathbb{N} \land n < m\}$$

$$\mathbb{N}_{> m} = \{n\ |\ n \in \mathbb{N} \land n > m\}$$
