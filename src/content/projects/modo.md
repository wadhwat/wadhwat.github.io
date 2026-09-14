---
title: MODO
hook: A Raspberry Pi 5 and STM32 embedded companion built around physical controls, a durable device protocol, and swappable AI services.
tier: current
status: in-progress
order: 50
where: Personal project
categories: ['Embedded Systems', 'AI Systems']
dates: 'Jun 2026 – present'
role: 'Own the system architecture, STM32 bring-up, device-interface specification, and planned Raspberry Pi application stack.'
stats:
  - { label: 'Host', value: 'Raspberry Pi 5' }
  - { label: 'Controller', value: 'STM32F4' }
  - { label: 'Controls', value: 'USB HID target' }
  - { label: 'Device link', value: '115200 baud' }
results:
  - { metric: 'Firmware status', value: 'Board bring-up verified' }
  - { metric: 'Protocol status', value: 'HID/UART interface specified' }
  - { metric: 'Application status', value: 'Architecture in progress' }
  - { metric: 'Service boundary', value: 'FastAPI planned' }
links:
  - { label: 'Source on GitHub', href: 'https://github.com/wadhwat/project-modo' }
---

## Project brief

MODO is an embedded companion built around a Raspberry Pi 5 and STM32 controller.
Physical inputs and indicators belong on the microcontroller; higher-level speech, vision,
agent, and storage services belong on the Pi behind replaceable interfaces.

## What is working

- STM32 development-board bring-up and firmware flashing.
- A documented USB HID and UART contract between the controller and host.
- A repository structure that separates firmware, host services, interfaces, and logs.

## Next

The Pi application, camera path, speech services, and tool-running agent remain planned
architecture. The next public milestone is an end-to-end physical control traveling through
the device interface and producing a visible host action.
