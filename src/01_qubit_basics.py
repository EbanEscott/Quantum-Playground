"""Lesson 01: Qubit basics with Qiskit.

This script covers:
1. Single-qubit superposition with the H gate.
2. Bell-state creation (entanglement).
3. Measurement comparisons using low vs high shot counts.
"""

from __future__ import annotations

from qiskit import QuantumCircuit, transpile
from qiskit.providers.basic_provider import BasicSimulator


def run_circuit(circuit: QuantumCircuit, shots: int) -> dict[str, int]:
    """Run a circuit on the built-in simulator and return measurement counts."""
    backend = BasicSimulator()
    compiled_circuit = transpile(circuit, backend)
    job = backend.run(compiled_circuit, shots=shots)
    result = job.result()
    return result.get_counts(compiled_circuit)


def to_probabilities(counts: dict[str, int]) -> dict[str, float]:
    """Convert measurement counts into probabilities for easier interpretation."""
    total = sum(counts.values())
    return {state: count / total for state, count in sorted(counts.items())}


def single_qubit_h(shots: int = 1024) -> dict[str, int]:
    """Create a superposition with H, then measure one qubit."""
    # QuantumCircuit(num_qubits, num_classical_bits)
    circuit = QuantumCircuit(1, 1)
    # Apply H to qubit index 0 (the only qubit in this circuit).
    circuit.h(0)
    # Measure qubit 0 and store the result in classical bit 0.
    # Indices must be in range or Qiskit raises an index error.
    circuit.measure(0, 0)
    return run_circuit(circuit, shots=shots)


def bell_state(shots: int = 1024) -> dict[str, int]:
    """Create a Bell state using H + CX and measure both qubits."""
    # This circuit has 2 qubits and 2 classical bits.
    circuit = QuantumCircuit(2, 2)
    # Put qubit 0 into superposition.
    circuit.h(0)
    # Controlled-X: qubit 0 is control and qubit 1 is target.
    circuit.cx(0, 1)
    # Measure qubits [0, 1] into classical bits [0, 1] one-to-one.
    # All listed indices must exist in their respective registers.
    circuit.measure([0, 1], [0, 1])
    return run_circuit(circuit, shots=shots)


def compare_shots() -> tuple[dict[str, int], dict[str, int]]:
    """Measure the same circuit at low and high shot counts."""
    low_shots_counts = single_qubit_h(shots=100)
    high_shots_counts = single_qubit_h(shots=10_000)
    return low_shots_counts, high_shots_counts


def main() -> None:
    """Run Lesson 01 experiments and print easy-to-read summaries."""
    print("=== Lesson 01: Single Qubit with H ===")
    h_counts = single_qubit_h()
    print("Counts:", h_counts)
    print("Probabilities:", to_probabilities(h_counts))

    print("\n=== Lesson 01: Bell State ===")
    bell_counts = bell_state()
    print("Counts:", bell_counts)
    print("Probabilities:", to_probabilities(bell_counts))

    print("\n=== Lesson 01: Shot Comparison (100 vs 10000) ===")
    low_counts, high_counts = compare_shots()
    print("100 shots counts:", low_counts)
    print("100 shots probabilities:", to_probabilities(low_counts))
    print("10000 shots counts:", high_counts)
    print("10000 shots probabilities:", to_probabilities(high_counts))


if __name__ == "__main__":
    main()
