Can you sugg# Quantum Playground

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
	pip install -r requirements.txt

### 3) Sanity check installation

	python -c "import qiskit; print(qiskit.__version__)"

## Suggested Repo Structure

	.
	├── notebooks/       # Exploratory notebooks
	├── src/             # Reusable Python helpers and experiments
	├── exercises/       # Practice tasks and solutions
	├── assets/          # Images/plots used in docs
	└── README.md

## Current Starter Content

- `src/01_qubit_basics.py`: First runnable Qiskit lesson.
- `exercises/01_qubit_basics.md`: Guided prompts for Lesson 01.
- `src/02_gate_intuition.py`: Gate intuition drills for X, Z, CX, and CCX.
- `exercises/02_gate_intuition.md`: Guided prompts for Lesson 02.
- `notebooks/01_qubit_basics.ipynb`: Explanations and code for Lesson 01.
- `notebooks/02_gate_intuition.ipynb`: Explanations and code for Lesson 02.
- `src/03_interference_basics.py`: Interference drills (phase to measurement intuition).
- `exercises/03_interference_basics.md`: Guided prompts for Lesson 03.
- `notebooks/03_interference_basics.ipynb`: Explanations and code for Lesson 03.
- `notebooks/README.md`: Notebook conventions and naming suggestion.
- `requirements.txt`: Initial Python dependencies.
- `terminology.md`: Quick glossary of core quantum terms.
- `foundation_math.md`: Fundamentals refresher (algebra, vectors, matrices, probability).
- `qantum_math.md`: Quantum-focused math formulas used in lessons.

## Start Learning Now

1. Run the first lesson script:

	python src/01_qubit_basics.py

2. Work through the guided exercise:

	open exercises/01_qubit_basics.md

3. Optional: Create your first notebook in `notebooks/`:

	01_qubit_basics.ipynb

## First Exercises

- Create a single-qubit circuit with an H gate and measure it.
- Create a Bell state circuit and inspect the measurement distribution.
- Compare 100 shots vs 10,000 shots and describe the differences.

## Notes

- Keep experiments small and focused.
- Add one concept per notebook to make learning easier to review.
- Commit often with short messages describing what you learned.

## Next Steps

- Run Lesson 03 focused on interference and basis changes.
- Add simple plotting/visualization for count distributions.
- Add beginner algorithm modules (Deutsch-Jozsa first).

## Move To Exercise 02

1. Run the second lesson script:

	python src/02_gate_intuition.py

2. Work through the guided exercise:

	open exercises/02_gate_intuition.md

3. Use the companion notebook:

	notebooks/02_gate_intuition.ipynb

## Move To Exercise 03

1. Run the third lesson script:

	python src/03_interference_basics.py

2. Work through the guided exercise:

	open exercises/03_interference_basics.md

3. Use the companion notebook:

	notebooks/03_interference_basics.ipynb
