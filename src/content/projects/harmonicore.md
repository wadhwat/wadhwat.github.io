---
title: HarmoniCore
hook: A real-time audio effects processor in SystemVerilog, where every effect has to match a Python reference model in fixed point, on hardware, within two least significant bits.
tier: selected
status: in-progress
order: 10
where: Embedded Systems @ Purdue
categories: ['Signal Processing', 'RTL & FPGA']
dates: 'TODO: e.g. Jan 2026 – present'
role: 'TODO: name the blocks that are yours. This is the one field an interviewer will probe.'
figureNote: 'Figure: ring modulator, hardware vs Python reference'
figure: "/figures/harmonicore-ringmod.png"
figureAlt: "SystemVerilog ring modulator output against the Python reference, with per-sample error in LSBs"
stats:
  - { label: 'Board', value: 'TODO', todo: true }
  - { label: 'Sample rate', value: 'TODO', todo: true }
  - { label: 'Sine LUT', value: '64 × Q11' }
  - { label: 'Datapath', value: '18×18 → 36 b' }
results:
  - { metric: 'Fmax', value: 'TODO MHz' }
  - { metric: 'LUT utilization', value: 'TODO / TODO' }
  - { metric: 'FF utilization', value: 'TODO / TODO' }
  - { metric: 'BRAM', value: 'TODO' }
  - { metric: 'DSP slices', value: 'TODO' }
  - { metric: 'Max error vs reference', value: 'TODO LSB' }
  - { metric: 'RMS error vs reference', value: 'TODO LSB' }
links:
  - { label: 'HarmoniCore2.0 on GitHub', href: 'https://github.com/embedded-purdue/HarmoniCore2.0' }
  - { label: 'v1 autotuner', href: 'https://github.com/embedded-purdue/HarmoniCore' }
---

## What it is

HarmoniCore is a real-time audio effects processor running in fabric on an FPGA, with no
processor anywhere in the signal path. The current version implements ring modulation,
distortion, chorus and a telephone-voice filter, each written in SystemVerilog against a
Python model that defines what "correct" means.

It started somewhere else. The first version was an autotuner: YIN pitch detection feeding
PSOLA pitch shifting, with a Python reference the team wrote to prove the algorithm before
any of it became RTL. That version taught us how much of the difficulty lives in the
conversion rather than the algorithm, and the second version is the one built on what we
learned.

## The constraint

An effect is only real if the hardware and the model agree. Anyone can write a ring
modulator that sounds approximately right; the work is making a fixed-point implementation
land within a bounded error of a floating-point reference, and being able to prove it.
The bound we hold the design to is **±2 least significant bits**, which is tight enough
that quantization choices actually matter and loose enough to absorb the LUT and truncation
error we accept on purpose.

<span class="todo">TODO: was there also a latency or resource constraint? A sample rate you
had to hit, or a slice budget? If so it belongs here.</span>

## Architecture

<figure>
  <img src="/figures/harmonicore-ringmod-arch.svg"
       alt="Ring modulator datapath: a phase accumulator feeds a quarter-wave sine lookup table, whose output multiplies the incoming audio before an 18-bit slice is taken from the 36-bit product." />
  <figcaption>The ring modulator datapath, end to end.</figcaption>
</figure>

The ring modulator is the clearest example of the pattern the rest follow. It computes
`output = input × sin(2πft)` entirely in fixed point:

- A phase accumulator increments by 27968 each sample, in a 2<sup>18</sup> phase space, giving a
  normalized frequency of about 0.1069 and an oscillator period of roughly 9.37 samples.
- Sine comes from a **64-entry quarter-phase lookup table in Q11**, with the other three
  quadrants reconstructed from symmetry rather than stored. That is a 4× memory saving for
  the cost of some sign and index logic.
- The multiply is **18 bits by 18 bits into 36**, and the output takes bits `[28:11]`,
  which is where the Q-format bookkeeping actually happens.
- Everything is two's complement, so the sign handling around the quadrant reconstruction
  is the part most likely to be subtly wrong.

## Three decisions

**A quarter-wave LUT with symmetry, rather than a full-period table.** Storing one quadrant
costs a quarter of the memory and buys back the logic to mirror and negate. At 64 entries in
Q11 the quantization error is inside the ±2 LSB budget, which is the only reason the
trade is available.

**Fixed point over floating point.** <span class="todo">TODO: the reasoning in your own
words. Why Q11 for the LUT, how you chose the 18-bit datapath width, what overflowed first
in simulation, and whether you used saturating arithmetic. This is the paragraph an FPGA
interviewer will most enjoy.</span>

**Verifying against Python rather than by ear.** <span class="todo">TODO: two sentences on
why you built the CSV-comparison flow instead of listening to output and calling it done.</span>

## Verification

The testbench writes every sample it produces to CSV, and a Python script recomputes the
expected value from the reference implementation and compares them sample by sample,
reporting maximum and RMS error in LSBs. The whole thing runs as one target:

```bash
cd v2-effects/sv
make ring_mod_verify
```

The suite is **114 samples across 11 test sets**, structured so that coverage is an
argument rather than a number:

- Each 10-sample set spans slightly more than one full oscillator period, so every phase
  of the sine gets exercised at each amplitude.
- Amplitudes run from zero through 1/8, 1/2 and 3/4 scale to full scale, in both signs,
  which is what verifies the multiplication scales linearly and the two's complement
  handling is symmetric.
- A final set covers alternating polarity and boundary values, where overflow and underflow
  would show up first.

## What broke

<span class="todo">TODO — the most important section on this page, and the only one no
tool can write for you. Pick the bug that cost the most time and answer four things: the
symptom, what you first thought it was, how you actually found it, and the fix. Sign errors
in quadrant reconstruction, an off-by-one in the bit slice, a testbench that passed while
the board did not; whichever it actually was.</span>

## What I would do differently

<span class="todo">TODO: two sentences.</span>
