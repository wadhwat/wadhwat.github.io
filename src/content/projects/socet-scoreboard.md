---
title: SoCET Basketball Scoreboard
hook: A complete FPGA scoreboard—from game-control RTL to a custom two-layer display board and hardware bring-up.
tier: selected
status: shipped
order: 20
where: SoCET
categories: ['RTL & FPGA', 'PCB Design']
dates: 'Jan 2026 – May 2026'
role: 'Led a five-person team and contributed the top-level integration, control FSM, verification, and custom-board design and bring-up.'
stats:
  - { label: 'FPGA board', value: 'Arty S7-25' }
  - { label: 'PCB', value: '2 layers' }
  - { label: 'Board size', value: '94 × 98 mm' }
  - { label: 'Team', value: '5' }
results:
  - { metric: 'Placed footprints', value: '45' }
  - { metric: 'Copper layers', value: '2' }
  - { metric: 'Board outline', value: '93.97 × 98 mm' }
  - { metric: 'Top-level clock', value: '100 MHz' }
links:
  - { label: 'Source on GitHub', href: 'https://github.com/wadhwat/socet-1-shot-clock' }
---

## Project brief

This scoreboard tracks the game clock, shot clock, scores, period, and possession. Buttons
drive the game controls, seven-segment displays show the state, and a buzzer marks clock
events. The final system runs on a Digilent Arty S7-25 and connects to a custom display
board.

## What I built

- Led the five-person project from module ownership through integration and bring-up.
- Wrote the top-level module, control-state-machine logic, and verification benches.
- Resolved reset, module-interface, timing, and memory-interface issues during integration.
- Designed the custom PCB schematic and layout in KiCad and helped bring up the assembled
  hardware.

## Hardware

The board is a two-layer, 1.6 mm FR-4 design with 45 placed footprints and a roughly
94 × 98 mm outline. The repository includes the FPGA constraints, RTL, testbenches,
schematics, layout, and hardware bring-up programs.
