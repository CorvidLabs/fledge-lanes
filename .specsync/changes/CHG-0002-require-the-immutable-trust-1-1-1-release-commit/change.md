---
id: CHG-0002-require-the-immutable-trust-1-1-1-release-commit
state: accepted
type: feature
base_commit: 86b1929a460c2b488998d31ed0b2d695dbf0ae07
---

# Require the immutable Trust 1.1.1 release commit

## Intent

Require the immutable Trust 1.1.1 release commit

## Affected Canonical Specs

- `fledge-lanes`

## Acceptance Criteria

- scripts/validate_templates.py accepts the immutable Trust 1.1.1 commit a239f78658e5ad0f12fa230f494890e40c6e4d7b and rejects the retired 1.0.0 pin; the Trust workflow using the 1.1.1 pin passes fledge lanes run verify; the canonical spec mandates Trust 1.1.1.

## No-spec Rationale

Not applicable
