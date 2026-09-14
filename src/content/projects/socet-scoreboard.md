---
title: SoCET Scoreboard
hook: "An FPGA design that also had to become copper: schematic capture, layout, fabrication, assembly, and the bring-up debugging that only starts once you power a board you drew yourself."
tier: selected
status: in-progress
order: 20
where: SoCET
categories: ['Hardware Design', 'RTL & FPGA', 'Embedded & Firmware']
dates: 'TODO'
role: 'TODO: which parts were yours versus the team'
figureNote: 'Figure: board photo or layout render'
stats:
  - { label: 'Layers', value: 'TODO', todo: true }
  - { label: 'Part', value: 'TODO', todo: true }
  - { label: 'EDA tool', value: 'TODO', todo: true }
  - { label: 'Board size', value: 'TODO', todo: true }
results:
  - { metric: 'Board size', value: 'TODO' }
  - { metric: 'Layer count', value: 'TODO' }
  - { metric: 'Component count', value: 'TODO' }
  - { metric: 'Revisions to a working board', value: 'TODO' }
links:
  - { label: 'Source on GitHub', href: 'https://github.com/TODO' }
---

## What it is

<span class="todo">TODO: two sentences on what the scoreboard actually does. What it
displays, what drives it, where it gets used.</span>

This project sits next to HarmoniCore rather than duplicating it for a reason. HarmoniCore
is about getting an algorithm into gates. This one is about getting a design into copper,
which fails in completely different ways.

## The constraint

<span class="todo">TODO: the requirement that made it hard. Board area, cost per unit,
drive current for the display, the I/O count the part could give you, a deadline.</span>

## Architecture

<span class="todo">TODO: block diagram — power tree, the FPGA or MCU, the display driver
chain, level shifting, connectors.</span>

<span class="todo">TODO: three to five sentences walking the diagram.</span>

## Three decisions

**Part selection.** <span class="todo">TODO: what you picked, what you rejected, and why.
Availability, package, I/O count, toolchain, cost.</span>

**Layout.** <span class="todo">TODO: stackup, ground plane strategy, where the fast signals
went, decoupling. Say what you would have done with more layers or more area.</span>

**What lives in hardware versus software.** <span class="todo">TODO: how the display is
driven, refresh strategy, and where you drew that line.</span>

## What broke

<span class="todo">TODO — bring-up stories are the best ones on a hardware portfolio. A part
that would not enumerate, pins swapped in the schematic, a rail that sagged under load, a
mirrored footprint, a bodge wire. Symptom, first hypothesis, how you actually found it, the
fix. Photograph the bodge if there is one; every hardware engineer reading this has made
the same one.</span>

## What I would do differently

<span class="todo">TODO: two sentences.</span>
