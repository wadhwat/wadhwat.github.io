---
title: STARS Digital FM Receiver
hook: Initial full-chain RTL for a wide-IF digital FM receiver, now moving through verification and refinement toward ASIC tapeout.
tier: current
status: in-progress
order: 30
where: STARS Chip Design
categories: ['ASIC Design', 'Digital Signal Processing']
dates: 'Sep 2026 – present'
role: 'Built the initial end-to-end RTL implementation and am refining the fixed-point datapath, rate changes, and interfaces for the ASIC flow.'
stats:
  - { label: 'Target', value: 'ASIC' }
  - { label: 'ADC target', value: '12-bit real IF' }
  - { label: 'Input rate', value: '38.4 MS/s' }
  - { label: 'Audio rate', value: '48 kS/s' }
results:
  - { metric: 'Stage 1 output', value: '1.536 MS/s complex' }
  - { metric: 'Channel rate', value: '384 kS/s complex' }
  - { metric: 'Audio output', value: '48 kS/s' }
  - { metric: 'Raw ADC payload', value: '460.8 Mb/s' }
---

## Project brief

STARS is a digital FM receiver intended for an ASIC implementation. The design starts with
a 12-bit real-IF stream at 38.4 MS/s and produces 48 kS/s I2S audio. The initial RTL spans
the full receiver chain; current work is focused on verification, fixed-point choices,
interfaces, and implementation tradeoffs before tapeout.

## Signal chain

- Programmable numerically controlled oscillator and complex mixer.
- Multistage decimation using CIC and FIR filtering.
- Channel selection, FM demodulation, and audio de-emphasis.
- Final conversion to a 48 kS/s I2S stream.

The rates above are the current design targets. They describe the implemented signal-chain
structure; synthesis, PPA, and silicon measurements will follow later in the ASIC flow.
