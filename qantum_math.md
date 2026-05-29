# Quantum Math Reference

A compact refresher for the math used in Exercises 01 to 03.

## 1) Numbers and Notation

- Complex number: $z = a + bi$
- Magnitude (modulus): $|z| = \sqrt{a^2 + b^2}$
- Conjugate: $z^* = a - bi$
- Euler form: $e^{i\theta} = \cos\theta + i\sin\theta$

Why this matters:
- Quantum amplitudes are generally complex numbers.
- Probabilities come from squared magnitudes, not raw values.

## 2) Qubit as a Vector

A single qubit state is:

$$
|\psi\rangle = \alpha|0\rangle + \beta|1\rangle
$$

Vector form:

$$
|\psi\rangle = \begin{bmatrix} \alpha \\ \beta \end{bmatrix}
$$

Normalization:

$$
|\alpha|^2 + |\beta|^2 = 1
$$

Basis vectors:

$$
|0\rangle = \begin{bmatrix}1 \\ 0\end{bmatrix}, \quad
|1\rangle = \begin{bmatrix}0 \\ 1\end{bmatrix}
$$

## 3) Probability and Measurement

For

$$
|\psi\rangle = \alpha|0\rangle + \beta|1\rangle
$$

measurement in computational basis gives:

$$
P(0) = |\alpha|^2, \quad P(1) = |\beta|^2
$$

Key point:
- Measurement outputs classical bits.
- Amplitudes are not directly observed.

## 4) Inner Product and Norm

- Inner product: $\langle u|v\rangle$
- Norm squared: $\|v\|^2 = \langle v|v\rangle$

Orthonormal basis property:

$$
\langle 0|0\rangle = 1,\; \langle 1|1\rangle = 1,\; \langle 0|1\rangle = 0
$$

## 5) Gate as Matrix (Linear Algebra)

Gates are unitary matrices $U$ acting on state vectors:

$$
|\psi'\rangle = U|\psi\rangle
$$

Unitary condition:

$$
U^\dagger U = I
$$

This preserves total probability.

## 6) Common Gate Matrices (Seen So Far)

X gate:

$$
X = \begin{bmatrix}0 & 1 \\ 1 & 0\end{bmatrix}
$$

Z gate:

$$
Z = \begin{bmatrix}1 & 0 \\ 0 & -1\end{bmatrix}
$$

H gate:

$$
H = \frac{1}{\sqrt{2}}\begin{bmatrix}1 & 1 \\ 1 & -1\end{bmatrix}
$$

Useful identities:

$$
H|0\rangle = \frac{|0\rangle + |1\rangle}{\sqrt{2}}, \quad
H|1\rangle = \frac{|0\rangle - |1\rangle}{\sqrt{2}}
$$

$$
H^2 = I, \quad HZH = X
$$

## 7) Phase and Relative Phase

Two states can have same immediate measurement probabilities but differ by phase:

$$
|+\rangle = \frac{|0\rangle + |1\rangle}{\sqrt{2}}, \quad
|-\rangle = \frac{|0\rangle - |1\rangle}{\sqrt{2}}
$$

Both are 50/50 in Z-basis measurement.
The minus sign is a relative phase difference.

## 8) Interference (Add and Cancel)

Quantum algorithms use amplitude addition rules:

- Constructive interference: amplitudes add, increasing probability.
- Destructive interference: amplitudes cancel, decreasing probability.

Exercise 03 example:
- $H$ then measure: near 50/50.
- $HZH$ then measure: near 100% on 1 for input $|0\rangle$.

Same initial-looking probabilities can diverge after extra gates because phase is converted into measurable differences.

## 9) Two-Qubit Basis and Bitstrings

Two-qubit computational basis:

$$
|00\rangle, |01\rangle, |10\rangle, |11\rangle
$$

State lives in a 4-dimensional complex vector space.

Bell state used earlier:

$$
\frac{|00\rangle + |11\rangle}{\sqrt{2}}
$$

## 10) Tensor Product (Kronecker Product)

Combining qubits uses tensor product $\otimes$:

$$
|a\rangle \otimes |b\rangle
$$

Example:

$$
|0\rangle \otimes |1\rangle = |01\rangle
$$

This is the math behind multi-qubit state spaces and controlled operations.

## 11) Quick Formula Checklist

- $P(k) = |\text{amplitude of } |k\rangle|^2$
- $U^\dagger U = I$
- $|\alpha|^2 + |\beta|^2 = 1$
- $H^2 = I$
- $HZH = X$
- $|+\rangle = (|0\rangle + |1\rangle)/\sqrt{2}$
- $|-\rangle = (|0\rangle - |1\rangle)/\sqrt{2}$

## 12) How To Use This File

1. Before a lesson: skim sections 2, 3, 6.
2. During debugging intuition: check sections 7 and 8.
3. Before moving to algorithms: review sections 5, 9, 10.
