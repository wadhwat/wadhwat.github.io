# Portfolio writing workbook

This working file is not loaded by the website. The public pages use facts verified
from repositories, commit history, project documentation, and the current resume as of
September 14, 2026.

Use these prompts for the parts a repository cannot establish: why a choice mattered,
what went wrong, what you learned, and what the finished system felt like to use.

## HarmoniCore

### Verified points

- Two generations: a YIN/PSOLA autotuner, followed by an Artix-7 effects pipeline.
- The second generation includes ring modulation, distortion, chorus, and telephone voice.
- Your commits cover distortion, ring modulation, an initial vibrato, interfaces and
  routing, testbenches, and first-generation control/datapath work.
- Ring-modulator verification checked 114 samples across 11 sets. Maximum error was
  1 LSB and RMS error was 0.234 LSB against a ±2 LSB test tolerance.
- The current interface uses 24-bit Q1.23 samples. The sine LUT has 64 Q11 entries.

### Article angles

- Turning an audio algorithm into fixed-point hardware without losing a numerical oracle.
- Why sample-by-sample Python comparison caught problems that listening could not.
- How signed arithmetic, latency alignment, and interfaces became the hard part.
- What changed between the autotuner and effects architectures.

### Only you can add

- Confirm the exact physical FPGA board and canonical end-to-end sample rate. The
  repositories name an Artix-7 device but contain both 44.1 and 48 kHz experiments.
- Describe one bug and the observation that finally exposed it.
- Explain team ownership and where your block boundaries began and ended.
- Say why you chose the fixed-point formats and what you would change next.
- Add a hardware photo or short input/output demo.

### Source trail

- C:\Users\tejas\Projects\harmonicore\README.md
- C:\Users\tejas\Projects\harmonicore\v2-effects\VERIFICATION_SUMMARY.md
- C:\Users\tejas\Projects\harmonicore\v2-effects\src
- C:\Users\tejas\Projects\harmonicore\v1-autotune

## SoCET Basketball Scoreboard

### Verified points

- A five-person project using a Digilent Arty S7-25 at 100 MHz.
- Tracks game and shot clocks, score, period, possession, buttons, displays, and a buzzer.
- Your commits include the top level, control FSM, testbenches, integration fixes, PCB
  schematic and layout, and bring-up programs.
- The populated KiCad design is two-layer, 1.6 mm FR-4, about 93.97 × 98 mm, with
  45 placed footprints.

### Article angles

- The moment separate RTL modules became one physical system.
- Why reset and interface contracts matter more at integration than inside a unit test.
- Moving from FPGA constraints into connectors, displays, and a manufacturable PCB.
- What project leadership meant when five people's modules had to work together.

### Only you can add

- Describe the first successful full-system demonstration and what was connected.
- Pick the best bring-up failure: symptom, measurements, root cause, and fix.
- Clarify which schematic/layout regions you personally owned versus reviewed.
- State whether the first assembled revision worked and any rework it needed.
- Add front/back board photos and a scoreboard-in-operation image.

### Source trail

- C:\Users\tejas\Projects\Intro 1\socet-1-shot-clock\README.md
- C:\Users\tejas\Projects\Intro 1\socet-1-shot-clock\constraints\top.xdc
- C:\Users\tejas\Projects\Intro 1\socet-1-shot-clock\KiCad_Files\ShotClockPCB\17pinPCB

## STARS Digital FM Receiver

### Verified points

- Current rate plan: 12-bit real input at 38.4 MS/s and 48 kS/s audio output.
- Planned intermediate rates are 1.536 MS/s complex and 384 kS/s complex.
- The raw ADC payload at the design point is 460.8 Mb/s.
- The planned chain includes a programmable NCO/mixer, CIC and FIR decimation, channel
  selection, FM demodulation, de-emphasis, and I2S output.
- This is architecture work; RTL results and silicon measurements do not exist yet.

### Article angles

- Deriving every sample rate instead of treating rates as magic numbers.
- Why the design moved toward a wide real-IF architecture.
- Choosing decimation stages from image rejection, channel bandwidth, and hardware cost.
- Specifying an ASIC datapath before block ownership and RTL settle.

### Only you can add

- Confirm the ADC, clocking parts, and evaluation hardware after the team freezes them.
- Name your exact datapath block and interfaces when ownership is assigned.
- Explain why the earlier architecture changed and which constraint forced the decision.
- Add rate-planning plots and later replace targets with synthesis results.

### Source trail

- C:\Users\tejas\Projects\stars-cdp\research\calc.py
- C:\Users\tejas\Projects\stars-cdp\research
- C:\Users\tejas\Projects\stars-cdp\docs

## Zucrow Interface Firmware

### Verified points

- The subsystem connects the TOAD engine controller with Zucrow ground interfaces.
- Existing code includes digital fault/synchronization signals and two analog valve
  telemetry outputs.
- The DAC driver targets a dual 12-bit MCP48xx-family device over 4 MHz SPI mode 0.
- Your personal implementation is too new to claim a finished result.

### Article angles

- Defining a safe, testable boundary between controller and ground equipment.
- Testing embedded interfaces when the full propulsion system is unavailable.
- Making failure states visible and deterministic.

### Only you can add

- Name the exact board, MCU, and ticket or requirement you own.
- Add your first merged implementation and test evidence after it lands.
- Explain the bench setup, expected safe states, and fault injection.
- Confirm which technical details are suitable for a public portfolio.

### Source trail

- C:\Users\tejas\Projects\psp-active-controls\toad-software
- C:\Users\tejas\Projects\psp-active-controls\tadpole-software\controller

## MODO

### Verified points

- Planned split: STM32 for physical controls and indicators; Raspberry Pi 5 for application,
  speech, vision, storage, and agent services.
- The repository proves STM32 board bring-up and documents USB HID and 115200-baud UART
  interfaces.
- The Pi application, camera path, and higher-level services remain planned architecture.

### Article angles

- Why a personal device needs a deterministic controller beside a Linux host.
- Designing the device protocol before the whole application exists.
- Keeping speech, vision, and model providers replaceable.
- Defining the smallest vertical slice that proves the architecture.

### Only you can add

- Confirm the exact STM32 part; current materials do not consistently distinguish F405/F411.
- State what works today beyond the verified blink/bring-up milestone.
- Describe the enclosure, controls, display, and daily interaction you want.
- Explain why you want this device to exist and what existing workflow frustrates you.
- Add a photo once the physical controls and Pi are connected.

### Source trail

- C:\Users\tejas\Projects\project-modo\README.md
- C:\Users\tejas\Projects\project-modo\docs\architecture.md
- C:\Users\tejas\Projects\project-modo\docs\interfaces.md
- C:\Users\tejas\Projects\project-modo\firmware\stm32

## RootSense

### Verified points

- STM32F091 firmware reads an ultrasonic channel and an AD8495 through a 12-bit ADC.
- Logic covers temperature compensation, a dry baseline, infiltration, ponding, runoff,
  and LED state.
- The Python side uses weather.gov data and presents risk through desktop/web interfaces.
- The hackathon dashboard used simulated sensor values rather than live STM32 telemetry.
- The project won first place in BoilerMake's Tech4Change track.

### Article angles

- Converting raw distance and temperature into a useful soil/water event.
- Making an environmental prototype honest about calibration and uncertainty.
- The boundary between real sensor firmware and simulated dashboard integration.

### Only you can add

- Clarify the team split and your exact ownership outside firmware.
- Describe what worked in the final demo and what had to be simulated.
- Explain the user or agricultural problem that shaped the thresholds.
- Say how you would connect, calibrate, and validate a second version in the field.

### Source trail

- C:\Users\tejas\Projects\hackathons\RootSense\Core
- C:\Users\tejas\Projects\hackathons\RootSense\python

## CATalyst

### Verified points

- Expo records video; FastAPI samples frames and coordinates analysis.
- The path combines object detection and a vision-language model, merges repeated findings,
  and produces a structured inspection report.
- Your commits cover authentication, user-scoped data, database APIs, mobile report flows,
  camera permissions, and vision-service integration.
- Partial frame failures can preserve usable findings.

### Article angles

- Turning unstructured inspection video into a report a human can review.
- Designing a pipeline where one failed frame does not discard the inspection.
- Separating mobile interaction from remote GPU inference.
- Preventing duplicate detections from becoming duplicate maintenance findings.

### Only you can add

- Describe the team split and the feature you drove from idea through demo.
- Explain the hardest integration failure and how you diagnosed it.
- State what counted as a successful inspection in the final demonstration.
- Add screenshots of capture, processing, and the report.

### Source trail

- C:\Users\tejas\Projects\hackathons\catalyst\README.md
- C:\Users\tejas\Projects\hackathons\catalyst

## Vincilium

### Verified points

- A multistage natural-language query path over PostgreSQL reduced prompt context by
  83–91% in measured workflows.
- Work included eight guarded MCP tools and a nine-test evaluation suite.
- Model routing covered six backends, with four validated in the target environment.
- Agent experience uses tenant-scoped memory and versioned skills while keeping host safety
  guards outside tenant control.

### Article angles

- Why schema and query context should be retrieved in stages instead of sent wholesale.
- Designing connector actions so retries cannot duplicate side effects.
- Letting an agent learn tenant behavior without letting a tenant weaken safety rules.
- What a useful cross-model evaluation measures.

### Only you can add

- Confirm what company and customer details are safe to publish.
- Identify the most important component you owned end to end.
- Explain how token reduction was measured and what quality guardrail you used.
- Tell one failure story involving an unsafe action, backend incompatibility, or bad learned
  behavior, and how the design changed afterward.

### Source trail

- C:\Users\tejas\Projects\Vincilium\PROJECT_STATUS_REPORT.md
- C:\Users\tejas\Projects\Vincilium\agent-experience\README.md
- C:\Users\tejas\Projects\Vincilium\vm-ml-usecase
