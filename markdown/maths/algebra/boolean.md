
# Boolean Algebra
**Boolean Algebra**: A Branch of Algebra where that works with Base 2 system

- `1` standing for **TRUE**, **ON**.
- `0` standing for **FALSE**, **OFF**.

## Logic

Main Logic:

- **Conjunction**, **AND** `(2 inputs)`: True if both inputs are True.
- **Disjunction**,  **OR** `(2 inputs)`: True if any of the inputs are True.
- **Negation**, **NOT** `(1 input)`: Inverts the given Input.
- **Exclusive OR**, **XOR** `(2 inputs)`: True if both inputs are not the same.

| $a$ | `NOT` $\lnot a$ |
| --- | --------------- |
| $0$ | $1$             |
| $1$ | $0$             |

| $a$ | $b$ | `AND` $a\land b$ | `OR` $a\lor b$ | `XOR` $a \oplus b$ |
| --- | --- | ---------------- | -------------- | ------------------- |
| $0$ | $0$ | $0$              | $0$            | $0$                 |
| $0$ | $1$ | $0$              | $1$            | $1$                 |
| $1$ | $0$ | $0$              | $1$            | $1$                 |
| $1$ | $1$ | $1$              | $1$            | $0$                 |

**Inverted Logic**:

- **NOT Conjunction**, **NAND** `(2 inputs)`: returns `1` if both inputs are NOT `1`.
- **NOT Disjunction**,  **NOR** `(2 inputs)`: returns `1` if any of the inputs are NOT `1`.
- **NOT Exclusive OR**, **XNOR** `(2 inputs)`: returns `1` if both inputs ARE the same.

| $a$ | $b$ | `NAND` $\lnot (a\land b)$ | `NOR` $\lnot (a\lor b)$ | `XNOR` $\lnot (a \oplus b)$ |
| --- | --- | ------------------------- | -------------- | ----------------------- |
| $0$ | $0$ | $1$                       | $1$            | $1$                     |
| $0$ | $1$ | $1$                       | $0$            | $0$                     |
| $1$ | $0$ | $1$                       | $0$            | $0$                     |
| $1$ | $1$ | $0$                       | $0$            | $1$                     |

**Totality of Logic**:

**Single Input**:
| $a$ | `BUFFER` | `NOT` |
| --- | -------- | ----- |
| $0$ | $0$      | $1$   |
| $1$ | $1$      | $0$   |

**Double Input**:
| $a$ | $b$ | `AND` | `OR` | `XOR` | `NAND` | `NOR` | `XNOR` |
| --- | --- | ----- | ---- | ----- | ------ | ----- | ------ |
| $0$ | $0$ | $0$   | $0$  | $0$   | $1$    | $1$   | $1$    |
| $0$ | $1$ | $0$   | $1$  | $1$   | $1$    | $0$   | $0$    |
| $1$ | $0$ | $0$   | $1$  | $1$   | $1$    | $0$   | $0$    |
| $1$ | $1$ | $1$   | $1$  | $0$   | $0$    | $0$   | $1$    |

## Latches

**SR Latch**: A Latch that can Hold upto 1 Bit of Data, with 2 Inputs and 2 Outputs

- $S$, $R$ Inputs
- $Q$, $\lnot Q$ Outputs
- $S$ Sets The Output $Q$ to 1, $\lnot Q$ to 0 
- $R$ Sets The Output $Q$ to 0, $\lnot Q$ to 1
- $\lnot Q$ is Invert of The Main Output $Q$
- value of $Q$ can be 0 or 1 depending on it's initial value
- $S$ and $R$ both 1 at the same is Invalid, as it's not supposed to happen and both Output $Q$ and $\lnot Q$ will be set to 0

Truth Table:

| $S$ | $R$ | $Q$    | $\lnot Q$   |
| --- | --- | ------ | ------ |
| $0$ | $0$ | $1, 0$ | $0, 1$ |
| $1$ | $0$ | $1$    | $0$    |
| $0$ | $1$ | $0$    | $1$    |
| $1$ | $1$ | $0$    | $0$    |

## Arithmetic

**Addition**: An Special Type of XOR Operation of Inputs, `a`, `b` and *Carry*

- $r = 1$, $c = 0$: IF any 1 is ON
- $r = 0$, $c = 1$: IF any 2 is ON
- $r = 1$, $c = 1$: IF all 3 is ON

| Carry | $a$ | $b$ | ($r$) result | Next Carry |
| ----- | --- | --- | ------------ | ---------- |
| $0$   | $0$ | $0$ | $0$          | $0$        |
| $0$   | $0$ | $1$ | $1$          | $0$        |
| $0$   | $1$ | $0$ | $1$          | $0$        |
| $0$   | $1$ | $1$ | $0$          | $1$        |
| $1$   | $0$ | $0$ | $1$          | $0$        |
| $1$   | $0$ | $1$ | $0$          | $1$        |
| $1$   | $1$ | $0$ | $0$          | $1$        |
| $1$   | $1$ | $1$ | $1$          | $1$        |

**Subtraction**: An Special Type of XOR Operation of Inputs, `a`, `-b` and *Carry*
- `Carry` acts as a Negative Value
- `0` Carry and `0` result if any 2 is `1`

| Carry | $a$ | $-b$ | ($r$) result | Next Carry |
| ----- | --- | ---- | ------------ | ---------- |
| $0$   | $0$ | $0$  | $0$          | $0$        |
| $0$   | $0$ | $1$  | $1$          | $1$        |
| $0$   | $1$ | $0$  | $1$          | $0$        |
| $0$   | $1$ | $1$  | $0$          | $0$        |
| $1$   | $0$ | $0$  | $1$          | $1$        |
| $1$   | $0$ | $1$  | $0$          | $1$        |
| $1$   | $1$ | $0$  | $0$          | $0$        |
| $1$   | $1$ | $1$  | $1$          | $1$        |

**Multiplication**: An `AND` Operation On Every Combination of Inputs `a` and `b`, there's no carry.

| $a$ | $b$ | $r$ |
| --- | --- | --- |
| $0$ | $0$ | $0$ |
| $0$ | $1$ | $0$ |
| $1$ | $0$ | $0$ |
| $1$ | $1$ | $1$ |

