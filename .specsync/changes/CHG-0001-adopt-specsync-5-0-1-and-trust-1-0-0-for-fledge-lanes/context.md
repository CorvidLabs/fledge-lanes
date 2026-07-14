---
change: CHG-0001-adopt-specsync-5-0-1-and-trust-1-0-0-for-fledge-lanes
artifact: context
---

# Context

Fledge Lanes publishes nine TOML manifests: a root starter and eight toolchain-specific examples. The manifests themselves are the repository's product, so the migration needs a canonical contract and stable requirement evidence rather than a zero-coverage exception. Verification must remain safe: example tasks include builds, releases, image publication, and intentionally customizable starter commands that must not run in governance CI.
