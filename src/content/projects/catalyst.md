---
title: CATalyst
hook: A mobile heavy-equipment inspection workflow that turns walkaround video into structured, reviewable defect reports.
tier: also
status: shipped
order: 70
where: HackIllinois
categories: ['Computer Vision', 'Full-stack']
dates: 'Feb 2026 – Mar 2026'
role: 'Built authentication, user-scoped data, machine and report APIs, mobile integration, and the vision-model service path.'
stats:
  - { label: 'Capture', value: 'Expo camera' }
  - { label: 'API', value: 'FastAPI' }
  - { label: 'Vision', value: 'YOLO + Qwen' }
  - { label: 'Storage', value: 'User-scoped database' }
results:
  - { metric: 'Input', value: 'Walkaround video' }
  - { metric: 'Processing', value: 'Sampled frames' }
  - { metric: 'Output', value: 'Structured inspection report' }
  - { metric: 'Failure handling', value: 'Partial-frame recovery' }
links:
  - { label: 'Source on GitHub', href: 'https://github.com/wadhwat/catalyst' }
---

## Project brief

CATalyst lets an operator record a walkaround inspection of heavy equipment. A FastAPI
service extracts and samples video frames, sends them through object-detection and
vision-language stages, merges repeated findings, and returns a structured report for
review.

## What I built

- JWT authentication, profiles, and user-scoped machine and report data.
- Mobile flows for capture, machine selection, report generation, and report review.
- Database APIs for machines, reports, and saved inspection context.
- Integration of the remote vision-language service into the analysis pipeline.
- Recovery paths that preserve usable findings when individual frame analyses fail.
