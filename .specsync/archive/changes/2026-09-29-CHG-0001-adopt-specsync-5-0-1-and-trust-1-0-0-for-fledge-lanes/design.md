---
change: CHG-0001-adopt-specsync-5-0-1-and-trust-1-0-0-for-fledge-lanes
artifact: design
---

# Design

Add one stable requirement per published manifest under a single `fledge-lanes` canonical specification. A deterministic Python validator parses each TOML document, checks the established lane names, validates task shapes and dependencies, and confirms every named lane step resolves. The root Fledge `verify` lane invokes that validator, giving Trust and SpecSync a repository-native entry point while never running consumer-oriented example commands. Trust uses the standard profile, blocking risk, progressive provenance, 100% contract coverage, and no Atlas publication.
