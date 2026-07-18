---
change: CHG-0002-require-the-immutable-trust-1-1-1-release-commit
artifact: context
---

# Context

The repository mandates the immutable Trust 1.0.0 release commit (pin `9d32b5786d2e9e4d39fc581c0091c721ee3d4226`) in REQ-fledge-lanes-011 and enforces it in `scripts/validate_templates.py`. The consumer workflow has been pinned to the released Trust v1.1.1 immutable commit `a239f78658e5ad0f12fa230f494890e40c6e4d7b`, so the canonical mandate and validator must move to Trust 1.1.1 for the verify lane to pass.
