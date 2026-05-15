
- [Back to Maths](./maths.md)
- [Back to Home](../../README.md)


$$\newcommand{\ray}{\text{Ray}}$$

# Geometry

**Primitive Objects**:

| Name  | Symbolic                      |
| ----- | ----------------------------- |
| Point | $A, B, C, D,E ...$            |
| Line  | $l, m, n, ...$                |
| Plane | $\rho, \sigma, \tau ...$      |


**Primitive Relations**:

- *Incidence*: $A \in l$, $l \in \rho$, $A \in \rho$
- *Betweenness*: $A * B * C$
- *Segment Congruence*: $\overline{AB} \cong \overline{CD}$
- *Angle Equality*: $\angle ABC = \angle XYZ$

# Axioms

**1. Incidence**:

- $I_1$. Exists a Unique line between any 2 distinct points:

$$\forall A, B[A \neq B \implies \exist l (A \in l \land B \in l)]$$

- $I_2$. Exists atleast 2 points exist on any given line:

$$\forall l \exist A, B(A \neq B \land A \in l \land B \in l)$$

- $I_3$. Exists 3 points such that no line covers them:

$$\exist A, B, C \lnot \exist l [A \in l \land B \in \land C \in l]$$

- $I_4$. If no line contains 3 given points there exists a unique plane that contains them:

$$\forall A, B, C [\lnot \exist l (A \in l \land B \in l \land C \in l) \implies \exist ! \rho(A \in \rho \land B \in \rho \land C \in \rho \land ABC = \rho)]$$

> Note: may also needs a more generic version (without uniqueness condition) as:
> $$\forall A, B, C \exist \rho[A \in \rho \land B \in \rho \land C \in \rho]$$

> wiki (original):
> $$\forall A, B, C [\lnot \exist l (A \in l \land B \in l \land C \in l) \implies \exist ! \rho(A \in \rho \land B \in \rho \land C \in \rho)]$$

- $I_5$. exists 3 points on a plane such that no line contains them:

$$\forall \rho \exist A, B, C [A \in \rho \land B \in \rho \land C \in \rho \land \lnot \exists l (A \in l \land B \in l \land C \in l)]$$

- $I_6$. If 2 distinct points are contained by both a line and a plane then that plane contains the line as well.

$$\forall A, B, l, \rho [(A \neq B \land A \in l \land B \in l \land A \in \rho \land B \in \rho) \implies l \in \rho]$$

- $I_7$. for any 2 distinct planes if they share a point then they share another point in common.

$$\forall \rho, \sigma \exist A[(A \in \rho \land A \in \sigma) \implies \exist B(A \neq B \land B \in \rho \land B \in \sigma)]$$

> Wiki:
> *for any 2 distinct planes if they share a point then they share a whole line in common*
> $$\color{gray} \forall \rho, \sigma[\exist A(A \in \rho \land A \in \sigma) \implies \exist l \forall B (B \in l \iff B \in \rho \land B \in \sigma)]$$
> fault: can be turned into a theorem.

> Wiki (Original):
> $$\color{gray} \forall \rho, \sigma[\rho \neq \sigma \land \exist A(A \in \rho \land A \in \sigma) \implies \exist l \forall B (B \in l \iff B \in \rho \land B \in \sigma)]$$
> fault: statement holds even when $\rho = \sigma$

- $I_8$. there exists 4 points such that no plane covers them.

$$\exist A, B, C, D \lnot \exist \rho [A \in \rho \land B \in \rho \land C \in \rho]$$

**2. Betweenness**:

- $B_1$. Betweeness is a symmetric relation and implies all 3 points are (1) distinct, (2) lie on the same line (colinear)

$$\forall A, B, C [A * B * C \implies (C * B * A \land A \neq B \land A \neq C \land B \neq C \land \exists l (A \in l \land B \in l \land C \in l))]$$

- $B_2$. for any 2 distinct points there exist a 3rd point such that they are collinear

$$\forall A, C [A \neq C \implies \exist B (A * B * C)\land \exist D (A * C * D)]$$

> Wiki (Original):
> $$\color{gray} \forall A, B [A \neq B \implies \exist C (A * B * C)]$$

- $B_3$. only 1 point can be admist the other 2.

$$\forall A, B, C [A * B * C \oplus B * A * C \oplus A * C * B]$$

- $B_4$. if a line passes through one of the line segments made by 3 points then that line must also pass through one of the other 2 line segments made by the 3 points.

$$\forall A, B, C, l[\lnot \exist m (A \in m \land B \in m  \land C \in m) \land \exists P(P \in l \land P \in \overline{AB}) \land \lnot (A \in l \lor B \in l \lor C \in l) \implies \exists Q [Q \in l \land (Q \in \overline{AC} \lor Q \in \overline{BC})]]$$

> Original:
> $$\forall A, B, C, l[(A, B, C \text{ non collinear}) \land (l \text{ intersects } AB) \land \lnot (l \text{ passes through } A, B, C) \implies (l \text{ intersects } AC \lor l \text{ intersects } BC)]$$
**3. Congruence**:

- $C_1$. 

$$\forall A, B, P, R \exists Q [\ray(P, R, Q) \land \overline{AB} \cong \overline{PQ}]$$

- $C_2$. Laws of Equivalence Relation, Segment Congruence

	- $C_{2.1}$. Reflexive:

	$$\forall A, B[\overline{AB} \cong \overline {AB}]$$

	- $C_{2.2}$. Symmetric:

	$$\forall A, B, P, Q[\overline{AB} \cong \overline {PQ} \iff \overline{PQ} \cong \overline {AB}]$$

	- $C_{2.3}$. Transitive:

	$$\forall A, B, P, Q, X, Y[(\overline{AB} \cong \overline{PQ} \land \overline{PQ} \cong \overline{XY}) \implies \overline{AB} \cong \overline{XY}]$$

- $C_3$.

$$\forall l, m, A, B, C, P, Q, R [(A \in l \land B \in l \land C \in l \land P \in m \land Q \in m \land R \in m \land \overline{AB} \cong \overline{PQ} \land \overline{BC} \cong \overline{QR}) \implies \overline{AC} \cong \overline{PR}]$$

> original:
> $$\color{gray} \forall A, B, C, P, Q, R [(\overline{AB} \cong \overline{PQ} \land \overline{BC} \cong \overline{QR}) \implies \overline{AC} \cong \overline{PR}]$$
> fault: implicit assumption of colinearity with points $A,B,C$ and $P,Q,R$

- $C_4$.

$$\forall A, B, C, P, Q, \exist R [\angle ABC = \angle PQR]$$

> original:
> $$\color{gray} \forall A, B, C, P, Q, \exist !R [\angle ABC = \angle PQR]$$
> fault: R is not unique, many points can subtend same angles.

- $C_5$. Laws of Equivalence Relation, Angle Equality

	- $C_{5.1}$.

	$$\forall A, B, C [\angle ABC = \angle ABC]$$

	- $C_{5.2}$.

	$$\forall A, B, C, P, Q, R[\angle ABC = \angle PQR \implies \angle PQR = \angle ABC]$$
	
	- $C_{5.3}$.

	$$\forall A, B, C, P, Q, R, X, Y, Z[(\angle ABC = \angle PQR \land \angle PQR = \angle XYZ) \implies \angle ABC = \angle XYZ]$$

- $C_6$.

$$\forall A, B, C, P, Q, R [(\overline{AB} \cong \overline{PQ} \land \overline{AC} \cong \overline{PR} \land \angle BAC = QPR) \implies \angle ACB = \angle {PRQ}]$$

**4. Parallels**:

$$\forall A, l [A \notin l \implies \exist !m (A \in m \land \lnot \exist B (B \in m \land B \in l))]$$

**5. Continuity**:

$$\forall l \forall X \subset \{P\ |\ P \in l\} \forall Y \subset \{P\ |\ P \in l\}[X \neq \emptyset \land Y \neq \emptyset \land X \cup Y = \{P\ |\ P \in l\} \land X \cap Y = \emptyset \land \forall x \in X \forall y \in Y \lnot \exist z (z \in l \land x * z * y) \implies \exist c (c \in l \land \forall x \in X \forall y \in Y(x * c * y \lor x = c \lor y = c))]$$
> The only axiom here I don't fully understand or agree with.

- [`Source (Wikipedia)`](https://en.wikipedia.org/wiki/Hilbert%27s_axioms)

All of these were the Hilbert's Axioms for Geometry.

# Elementary Results


a 'straight angle' is defined as the following for $A*B*C$:

$$180\degree = \angle ABC$$

and a 'right angle' as:

$$$$


we define a triangle $\triangle ABC$ such that the points $A, B, C$ are distinct:

$$A \neq B \land A \neq C \land B \neq C$$

# Naive:

**Geometry**: a field of Mathematics consisting Entirely of Geometric Shapes and their Properties

- [Symmetry](#symmetry)
- [2D](#2D)
	- [Lines](#lines)
	- [Curves](#curves)
	- [Angles](#angles)
	- [Circle](#circle)
	- [Polygon](#polygon)
- [3D](#3D)
	- [Segments](#segments)
	- [Sphere](#sphere)
	- [Cube](#Cube)

Properties:
- **Vertex**: Meeting Point of 2 Line Segments
- **Adjacent sides**: lines that share a common vertex.
- **Adjacent angles**: angles that share a common side.

**Congruent**: when 2 shapes are equal and have the same size

# Symmetry

**Symmetry**: Figures with Evenly Balanced Proportions

## Lines

**Line Segment**: A Line that stop at 2 distinct points.

**Pairs**:
- **Point of Intersection**: when 2 lines cross each other and a point is formed

- **Parallel lines**: Lines that can Never Meet at any point.

- **Bisector**: a Line that divides another line or any Shape into 2 Pieces

- **Perpendicular**: when 2 Lines meet at 1 point and the Angle between them is $90\deg$ (`Right Angle`)

- **Perpendicular Bisector**: When a Line Bisects another line or Shape and the angle between them is a Right Angle

- **Transversal**: A lines that intersects two or more lines at distinct points

## Curves

**Simple Curve**: A Curve that doesn't cross itself

**Open Curve**: A Curve whose both points doesn't join each other

**Closed Curve**: A Curve whose both points joins each other

- **Interior**: Area Inside the Curve
- **Boundary**: Boundary of the Curve
- **Exterior**: Area Outside the Curve
- **Region**: Interior and Boundary

## Angles

Unit:

Angles measured in degrees 

- $A$ = angle

- $A\degree$ $A\deg$

- $360\degree$ is the maximum value.

Types:
- **Acute Angle**: in which angle is $<90\degree$
- **Right Angle**: in which angle is $90\degree$
- **Obtuse Angle**: in which angle is greater than $90\degree$ and less than $180\degree$.

	$\angle a > 90\degree \land  \angle a < 180\degree$

- **Straight Angle**: in which angle is $180\degree$
- **Reflex Angle**: in which angle is greater than $180\degree$ and less than $360\degree$.

	$\angle a > 180\degree \land  \angle a < 360\degree$

- **Complete Angle**: in which angle is $360\degree$

Sum Types:
- **Complementary Angles**: when sum of 2 angles equals to $90\degree$

	$\angle a + \angle b = 90\degree$

- **Supplementary Angles**: when sum of 2 angles equals to $180\degree$

	$\angle a + \angle b = 180\degree$

# 2D

**Perimeter**: Length along the Boundaries of any Shape.

**Area**: Amount of space covered by any Shape.

## Circle

Line Segments and Curves:

![](../../img/maths/shapes/circle_segments.png)

- **Radius**, $r$: length from the Center of the circle to it's boundary in a straight line.
	- *Raddi*: plural for 2Radius

- **Diameter**, $2r$: length from one side of the boundary of the circle to it's opposite side boundary in a straight line.

- **Circumference**: Length of the Entire Boundary (`Perimeter`) of the Circle

$$
2\pi r
$$

- **Chord**: a Line Connecting 2 Points on the Boundary of the Circle

Areas:

- **Complete Area**:
		
$$
\pi r^2
$$

- **Arc**: A specific area of the Boundary of the Circle

- **Sector**: Region in the interior of a circle enclosed by Arc and Raddi

- **Segment**: Region in the interior of a circle enclosed by a chord and the arc

Similar Shapes
- **Semi-circle**: Half of a Circle
- **Quadrant**: Quarter of a Circle

## Polygon

**Polygon**: A simple closed Shape made up only line segments

Properties:
- **Equiangular**: All interior angles equivalent to each-other.
- **Equilateral**: Length of all sides equivalent to each-other.
- **Diagonals**: lines that join any 2 opposite vertex of a Polygon.
- Sum of all exterior angles of any Polygon is `360\degree`deg.

Types:

- **Regular Polygon**: A Polygon which is Both Equiangular and Equilateral
- **Concave Polygon**: A Polygon with an In-words Curve
- **Convex Polygon**: A Polygon without any In-words Curve

### Triangle

---

**Triangle**: A Polygon with 3 sides

Properties: 
- $180\deg$ Sum of all Interior Angles
- Regular: $60\deg$
- Area: 
	$$\frac{1}{2}hb$$

**Types of triangles**
> The 3 Sides of the Triangle are declared as $a, b, c$ for representation purposes in this example
- **Side Length Based**:
	- **Scalene Triangle**: A Triangle with all of it's sides Unequal 
	$$a \neq b \neq c$$
	- **Isosceles Triangle**: A Triangle with 2 of it's sides equal and 1 not.
	$$a = b \neq c$$
	$$a \neq b = c$$
	$$a = c \neq b$$
	- **Equilateral Triangle**: A Triangle with all 3 of it's sides equal
	$$a = b = c$$
> The 3 Angles of the Triangle are declared as $a, b, c$ for representation purposes in this example
- **Angle Based**:
	- **Acute Angled Triangle**: A Triangle with All angles less than $90\deg$

	$$90 \deg > a,  b,  c$$
	- **Right Angled Triangle**: A Triangle with any one Angle equivalent to $90\deg$

	$$90 \deg = a \lor  b \lor  c$$
	- **Obtuse Angled Triangle**: A Triangle with any one Angle Greater than $90\deg$
	$$90 \deg > a \lor  b \lor  c$$


### Quadrilateral

---

**Quadrilateral**: A Polygon Type with 4 Sides and Vertexes

Properties: 
- $360\deg$ Sum of all Interior Angles
- Regular: $90\deg$

**Trapezium**: A Quadrilateral with a Set of parallel lines

![](../../img/maths/shapes/trapezium.png)
- **Area**:
	$\frac{1}{2}hb$

**Kite**: a Quadrilateral with 2 distinct consecutive pairs of equal length

**Parallelogram**: a Quadrilateral with 2 Pairs of Parallel Lines

![](../../img/maths/shapes/parallelogram.png)

- **Area**: 
	$hb$

**Rhombus**: a Quadrilateral, Equilateral

- **Area**: 
	$\frac{1}{2}hw$

**Rectangle**: a Quadrilateral, Equiangular with sets of 2 pairs of parallel lines

- **Area**: 
	$hb$

**Square**: a Quadrilateral, Regular Polygon, Equilateral and Equiangular.

- **Area**: 
	$a^2$

### Pentagon

---

**Pentagon**: A Polygon with 5 sides and vertex

- $540\deg$: sum of All Interior Angles
- Regular: $108\deg$

### Hexagon

---

**Hexagon**: A Polygon with 6 sides and vertex

- $720\deg$: sum of All Interior Angles
- Regular: $120\deg$

## 3D

## Segments

**Surface Area**: Amount of Area exposed to the Outside of an object
- **Net**: Flattened version of Surface of a 3D shape into a 2D space
- **Cross-Section**: Area which gets exposed when cutting open a 3D Object

**Volume**: Amount of Space occupied by a 3D Object

**Face**: flat surface side of a 3d Shape

**Edge**: meeting of 2 Faces at a line segment

**Vertex**: Intersection point of 3 

## Sphere


**Sphere**: A 3 Dimentional Circle

## **Cube**


## **Triangular**


### **Pyramid**

---

### **Tetrahedron**

---
