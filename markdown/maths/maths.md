
- [Back to Home](../../README.md)

Sections:

[Other](#Other)
- [Symbols](#symbols)
- [Constants](#constants)

Pure Mathematics

- [Arithmetic](./arithmetic.md)
- [Algebra](./algebra/algebra.md)
- [Linear Algebra](./linear_algebra.md)
- [Geometry](./geometry.md)
- [Trigonometry](./trigonometry.md)
- [Number Theory](./number_theory/number_theory.md)
- [Calculus](./calculus/calculus.md)
- [Differential Equations](./differential_equations.md)
- [Combinatorics](./combinatorics.md)
- [Topology](./topology.md)
- [Logic](./logic.md)

Applied Mathematics

- [Financial Mathematics](./financial_mathematics.md)
- [Turing Machine](./turing_machine.md)
- [Information Theory](./information_theory.md)
- [Statistics](./statistics.md)
- [Game Theory](./game_theory.md)

Extra

- [Papers](./papers/)
- [Meta-Mathematics](./meta-mathematics/)


# General Mathematics Overview 

## Symbols

| Symbol                                  | Name                          | Syntax/Example                    |
| --------------------------------------- | ----------------------------- | --------------------------------- |
**Arithmetic**
| $+$                                     | **Addition, Positive**        | $a + b$ <br> $+ a$                |
| $-$                                     | **Subtraction, Negative**     | $a - b$ <br> $- a$                |
| $\times$ <br> $\ast$ <br> $\cdot$       | **Multiplication**            | $a \times b$ <br> $a \ast b$ <br> $a \cdot b$ <br> $ab$ |
| $\div$ <br> $:$ <br> $\frac{a}{b}$      | **Division**                  | $a \div b$ <br> $a : b$ <br> $\frac{a}{b}$ |
| $\sqrt{}$                               | **Radical** (Root)            | $\sqrt{a}$ <br> $\sqrt[n]{a}$     |
| $\mod{}$                                | **Remainder, Modulo**         | $a \mod b$                        |
| $\%$                                    | **Percent**                   | $a\%$                             |
| $!$                                     | **Factorial**                 | $a!$                              |
| $\pm$                                   | **Plus-Minus**                | $a \pm b$                         |
| $\mp$                                   | **Minus-Plus**                | $a \mp b$                         |
**Equality**
| $=$                                     | **Equal**                     | $a = b$                           |
| $\neq$                                  | **Not Equal**                 | $a \neq b$                        |
| $\approx$                               | **Approximately Equal**       | $a \approx b$                     |
| $\colonequals$                          | **Definition**                | $a \colonequals b$                |
| $\equiv$                                | **Equivalent**                | $a \equiv b$                      |
| $\cong$                                 | **Congruence**                | $a \cong b$                       |
**Comparison**
| $<$                                     | **Less Than**                 | $a < b$                           |
| $>$                                     | **Greater Than**              | $a > b$                           |
| $\leq$                                  | **Less Than or Equal**     | $a \leq b$                        |
| $\geq$                                  | **Greater Than or Equal**     | $a \geq b$                        |
| $\ll$                                   | **Much Less**                 | $a \ll b$                         |
| $\gg$                                   | **Much Greater**              | $a \gg b$                         |
| $\propto$                               | **Proportion**                | $a\propto b$                      |
| $\sim$                                  | **Similar**                   | $A \sim B$                        |
| $\simeq$                                | **Similar or Equal**          | $A \simeq B$                      |
| $\prec$                                 | **Precede**                   | $a \prec b$                       |
| $\preceq$                               | **Precede or Equal**          | $a \preceq b$                     |
| $\succ$                                 | **Succede**                   | $a \succ b$                       |
| $\succeq$                               | **Succede or Equal**          | $a \succeq b$                     |
**Geometry**
| $\deg$ <br> $\degree$                   | **Degrees**                   | $x \deg$ <br> $x \degree$         |
| $\angle$                                | **Angle**                     | $\angle ABC$                      |
| $\overrightarrow{\ \ }$                 | **Arrow**, **Ray**            | $\overrightarrow{AB}$             |
| $\overline{\ \ }$                       | **Line**                      | $\overline{AB}$                   |
| $\parallel$                             | **Parallel**                  | $AB \parallel CD$                 |
| $\nparallel$                            | **Not Parallel**              | $AB \nparallel CD$                |
| $\perp$                                 | **Perpendicularity, Coprime** | $AB \perp CD$<br> $a \perp b$     |
| $\overleftrightarrow{\ \ }$             | **Bidirectional Arrow**       | $\overleftrightarrow{AB}$         |
| $\triangle$                             | **Triangle**                  | $\triangle ABC$                   |
| $\square$                               | **Square**                    | $\square ABCD$                    |
**Logic**
| $\land$                                 | **AND**                       | $A \land B$                       |
| $\lor$                                  | **OR**                        | $A \lor B$                        |
| $\lnot$                                 | **NOT**                       | $\lnot A$                         |
| $\oplus$                                | **Exclusive OR**              | $A \oplus B$                      |
| $\implies$                              | **Implies**                   | $A \implies B$                    |
| $\iff$                                  | **Logical Equivalence**       | $A \iff B$                        |
| $\therefore$                            | **Therefore**                 | $A \therefore B$                  |
| $\because$                              | **Because**                   | $A \because B$                    |
| $\top$                                  | **Tee, True**                 | $\top$                            |
| $\bot$                                  | **Up Tack, False**            | $\bot$                            |
| $\dashv$                                | **Asserted**                  | $\dashv A$                        |
| $\vdash$                                | **Provable**                  | $A \vdash B$                      |
| $\models$                               | **Entails**                   | $A \models B$                     |
| $\forall$                               | **Universal Quantifier**      | $\forall A$                       |
| $\exists$                               | **Existential Quantifier**    | $\exists A$                       |
| $\nexists$                              | **Not Exists Quantifier**     | $\nexists A$                      |
| $\exists!$                              | **Uniqueness Quantifier**     | $\exists! A$                      |
**Set Theory**
| $\emptyset$                             | **Empty Set**                 | $\emptyset$                       |
| $\|A\|$                                 | **Cardinality/Size**          | $\|A\|$                           |
| $\in$                                   | **Element of**                | $a \in A$                         |
| $\notin$                                | **Not Element of**            | $a \notin A$                      |
| $\subset$                               | **Subset**                    | $A \subset B$                     |
| $\subseteq$                             | **Subset or Equal**           | $A \subseteq B$                   |
| $\subsetneq$                            | **Proper Subset**             | $A \subsetneq B$                  |
| $\supset$                               | **Superset**                  | $A \supset B$                     |
| $\supseteq$                             | **Superset or Equal**         | $A \supseteq B$                   |
| $\supsetneq$                            | **Proper Superset**           | $A \supsetneq B$                  |
| $\cup$                                  | **Union**                     | $A \cup B$                        |
| $\cap$                                  | **Intersection**              | $A \cap B$                        |
| $\setminus$                             | **Difference**                | $A \setminus B$                   |
| $\ominus$ <br> $\Delta$                 | **Symmetrical Difference**    | $A \ominus B$ <br> $A \Delta B$   |
**Derivative**
| $'$                                     | **Lagrange's Notation**      | $f'$                              |
| $\dot{}$                                | **Netwon's Notation**         | $\dot{x}$                         |
| $$\frac{dy}{dx}$$                       | **Leibniz's Notation**         | $$\frac{df}{dx}$$                 |
| $$\frac{\partial f}{\partial x}$$       | **Leibniz's Notation**         | $$\frac{\partial f}{\partial x}$$ |
**Analysis/Calculus**
| $\Re$                                   | **Real**                      | $\Re(z)$                          |
| $\Im$                                   | **Imaginary**                 | $\Im(z)$                          |
| $\bar{}$                                | **Complex Conjugate**         | $\bar{z}$                         |
| $\|x\|$                                 | **Absolute Value**            | $\|x\|$                           |
| $\lfloor x \rfloor$                     | **Floor**                     | $\lfloor x \rfloor$               |
| $\lceil x \rceil$                       | **Ceil**                      | $\lceil x \rceil$                 |
| $\lfloor x \rceil$                      | **Nearest**                   | $\lfloor x \rceil$                |
| $\infty$                                | **Infinity**                  | $\infty$                          |
| $$\int$$                                | **Integral**                  | $$\int_a^b$$                      |
| $\mapsto$                               | **Namesless Function**        | $x \mapsto y$                     |
| $\log$                                  | **Logarithm**                 | $\log_ab = n$<br>$a^n = b$        |
| $\ln$                                   | **Natural Logarithm**         | $\ln(a) =\log_ea$                 |
| $$\lim$$                                | **Limit**                     | $$\lim_{x \to a} f(x) = L$$       |
| $$\sum$$                                | **Capital Sigma**             | $$\sum_{k = a}^bf(k)$$            |
| $$\prod$$                               | **Capital Pi**                | $$\prod_{k = a}^bf(k)$$           |
| $\nabla$                                | **Nabla**                     | $\nabla f$                        |
**Number Theory**
| $\mid$                                  | **Divisible**                 | $a \mid b$                        |
| $\nmid$                                 | **Not Divisible**             | $a \nmid b$                       |
**Miscellaneous**
| $$\begin{pmatrix}n \cr k\end{pmatrix}$$ | **Binomial Coefficient**      | $$\begin{pmatrix}n \cr k\end{pmatrix} = \frac{n!}{k!(n - k)!}$$ |

**Greek Alphabet**:

| Name        | Symbol (Lower)          | Symbol (Upper) |
| ----------- | ----------------------- | -------------- |
| **Alpha**   | $\alpha$                | $\Alpha$       |
| **Beta**    | $\beta$                 | $\Beta$        |
| **Gamma**   | $\gamma$                | $\Gamma$       |
| **Delta**   | $\delta$                | $\Delta$       |
| **Epsilon** | $\epsilon, \varepsilon$ | $\Epsilon$     |
| **Zeta**    | $\zeta$                 | $\Zeta$        |
| **Eta**     | $\eta$                  | $\Eta$         |
| **Theta**   | $\theta, \vartheta$     | $\Theta$       |
| **Iota**    | $\iota$                 | $\Iota$        |
| **Kappa**   | $\kappa, \varkappa$     | $\Kappa$       |
| **Lambda**  | $\lambda$               | $\Lambda$      |
| **Mu**      | $\mu$                   | $\Mu$          |
| **Nu**      | $\nu$                   | $\Nu$          |
| **Xi**      | $\xi$                   | $\Xi$          |
| **Omicron** | $\omicron$              | $\Omicron$     |
| **Pi**      | $\pi, \varpi$           | $\Pi$          |
| **Rho**     | $\rho, \varrho$         | $\Rho$         |
| **Sigma**   | $\sigma, \varsigma$     | $\Sigma$       |
| **Tau**     | $\tau$                  | $\Tau$         |
| **Upsilon** | $\upsilon$              | $\Upsilon$     |
| **Phi**     | $\phi, \varphi$         | $\Phi$         |
| **Chi**     | $\chi$                  | $\Chi$         |
| **Psi**     | $\psi$                  | $\Psi$         |
| **Omega**   | $\omega$                | $\Omega$       |

**Hebrew**:

| Name        | Symbol   |
| ----------- | -------- |
| **Aleph**   | $\aleph$ |
| **Beth**    | $\beth$  |
| **Gimel**   | $\gimel$ |
| **Dalet**   | ---      |
| **He**      | ---      |
| **Waw**     | ---      |
| **Zayin**   | ---      |
| **Het**     | ---      |
| **Tet**     | ---      |
| **Yod**     | ---      |
| **Kaf**     | ---      |
| **Lamed**   | ---      |
| **Mem**     | ---      |
| **Nun**     | ---      |
| **Samekh**  | ---      |
| **Ayin**    | ---      |
| **Pe**      | ---      |
| **Tsadi**   | ---      |
| **Qof**     | ---      |
| **Resh**    | ---      |
| **Shin**    | ---      |
| **Tav**     | ---      |

> "Unable to Render these as from my testing."

## Typefaces

**Blackboard Board Typeface**:

`\mathbb{}`

| Sort | Upper case   |
| ---- | ------------ |
| 1.   | $\mathbb{A}$ |
| 2.   | $\mathbb{B}$ |
| 3.   | $\mathbb{C}$ |
| 4.   | $\mathbb{D}$ |
| 5.   | $\mathbb{E}$ |
| 6.   | $\mathbb{F}$ |
| 7.   | $\mathbb{G}$ |
| 8.   | $\mathbb{H}$ |
| 9.   | $\mathbb{I}$ |
| 10.  | $\mathbb{J}$ |
| 11.  | $\mathbb{K}$ |
| 12.  | $\mathbb{L}$ |
| 13.  | $\mathbb{M}$ |
| 14.  | $\mathbb{N}$ |
| 15.  | $\mathbb{O}$ |
| 16.  | $\mathbb{P}$ |
| 17.  | $\mathbb{Q}$ |
| 18.  | $\mathbb{R}$ |
| 19.  | $\mathbb{S}$ |
| 20.  | $\mathbb{T}$ |
| 21.  | $\mathbb{U}$ |
| 22.  | $\mathbb{V}$ |
| 23.  | $\mathbb{W}$ |
| 24.  | $\mathbb{X}$ |
| 25.  | $\mathbb{Y}$ |
| 26.  | $\mathbb{Z}$ |

**Fraktur**:

`\mathfrak{}`

| Sort | Lower case     | Upper case     |
| ---- | -------------- | -------------- |
| 1.   | $\mathfrak{a}$ | $\mathfrak{A}$ |
| 2.   | $\mathfrak{b}$ | $\mathfrak{B}$ |
| 3.   | $\mathfrak{c}$ | $\mathfrak{C}$ |
| 4.   | $\mathfrak{d}$ | $\mathfrak{D}$ |
| 5.   | $\mathfrak{e}$ | $\mathfrak{E}$ |
| 6.   | $\mathfrak{f}$ | $\mathfrak{F}$ |
| 7.   | $\mathfrak{g}$ | $\mathfrak{G}$ |
| 8.   | $\mathfrak{h}$ | $\mathfrak{H}$ |
| 9.   | $\mathfrak{i}$ | $\mathfrak{I}$ |
| 10.  | $\mathfrak{j}$ | $\mathfrak{J}$ |
| 11.  | $\mathfrak{k}$ | $\mathfrak{K}$ |
| 12.  | $\mathfrak{l}$ | $\mathfrak{L}$ |
| 13.  | $\mathfrak{m}$ | $\mathfrak{M}$ |
| 14.  | $\mathfrak{n}$ | $\mathfrak{N}$ |
| 15.  | $\mathfrak{o}$ | $\mathfrak{O}$ |
| 16.  | $\mathfrak{p}$ | $\mathfrak{P}$ |
| 17.  | $\mathfrak{q}$ | $\mathfrak{Q}$ |
| 18.  | $\mathfrak{r}$ | $\mathfrak{R}$ |
| 19.  | $\mathfrak{s}$ | $\mathfrak{S}$ |
| 20.  | $\mathfrak{t}$ | $\mathfrak{T}$ |
| 21.  | $\mathfrak{u}$ | $\mathfrak{U}$ |
| 22.  | $\mathfrak{v}$ | $\mathfrak{V}$ |
| 23.  | $\mathfrak{w}$ | $\mathfrak{W}$ |
| 24.  | $\mathfrak{x}$ | $\mathfrak{X}$ |
| 25.  | $\mathfrak{y}$ | $\mathfrak{Y}$ |
| 26.  | $\mathfrak{z}$ | $\mathfrak{Z}$ |

**Calligraphic**:

`\mathcal`

| Sort | Lower case    | Upper case    |
| ---- | ------------- | ------------- |
| 1.   | $\mathcal{a}$ | $\mathcal{A}$ |
| 2.   | $\mathcal{b}$ | $\mathcal{B}$ |
| 3.   | $\mathcal{c}$ | $\mathcal{C}$ |
| 4.   | $\mathcal{d}$ | $\mathcal{D}$ |
| 5.   | $\mathcal{e}$ | $\mathcal{E}$ |
| 6.   | $\mathcal{f}$ | $\mathcal{F}$ |
| 7.   | $\mathcal{g}$ | $\mathcal{G}$ |
| 8.   | $\mathcal{h}$ | $\mathcal{H}$ |
| 9.   | $\mathcal{i}$ | $\mathcal{I}$ |
| 10.  | $\mathcal{j}$ | $\mathcal{J}$ |
| 11.  | $\mathcal{k}$ | $\mathcal{K}$ |
| 12.  | $\mathcal{l}$ | $\mathcal{L}$ |
| 13.  | $\mathcal{m}$ | $\mathcal{M}$ |
| 14.  | $\mathcal{n}$ | $\mathcal{N}$ |
| 15.  | $\mathcal{o}$ | $\mathcal{O}$ |
| 16.  | $\mathcal{p}$ | $\mathcal{P}$ |
| 17.  | $\mathcal{q}$ | $\mathcal{Q}$ |
| 18.  | $\mathcal{r}$ | $\mathcal{R}$ |
| 19.  | $\mathcal{s}$ | $\mathcal{S}$ |
| 20.  | $\mathcal{t}$ | $\mathcal{T}$ |
| 21.  | $\mathcal{u}$ | $\mathcal{U}$ |
| 22.  | $\mathcal{v}$ | $\mathcal{V}$ |
| 23.  | $\mathcal{w}$ | $\mathcal{W}$ |
| 24.  | $\mathcal{x}$ | $\mathcal{X}$ |
| 25.  | $\mathcal{y}$ | $\mathcal{Y}$ |
| 26.  | $\mathcal{z}$ | $\mathcal{Z}$ |

**Script**:

`\mathscr`

| Sort | Upper case    |
| ---- | ------------- |
| 1.   | $\mathscr{A}$ |
| 2.   | $\mathscr{B}$ |
| 3.   | $\mathscr{C}$ |
| 4.   | $\mathscr{D}$ |
| 5.   | $\mathscr{E}$ |
| 6.   | $\mathscr{F}$ |
| 7.   | $\mathscr{G}$ |
| 8.   | $\mathscr{H}$ |
| 9.   | $\mathscr{I}$ |
| 10.  | $\mathscr{J}$ |
| 11.  | $\mathscr{K}$ |
| 12.  | $\mathscr{L}$ |
| 13.  | $\mathscr{M}$ |
| 14.  | $\mathscr{N}$ |
| 15.  | $\mathscr{O}$ |
| 16.  | $\mathscr{P}$ |
| 17.  | $\mathscr{Q}$ |
| 18.  | $\mathscr{R}$ |
| 19.  | $\mathscr{S}$ |
| 20.  | $\mathscr{T}$ |
| 21.  | $\mathscr{U}$ |
| 22.  | $\mathscr{V}$ |
| 23.  | $\mathscr{W}$ |
| 24.  | $\mathscr{X}$ |
| 25.  | $\mathscr{Y}$ |
| 26.  | $\mathscr{Z}$ |

**Bold**:

`\mathbf`

| Sort | Lower case   | Upper case   |
| ---- | ------------ | ------------ |
| 1.   | $\mathbf{a}$ | $\mathbf{A}$ |
| 2.   | $\mathbf{b}$ | $\mathbf{B}$ |
| 3.   | $\mathbf{c}$ | $\mathbf{C}$ |
| 4.   | $\mathbf{d}$ | $\mathbf{D}$ |
| 5.   | $\mathbf{e}$ | $\mathbf{E}$ |
| 6.   | $\mathbf{f}$ | $\mathbf{F}$ |
| 7.   | $\mathbf{g}$ | $\mathbf{G}$ |
| 8.   | $\mathbf{h}$ | $\mathbf{H}$ |
| 9.   | $\mathbf{i}$ | $\mathbf{I}$ |
| 10.  | $\mathbf{j}$ | $\mathbf{J}$ |
| 11.  | $\mathbf{k}$ | $\mathbf{K}$ |
| 12.  | $\mathbf{l}$ | $\mathbf{L}$ |
| 13.  | $\mathbf{m}$ | $\mathbf{M}$ |
| 14.  | $\mathbf{n}$ | $\mathbf{N}$ |
| 15.  | $\mathbf{o}$ | $\mathbf{O}$ |
| 16.  | $\mathbf{p}$ | $\mathbf{P}$ |
| 17.  | $\mathbf{q}$ | $\mathbf{Q}$ |
| 18.  | $\mathbf{r}$ | $\mathbf{R}$ |
| 19.  | $\mathbf{s}$ | $\mathbf{S}$ |
| 20.  | $\mathbf{t}$ | $\mathbf{T}$ |
| 21.  | $\mathbf{u}$ | $\mathbf{U}$ |
| 22.  | $\mathbf{v}$ | $\mathbf{V}$ |
| 23.  | $\mathbf{w}$ | $\mathbf{W}$ |
| 24.  | $\mathbf{x}$ | $\mathbf{X}$ |
| 25.  | $\mathbf{y}$ | $\mathbf{Y}$ |
| 26.  | $\mathbf{z}$ | $\mathbf{Z}$ |

**Sans-serif**:

`\mathsf`

| Sort | Lower case   | Upper case   |
| ---- | ------------ | ------------ |
| 1.   | $\mathsf{a}$ | $\mathsf{A}$ |
| 2.   | $\mathsf{b}$ | $\mathsf{B}$ |
| 3.   | $\mathsf{c}$ | $\mathsf{C}$ |
| 4.   | $\mathsf{d}$ | $\mathsf{D}$ |
| 5.   | $\mathsf{e}$ | $\mathsf{E}$ |
| 6.   | $\mathsf{f}$ | $\mathsf{F}$ |
| 7.   | $\mathsf{g}$ | $\mathsf{G}$ |
| 8.   | $\mathsf{h}$ | $\mathsf{H}$ |
| 9.   | $\mathsf{i}$ | $\mathsf{I}$ |
| 10.  | $\mathsf{j}$ | $\mathsf{J}$ |
| 11.  | $\mathsf{k}$ | $\mathsf{K}$ |
| 12.  | $\mathsf{l}$ | $\mathsf{L}$ |
| 13.  | $\mathsf{m}$ | $\mathsf{M}$ |
| 14.  | $\mathsf{n}$ | $\mathsf{N}$ |
| 15.  | $\mathsf{o}$ | $\mathsf{O}$ |
| 16.  | $\mathsf{p}$ | $\mathsf{P}$ |
| 17.  | $\mathsf{q}$ | $\mathsf{Q}$ |
| 18.  | $\mathsf{r}$ | $\mathsf{R}$ |
| 19.  | $\mathsf{s}$ | $\mathsf{S}$ |
| 20.  | $\mathsf{t}$ | $\mathsf{T}$ |
| 21.  | $\mathsf{u}$ | $\mathsf{U}$ |
| 22.  | $\mathsf{v}$ | $\mathsf{V}$ |
| 23.  | $\mathsf{w}$ | $\mathsf{W}$ |
| 24.  | $\mathsf{x}$ | $\mathsf{X}$ |
| 25.  | $\mathsf{y}$ | $\mathsf{Y}$ |
| 26.  | $\mathsf{z}$ | $\mathsf{Z}$ |

**Monospace, Typewriter**:

`\mathtt`

| Sort | Lower case   | Upper case   |
| ---- | ------------ | ------------ |
| 1.   | $\mathtt{a}$ | $\mathtt{A}$ |
| 2.   | $\mathtt{b}$ | $\mathtt{B}$ |
| 3.   | $\mathtt{c}$ | $\mathtt{C}$ |
| 4.   | $\mathtt{d}$ | $\mathtt{D}$ |
| 5.   | $\mathtt{e}$ | $\mathtt{E}$ |
| 6.   | $\mathtt{f}$ | $\mathtt{F}$ |
| 7.   | $\mathtt{g}$ | $\mathtt{G}$ |
| 8.   | $\mathtt{h}$ | $\mathtt{H}$ |
| 9.   | $\mathtt{i}$ | $\mathtt{I}$ |
| 10.  | $\mathtt{j}$ | $\mathtt{J}$ |
| 11.  | $\mathtt{k}$ | $\mathtt{K}$ |
| 12.  | $\mathtt{l}$ | $\mathtt{L}$ |
| 13.  | $\mathtt{m}$ | $\mathtt{M}$ |
| 14.  | $\mathtt{n}$ | $\mathtt{N}$ |
| 15.  | $\mathtt{o}$ | $\mathtt{O}$ |
| 16.  | $\mathtt{p}$ | $\mathtt{P}$ |
| 17.  | $\mathtt{q}$ | $\mathtt{Q}$ |
| 18.  | $\mathtt{r}$ | $\mathtt{R}$ |
| 19.  | $\mathtt{s}$ | $\mathtt{S}$ |
| 20.  | $\mathtt{t}$ | $\mathtt{T}$ |
| 21.  | $\mathtt{u}$ | $\mathtt{U}$ |
| 22.  | $\mathtt{v}$ | $\mathtt{V}$ |
| 23.  | $\mathtt{w}$ | $\mathtt{W}$ |
| 24.  | $\mathtt{x}$ | $\mathtt{X}$ |
| 25.  | $\mathtt{y}$ | $\mathtt{Y}$ |
| 26.  | $\mathtt{z}$ | $\mathtt{Z}$ |

## Decorators

| $\LaTeX$                | Symbolic                 | Name                                |
| ----------------------- | ------------------------ | ----------------------------------- |
| `{}^{}`                 | $a^{\square}$            | **Superscript**                     |
| `{}_{}`                 | $a_{\square}$            | **Subscript**                       |
| `{}^{} {}`              | ${}^{\square} a$         | **Left Superscript** (non-standard) |
| `{}_{} {}`              | ${}_{\square} a$         | **Left Subscript** (non-standard)   |
| `\overset{}{}`          | $\overset{\square}{a}$   | **Overset**                         |
| `\underset{}{}`         | $\underset{\square}{a}$  | **Underset**                        |
| `\dot{}`                | $\dot{a}$                | **Dot**                             |
| `\bar{}`                | $\bar{a}$                | **Conjugate**                       |
| `\v{}`                  | $\v{a}$                  | **V**                               |
| `\tilde{}`              | $\tilde{a}$              | **Tilde**                           |
| `\overline{}`           | $\overline{A}$           | **Line**                            |
| `\overrightarrow{}`     | $\overrightarrow{A}$     | **Ray (R)**                         |
| `\overleftarrow{}`      | $\overleftarrow{A}$      | **Ray (L)**                         |
| `\overleftrightarrow{}` | $\overleftrightarrow{A}$ | **Ray (RL)**                        |
| `\underline{}`          | $\underline{A}$          | **Under Line**                      |
| `\vec{}`                | $\vec{v}$                | **Vector**                          |
| `\hat{}`                | $\hat{v}$                | **Unit Vector**                     |
| `\dagger`               | $A^\dagger$              | **Dagger**                          |
| `\ddagger`              | $A\ddagger$              | **Double Dagger**                   |
| `\diamond`              | $\diamond P$             | **Diamond**                         |

## Color Pallet

In some sections within this archive there is use of color in formula's and equations, while they are mostly for decoration, some colors actually hold meaning in order to make it clearer to someone new what's going on:

| Color                                | Name           | Meaning                                      |
| ------------------------------------ | -------------- | -------------------------------------------- |
| $\color{Dodgerblue}\blacksquare$     | Dodgerblue     | Usage of known Identities/Simplification     |
| $\color{MediumSeaGreen}\blacksquare$ | MediumSeaGreen | Addition of a new term/Applying an operation |
| $\color{OrangeRed}\blacksquare$      | OrangeRed      | Cancellation of Operations                   |

while any other color used other than these are mostly just for decoration.

## Constants

$f(0) = 0$

$f(1) = 1$

$f(n) = f(n-1) + f(n-2)$

| Symbol   | Name                              | Decimal Value               | Formula                                                             |
| -------- | --------------------------------- | --------------------------- | ------------------------------------------------------------------- |
| $\pi$    | **Pi**                            | $3.14159265358979323846...$ |                                                                     |
| $\tau$   | **tau**                           | $6.28318530717958647692...$ | $2\pi$                                                              |
| $e$      | **Euler's Number**                | $2.71828182845904523536...$ | $$\sum_{n=0}^\infty\frac{1}{n!}$$                                   |
| $i$      | **Imaginary Unit**                | $i$                         | $\sqrt{-1}$                                                         |
| $\phi$   | **Golden Ratio**                  | $1.61803398874989484820...$ | $$\lim_{n \to \infty}\frac{f(n)}{f(n-1)} = \frac{1 + \sqrt{5}}{2}$$ |
| $\psi$   | **Reciprocal Fibonacci Constant** | $3.35988566624317755317...$ | $$\sum_{n=1}^{\infty}\frac{1}{f(n)}$$                               |
| $\gamma$ | **Euler-Mascheroni Constant**     | (pending...)                |                                                                     |

## Notation

These are Patches for common Mathematical Notation that can be very confusing for some people in case Contexts Overlap or are just generally bad, may also includes some new notations.

### Degrees

The normal $5\degree$ notation should not be used outside the Geometry/Trig section, since it can possible cause confusion with a 0th exponent, if needed use the following notation:

$$
5 \deg
$$

### Intervals

All intervals should be expressed in the following way to avoid confusion with points:

| Type                    | Notation |
| ----------------------- | -------- |
| **Open Ended**          | $(a;b)$  |
| **Half Open Ended (1)** | $[a;b)$  |
| **Half Open Ended (2)** | $(a;b]$  |
| **Closed Ended**        | $[a;b]$  |

It replaces the formal `,` separation of `a` and `b` with `;` as to make it more clear that it's an Interval.

### Functions

**Function Exponent**, to raise the function a power `n` append the number after the arguments in the superscript

$$
f(x)^{-1} = \frac{1}{f(x)}
$$
$$
f(x) = 4x
$$
$$
f(x)^3 = (4x)^3
$$
$$
f^3 = (4x)^3
$$

**Inverse Function**: a function raised to the -1 power should be interpreted as  the inverse of that function
$$
f^{-1}(x)
$$
$$
f^{-1}(f(x)) = x$$
in general the number `-1` can be by any integer, in the context it means to successively apply it:

$$
f^3(x) = \underbrace{f(f(f(x)))}_{3\text { times}}
$$
$$
f^{-4}(x) = \underbrace{f^{-1}(f^{-1}(f^{-1}(f^{-1}(x))))}_{4 \text { times}}
$$

### Piece-wise Functions:

There are functions that are defined as conditionals:


$$f(x) =
\begin{cases}
P_1(x) : f_1(x) \cr
P_2(x) : f_2(x) \cr
P_3(x) : f_3(x) \cr
... : ... \cr
\end{cases}$$

this is a bit custom so it's better to explain it's evaluation:

"if $P_1(x)$ then $f_1(x)$"

"if $P_2(x)$ then $f_2(x)$"

"if $P_3(x)$ then $f_3(x)$"

and so on.
