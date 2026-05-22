# Exercise 02: Gate Intuition Drills

## Goal

Build practical intuition for how X, Z, CX, and CCX transform qubit states.

## Setup

1. Activate your virtual environment.
2. Install dependencies if needed:

       pip install -r requirements.txt

3. Run the lesson script:

       python src/02_gate_intuition.py

## Prediction-First Tasks

Before running each circuit, write your prediction for the dominant measurement result.

1. X on `|0>`: What output do you expect and why?
2. Z on `|0>`: Why does measurement look unchanged?
3. H-Z-H on `|0>`: Why does this now look like a bit flip?
4. CX with control in `|1>`: Which two-bit output do you expect?
5. CCX with both controls in `|1>`: Which three-bit output do you expect?

## Reflection Prompts

1. In one sentence, explain the difference between a **bit flip** and a **phase flip**.
2. Why can phase changes be invisible until another gate converts phase into population differences?
3. What condition must be true for CX to flip its target?
4. What extra condition does CCX add beyond CX?

## Stretch Tasks

1. Change the CX control to `|0>` and re-run. What changed?
2. Prepare only one CCX control as `|1>` and observe the target behavior.
3. Add your own mini-circuit that combines X, H, and Z, then explain the output.
