---
spec: fledge-lanes.spec.md
---

# Requirements

### REQ-fledge-lanes-001

The repository SHALL provide a root starter manifest with the established `check`, `ci`, `ci-fast`, and `audit` examples and a deterministic `verify` lane covering every published manifest.

Acceptance Criteria
- Structural validation confirms the root lane inventory and resolves all named steps without executing starter commands.

### REQ-fledge-lanes-002

The repository SHALL provide the Rust template with `check`, `ci`, `ci-fast`, `release`, `audit`, and `docs` lanes composed from defined Cargo tasks.

Acceptance Criteria
- Structural validation confirms the Rust lane inventory and resolves all task dependencies and named steps.

### REQ-fledge-lanes-003

The repository SHALL provide the compact Rust CI template with `check`, `ci`, and `full` lanes composed from defined formatting, lint, test, and build tasks.

Acceptance Criteria
- Structural validation confirms the compact Rust CI lane inventory and resolves all task dependencies and named steps.

### REQ-fledge-lanes-004

The repository SHALL provide the Node.js and TypeScript template with `check`, `ci`, `ci-fast`, `fix`, `audit`, and `release` lanes composed from defined project tasks.

Acceptance Criteria
- Structural validation confirms the Node.js and TypeScript lane inventory and resolves all task dependencies and named steps.

### REQ-fledge-lanes-005

The repository SHALL provide the compact Node CI template with `check`, `ci`, and `build-only` lanes whose named steps and dependencies resolve to defined tasks.

Acceptance Criteria
- Structural validation confirms the compact Node CI lane inventory and resolves all task dependencies and named steps.

### REQ-fledge-lanes-006

The repository SHALL provide the Python template with `check`, `ci`, `ci-fast`, `fix`, `audit`, and `release` lanes composed from defined Python project tasks.

Acceptance Criteria
- Structural validation confirms the Python lane inventory and resolves all task dependencies and named steps.

### REQ-fledge-lanes-007

The repository SHALL provide the Go template with `check`, `ci`, `ci-fast`, `ci-race`, `audit`, and `release` lanes composed from defined Go project tasks.

Acceptance Criteria
- Structural validation confirms the Go lane inventory and resolves all task dependencies and named steps.

### REQ-fledge-lanes-008

The repository SHALL provide the Docker template with `ci`, `publish`, and `fast-build` lanes composed from defined image validation, build, test, cache, and publication tasks.

Acceptance Criteria
- Structural validation confirms the Docker lane inventory and resolves all task dependencies and named steps.

### REQ-fledge-lanes-009

The repository SHALL provide the release template with `release`, `dry-run`, and `publish-only` lanes composed from defined version, changelog, commit, tag, publish, and push tasks.

Acceptance Criteria
- Structural validation confirms the release lane inventory and resolves all task dependencies and named steps.

### REQ-fledge-lanes-010

The repository SHALL provide deterministic structural validation that parses all published manifests and rejects invalid task shapes, unresolved dependencies, unresolved lane steps, unsupported step representations, and unexpected lane inventories without executing template commands.

Acceptance Criteria
- Running the root `verify` lane reports passing evidence for every published manifest and exits non-zero for any invalid structure or reference.

### REQ-fledge-lanes-011

The repository SHALL run the unified Trust gate on pull requests and main-branch pushes using the immutable Trust 1.0.0 release commit.

Acceptance Criteria
- Deterministic validation confirms the pull-request and main-branch push triggers and the exact immutable Trust action pin.

