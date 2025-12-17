# Quartic Polynomials

Polynomial with a degree of `4`

where:
$a \neq 0$

**General**

$$
ax^4 + bx^3 + cx^2 + dx + e
$$

**Depressed Quartic**

$$
ax^4 + bx^2 + cx + d
$$

**Bi-quartic**

$$
ax^4 + bx^2 + c
$$



# Root Finding

assuming you already know how to solve Cubic and Quadratic Polynomails (degree `2` and `3`)

$$
ax^4 + bx^3 + cx^2 + dx + e = 0
$$

> Shift:
> $$
> f(x) = ax^4 + bx^3 + cx^2 + dx + e
> $$
> $$
> f'''(x) = 0
> $$
> $$
> f'''(x) = 4 \cdot 3 \cdot 2 \cdot ax + 3 \cdot 2 \cdot b + 0 + 0 + 0 \newline
> = 24ax + 6b
> $$
> 
> $$
> 24ax + 6b = 0 \newline
> x = \frac{-6b}{24a} \newline
> $$
> $$
> x = \frac{-b}{4a} \newline
> $$
> back to the quartic formula:

$$
ax^4 + bx^3 + cx^2 + dx + e = 0
$$
$$
x = y - \frac{b}{4a}
$$
substitute:
$$
a\left(y - \frac{b}{4a}\right)^4 + 
b\left(y - \frac{b}{4a}\right)^3 + 
c\left(y - \frac{b}{4a}\right)^2 + 
d\left(y - \frac{b}{4a}\right) + 
e = 0$$

Simplfying:

$$
a \left(
	y^4 + 
	4y^3\left(- \frac{b}{4a}\right) + 
	6y^2\left(- \frac{b}{4a}\right)^2 + 
	4y\left(- \frac{b}{4a}\right)^3 + 
	\left(- \frac{b}{4a}\right)^4
\right) + \newline
b\left(
	y^3+
	3y^2\left(- \frac{b}{4a}\right) +
	3y\left(- \frac{b}{4a}\right)^2 +
	\left(- \frac{b}{4a}\right)^3

\right) + 
c\left(
	y^2 +
	2y\left(- \frac{b}{4a}\right) +
	\left(- \frac{b}{4a}\right)^2
\right) + 
d\left(y - \frac{b}{4a}\right) + 
e = 0
$$


$$
a \left(
	y^4 + 
	4y^3 \left(- \frac{b}{4a}\right) + 
	6y^2 \left(\frac{b^2}{16a^2}\right)  + 
	4y   \left(- \frac{b^3}{64a^3}\right) + 
	\left(\frac{b^4}{256a^4}\right)
\right) + \newline
b\left(
	y^3+
	3y^2 \left(- \frac{b}{4a}\right) +
	3y   \left(\frac{b^2}{16a^2}\right) +
	\left(- \frac{b^3}{64a^3}\right)

\right) + 
c\left(
	y^2 +
	2y   \left(- \frac{b}{4a}\right) +
	\left(\frac{b^2}{16a^2}\right)
\right) + 
d\left(y - \frac{b}{4a}\right) + 
e = 0 \newline
$$

$$
a \left(
	y^4 + 
	4y^3 \left(- \frac{b}{4a}\right) + 
	6y^2 \left(\frac{b^2}{16a^2}\right)  + 
	4y   \left(- \frac{b^3}{64a^3}\right) + 
	\left(\frac{b^4}{256a^4}\right)
\right) + \newline
b\left(
	y^3+
	3y^2 \left(- \frac{b}{4a}\right) +
	3y   \left(\frac{b^2}{16a^2}\right) +
	\left(- \frac{b^3}{64a^3}\right)

\right) + 
c\left(
	y^2 +
	2y   \left(- \frac{b}{4a}\right) +
	\left(\frac{b^2}{16a^2}\right)
\right) + 
d\left(y - \frac{b}{4a}\right) + 
e = 0 \newline
$$

$$
a \left(
	y^4
	- \frac{ by^3   }{   a  }
	+ \frac{3b^2 y^2}{  8a^2}
	- \frac{ b^3  y }{ 16a^3}
	+ \frac{ b^4    }{256a^4}
\right) + \newline
b\left(
	y^3
	- \frac{3b  y^2}{ 4a  }
	+ \frac{3b^2y  }{16a^2}
	- \frac{ b^3   }{64a^3}

\right) + 
c\left(
	y^2
	- \frac{by  }{ 2a  }
	+ \frac{b^2 }{16a^2}
\right) + 
d\left(y - \frac{b}{4a}\right) + 
e = 0 \newline
$$

$$
ay^4
- by^3
+ \frac{3b^2 y^2}{  8a}
- \frac{ b^3  y }{ 16a^2}
+ \frac{ b^4    }{256a^3}
+ by^3
- \frac{3b^2  y^2}{ 4a  }
+ \frac{3b^3y  }{16a^2}
- \frac{ b^4   }{64a^3}
+ cy^2
- \frac{bcy  }{ 2a  }
+ \frac{b^2c }{16a^2}
+ dy
- \frac{bd}{4a}
+ e = 0 \newline
$$

$$
ay^4
- by^3
+ by^3
+ \frac{3b^2 y^2 }{  8a   }
- \frac{6b^2 y^2 }{  8a   }
+ cy^2
- \frac{ b^3 y   }{ 16a^2 }
+ \frac{3b^3 y   }{ 16a^2 }
- \frac{bc   y   }{ 2a    }
+ dy
+ \frac{ b^4     }{256a^3 }
- \frac{ 4b^4    }{ 256a^3}
+ \frac{b^2c     }{ 16a^2 }
- \frac{bd       }{  4a   }
+ e = 0 \newline
$$
$$
ay^4
- \frac{3b^2 y^2}{  8a   }
+ cy^2
+ \frac{b^3 y    }{ 8a^2 }
- \frac{bc   y   }{ 2a   }
+ dy
- \frac{ 3b^4   }{256a^3}
+ \frac{b^2c    }{ 16a^2}
- \frac{bd      }{  4a  }
+ e = 0 \newline
$$

$$
\left(ay^4
- \frac{3b^2 y^2}{  8a   }
+ cy^2
+ \frac{b^3 y    }{ 8a^2 }
- \frac{bc   y   }{ 2a   }
+ dy
- \frac{ 3b^4   }{256a^3}
+ \frac{b^2c    }{ 16a^2}
- \frac{bd      }{  4a  }
+ e\right)/a = 0/a \newline
$$

$$
y^4
- \frac{3b^2 y^2}{  8a^2   }
+ \frac{cy^2}{a}
+ \frac{b^3 y    }{ 8a^3 }
- \frac{bc   y   }{ 2a^2   }
+ \frac{dy}{a}
- \frac{ 3b^4   }{256a^4}
+ \frac{b^2c    }{ 16a^3}
- \frac{bd      }{  4a^2  }
+ \frac{e}{a} = 0 \newline
$$
$$
y^4
+ \left( - \frac{3b^2}{  8a^2} + \frac{   c }{  a  } \right)y^2
+ \left(   \frac{ b^3}{  8a^3} - \frac{b  c    }{ 2a^2} + \frac{d }{ a  } \right)y
+ \left( - \frac{3b^4}{256a^4} + \frac{b^2c    }{16a^3} - \frac{bd}{4a^2} + \frac{e}{a} \right)
= 0 \newline
$$
$$
y^4
+ \left( - \frac{3b^2}{  8a^2} + \frac{8a   c }{  8a^2} \right)y^2
+ \left(   \frac{ b^3}{  8a^3} - \frac{4ab  c }{  8a^3} + \frac{ 8a^2  d}{  8a^3} \right)y
+ \left( - \frac{3b^4}{256a^4} + \frac{16ab^2c}{256a^4} - \frac{64a^2b d}{256a^2} + \frac{256a^3e}{256a^4} \right)
= 0 \newline
$$
$$
y^4
+ \underbrace{\left( \frac{- 3b^2 + 8ac}{8a^2} \right)}_{p}y^2
+ \underbrace{\left( \frac{b^3 - 4abc + 8a^2d}{8a^3} \right)}_{q}y
+ \underbrace{\left( \frac{- 3b^4 + 16ab^2c - 64a^2bd + 256a^3e}{256a^4} \right)}_{r}
= 0 \newline
$$
Now it has taken form of a Depressed Quartic

$$
y^4 + py^2 + qy + r = 0
$$

where:

$$
p = \frac{- 3b^2 + 8ac}{ 8a^2  }\newline
$$
$$
q =   \frac{b^3 - 4abc - 8a^2d }{ 8a^3  }\newline
$$
$$
r = \frac{- 3b^4 + 16ab^2c - 64a^2bd + 256a^3e}{256a^4}\newline
$$

Solving the Depressed Quartic:

$$
y^4 + py^2 + qy + r = 0 \newline
y^4 + py^2 = - qy - r \newline
(y^2)^2 + p(y^2) = - qy - r \newline
(y^2)^2 + 2p(y^2) + p^2 = py^2 + p^2 - qy - r \newline
(y^2 + p)^2 = py^2 - qy + p^2 - r \newline
$$
new variable `z`:
$$
(y^2 + p)^2 = py^2 - qy + p^2 - r \newline
(y^2 + p)^2 + 2(y^2 + p)z + z^2 = py^2 - qy + p^2 - r  + 2(y^2 + p)z + z^2\newline
(y^2 + p + z)^2 = py^2 - qy + p^2 - r  + 2zy^2 + 2zp + z^2\newline
(y^2 + p + z)^2 = (p + 2z)y^2 + (- q)y + (p^2 + 2zp + z^2 - r)\newline
$$
define z such that:

$$
(- q)^2 - 4(p + 2z)(p^2 + 2pz + z^2 - r) = 0 \newline
q^2 - 4(p^3 + 2p^2z + pz^2 - pr + 2p^2z + 4pz^2 + 2z^3 - 2rz) = 0 \newline
p^3 + 2p^2z + pz^2 - pr + 2p^2z + 4pz^2 + 2z^3 - 2rz = \frac{q^2}{4} \newline
2z^3 + 5pz^2 + 4p^2z - 2rz + p^3 - pr - \frac{q^2}{4} = 0 \newline
z^3 + \frac{5pz^2}{2} + 2p^2z - rz + \frac{p^3}{2} - \frac{pr}{2} - \frac{q^2}{8} = 0 \newline
z^3 + \left(\frac{5p}{2}\right)z^2 + \left(2p^2 - r\right)z + \left(\frac{p^3}{2} - \frac{pr}{2} - \frac{q^2}{8}\right) = 0 \newline
$$

solving for `z` as a Cubic Polynomial:
> Discrimnants from Cubics Formula:
>
> $$
> p = \frac{c}{a^2} - \frac{b^2}{3a^3} \newline
> q = \frac{2b^3}{27a^3} - \frac{abc}{3a^3} + \frac{d}{a^2}
> $$ 
>
simplify:

$$
\Delta_0 = \frac{\left(2p^2 - r\right)}{(1)^2} - \frac{\left(\frac{5p}{2}\right)^2}{3(1)^3} \newline
\Delta_0 = \left(2p^2 - r\right) - \frac{\left(\frac{25p^2}{4}\right)}{3} \newline
\Delta_0 = 2p^2 - r - \frac{25p^2}{12} \newline
\Delta_0 = \frac{24p^2}{12} - r - \frac{25p^2}{12} \newline
\Delta_0 = - \frac{p^2}{12} - r\newline
$$

$$
\Delta_1 = \frac{2\left(\frac{5p}{2}\right)^3}{27(1)^3} - \frac{(1)\left(\frac{5p}{2}\right)\left(2p^2 - r\right)}{3(1)^3} + \frac{\left(\frac{p^3}{2} - \frac{pr}{2} - \frac{q^2}{8}\right)}{(1)^2} \newline
\Delta_1 = \frac{2\left(\frac{125p^3}{8}\right)}{27} - \frac{\left(5p\right)\left(2p^2 - r\right)}{6} + \left(\frac{p^3}{2} - \frac{pr}{2} - \frac{q^2}{8}\right) \newline
\Delta_1 = \frac{125p^3}{108} - \frac{10p^3 - 5pr}{6} + \frac{p^3}{2} - \frac{pr}{2} - \frac{q^2}{8} \newline
\Delta_1 = \frac{125p^3}{108} - \frac{5p^3}{3} + \frac{5pr}{6} + \frac{p^3}{2} - \frac{pr}{2} - \frac{q^2}{8} \newline
\Delta_1 = \frac{125p^3}{108} - \frac{180p^3}{108} + \frac{5pr}{6} + \frac{54p^3}{108} - \frac{3pr}{6} - \frac{q^2}{8} \newline
\Delta_1 = \frac{179p^3 - 180p^3}{108} + \frac{2pr}{6} - \frac{q^2}{8} \newline
\Delta_1 = - \frac{p^3}{108} + \frac{pr}{3} - \frac{q^2}{8} \newline
$$

we get:
$$
\Delta_0 = -\frac{p^2}{12} - r\newline
\Delta_1 = -\frac{p^3}{108} + \frac{pr}{3} - \frac{q^2}{8}
$$

$$
z = \sqrt[3]{- \frac{\Delta_1}{2} + \sqrt{\left(\frac{\Delta_1}{2}\right)^2 + \left(\frac{\Delta_0}{3}\right)^3}} + \sqrt[3]{- \frac{\Delta_1}{2} - \sqrt{\left(\frac{\Delta_1}{2}\right)^2 + \left(\frac{\Delta_0}{3}\right)^3}} - \frac{\Delta_0}{3}
$$

now continue:

$$
(y^2 + p + z)^2 = (p + 2z)y^2 + (- q)y + (p^2 + 2zp + z^2 - r)\newline
(y^2 + p + z)^2 = \left(\sqrt{p + 2z}y\right)^2 + 2 \left(\frac{- q}{2\sqrt{p + 2z}}\right) \left(\sqrt{p + 2z}y\right) + \left(\frac{- q}{2\sqrt{p + 2z}}\right)^2\newline

(y^2 + p + z)^2 = \left(\sqrt{p + 2z}y + \frac{- q}{2\sqrt{p + 2z}}\right)^2 \newline
\sqrt{(y^2 + p + z)^2} = \sqrt{\left(\sqrt{p + 2z}y + \frac{- q}{2\sqrt{p + 2z}}\right)^2} \newline
y^2 + p + z = \sqrt{p + 2z}y + \frac{- q}{2\sqrt{p + 2z}} \newline
y^2 + (- \sqrt{p + 2z})y + \left(p + z + \frac{- q}{2\sqrt{p + 2z}}\right) = 0 \newline
$$
solving as a quadratic:
$$
y = \frac{\sqrt{p + 2z}}{2} + \frac{1}{2}\sqrt{p + 2z - 4\left(p + z + \frac{- q}{2\sqrt{p + 2z}}\right)}
$$

final step:

$$
x = y - \frac{b}{4a}
$$
$$
y - \frac{b}{4a} = - \frac{b}{4a} + \frac{\sqrt{p + 2z}}{2} + \frac{1}{2}\sqrt{p + 2z - 4\left(p + z + \frac{- q}{2\sqrt{p + 2z}}\right)}
$$

$$
x = - \frac{b}{4a} + \frac{\sqrt{p + 2z}}{2} + \frac{1}{2}\sqrt{p + 2z - 4\left(p + z + \frac{- q}{2\sqrt{p + 2z}}\right)}
$$

## Root Formula
$$
ax^4 + bx^3 + cx^2 + dx + e = 0
$$

$$
x = - \frac{b}{4a} + \frac{\sqrt{p + 2z}}{2} + \frac{1}{2}\sqrt{p + 2z - 4\left(p + z + \frac{- q}{2\sqrt{p + 2z}}\right)}
$$

when $a \neq 0$ and where:

$$
z = \sqrt[3]{- \frac{\Delta_1}{2} + \sqrt{\left(\frac{\Delta_1}{2}\right)^2 + \left(\frac{\Delta_0}{3}\right)^3}} + \sqrt[3]{- \frac{\Delta_1}{2} - \sqrt{\left(\frac{\Delta_1}{2}\right)^2 + \left(\frac{\Delta_0}{3}\right)^3}} - \frac{\Delta_0}{3}
$$

$$
\Delta_0 = -\frac{p^2}{12} - r\newline
\Delta_1 = -\frac{p^3}{108} + \frac{pr}{3} - \frac{q^2}{8}
$$

$$
p = \frac{- 3b^2 + 8ac}{ 8a^2  }\newline
$$
$$
q =   \frac{b^3 - 4abc - 8a^2d }{ 8a^3  }\newline
$$
$$
r = \frac{- 3b^4 + 16ab^2c - 64a^2bd + 256a^3e}{256a^4}\newline
$$

It is impractical to use by hand however there is an implementation of it within this library:
[`code (python)`](../../scripts/experiment.py)
