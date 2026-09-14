---
title: RootSense
hook: "Field-edge runoff monitoring: STM32 firmware reading an ultrasonic sensor and a thermocouple amplifier, with a Python advisor on top that pulls NOAA forecasts and scores risk. First place at Tech4Change."
tier: also
status: shipped
order: 60
where: Hackathon
categories: ['Embedded & Firmware', 'AI Systems']
dates: 'Nov 2025'
role: 'TODO: which parts were yours'
figureNote: 'Figure: sensing and advisory pipeline'
stats:
  - { label: 'MCU', value: 'STM32F091' }
  - { label: 'Core', value: 'Cortex-M0' }
  - { label: 'Sensing', value: 'Ultrasonic · AD8495' }
  - { label: 'Result', value: '1st place' }
links:
  - { label: 'Source on GitHub', href: 'https://github.com/TODO' }
---

Won first place at the Tech4Change Hackathon in November 2025.

RootSense estimates runoff risk on a field and tells a farmer what to do about it. The
firmware side runs on an STM32F091 (a Cortex-M0 part): it reads an ultrasonic distance
sensor for ponding depth against a calibrated dry baseline, samples an AD8495 thermocouple
amplifier on the ADC, and drives green, yellow and red indicators for low, moderate and high
risk. The Python side pulls NOAA weather data, scores runoff risk from sensor readings and
forecast together, and exposes the whole thing through a CLI, a Flask API and a small GUI.

Worth saying plainly: the sensing is real and the advisory layer is a weekend's work on top
of it. <span class="todo">TODO: one sentence on which half was yours, and one honest line on
what you would fix given more than a weekend.</span>
