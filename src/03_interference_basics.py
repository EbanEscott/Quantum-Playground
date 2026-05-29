"""Lesson 03: Interference basics with Qiskit.

This lesson shows how phase differences can produce different outcomes
once another gate converts phase into measurable populations.
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
    """Print circuit diagram and measurement summary."""
    print(f"\n=== {title} ===")
    print(circuit.draw(output="text"))
    c = run_counts(circuit, shots=shots)
    print("Counts:", c)
    print("Probabilities:", probs(c))


# ── Circuits ─────────────────────────────────────────────────────────────
def h_then_measure() -> QuantumCircuit:
    """Prepare superposition from |0> with H and measure.

    Expected: close to 50/50 over many shots.
    """
    # QuantumCircuit(num_qubits, num_classical_bits)
    qc = QuantumCircuit(1, 1)

    # H on qubit 0 creates equal superposition.
    qc.h(0)

    # Measure qubit 0 into classical bit 0.
    qc.measure(0, 0)
    return qc


def h_z_then_measure() -> QuantumCircuit:
    """Apply H then Z, then measure directly.

    Expected: still close to 50/50 in Z basis.
    """
    qc = QuantumCircuit(1, 1)
    qc.h(0)

    # Z changes phase, but direct Z-basis measurement still looks 50/50.
    qc.z(0)
    qc.measure(0, 0)
    return qc


def h_h_then_measure() -> QuantumCircuit:
    """Apply H twice.

    Since H*H = I, this should return to |0>.
    """
    qc = QuantumCircuit(1, 1)
    qc.h(0)
    qc.h(0)
    qc.measure(0, 0)
    return qc


def h_z_h_then_measure() -> QuantumCircuit:
    """Apply H-Z-H.

    This sequence behaves like X on |0>, so expected output is mostly 1.
    """
    qc = QuantumCircuit(1, 1)

    # First H creates superposition.
    qc.h(0)

    # Z injects a relative phase sign change.
    qc.z(0)

    # Final H converts phase information into bit-value difference.
    qc.h(0)

    qc.measure(0, 0)
    return qc


def compare_shot_stability() -> tuple[dict[str, int], dict[str, int]]:
    """Compare low and high shot stability on H then measure."""
    low = run_counts(h_then_measure(), shots=100)
    high = run_counts(h_then_measure(), shots=10_000)
    return low, high


def main() -> None:
    """Run all Lesson 03 experiments."""
    report("H then measure", h_then_measure())
    report("H then Z then measure", h_z_then_measure())
    report("H then H then measure", h_h_then_measure())
    report("H then Z then H then measure", h_z_h_then_measure())

    print("\n=== Shot Stability (100 vs 10000) ===")
    low, high = compare_shot_stability()
    print("100 shots:", low, probs(low))
    print("10000 shots:", high, probs(high))


if __name__ == "__main__":
    main()
