# Exercise 04: Statevector and Amplitudes

## Goal

Look at the quantum state before measurement and connect amplitudes to sampled measurement counts.

## Setup

1. Activate your virtual environment.
2. Install dependencies if needed:

       pip install -r requirements.txt

3. Run the lesson script:

       python src/04_statevector_amplitudes.py

If your shell does not have `python` on PATH, use:

       .venv/bin/python src/04_statevector_amplitudes.py

## Prediction-First Tasks

Before running each circuit, write both predictions:

- What amplitudes do you expect?
- What measurement counts do you expect?

Then run the script and compare your prediction with the output.

1. H on `|0>`: Why do `|0>` and `|1>` have equal probabilities?
2. X on `|0>`: Why is the full probability on `|1>`?
3. Z on `|0>`: Why does the state still measure as `0`?
4. H then Z: What changed in the amplitudes, and why do the counts still look close to 50/50?
5. H then Z then H: Why does the final H make the earlier phase change visible?
6. Bell state: Which amplitudes are present, and which basis states have zero probability?

## Reflection Prompts

1. What is the difference between an amplitude and a probability?
2. Why can two states produce the same measurement distribution but still be different quantum states?
3. What does the statevector show that counts do not show?
4. How does this exercise clarify the idea that measurement is sampled evidence, not the whole state?

## Search Connection

For search-style algorithms, the important mark is often a phase change. That mark may not be obvious in measurement immediately.

This exercise shows the reason: phase lives in the amplitudes first. Later gates use interference to turn that hidden phase information into a measurement distribution where useful answers appear more often.

## Stretch Tasks

1. Add an `x_h_state()` circuit that applies X then H. Predict how it differs from H on `|0>`.
2. Add an `h_x_h_state()` circuit and compare it with H-Z-H.
3. Change the Bell-state circuit to prepare `(|01> + |10>) / sqrt(2)` and inspect the amplitudes.
4. Run one circuit with 100 shots and 10,000 shots. What changes in the sampled counts, and what does not change in the exact probabilities?
