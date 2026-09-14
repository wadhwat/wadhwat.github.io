---
title: STARS CDP
hook: RTL for a digital FM receiver heading toward an ASIC. I own the digital plumbing and integration; my teammate owns the RF front end.
tier: current
status: in-progress
order: 30
where: SoCET · VIP
categories: ['RTL & FPGA', 'Signal Processing']
dates: '2026 – present'
role: 'RTL and digital integration'
figureNote: 'Figure: receiver signal chain'
stats:
  - { label: 'Target', value: 'ASIC' }
  - { label: 'Domain', value: 'Digital FM RX' }
  - { label: 'HDL', value: 'SystemVerilog' }
  - { label: 'Team', value: 'JJTS' }
links: []
---

In progress, through Purdue's SoCET vertically integrated project. The system is a digital
FM receiver intended for tapeout; I work on the RTL side, meaning the digital signal chain
and the integration between blocks, while a teammate handles the RF front end.

<span class="todo">TODO: two or three sentences on what the digital chain actually does.
Which stages (mixer, decimation, demodulation, audio path), what sample rates, and which
blocks are yours specifically.</span>

The reason this belongs next to HarmoniCore rather than repeating it: HarmoniCore targets an
FPGA, where a bad decision costs a rebuild. This targets silicon, where it does not.
