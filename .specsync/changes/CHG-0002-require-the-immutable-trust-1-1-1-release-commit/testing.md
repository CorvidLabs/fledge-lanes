---
change: CHG-0002-require-the-immutable-trust-1-1-1-release-commit
artifact: testing
---

# Testing

The change is verified with `fledge lanes run verify` and `specsync check`. The deterministic validator reports `REQ-fledge-lanes-011 PASS immutable pull-request Trust workflow` with the Trust 1.1.1 pin in place, and rejects the workflow when the immutable Trust 1.1.1 commit marker is absent (the retired 1.0.0 pin no longer satisfies the check).
