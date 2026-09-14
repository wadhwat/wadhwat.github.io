---
title: HarmoniCore
hook: Real-time audio effects in SystemVerilog, developed from Python reference models and verified sample by sample in fixed point.
tier: selected
status: shipped
order: 10
where: Embedded Systems @ Purdue
categories: ['Signal Processing', 'RTL & FPGA']
dates: 'Sep 2025 – May 2026'
role: 'Major RTL contributor on a five-person team; designed and verified distortion, ring modulation, vibrato, routing, and first-generation control/datapath logic.'
figure: '/figures/harmonicore-ringmod.png'
figureAlt: 'SystemVerilog ring-modulator output overlaid with the bit-accurate Python reference'
stats:
  - { label: 'FPGA', value: 'Artix-7 25T' }
  - { label: 'Datapath', value: '24-bit Q1.23' }
  - { label: 'My RTL', value: '5 modules' }
  - { label: 'Verification', value: '104 vectors' }
results:
  - { metric: 'Ring-modulator product', value: '24 × 24 → 48 bits' }
  - { metric: 'Requantization', value: 'Arithmetic shift by 23' }
  - { metric: 'Sine lookup table', value: '64-entry quarter wave, Q1.23' }
  - { metric: 'Error vs bit-accurate reference', value: '0 LSB across 104 vectors' }
links:
  - { label: 'HarmoniCore 2.0', href: 'https://github.com/embedded-purdue/HarmoniCore2.0' }
  - { label: 'v1 autotuner', href: 'https://github.com/embedded-purdue/HarmoniCore' }
---

## Project brief

HarmoniCore is an FPGA audio-effects pipeline. The second generation implements ring
modulation, distortion, chorus, and a telephone-voice effect. Each block began with a
Python reference and moved into synthesizable SystemVerilog.

It was a five-person team project. I was a major RTL contributor, with work spanning
individual effects, their testbenches, the routing layer, and first-generation control and
datapath logic.

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

The current ring-modulator simulation was compared sample by sample with a bit-accurate
Python model. All 104 vectors matched exactly. The datapath uses a 64-entry Q1.23
quarter-wave sine table, quadrant mirroring and sign reconstruction, a 48-bit product,
an arithmetic shift by 23, and saturation back to 24 bits.

![Ring-modulator datapath from phase accumulation and quarter-wave lookup through fixed-point multiplication and saturation](/figures/harmonicore-ringmod-arch.svg)

## Engineering details

- Target: Xilinx Artix-7 25T.
- Fixed-point formats are explicit at module boundaries.
- Verification checks numerical agreement rather than relying only on listening tests.
- The source repositories contain the reference models, RTL, testbenches, and FPGA build
  scripts.
