# Quantum Playground

A hands-on sandbox for learning quantum programming step by step.

## Goal

This repository is for experimenting with quantum computing concepts through small, practical examples.

Our first platform is **Qiskit**.

## Learning Path (Qiskit First)

1. Build intuition for qubits, superposition, entanglement, and measurement.
2. Create simple circuits with 1-3 qubits.
3. Simulate circuits locally.
4. Study common quantum gates (X, H, Z, CX, CCX) and what they do.
5. Implement beginner algorithms (Deutsch-Jozsa, Grover, QFT basics).

## Quick Start

### 1) Create and activate a virtual environment

macOS/Linux:

	python3 -m venv .venv
	source .venv/bin/activate

Windows (PowerShell):

	py -m venv .venv
	.venv\Scripts\Activate.ps1

### 2) Install dependencies

	python -m pip install --upgrade pip
	pip install qiskit jupyter matplotlib

### 3) Sanity check installation

	python -c "import qiskit; print(qiskit.__version__)"

## Suggested Repo Structure

	.
	├── notebooks/       # Exploratory notebooks
	├── src/             # Reusable Python helpers and experiments
	├── exercises/       # Practice tasks and solutions
	├── assets/          # Images/plots used in docs
	└── README.md

## First Exercises

- Create a single-qubit circuit with an H gate and measure it.
- Create a Bell state circuit and inspect the measurement distribution.
- Compare 100 shots vs 10,000 shots and describe the differences.

## Notes

- Keep experiments small and focused.
- Add one concept per notebook to make learning easier to review.
- Commit often with short messages describing what you learned.

## Next Steps

- Add a `notebooks/` folder with a first notebook: "01_qubit_basics.ipynb".
- Add a `requirements.txt` once dependencies stabilize.
