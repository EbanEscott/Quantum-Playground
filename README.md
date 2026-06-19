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

- `src/01_qubit_basics.py`: Single-qubit superposition, Bell-state entanglement, and shot-count comparison.
- `exercises/01_qubit_basics.md`: Guided prompts for Exercise 01.
- `notebooks/01_qubit_basics.ipynb`: Explanations and code for Exercise 01.
- `src/02_gate_intuition.py`: Gate intuition drills for X, Z, CX, and CCX.
- `exercises/02_gate_intuition.md`: Guided prompts for Exercise 02.
- `notebooks/02_gate_intuition.ipynb`: Explanations and code for Exercise 02.
- `src/03_interference_basics.py`: Interference drills showing how phase becomes measurable.
- `exercises/03_interference_basics.md`: Guided prompts for Exercise 03.
- `notebooks/03_interference_basics.ipynb`: Explanations and code for Exercise 03.
- `src/04_statevector_amplitudes.py`: Statevector inspections that connect amplitudes to counts.
- `exercises/04_statevector_amplitudes.md`: Guided prompts for Exercise 04.
- `notebooks/04_statevector_amplitudes.ipynb`: Explanations and code for Exercise 04.
- `quantum_programming.md`: Mental model for quantum programming from a software engineering point of view.
- `terminology.md`: Quick glossary of core quantum terms.
- `foundation_math.md`: Fundamentals refresher for algebra, vectors, matrices, and probability.
- `qantum_math.md`: Quantum-focused math formulas used in the early exercises.
- `notebooks/README.md`: Notebook conventions and naming suggestions.
- `requirements.txt`: Initial Python dependencies.

## Exercise Plan

The learning path is meant to move from small circuit mechanics toward a concrete search-style project. The search mental model is: represent candidates as qubit states, use an oracle/checker to mark valid candidates, use interference to amplify marked candidates, measure many times, then interpret the result with classical code.

Each exercise should stay small: one runnable script in `src/`, one guided prompt in `exercises/`, and optionally one notebook in `notebooks/`. The normal shape is prediction first, run the circuit, inspect counts/probabilities, then explain what happened.

### Exercise 01: Qubit Basics

Goal: Build intuition for superposition, measurement randomness, basic entanglement, and shot noise.

Main tasks:

- Create a single-qubit H circuit and measure it.
- Create a Bell state and inspect why only correlated outcomes appear.
- Compare 100 shots vs 10,000 shots.

Why it matters: measurement is not a normal return statement. It is sampling from a distribution shaped by the circuit.

### Exercise 02: Gate Intuition Drills

Goal: Understand how X, Z, CX, and CCX affect small circuits.

Main tasks:

- Predict and run X on `|0>`.
- Compare bit flips with phase flips.
- Use H-Z-H to turn hidden phase into a visible bit difference.
- Use CX and CCX to see controlled behavior.

Why it matters: gates are the basic transformations used to build oracles, algorithms, and search circuits.

### Exercise 03: Interference Basics

Goal: Understand how phase can be hidden in one measurement step but become visible after more gates.

Main tasks:

- Compare H, H-Z, H-H, and H-Z-H.
- Explain why two circuits can have similar immediate measurements but different internal states.
- Connect phase changes to constructive and destructive interference.

Why it matters: interference is the mechanism that lets quantum algorithms make useful answers more likely and less useful answers less likely.

### Exercise 04: Statevector and Amplitude Inspection

Goal: Look at the quantum state before measurement.

Main tasks:

- Inspect statevectors for H, X, Z, H-Z, and H-Z-H circuits.
- Compare amplitudes with final measurement counts.
- Show that phase can exist even when measurement probabilities look unchanged.
- Inspect a Bell state as a statevector.

Why it matters: counts show the sampled result, but statevectors reveal the amplitudes and phase information that measurement hides.

### Exercise 05: Multi-Qubit Basis and Bit Ordering

Goal: Get comfortable with multi-qubit states, bitstrings, and Qiskit's output ordering.

Planned tasks:

- Prepare `|00>`, `|01>`, `|10>`, and `|11>` with X gates.
- Measure two and three qubit circuits and explain the printed bitstrings.
- Rebuild Bell and GHZ states with clearer basis-state notation.
- Write predictions before each measurement.

Why it matters: search examples depend on representing candidates as bitstrings. If the bit ordering is confusing, the algorithm output will be confusing.

### Exercise 06: Oracles and Checkers

Goal: Learn how a quantum circuit can mark candidates that satisfy a known rule.

Planned tasks:

- Build a simple classical checker like `is_solution(x)` for a tiny search space.
- Build the matching quantum oracle for one marked two-bit candidate.
- Use phase marking to tag the valid candidate without directly measuring it.
- Compare "knowing the rule" with "knowing the answer."

Why it matters: in search, the oracle is not the answer. It is the checker that recognizes a valid answer when given a candidate.

### Exercise 07: Phase Kickback

Goal: Understand how an oracle can mark a candidate by changing phase.

Planned tasks:

- Prepare a helper qubit in `|->`.
- Apply a controlled operation and observe phase kickback.
- Compare a target-bit flip oracle with a phase-marking oracle.
- Explain why the mark is invisible until later interference uses it.

Why it matters: phase kickback is one of the main tricks that makes oracle-based quantum algorithms work.

### Exercise 08: Deutsch-Jozsa Algorithm

Goal: Build the first complete beginner algorithm.

Planned tasks:

- Implement simple constant and balanced oracles.
- Run the Deutsch-Jozsa circuit and classify the oracle from measurement.
- Compare the quantum query pattern with a classical checker.
- Explain what global property the algorithm detects.

Why it matters: Deutsch-Jozsa is a small, clean example of using superposition, an oracle, phase, and measurement to learn something about a function.

### Exercise 09: Grover Search Basics

Goal: Build a tiny search algorithm around the marked-item mental model.

Planned tasks:

- Create a two-qubit search space with four candidates.
- Build an oracle/checker that marks one candidate.
- Apply amplitude amplification.
- Compare measurement counts before and after amplification.
- Change the marked item and confirm the measured result changes.

Why it matters: Grover search is the clearest beginner example of the quantum programmer's job: mark useful states, amplify them, then sample the distribution.

### Exercise 10: Mini Capstone

Goal: Combine the earlier tools into one small end-to-end project.

Planned tasks:

- Pick a tiny search/checker problem with 2 or 3 qubits.
- Encode candidates as bitstrings.
- Build or adapt an oracle.
- Run the circuit, collect counts, and identify the likely answer.
- Write a short explanation of the classical checker, the quantum circuit, and the final measurement distribution.

Why it matters: this turns the individual mechanics into a small project with a recognizable software shape: problem, representation, checker, algorithm, output, and explanation.

## How To Work Through Exercises

1. Run the matching script:

	python src/01_qubit_basics.py

2. Work through the matching exercise:

	open exercises/01_qubit_basics.md

3. Use the matching notebook when available:

	notebooks/01_qubit_basics.ipynb

For later exercises, follow the same naming pattern:

```text
src/04_statevector_amplitudes.py
exercises/04_statevector_amplitudes.md
notebooks/04_statevector_amplitudes.ipynb
```

## Notes

- Keep experiments small and focused.
- Add one concept per script or notebook.
- Predict the result before running the circuit.
- Treat counts as sampled evidence, not a direct return value.
- Use `quantum_programming.md` when the big-picture mental model gets fuzzy.
