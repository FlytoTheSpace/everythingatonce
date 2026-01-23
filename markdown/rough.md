

$$
\det([\vec{v}, \vec{u}]) = |\vec{v}| |\vec{u}| |\vec{w}| \sin(\theta_u) \sin(\theta_w)
$$

$$
\newcommand{\proj}[1]{\text{proj}#1}
\newcommand{\span}[1]{\text{span}#1}
$$

$$
\vec{p} = \proj(\vec{w})
$$
$$
\vec{p} \in \span(\vec{v}, \vec{u}) \newline
\vec{p} = \alpha\vec{v} + \beta\vec{u} \newline
$$

$$
\begin{cases}
\vec{v} \cdot (\vec{w} - \vec{p}) = 0 \newline
\vec{u} \cdot (\vec{w} - \vec{p}) = 0 \newline
\end{cases}
$$
$$
\begin{cases}
\vec{v} \cdot (\vec{w} - \alpha\vec{v} - \beta\vec{u}) = 0 \newline
\vec{u} \cdot (\vec{w} - \alpha\vec{v} - \beta\vec{u}) = 0 \newline
\end{cases}
$$
$$
\begin{cases}
\vec{v} \cdot \vec{w} - (\vec{v} \cdot \alpha\vec{v} + \vec{v} \cdot \beta\vec{u}) = 0 \newline
\vec{u} \cdot \vec{w} - (\vec{u} \cdot \alpha\vec{v} + \vec{u} \cdot \beta\vec{u}) = 0 \newline
\end{cases}
$$

$$
\begin{cases}
- \alpha (\vec{v} \cdot\vec{v}) - \beta(\vec{v} \cdot \vec{u}) + (\vec{v} \cdot \vec{w}) = 0 \newline
- \alpha (\vec{u} \cdot\vec{v}) - \beta(\vec{u} \cdot \vec{u}) + (\vec{u} \cdot \vec{w}) = 0 \newline
\end{cases}
$$

$$
\begin{cases}
- \alpha (\vec{v} \cdot\vec{v}) - \beta(\vec{v} \cdot \vec{u}) + (\vec{v} \cdot \vec{w}) = 0 \newline
- \alpha (\vec{u} \cdot\vec{v}) - \beta(\vec{u} \cdot \vec{u}) + (\vec{u} \cdot \vec{w}) = 0 \newline
\end{cases}
$$

Linear Systems of Equations
$$
\begin{cases}
\alpha (-1)(\vec{v} \cdot \vec{v}) + \beta(-1)(\vec{v} \cdot \vec{u}) + (\vec{v} \cdot \vec{w}) = 0 \newline
\alpha (-1)(\vec{u} \cdot \vec{v}) + \beta(-1)(\vec{u} \cdot \vec{u}) + (\vec{u} \cdot \vec{w}) = 0 \newline
\end{cases}
$$

$$
\beta = \frac{(\vec{v} \cdot \vec{w}) - \alpha (\vec{v} \cdot \vec{v})}{\vec{v} \cdot \vec{u}} = \frac{(\vec{u} \cdot \vec{w}) - \alpha (\vec{u} \cdot \vec{v})}{\vec{u} \cdot \vec{u}} \newline
\frac{(\vec{v} \cdot \vec{w})}{\vec{v} \cdot \vec{u}} - \alpha \frac{(\vec{v} \cdot \vec{v})}{\vec{v} \cdot \vec{u}} = \frac{(\vec{u} \cdot \vec{w})}{\vec{u} \cdot \vec{u}} - \alpha \frac{(\vec{u} \cdot \vec{v})}{\vec{u} \cdot \vec{u}} \newline
$$
$$
\left(\frac{\vec{v} \cdot \vec{w}}{\vec{v} \cdot \vec{u}} - \frac{\vec{u} \cdot \vec{w}}{\vec{u} \cdot \vec{u}} \right) + \alpha \left( \frac{\vec{u} \cdot \vec{v}}{\vec{u} \cdot \vec{u}} - \frac{\vec{v} \cdot \vec{v}}{\vec{v} \cdot \vec{u}} \right) = 0 \newline
$$
$$
\alpha = \large \frac{\frac{\vec{v} \cdot \vec{w}}{\vec{v} \cdot \vec{u}} - \frac{\vec{u} \cdot \vec{w}}{\vec{u} \cdot \vec{u}}}{\frac{\vec{u} \cdot \vec{v}}{\vec{u} \cdot \vec{u}} - \frac{\vec{v} \cdot \vec{v}}{\vec{v} \cdot \vec{u}}} \normalsize \newline
$$

$$
\alpha = \frac{(\vec{v} \cdot \vec{w})(\vec{u} \cdot \vec{u}) - (\vec{u} \cdot \vec{w})(\vec{v} \cdot \vec{u})}{(\vec{u} \cdot \vec{v})(\vec{v} \cdot \vec{u}) - (\vec{v} \cdot \vec{v})(\vec{u} \cdot \vec{u})} \newline
$$

...

General Case:



Testing:

$$
\bigcup_{123}
$$

$$

$$

Expression Simplify:

$$
(x + a_1)(x + a_2)(x + a_3) = K_{0}^{3} + K_{1}^{3} x^{1} + K_{2}^{3} x^{2}+ K_{3}^{3} x^{3} \newline
(x + a_1)(x + a_2)(x + a_3)(x + a_4) 
= (K_{0}^{3}x^{0} + K_{1}^{3}x^{1} + K_{2}^{3}x^{2} + K_{3}^{3}x^{3})(x + a_4) \newline
= K_{0}^{3}x^{1} + K_{1}^{3}x^{2} + K_{2}^{3}x^{3} + K_{3}^{3}x^{4} + K_{0}^{3}a_4x^{0} + K_{1}^{3}a_4x^{1} + K_{2}^{3}a_4x^{2}+ K_{3}^{3}a_4x^{3} \newline
= K_{0}^{3}a_4x^{0} + K_{0}^{3}x^{1} + K_{1}^{3}a_4x^{1} + K_{1}^{3}x^{2} + K_{2}^{3}a_4x^{2} + K_{2}^{3}x^{3} + K_{3}^{3}a_4x^{3} + K_{3}^{3}x^{4} \newline
= K_{0}^{3}a_4x^{0} + (K_{0}^{3} + K_{1}^{3}a_4)x^{1} + (K_{1}^{3} + K_{2}^{3}a_4)x^{2} + (K_{2}^{3} + K_{3}^{3}a_4)x^{3} + K_{3}^{3}x^{4} \newline
$$

$$
K_{0}^{4} = K_{0}^{3} \newline
K_{1}^{4} = K_{0}^{3} + K_{1}^{3}a_4 \newline
K_{2}^{4} = K_{1}^{3} + K_{2}^{3}a_4 \newline
K_{3}^{4} = K_{2}^{3} + K_{3}^{3}a_4 \newline
K_{4}^{4} = K_{3}^{3} + \underbrace{K_{4}^{3}a_4}_{0} \newline
$$

$$
K_{i} \newline
K_{i}^{n} = K_{i}^{n - 1} a_{n} + K_{i - 1}^{n - 1} \newline
$$