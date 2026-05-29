# Exercise 03: Interference Basics

## Goal

Understand how phase can be hidden in one measurement step but become visible after additional gates.

## Setup

1. Activate your virtual environment.
2. Install dependencies if needed:

       pip install -r requirements.txt

3. Run the lesson script:

       python src/03_interference_basics.py

## Prediction-First Tasks

Before running each circuit, write your predicted dominant outcome.

1. H then measure on `|0>`: What distribution do you expect?
2. H then Z then measure: Why might this look similar to task 1?
3. H then H then measure: Why should this return to mostly `0`?
4. H then Z then H then measure: Why should this return mostly `1`?

## Reflection Prompts

1. In your own words, what is interference in a quantum circuit?
2. Why can two states have the same immediate measurement distribution but represent different quantum information?
3. What role do the first and last H gates play in H-Z-H?
4. How does this exercise connect to the idea that quantum algorithms shape adds and cancels?

## Bonus Notes and Answer Guide

### 1) Why can H and H-Z both look 50/50?

Both place probability mass across `0` and `1` similarly in direct Z-basis measurement, even though H-Z introduces a relative phase sign change.

### 2) Why does H-H return to 0?

Applying H twice acts like identity (`H*H = I`), so a qubit starting in `|0>` returns to `|0>`.

### 3) Why does H-Z-H return to 1?

The middle Z changes phase and the final H converts that phase difference into a measurable population difference. Net effect on `|0>` is like X.

### 4) Why this matters for algorithms

Quantum algorithms often use phase changes plus basis changes to constructively amplify desired answers and destructively suppress undesired ones.

## Stretch Tasks

1. Repeat each experiment with 100 and 10,000 shots. What stabilizes and what does not?
2. Add an extra Z at the end of H-Z-H and explain why results do or do not change.
3. Build your own 1-qubit sequence with H, X, Z, and H, then explain the measured output.
