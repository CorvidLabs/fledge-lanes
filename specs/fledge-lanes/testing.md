---
spec: fledge-lanes.spec.md
---

## Test Plan

Run `python3 scripts/validate_templates.py` to parse every published TOML manifest, confirm the exact established lane inventory, and resolve every named task dependency and lane step. Run the root `verify` lane to exercise the same deterministic validation through Fledge.

The validator emits one stable requirement ID per manifest only after that manifest passes all checks. It also confirms its own successful execution and the Trust workflow's triggers and immutable action pin. It deliberately does not execute example commands, release operations, publication steps, or network calls.
