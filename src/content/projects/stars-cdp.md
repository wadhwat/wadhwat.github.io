---
title: STARS Digital FM Receiver
hook: A wide-IF digital receiver architecture that takes a 38.4 MS/s real input down to a 48 kS/s audio stream.
tier: current
status: in-progress
order: 30
where: STARS Chip Design
categories: ['ASIC Design', 'Digital Signal Processing']
dates: 'Sep 2026 – present'
role: 'Working on digital architecture and integration; specific datapath block ownership is still being assigned.'
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

STARS is a digital FM receiver intended for an ASIC implementation. The current
architecture starts with a 12-bit real-IF stream at 38.4 MS/s and targets stereo-compatible
I2S audio at 48 kS/s.

## Planned signal chain

- Programmable numerically controlled oscillator and complex mixer.
- Multistage decimation using CIC and FIR filtering.
- Channel selection, FM demodulation, and audio de-emphasis.
- Final conversion to a 48 kS/s I2S stream.

The figures above are design targets from the current rate plan. Implementation results,
silicon measurements, and personal block ownership will be added as the project reaches
those milestones.
