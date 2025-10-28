# Cubic

where the degree of the Polynomial is `3`

$$ax^3 + bx^2 + cx + d = 0$$


Roots of The Polynomial:

- **Depressed Cubic**


# Root Finding

$$ax^3 + bx + c$$
$$ax^3 + bx + c = 0$$
$$\frac{ax^3 + bx + c}{a} = \frac{0}{a}$$
$$x^3 + \frac{b}{a}x + \frac{c}{a} = 0$$

Binomial Expansion of $u + v$ raised to the power $3$:
$$ (u + v)^3 = u^3 + 3u^2v + 3uv^2 + v^3 \newline
= u^3 + 3uv(u + v) + v^3 \newline
(u + v)^3 - (u^3 + 3uv(u + v) + v^3) = 0 \newline
(\underbrace{u + v}_{x})^3 + (\underbrace{- 3uv}_{b/a})(\underbrace{u + v}_{x}) + \underbrace{(- u^3 - v^3)}_c{} = 0 \newline
$$

$$
x = u + v \newline
\frac{b}{a} = -3uv \newline
\frac{c}{a} = - (u^3+ v^3) \newline
uv = - \frac{b}{3a} \newline
u^3 + v^3 + \frac{c}{a} = 0\newline
u^3 (u^3 + v^3 + \frac{c}{a}) = u^3(0)\newline
u^6 + (uv)^3 + \frac{c}{a}u^3 = 0\newline
(u^3)^2 + \frac{c}{a}(u^3) + (- \frac{b}{3a})^3 = 0\newline
$$

using the quadratic:
$$
u^3 = \frac{- (c/a) \pm \sqrt{(c/a)^2 - 4\cdot 1 \cdot (- \frac{b}{3a})^3}}{2 \cdot 1} \newline
= \frac{- (c/a)}{2} \pm \frac{\sqrt{(c/a)^2 + 4 (\frac{b}{3a})^3}}{2} \newline
= - \frac{c}{2a} \pm \sqrt{\frac{1}{4}((\frac{c}{a})^2 + 4(\frac{b}{3a})^3)} \newline
u^3 = - \frac{c}{2a} \pm \sqrt{(\frac{c}{2a})^2 + (\frac{b}{3a})^3} \newline
u, v = \sqrt[3]{- \frac{c}{2a} \pm \sqrt{(\frac{c}{2a})^2 + (\frac{b}{3a})^3}} \newline

x = u + v \newline
$$

$$
x = \sqrt[3]{- \frac{c}{2a} \pm \sqrt{(\frac{c}{2a})^2 + (\frac{b}{3a})^3}} + \sqrt[3]{- \frac{c}{2a} \mp \sqrt{(\frac{c}{2a})^2 + (\frac{b}{3a})^3}}
$$ 

$b/a$ and $c/a$ are usually taken as `p` and `q` correspondingly, so it becomes

$$x^3 + px + q = 0$$
$$
x = \sqrt[3]{- \frac{q}{2} \pm \sqrt{\left(\frac{q}{2}\right)^2 + \left(\frac{p}{3}\right)^3}} + \sqrt[3]{- \frac{q}{2} \mp \sqrt{\left(\frac{q}{2}\right)^2 + \left(\frac{p}{3}\right)^3}}
$$

**General Solution**:

$$
ax^3 + bx^2 + cx + d = 0
$$
Inflication point
$$
\frac{d^2}{dx^2}(ax^3 + bx^2 + cx + d) = 0 \newline
6ax + 2b = 0 \newline
x = -\frac{b}{3a} \newline
$$
Substituion:

$$
x = y + (-\frac{b}{3a})
$$

$$
ax^3 + bx^2 + cx + d = 0 \newline

a(y - \frac{b}{3a})^3 + 
b(y - \frac{b}{3a})^2 + 
c(y - \frac{b}{3a}) + 
d = 0 \newline

a(y^3 - 3y^2\frac{b}{3a} + 3y(\frac{b}{3a})^2 - (\frac{b}{3a})^3 ) + 
b(y^2 - 2y\frac{b}{3a} + (\frac{b}{3a})^2) + 
cy - \frac{cb}{3a} + 
d = 0 \newline

a(y^3 - \frac{3by^2}{3a} + \frac{3b^2y}{9a^2} - \frac{b^3}{27a^3} ) + 
b(y^2 - \frac{2yb}{3a} + \frac{b^2}{9a^2}) + 
cy - \frac{cb}{3a} + 
d = 0 \newline

ay^3 - \frac{aby^2}{a} + \frac{ab^2y}{3a^2} - \frac{ab^3}{27a^3}+ 
by^2 - \frac{2yb^2}{3a} + \frac{b^3}{9a^2} + 
cy - \frac{cb}{3a} + 
d = 0 \newline

ay^3 - by^2 + \frac{b^2y}{3a} - \frac{b^3}{27a^2} + 
by^2 - \frac{2b^2y}{3a} + \frac{b^3}{9a^2} + 
cy - \frac{bc}{3a} + 
d = 0 \newline

ay^3 + \frac{b^2y}{3a} - \frac{b^3}{27a^2} 
- \frac{2b^2y}{3a} + \frac{b^3}{9a^2} + 
cy - \frac{bc}{3a} + 
d = 0 \newline

ay^3 + \frac{b^2}{3a}y - \frac{2b^2}{3a}y + cy - \frac{b^3}{27a^2} + \frac{b^3}{9a^2} - \frac{bc}{3a} + d = 0 \newline
ay^3 + (\frac{b^2}{3a} - \frac{2b^2}{3a} + c)y + (- \frac{b^3}{27a^2} + \frac{b^3}{9a^2} - \frac{bc}{3a} + d) = 0 \newline
ay^3 + (c - \frac{b^2}{3a})y + (\frac{3b^3 - b^3}{27a^2} - \frac{bc}{3a} + d) = 0 \newline

ay^3 + 
(c - \frac{b^2}{3a})y + 
(\frac{2b^3}{27a^2} - \frac{bc}{3a} + d) = 0 \newline
$$

$$
p = \frac{c}{a} - \frac{b^2}{3a^2} \newline
q = \frac{2b^3}{27a^2} - \frac{abc}{3a^2} + \frac{d}{a}
$$

Using the Depressed Cubic to solve for `y`

> Depressed Cubic general formula: ($a \neq 0$)
> $$ax^3 + bx + c = 0$$ 
> $$ x = \sqrt[3]{- \frac{c}{2a} \pm \sqrt{(\frac{c}{2a})^2 + (\frac{b}{3a})^3}} + \sqrt[3]{- \frac{c}{2a} \mp \sqrt{(\frac{c}{2a})^2 + (\frac{b}{3a})^3}}$$

$$
y = \sqrt[3]{- \frac{(\frac{2b^3}{27a^2} - \frac{bc}{3a} + d)}{2a} \pm \sqrt{(\frac{(\frac{2b^3}{27a^2} - \frac{bc}{3a} + d)}{2a})^2 + (\frac{(c - \frac{b^2}{3a})}{3a})^3}} + ... \newline
$$

$$
y = \sqrt[3]{(- \frac{b^3}{27a^3} + \frac{bc}{6a^2} - \frac{d}{2a}) \pm \sqrt{(- \frac{b^3}{27a^3} + \frac{bc}{6a^2} - \frac{d}{2a})^2 + (\frac{c}{3a} - \frac{b^2}{9a^2})^3}} + \newline
\sqrt[3]{(- \frac{b^3}{27a^3} + \frac{bc}{6a^2} - \frac{d}{2a}) \mp \sqrt{(- \frac{b^3}{27a^3} + \frac{bc}{6a^2} - \frac{d}{2a})^2 + (\frac{c}{3a} - \frac{b^2}{9a^2})^3}}
$$

Final Step:
$$x = y - \frac{b}{3a}$$
$$
y - \frac{b}{3a} = \sqrt[3]{\left(- \frac{b^3}{27a^3} + \frac{bc}{6a^2} - \frac{d}{2a}\right) \pm \sqrt{\left(- \frac{b^3}{27a^3} + \frac{bc}{6a^2} - \frac{d}{2a}\right)^2 + \left(\frac{c}{3a} - \frac{b^2}{9a^2}\right)^3}} + \newline
\sqrt[3]{\left(- \frac{b^3}{27a^3} + \frac{bc}{6a^2} - \frac{d}{2a}\right) \mp \sqrt{\left(- \frac{b^3}{27a^3} + \frac{bc}{6a^2} - \frac{d}{2a}\right)^2 + \left(\frac{c}{3a} - \frac{b^2}{9a^2}\right)^3}} - \frac{b}{3a}
$$

**Full General Cubic Solution**:

$$
ax^3 + bx^2 + cx + d = 0
$$

$$
x = \sqrt[3]{\left(- \frac{b^3}{27a^3} + \frac{bc}{6a^2} - \frac{d}{2a}\right) \pm \sqrt{\left(- \frac{b^3}{27a^3} + \frac{bc}{6a^2} - \frac{d}{2a}\right)^2 + \left(\frac{c}{3a} - \frac{b^2}{9a^2}\right)^3}} + \newline
\sqrt[3]{\left(- \frac{b^3}{27a^3} + \frac{bc}{6a^2} - \frac{d}{2a}\right) \mp \sqrt{\left(- \frac{b^3}{27a^3} + \frac{bc}{6a^2} - \frac{d}{2a}\right)^2 + \left(\frac{c}{3a} - \frac{b^2}{9a^2}\right)^3}} - \frac{b}{3a}
$$