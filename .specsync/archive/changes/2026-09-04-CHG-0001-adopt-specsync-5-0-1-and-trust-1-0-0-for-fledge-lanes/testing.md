---
change: CHG-0001-adopt-specsync-5-0-1-and-trust-1-0-0-for-fledge-lanes
artifact: testing
---

# Testing

The change is verified with `fledge lanes run verify`, `specsync check --strict --require-coverage 100 --force`, `specsync agents status`, `fledge trust doctor`, and `fledge trust verify`.

The deterministic validator reports evidence for every requirement after its manifest passes:

- `REQ-fledge-lanes-001` — root starter and repository verification lanes.
- `REQ-fledge-lanes-002` — Rust template.
- `REQ-fledge-lanes-003` — compact Rust CI template.
- `REQ-fledge-lanes-004` — Node.js and TypeScript template.
- `REQ-fledge-lanes-005` — compact Node CI template.
- `REQ-fledge-lanes-006` — Python template.
- `REQ-fledge-lanes-007` — Go template.
- `REQ-fledge-lanes-008` — Docker template.
- `REQ-fledge-lanes-009` — release template.
- `REQ-fledge-lanes-010` — deterministic structural validator behavior.
- `REQ-fledge-lanes-011` — pull-request and main-branch Trust triggers with immutable action pin.

Validation parses structure only. It does not run toolchain, release, publication, deployment, network, or customizable starter commands.
