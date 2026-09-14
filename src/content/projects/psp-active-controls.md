---
title: Zucrow Interface Firmware
hook: Embedded interface firmware for Purdue Space Program's liquid-engine controller and ground-support electronics.
tier: current
status: in-progress
order: 40
where: Purdue Space Program
categories: ['Embedded Firmware', 'Controls']
dates: 'Sep 2026 – present'
role: 'Developing the controller-to-ground-system interface firmware for the Zucrow test environment.'
stats:
  - { label: 'Controller', value: 'TOAD' }
  - { label: 'Signals', value: 'Digital I/O' }
  - { label: 'Bus', value: 'SPI' }
  - { label: 'DAC family', value: 'MCP48xx' }
results:
  - { metric: 'DAC channels', value: '2' }
  - { metric: 'DAC resolution', value: '12-bit' }
  - { metric: 'Driver SPI clock', value: '4 MHz' }
  - { metric: 'SPI mode', value: 'Mode 0' }
---

## Project brief

The interface sits between Purdue Space Program's TOAD engine controller and Zucrow
ground systems. Existing firmware coordinates digital fault and synchronization signals
and uses a dual-channel DAC to expose valve telemetry.

## Current scope

- Understand the controller-to-ground-system signal contract.
- Work within the existing STM32 firmware and board interfaces.
- Add and validate interface behavior as subsystem ownership is finalized.

Current work centers on making that boundary explicit, testable, and safe before it is
exercised with the full ground system.
