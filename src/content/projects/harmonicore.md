---
title: HarmoniCore
hook: Real-time audio effects in SystemVerilog, developed from Python reference models and verified sample by sample in fixed point.
tier: selected
status: shipped
order: 10
where: Embedded Systems @ Purdue
categories: ['Signal Processing', 'RTL & FPGA']
dates: 'Sep 2025 – May 2026'
role: 'Designed and verified the distortion, ring-modulator, vibrato, routing, and first-generation control/datapath RTL.'
figure: '/figures/harmonicore-ringmod.png'
figureAlt: 'SystemVerilog ring-modulator output against the Python reference, with per-sample error in LSBs'
stats:
  - { label: 'FPGA', value: 'Artix-7' }
  - { label: 'Audio', value: '24-bit Q1.23' }
  - { label: 'Effects', value: '4' }
  - { label: 'Test tolerance', value: '±2 LSB' }
results:
  - { metric: 'Ring-modulator samples checked', value: '114' }
  - { metric: 'Maximum ring-modulator error', value: '1 LSB' }
  - { metric: 'Ring-modulator RMS error', value: '0.234 LSB' }
  - { metric: 'Sine lookup table', value: '64 entries, Q11' }
links:
  - { label: 'HarmoniCore 2.0', href: 'https://github.com/embedded-purdue/HarmoniCore2.0' }
  - { label: 'v1 autotuner', href: 'https://github.com/embedded-purdue/HarmoniCore' }
---

## Project brief

HarmoniCore is an FPGA audio-effects pipeline. The second generation implements ring
modulation, distortion, chorus, and a telephone-voice effect. Each block began with a
Python reference and moved into synthesizable SystemVerilog.

The earlier version explored automatic pitch correction using YIN pitch detection and
PSOLA pitch shifting. That work established the reference-model and RTL verification
workflow used in the second generation.

## What I built

- Distortion and ring-modulation blocks, their testbenches, and the ring-modulator sine
  lookup table.
- An initial vibrato implementation and verification bench.
- Effect interfaces and routing for a 24-bit Q1.23 audio path.
- Control and datapath RTL for the first-generation autotuner.
- Tcl-based FPGA project setup and fixes for signed arithmetic and pipeline alignment.

## Verification

The ring modulator was compared sample by sample with its Python model across 11 test
sets. All 114 checked samples stayed inside a ±2 LSB test tolerance; the measured maximum
error was 1 LSB and RMS error was 0.234 LSB.

## Engineering details

- Target family: Xilinx Artix-7.
- Fixed-point formats are explicit at module boundaries.
- Verification checks numerical agreement rather than relying only on listening tests.
- The source repositories contain the reference models, RTL, testbenches, and FPGA build
  scripts.
