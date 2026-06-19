# Quantum Terminology Reference

This glossary covers the main terms used in Exercises 01 to 03.

## Core State Terms

- Qubit: The basic unit of quantum information. A 2-level quantum system.
- Basis states: Standard computational states |0> and |1>.
- Ket notation: A state label written like |psi>. 
- State vector: Vector form of a qubit state, often written as [alpha, beta]^T.
- Superposition: A state like alpha|0> + beta|1>, where both basis components are present.
- Amplitude: The coefficient (alpha or beta) attached to a basis state.
- Normalization: Constraint that |alpha|^2 + |beta|^2 = 1.
- Probability: Measurement likelihood from squared amplitude magnitude.

## Phase and Interference Terms

- Phase: Wave-angle information carried by amplitudes.
- Relative phase: Phase difference between basis components (for example, + vs -).
- Sign change: A phase flip like beta becoming -beta.
- Hidden phase: Phase information that may not change immediate measurement outcomes.
- Interference: Amplitudes adding or canceling after gate sequences.
- Constructive interference: Amplitudes add, increasing outcome likelihood.
- Destructive interference: Amplitudes cancel, decreasing outcome likelihood.

## Gate Terms

- Quantum gate: A reversible operation on qubits (unitary transform).
- X gate (Pauli-X): Bit flip on a qubit; maps |0> <-> |1>.
- Z gate (Pauli-Z): Phase flip; changes sign on the |1> component.
- H gate (Hadamard): Basis-change gate creating/using superposition.
- CX gate (CNOT): Controlled-X. Flips target only if control is 1.
- CCX gate (Toffoli): Double-controlled X. Flips target only if both controls are 1.

## Circuit Terms

- QuantumCircuit(n_qubits, n_classical_bits): Circuit with quantum wires and classical memory bits.
- Control qubit: Qubit that decides whether a controlled gate activates.
- Target qubit: Qubit modified when gate condition is satisfied.
- Measurement: Operation that maps qubit state to a classical bit outcome.
- measure(q, c): Measure qubit index q and store result in classical bit index c.
- Circuit diagram: Visual flow of gates left to right.

## Diagram Legend (Text Draw Output)

- q:: Quantum wire label.
- c:: Classical register label.
- M: Measurement operation.
- Single horizontal wire: Quantum wire.
- Double horizontal wire: Classical wire.
- Vertical connector from M to c: Measurement result mapping.

## Simulation Terms

- Simulator: Software backend that executes circuits without hardware noise (idealized by default).
- Shots: Number of repeated circuit runs used to estimate probabilities.
- Counts: Raw frequency results, for example {'0': 512, '1': 512}.
- Distribution: Normalized probabilities computed from counts.

## Useful Identities Seen So Far

- H|0> = (|0> + |1>) / sqrt(2)
- H|1> = (|0> - |1>) / sqrt(2)
- H * H = I (Hadamard twice gives identity)
- H * Z * H = X (phase can become measurable bit difference)

## Practical Notes

- Same immediate probabilities does not always mean same quantum state.
- Phase effects often appear only after additional gates.
- Larger shot counts reduce sampling noise in observed distributions.
