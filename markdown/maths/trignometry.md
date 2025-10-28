
- [Back to Maths](./maths.md)
- [Back to Home](../../README.md)

# Trignometry
**Trignometry**: a sub-field of Geometry only consisting of Triangles and Their Angles related Geometry

![](../../img/maths/shapes/right_triangle.png)

- $\theta$ is an angle that exists inside the Right angled Triangle
- **Hypotenuse**: is the Longer side, opposite to the right angle
- **Adjacent**: The shorter side, next to the angle $\theta$
- **Opposite**: The side that the angle $\theta$ does not lie next to

# Pythagoream Theorem
This Theorem that a Right Angled Triangle with sides $a$, $b$, $c$ where $a$ and $b$ are the legs of the right angled triangle, while $c$ is the Hypotenuse, have the following relation:
$$
a^2 + b^2 = c^2
$$

![](../../img/maths/shapes/right_triangle_abc_squared.png)

# Main Trigometric Functions

$\sin$ and $\cos$ are the solutions to the following equation:
$$ x^2 + y^2 = 1 $$
(equation of a unit circle centered at the origin)

$$\sin(\theta)^2 + \cos(\theta)^2 = 1$$

$$\tan(\theta) = \frac{\sin(\theta)}{\cos(\theta)}$$

$$ \csc(\theta) = \frac{1}{\sin(\theta)} $$
$$ \sec(\theta) = \frac{1}{\cos(\theta)} $$
$$ \cot(\theta) = \frac{1}{\tan(\theta)} $$

| Trig Function  | sin                                                | cos                                                | tan                                                     | csc                                                | sec                                               | cot                                                               |
| -------------- | -------------------------------------------------- | -------------------------------------------------- | --------------------------------------------------------| -------------------------------------------------- | ------------------------------------------------- | ----------------------------------------------------------------- |
| $\sin(\theta)$ | $\sin(\theta)$                                     | $\sqrt{1 - \cos(\theta)^2}$                        | $\frac{\tan(\theta)}{\sqrt{1 + \tan(\theta)^2} }$       | $\frac{1}{\csc(\theta)}$                           | $\sqrt{1 - \frac{1}{\sec(\theta)^2} }$            | $\frac{1}{\sqrt{1 + \cot(\theta)^2} }$                            |
| $\cos(\theta)$ | $\sqrt{1 - \sin(\theta)^2}$                        | $\cos(\theta)$                                     | $\sqrt{1 - \frac{\tan(\theta)^2}{1 + \tan(\theta)^2} }$ | $\sqrt{1 - \frac{1}{\csc(\theta)^2} }$             | $\frac{1}{\sec(\theta)}$                          | $\sqrt{1 - \frac{1}{1 + \cot(\theta)^2} }$                        |
| $\tan(\theta)$ | $\frac{\sin(\theta)}{\sqrt{1 - \sin(\theta)^2} }$  | $\frac{\sqrt{1 - \cos(\theta)^2} }{\cos(\theta)}$  | $\tan(\theta)$                                          | $\frac{1 }{\sqrt{\csc(\theta)^2 - 1} }$            | $\sqrt{\sec(\theta)^2 - 1}$                       | $\frac{1}{\cot(\theta)}$                                          |
| $\csc(\theta)$ | $\frac{1}{\sin(\theta)}$                           | $\frac{1}{\sqrt{1 - \cos(\theta)^2} }$             | $\frac{\sqrt{1 + \tan(\theta)^2} }{\tan(\theta)}$       | $\csc(\theta)$                                     | $\frac{\sec(\theta)}{\sqrt{\sec(\theta)^2 - 1} }$ | $\sqrt{\cot(\theta)^2 + 1}$                                       |
| $\sec(\theta)$ | $\frac{1}{\sqrt{1 -\sin(\theta)^2} }$              | $\frac{1}{\cos(\theta)}$                           | $\sqrt{1 + \tan(\theta)^2}$                             | $\frac{\csc(\theta)}{\sqrt{\csc(\theta)^2 - 1 } }$ | $\sec(\theta)$                                    | $\sqrt{1 + \frac{1}{\tan(\theta)^2} }$                            |
| $\cot(\theta)$ | $\frac{\sqrt{1 - \sin(\theta)^2} }{\sin(\theta)}$  | $\frac{\cos(\theta)}{\sqrt{1 - \cos(\theta)^2} }$  | $\frac{1}{\tan(\theta)}$                                | $\sqrt{\csc(\theta)^2 - 1}$                        | $\frac{1}{\sqrt{\sec(\theta)^2 - 1} }$            | $\cot(\theta)$                                                    |

# Identities:

> Context:
> $ \theta = \theta_{rad}$ same for $\alpha$ and $\beta$
> 
> $$ \theta_{rad} = \frac{2 \pi}{360}(\theta_{deg})$$
> 
> (for compactness use purpose)
> $$ S := \{\sin(\theta), \cos(\theta), \tan(\theta), \csc(\theta), \sec(\theta), \cot(\theta)\} $$

$$\forall (f \in S) [f(\theta \pm 2\pi) = f(\theta \mod 2\pi) = f(\theta)]$$

$$\sin(- \theta) = - \sin(\theta)$$
$$\cos(- \theta) = \cos(\theta)$$

**Pythagorean Identities**:

$$ \sin(\theta)^2 + \cos(\theta)^2 = 1$$
$$ 1 + \tan(\theta)^2 = \sec(\theta)^2$$
$$ 1 + \cot(\theta)^2 = \csc(\theta)^2$$

**Sum/Difference Identities**:

$$\sin(\alpha + \beta) = \sin(\alpha) \cdot \cos(\beta) + \cos(\alpha) \cdot \sin(\beta)$$
$$\sin(\alpha - \beta) = \sin(\alpha) \cdot \cos(\beta) - \cos(\alpha) \cdot \sin(\beta)$$
$$\cos(\alpha + \beta) = \cos(\alpha) \cdot \cos(\beta) - \sin(\alpha) \cdot \sin(\beta)$$
$$\cos(\alpha - \beta) = \cos(\alpha) \cdot \cos(\beta) + \sin(\alpha) \cdot \sin(\beta)$$

**Product Identites** (function):

$$\sin(\alpha) \cdot \sin(\beta) = \frac{\cos(\alpha - \beta) - \cos(\alpha + \beta)}{2}$$
$$\sin(\alpha) \cdot \cos(\beta) = \frac{\sin(\alpha - \beta) + \sin(\alpha + \beta)}{2}$$
$$\cos(\alpha) \cdot \cos(\beta) = \frac{\cos(\alpha - \beta) + \cos(\alpha + \beta)}{2}$$

**Square Identities**:

$$ \sin(\theta)^2 = \frac{1 - \cos(2x)}{2} $$
$$ \cos(\theta)^2 = \frac{1 + \cos(2x)}{2} $$

# Inverses:

each of the 6 trig functions have a defined Inverse function for symbolic purposes:

| Trig Function  | Inverse                                     |
| -------------- | ------------------------------------------- |
| $\sin(\theta)$ | $\sin^{-1}(\theta) = \arcsin(\theta)$       |
| $\cos(\theta)$ | $\cos^{-1}(\theta) = \arccos(\theta)$       |
| $\tan(\theta)$ | $\tan^{-1}(\theta) = \arctan(\theta)$       |
| $\csc(\theta)$ | $\csc^{-1}(\theta) = \text{arccsc}(\theta)$ |
| $\sec(\theta)$ | $\sec^{-1}(\theta) = \text{arcsec}(\theta)$ |
| $\cot(\theta)$ | $\cot^{-1}(\theta) = \text{arccot}(\theta)$ |
