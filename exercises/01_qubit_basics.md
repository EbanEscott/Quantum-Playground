# Exercise 01: Qubit Basics

## Goal

Build intuition for superposition, measurement randomness, and basic entanglement.

## Setup

1. Create/activate your virtual environment.
2. Install dependencies:

       pip install -r requirements.txt

3. Run the starter lesson:

       python src/01_qubit_basics.py

## Tasks

1. Read the output from the single-qubit H experiment.
2. Explain why states `0` and `1` are close to 50/50 but not exactly equal.
3. Read the Bell-state output and confirm why `01` and `10` should be near zero.
4. Compare 100 vs 10000 shots and write one sentence on why more shots stabilize probabilities.

## Stretch Tasks

1. Add a function that applies X before H and predict the outcome.
2. Create a 3-qubit GHZ state and inspect the counts.
3. Export your counts to a CSV file in a new `outputs/` folder.

## Reflection Prompt

What changed in your mental model of "measurement" after this exercise?
