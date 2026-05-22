"""Lesson 02: Gate intuition drills with Qiskit.

This lesson focuses on X, Z, CX, and CCX behavior through
prediction-first experiments and measurement counts.
"""

from __future__ import annotations

from qiskit import QuantumCircuit, transpile
from qiskit.providers.basic_provider import BasicSimulator


# ── Helpers ──────────────────────────────────────────────────────────────
def run_counts(circuit: QuantumCircuit, shots: int = 1024) -> dict[str, int]:
    """Run a circuit on BasicSimulator and return measurement counts."""
    backend = BasicSimulator()
    compiled = transpile(circuit, backend)
    job = backend.run(compiled, shots=shots)
    return job.result().get_counts(compiled)


def probs(counts: dict[str, int]) -> dict[str, float]:
    """Convert counts to sorted probabilities."""
    total = sum(counts.values())
    return {state: value / total for state, value in sorted(counts.items())}


def report(title: str, circuit: QuantumCircuit, shots: int = 1024) -> None:
    """Print circuit, counts, and probabilities for one experiment."""
    print(f"\n=== {title} ===")
    print(circuit.draw(output="text"))
    c = run_counts(circuit, shots=shots)
    print("Counts:", c)
    print("Probabilities:", probs(c))


# ── Experiments ──────────────────────────────────────────────────────────
def x_gate_flip() -> QuantumCircuit:
    """Apply X to |0> and measure. Expected dominant outcome: 1."""
    # QuantumCircuit(num_qubits, num_classical_bits)
    qc = QuantumCircuit(1, 1)
    # Apply X to qubit 0, which flips |0> to |1>.
    qc.x(0)
    # Measure qubit 0 into classical bit 0.
    # Indices must exist in their registers.
    qc.measure(0, 0)
    return qc


def z_gate_phase_only() -> QuantumCircuit:
    """Apply Z to |0> and measure. Expected dominant outcome: 0.

    Z changes phase, not classical bit value, for basis state |0>.
    """
    # One qubit and one classical bit for measurement output.
    qc = QuantumCircuit(1, 1)
    # Apply Z to qubit 0 (phase flip, not a direct bit flip).
    qc.z(0)
    # Measure qubit 0 into classical bit 0.
    qc.measure(0, 0)
    return qc


def z_visible_with_h() -> QuantumCircuit:
    """Show Z effect with H-Z-H, which acts like X on |0>."""
    # One qubit and one classical bit.
    qc = QuantumCircuit(1, 1)
    # First H puts the qubit into superposition.
    qc.h(0)
    # Z changes relative phase in that superposition.
    qc.z(0)
    # Final H converts phase difference into a bit-value difference.
    qc.h(0)
    # Measure qubit 0 into classical bit 0.
    qc.measure(0, 0)
    return qc


def cx_controlled_flip() -> QuantumCircuit:
    """Create |10>, then apply CX(control=1,target=0).

    Expected final state is |11> because the control qubit is 1.
    """
    # Two qubits and two classical bits.
    qc = QuantumCircuit(2, 2)
    # Prepare control qubit (index 1) in |1>.
    qc.x(1)
    # CX(control=1, target=0): flip target only when control is 1.
    qc.cx(1, 0)
    # Measure qubits [0, 1] into classical bits [0, 1] one-to-one.
    qc.measure([0, 1], [0, 1])
    return qc


def ccx_toffoli() -> QuantumCircuit:
    """Demonstrate CCX: target flips only when both controls are 1."""
    # Three qubits and three classical bits.
    qc = QuantumCircuit(3, 3)
    # Prepare both control qubits in |1>.
    qc.x(2)
    qc.x(1)
    # CCX(control1=2, control2=1, target=0).
    # Target flips only if both controls are 1.
    qc.ccx(2, 1, 0)
    # Measure qubits [0, 1, 2] into matching classical bits.
    qc.measure([0, 1, 2], [0, 1, 2])
    return qc


def main() -> None:
    """Run all Lesson 02 drills."""
    report("X gate flips |0> to |1>", x_gate_flip())
    report("Z on |0> does not change measurement", z_gate_phase_only())
    report("H-Z-H exposes phase as a bit flip", z_visible_with_h())
    report("CX controlled flip", cx_controlled_flip())
    report("CCX (Toffoli) with both controls on", ccx_toffoli())


if __name__ == "__main__":
    main()
