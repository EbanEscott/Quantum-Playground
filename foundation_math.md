# Foundation Math Reference

A fundamentals-first refresher before quantum-specific math.

## 1) Algebra Basics

- Variable: symbol for an unknown value.
- Expression: combination of numbers, variables, and operations.
- Equation: statement that two expressions are equal.

Core operations:

- Distributive law: $a(b + c) = ab + ac$
- Factoring: $ab + ac = a(b + c)$
- Exponent rules:
  - $a^m a^n = a^{m+n}$
  - $a^{-n} = 1/a^n$
  - $(a^m)^n = a^{mn}$

## 2) Functions and Graphs

- Function: maps each input to exactly one output.
- Linear function: $f(x) = mx + b$
- Quadratic function: $f(x) = ax^2 + bx + c$

Why this matters:
- Many physics and optimization problems are expressed as functions.

## 3) Trigonometry Essentials

- Right-triangle ratios: sine, cosine, tangent.
- Unit circle links:
  - $\cos(\theta)$ = x-coordinate
  - $\sin(\theta)$ = y-coordinate

Key identity:

$$
\sin^2(\theta) + \cos^2(\theta) = 1
$$

## 4) Complex Numbers

- Standard form: $z = a + bi$
- Imaginary unit: $i^2 = -1$
- Conjugate: $z^* = a - bi$
- Magnitude: $|z| = \sqrt{a^2 + b^2}$

Euler form:

$$
e^{i\theta} = \cos\theta + i\sin\theta
$$

Why this matters:
- Quantum amplitudes are complex numbers.

## 5) Vectors

A vector is an ordered list of numbers, for example:

$$
\mathbf{v} = \begin{bmatrix} v_1 \\ v_2 \end{bmatrix}
$$

Core operations:

- Addition: $\mathbf{u} + \mathbf{v}$
- Scalar multiply: $c\mathbf{v}$
- Dot product: $\mathbf{u}\cdot\mathbf{v}$
- Length (norm): $\|\mathbf{v}\| = \sqrt{\mathbf{v}\cdot\mathbf{v}}$

## 6) Matrices

Matrix example:

$$
A = \begin{bmatrix} a & b \\ c & d \end{bmatrix}
$$

Important operations:

- Matrix-vector multiply: $A\mathbf{v}$
- Matrix-matrix multiply: $AB$
- Identity matrix: $I$ (does not change vectors)
- Inverse matrix: $A^{-1}$ if it exists

## 7) Linear Transformations

A matrix represents a transformation of vectors:

$$
\mathbf{v}' = A\mathbf{v}
$$

Interpretation:
- Rotations, reflections, scalings, and shears are all matrix transformations.

Why this matters:
- Quantum gates are special matrix transformations.

## 8) Probability Basics

- Probability range: $0 \le P(E) \le 1$
- Total probability over all outcomes is 1.
- Complement: $P(\text{not }E) = 1 - P(E)$

If outcomes are independent:

$$
P(A \cap B) = P(A)P(B)
$$

Expected value (discrete):

$$
\mathbb{E}[X] = \sum x_i p_i
$$

## 9) Statistics for Experiments

- Sample vs population
- Mean and variance
- Random fluctuation decreases with larger sample size

Rule of thumb:
- Sampling error often scales like $1/\sqrt{N}$.

Why this matters:
- More shots in simulation produce more stable observed frequencies.

## 10) Bridge to Quantum Math

From this file to quantum topics:

1. Complex numbers -> amplitudes
2. Vectors -> state vectors
3. Matrices -> gates
4. Matrix-vector multiplication -> state evolution
5. Probability/statistics -> measurement outcomes and shot-based estimates

## 11) Quick Review Checklist

- Can you multiply a 2x2 matrix by a 2x1 vector?
- Can you compute a vector norm?
- Can you explain complex magnitude?
- Can you normalize a 2-entry vector so its squared magnitudes sum to 1?
- Can you compute simple probabilities from repeated trials?

If yes, you have the math foundation needed for the current quantum exercises.
