---
title: Zucrow Interface Firmware
hook: Embedded interface firmware for Purdue Space Program's liquid-engine controller and ground-support electronics.
tier: current
status: in-progress
order: 40
where: Purdue Space Program
categories: ['Embedded Firmware', 'Controls']
dates: 'Sep 2026 – present'
role: 'New contributor focused on the Zucrow interface firmware; personal implementation results are still in progress.'
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

This page currently describes the assigned subsystem and facts verified from its source
tree. Personal results will replace this status note as implementation and testing land.
