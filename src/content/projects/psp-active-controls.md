---
title: Zucrow interface board firmware
hook: Firmware for the interface board on a liquid rocket engine controller — digital I/O plus an SPI DAC, on hardware that sits in a test cell.
tier: current
status: in-progress
order: 35
where: Purdue Space Program
categories: ['Embedded & Firmware']
dates: '2026 – present'
role: 'Interface board firmware, GNC embedded software'
figureNote: 'Figure: interface board signal chain'
stats:
  - { label: 'MCU', value: 'STM32' }
  - { label: 'Interfaces', value: 'DI/DO · SPI' }
  - { label: 'DAC', value: 'MCP48xx' }
  - { label: 'System', value: 'TOAD' }
links:
  - { label: 'activecontrols on GitHub', href: 'https://github.com/activecontrols' }
---

In progress, on Purdue Space Program's Active Controls team. I work on the embedded side of
guidance, navigation and control; my piece is the firmware for the Zucrow interface board
that sits between the TOAD engine controller and the hardware in the test cell.

That means digital inputs and outputs, and analog setpoints driven through an MCP48xx
digital-to-analog converter over SPI. <span class="todo">TODO: two sentences on what the
board actually controls, and what the failure modes are. This is the project where "being
wrong is expensive" is literally true, which is worth saying plainly.</span>

<span class="todo">TODO: anything you can say about testing. How do you validate firmware
for something you cannot iterate on casually?</span>
