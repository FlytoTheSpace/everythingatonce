
- [Back to Maths](./maths.md)
- [Back to Home](../README.md)

# Trignometry
**Trignometry**: a sub-field of Geometry only consisting of Triangles and Their Angles related Geometry

![](../img/maths/shapes/right_triangle.png)

- $\theta$ is an angle that exists inside the Right angled Triangle
- **Hypotenuse**: is the Longer side, opposite to the right angle
- **Adjacent**: The shorter side, next to the angle $\theta$
- **Opposite**: The side that the angle $\theta$ does not lie next to

# Pythagoream Theorem
This Theorem that a Right Angled Triangle with sides $a$, $b$, $c$ where $a$ and $b$ are the legs of the right angled triangle, while $c$ is the Hypotenuse, have the following relation:
$$
a^2 + b^2 = c^2
$$

![](../img/maths/shapes/right_triangle_abc_squared.png)

# Trigometric Functions

<script src="../modules/function-plot.min.js"></script>

**Sine**, **sin**: The Ratio between the Opposite and the Hypotenuse side.


$$\sin(\theta) = \frac{\text{Opposite}}{\text{Hypotenuse}}$$

- **SOH**: standing for $\color{MediumSeaGreen}\sin\color{white}(\theta) = \text{\color{MediumSeaGreen}O\color{white}pposite} / \text{\color{MediumSeaGreen}H\color{white}ypotenuse}$

<div id="sinwave"></div>

**Cosine**, **cos**: The Ratio between the Adjacent and the Hypotenuse side.

<div id="coswave"></div>

$$\cos(\theta) = \frac{\text{Adjacent}}{\text{Hypotenuse}}$$

- **CAH**: standing for $\color{MediumSeaGreen}\cos\color{white}(\theta) = \text{\color{MediumSeaGreen}A\color{white}djacent} / \text{\color{MediumSeaGreen}H\color{white}ypotenuse}$

**Tangent**, **tan**: The Ratio between the Opposite and the Adjacent side.

$$\tan(\theta) = \frac{\text{Opposite}}{\text{Adjacent}}$$

<div id="tanwave"></div>

- **TOA**: standing for $\color{MediumSeaGreen}\tan\color{white}(\theta) = \text{\color{MediumSeaGreen}O\color{white}pposite} / \text{\color{MediumSeaGreen}A\color{white}djacent}$


**csc**: The Ratio between the Hypotenuse and the Opposite side.
$$\csc(\theta) = \frac{\text{Hypotenuse}}{\text{Opposite}}$$

**sec**: The Ratio between the Hypotenuse and the Adjacent side.
$$\sec(\theta) = \frac{\text{Hypotenuse}}{\text{Adjacent}}$$

**cot**: The Ratio between the Adjacent and the Opposite side.
$$\cot(\theta) = \frac{\text{Adjacent}}{\text{Opposite}}$$

<script>
    const sinwave = functionPlot({
        target: '#sinwave',
        width: 600,
        height: 400,
        grid: true,
        data: [
            {
                fn: 'sin(x)',
                color: "Dodgerblue"
            }
        ]
    });
    const coswave = functionPlot({
        target: '#coswave',
        width: 600,
        height: 400,
        grid: true,
        data: [
            {
                fn: 'cos(x)',
                color: "MediumSeaGreen"
            }
        ]
    });
    const tanwave = functionPlot({
        target: '#tanwave',
        width: 600,
        height: 400,
        grid: true,
        data: [
            {
                fn: 'tan(x)',
                color: "red"
            }
        ]
    });

    sinwave.addLink(coswave, tanwave);
    coswave.addLink(sinwave, tanwave);
    tanwave.addLink(sinwave, coswave);
</script>