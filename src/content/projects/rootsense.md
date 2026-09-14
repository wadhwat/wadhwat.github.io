---
title: RootSense
hook: A soil-monitoring prototype that combines STM32 sensor firmware with weather-aware runoff and infiltration risk analysis.
tier: also
status: shipped
order: 60
where: BoilerMake · 1st, Tech4Change
categories: ['Embedded Systems', 'Sensors']
dates: 'Nov 2025'
role: 'Developed STM32 sensor firmware and the threshold logic for infiltration, ponding, and runoff events.'
stats:
  - { label: 'MCU', value: 'STM32F091' }
  - { label: 'Temperature', value: 'AD8495 · 12-bit ADC' }
  - { label: 'Distance', value: 'Ultrasonic' }
  - { label: 'Award', value: '1st · Tech4Change' }
results:
  - { metric: 'Firmware outputs', value: 'Infiltration, ponding, runoff' }
  - { metric: 'Environmental correction', value: 'Temperature-compensated distance' }
  - { metric: 'Dashboard weather source', value: 'weather.gov' }
  - { metric: 'Prototype link', value: 'Simulated sensor values' }
links:
  - { label: 'Source on GitHub', href: 'https://github.com/sultanMEHMET-1/RootSense' }
---

## Project brief

RootSense measures water level and temperature near the soil surface, then classifies
infiltration, ponding, and runoff behavior. The firmware uses an ultrasonic sensor and an
AD8495 temperature channel, compensates the distance calculation, and drives local status
indicators.

The companion Python application combines readings with National Weather Service data,
calculates risk, and presents the result through desktop and web interfaces.

## Prototype boundary

The embedded firmware contains the real sensor-processing and event logic. In the
hackathon prototype, the Python dashboard used simulated sensor values rather than a live
telemetry connection to the STM32.
