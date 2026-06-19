"""Exercise 04: Statevector and amplitude inspection with Qiskit.

This lesson shows the quantum state before measurement, then compares that
state with sampled measurement counts.
"""

from __future__ import annotations

from qiskit import QuantumCircuit, transpile
from qiskit.providers.basic_provider import BasicSimulator
from qiskit.quantum_info import Statevector


def run_counts(circuit: QuantumCircuit, shots: int = 1024) -> dict[str, int]:
    """Run a measured circuit on BasicSimulator and return counts."""
    backend = BasicSimulator()
    compiled = transpile(circuit, backend)
    job = backend.run(compiled, shots=shots)
    return job.result().get_counts(compiled)


def probs(counts: dict[str, int]) -> dict[str, float]:
    """Convert counts to sorted probabilities."""
    total = sum(counts.values())
    return {state: value / total for state, value in sorted(counts.items())}


def statevector(circuit: QuantumCircuit) -> Statevector:
    """Return the statevector for a circuit before measurement."""
    return Statevector.from_instruction(circuit)


def basis_labels(num_qubits: int) -> list[str]:
    """Return computational-basis labels in display order."""
    width = max(num_qubits, 1)
    return [format(index, f"0{width}b") for index in range(2**num_qubits)]


def measured_copy(circuit: QuantumCircuit) -> QuantumCircuit:
    """Copy a no-measurement circuit and add matching classical measurements."""
    measured = QuantumCircuit(circuit.num_qubits, circuit.num_qubits)
    measured.compose(circuit, inplace=True)
    measured.measure(range(circuit.num_qubits), range(circuit.num_qubits))
    return measured


def format_amplitude(value: complex) -> str:
    """Format a complex amplitude in a compact, readable form."""
    real = float(value.real)
    imag = float(value.imag)
    if abs(real) < 1e-12:
        real = 0.0
    if abs(imag) < 1e-12:
        imag = 0.0
    return f"{real:+.3f}{imag:+.3f}j"


def report_state(title: str, circuit: QuantumCircuit, shots: int = 1024) -> None:
    """Print circuit, amplitudes, exact probabilities, and sampled counts."""
    print(f"\n=== {title} ===")
    print(circuit.draw(output="text"))

    sv = statevector(circuit)
    amplitudes = {str(label): amplitude for label, amplitude in sv.to_dict().items()}
    exact_probs = {str(label): float(prob) for label, prob in sv.probabilities_dict().items()}
    labels = basis_labels(circuit.num_qubits)

    print("Amplitudes:")
    for label in labels:
        print(f"  |{label}>: {format_amplitude(amplitudes.get(label, 0j))}")

    print("Exact probabilities from amplitudes:")
    for label in labels:
        print(f"  |{label}>: {exact_probs.get(label, 0.0):.3f}")

    measured = measured_copy(circuit)
    counts = run_counts(measured, shots=shots)
    print("Sampled counts:", counts)
    print("Sampled probabilities:", probs(counts))


def h_state() -> QuantumCircuit:
    """Create (|0> + |1>) / sqrt(2)."""
    qc = QuantumCircuit(1)
    qc.h(0)
    return qc


def x_state() -> QuantumCircuit:
    """Create |1> from |0>."""
    qc = QuantumCircuit(1)
    qc.x(0)
    return qc


def z_on_zero_state() -> QuantumCircuit:
    """Apply Z to |0>, which leaves the state unchanged."""
    qc = QuantumCircuit(1)
    qc.z(0)
    return qc


def h_z_state() -> QuantumCircuit:
    """Create a superposition, then add relative phase with Z."""
    qc = QuantumCircuit(1)
    qc.h(0)
    qc.z(0)
    return qc


def h_z_h_state() -> QuantumCircuit:
    """Convert the H-Z phase difference into a measurable bit difference."""
    qc = QuantumCircuit(1)
    qc.h(0)
    qc.z(0)
    qc.h(0)
    return qc


def bell_state() -> QuantumCircuit:
    """Create (|00> + |11>) / sqrt(2)."""
    qc = QuantumCircuit(2)
    qc.h(0)
    qc.cx(0, 1)
    return qc


def main() -> None:
    """Run all Exercise 04 statevector inspections."""
    report_state("H creates equal amplitudes", h_state())
    report_state("X flips |0> to |1>", x_state())
    report_state("Z on |0> leaves measurement unchanged", z_on_zero_state())
    report_state("H then Z changes relative phase", h_z_state())
    report_state("H-Z-H turns phase into a bit result", h_z_h_state())
    report_state("Bell state amplitudes", bell_state())


if __name__ == "__main__":
    main()
