---
change: CHG-0002-require-the-immutable-trust-1-1-1-release-commit
artifact: requirements
---

# Requirements

- REQ-fledge-lanes-011 is modified to mandate the immutable Trust 1.1.1 release commit.
- `scripts/validate_templates.py` accepts the immutable Trust 1.1.1 commit `a239f78658e5ad0f12fa230f494890e40c6e4d7b` and rejects the retired 1.0.0 pin.
- The Trust workflow using the 1.1.1 pin passes `fledge lanes run verify`.
