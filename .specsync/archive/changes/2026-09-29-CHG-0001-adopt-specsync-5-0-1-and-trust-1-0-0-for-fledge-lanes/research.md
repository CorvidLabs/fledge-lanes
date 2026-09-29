---
change: CHG-0001-adopt-specsync-5-0-1-and-trust-1-0-0-for-fledge-lanes
artifact: research
---

# Research

The root README documents the eight importable toolchain templates, task dependencies, sequential and parallel lane steps, inline commands, and fail-fast behavior. The root `fledge.toml` is also a published starter manifest and now owns the repository verification lane. Python 3.11's standard-library `tomllib` can parse all manifests deterministically. A structural validator can therefore confirm exact lane inventories and resolve named references without invoking Cargo, package managers, Docker, release tooling, or network services.
