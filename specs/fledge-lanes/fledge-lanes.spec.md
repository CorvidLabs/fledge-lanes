---
module: fledge-lanes
version: 1
status: stable
files:
  - fledge.toml
  - rust/fledge.toml
  - rust-ci/fledge.toml
  - node-typescript/fledge.toml
  - node-ci/fledge.toml
  - python/fledge.toml
  - go/fledge.toml
  - docker/fledge.toml
  - release/fledge.toml
  - scripts/validate_templates.py
  - .github/workflows/trust.yml
db_tables: []
depends_on: []
---

# Fledge Lanes Specification

## Purpose

Provide importable example Fledge task and lane manifests for common project toolchains, plus a root starter manifest and deterministic repository verification lane.

## Public API

The public interface is the set of named tasks and lanes in each published `fledge.toml`. Consumers copy or import a manifest and customize its commands for their own project. The root manifest provides general-purpose `check`, `ci`, `ci-fast`, and `audit` examples and a repository-only `verify` lane.

The following identifiers are implementation-facing governance exports rather than consumer lane APIs:

| Export | Description |
|--------|-------------|
| `EXPECTED_LANES` | Exact established lane inventory keyed by published manifest path. |
| `REQUIREMENTS` | Stable requirement-evidence ID keyed by published manifest path. |
| `task_names_from_step` | Resolves named tasks from sequential, parallel, and inline lane-step representations. |
| `validate_manifest` | Parses and validates one published manifest without executing its commands. |
| `main` | Validates all manifests and the immutable Trust workflow, returning a process status. |
| `name` | Names the hosted workflow `trust`. |
| `on` | Runs the hosted gate for pull requests and main-branch pushes. |
| `permissions` | Defines the workflow's least-privilege permission map. |
| `permissions.contents` | Grants read-only repository content access. |
| `jobs` | Contains the workflow job map. |
| `jobs.trust` | Runs the unified Trust gate on Ubuntu with full checkout history. |

## Invariants

1. Every published manifest is valid TOML with non-empty `tasks` and `lanes` tables.
2. Every named task dependency and every named lane step resolves within the same manifest.
3. Parallel groups contain named tasks; inline `run` steps remain self-contained commands.
4. Validation parses manifest structure without executing toolchain commands, release operations, container publication, or customizable starter examples.
5. The established lane names for every template remain stable unless an intentional semantic change updates this specification.
6. Repository verification fails when the Trust workflow no longer runs on pull requests and main-branch pushes or no longer uses the immutable Trust 1.0.0 commit.

## Behavioral Examples

- Importing `rust/fledge.toml` provides `check`, `ci`, `ci-fast`, `release`, `audit`, and `docs` lanes composed from Cargo-oriented tasks.
- Importing `node-ci/fledge.toml` provides `check`, `ci`, and `build-only` lanes whose dependency graph begins with package installation.
- Running the root `verify` lane validates all nine manifests without running any example build, test, publish, or deployment command.
- Changing a lane to reference an undefined task or moving the Trust action off its immutable release commit makes repository verification fail.

## Error Cases

- Invalid TOML fails repository verification with the manifest path and parser error.
- A missing or unexpected published lane fails verification with the affected manifest and observed lane names.
- A task dependency or lane step that references a missing task fails verification with the unresolved names.
- An unsupported lane-step representation fails verification rather than being ignored.
- A missing Trust trigger or immutable action pin fails verification with the missing workflow marker.

## Dependencies

- Fledge consumes the manifests when users run or import lanes.
- Deterministic repository verification uses Python 3.11 or newer for the standard-library `tomllib` parser.
- Individual templates intentionally reference their documented ecosystem tools, including Cargo, Bun/npm-compatible commands, Python tooling, Go, Docker, and release utilities; those commands are not executed by repository verification.

## Change Log

| Version | Date | Changes |
|---------|------|---------|
| 0 | 2026-07-13 | Baseline contract prepared for the SpecSync 5.0.1 and Trust 1.0.0 migration. |
| 2026-07-14 | CHG-0001-adopt-specsync-5-0-1-and-trust-1-0-0-for-fledge-lanes: Adopt SpecSync 5.0.1 and Trust 1.0.0 for Fledge Lanes |
