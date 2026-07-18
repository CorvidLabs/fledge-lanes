---
change: CHG-0002-require-the-immutable-trust-1-1-1-release-commit
artifact: plan
---

# Plan

1. Record the Trust 1.1.1 mandate as a MODIFIED delta for REQ-fledge-lanes-011.
2. Update the required workflow marker in `scripts/validate_templates.py` to the Trust 1.1.1 immutable commit.
3. Verify with `fledge lanes run verify`, apply the delta on acceptance, and re-accept CHG-0001.
