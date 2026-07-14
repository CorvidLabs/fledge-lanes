#!/usr/bin/env python3
"""Validate the published Fledge lane templates without running their commands."""

from __future__ import annotations

import pathlib
import sys
import tomllib


EXPECTED_LANES = {
    "fledge.toml": {"audit", "check", "ci", "ci-fast", "verify"},
    "rust/fledge.toml": {"audit", "check", "ci", "ci-fast", "docs", "release"},
    "rust-ci/fledge.toml": {"check", "ci", "full"},
    "node-typescript/fledge.toml": {"audit", "check", "ci", "ci-fast", "fix", "release"},
    "node-ci/fledge.toml": {"build-only", "check", "ci"},
    "python/fledge.toml": {"audit", "check", "ci", "ci-fast", "fix", "release"},
    "go/fledge.toml": {"audit", "check", "ci", "ci-fast", "ci-race", "release"},
    "docker/fledge.toml": {"ci", "fast-build", "publish"},
    "release/fledge.toml": {"dry-run", "publish-only", "release"},
}

REQUIREMENTS = {
    "fledge.toml": "REQ-fledge-lanes-001",
    "rust/fledge.toml": "REQ-fledge-lanes-002",
    "rust-ci/fledge.toml": "REQ-fledge-lanes-003",
    "node-typescript/fledge.toml": "REQ-fledge-lanes-004",
    "node-ci/fledge.toml": "REQ-fledge-lanes-005",
    "python/fledge.toml": "REQ-fledge-lanes-006",
    "go/fledge.toml": "REQ-fledge-lanes-007",
    "docker/fledge.toml": "REQ-fledge-lanes-008",
    "release/fledge.toml": "REQ-fledge-lanes-009",
}


def task_names_from_step(step: object) -> list[str]:
    if isinstance(step, str):
        return [step]
    if not isinstance(step, dict):
        raise ValueError(f"unsupported lane step: {step!r}")
    if set(step) == {"parallel"} and isinstance(step["parallel"], list):
        return [name for name in step["parallel"] if isinstance(name, str)]
    if set(step) == {"run"} and isinstance(step["run"], str):
        return []
    raise ValueError(f"unsupported lane step: {step!r}")


def validate_manifest(path: pathlib.Path) -> None:
    relative = path.as_posix()
    document = tomllib.loads(path.read_text(encoding="utf-8"))
    tasks = document.get("tasks")
    lanes = document.get("lanes")
    if not isinstance(tasks, dict) or not tasks:
        raise ValueError(f"{relative}: tasks must be a non-empty table")
    if not isinstance(lanes, dict) or not lanes:
        raise ValueError(f"{relative}: lanes must be a non-empty table")
    if set(lanes) != EXPECTED_LANES[relative]:
        raise ValueError(
            f"{relative}: lanes are {sorted(lanes)}, expected {sorted(EXPECTED_LANES[relative])}"
        )

    for task_name, task in tasks.items():
        if isinstance(task, str):
            continue
        if not isinstance(task, dict) or not isinstance(task.get("cmd"), str):
            raise ValueError(f"{relative}: task {task_name!r} must define a command")
        dependencies = task.get("deps", [])
        if not isinstance(dependencies, list) or not all(
            isinstance(dependency, str) for dependency in dependencies
        ):
            raise ValueError(f"{relative}: task {task_name!r} has invalid dependencies")
        missing = set(dependencies) - set(tasks)
        if missing:
            raise ValueError(f"{relative}: task {task_name!r} references missing tasks {sorted(missing)}")

    for lane_name, lane in lanes.items():
        if not isinstance(lane, dict) or not isinstance(lane.get("steps"), list):
            raise ValueError(f"{relative}: lane {lane_name!r} must define steps")
        referenced = {
            task_name
            for step in lane["steps"]
            for task_name in task_names_from_step(step)
        }
        missing = referenced - set(tasks)
        if missing:
            raise ValueError(f"{relative}: lane {lane_name!r} references missing tasks {sorted(missing)}")


def main() -> int:
    try:
        for relative in EXPECTED_LANES:
            validate_manifest(pathlib.Path(relative))
            print(f"{REQUIREMENTS[relative]} PASS {relative}")

        workflow = pathlib.Path(".github/workflows/trust.yml").read_text(encoding="utf-8")
        workflow_markers = (
            "pull_request:",
            "push:",
            "branches: [main]",
            "actions/checkout@v5",
            "CorvidLabs/trust@9d32b5786d2e9e4d39fc581c0091c721ee3d4226",
        )
        missing_markers = [marker for marker in workflow_markers if marker not in workflow]
        if missing_markers:
            raise ValueError(f"Trust workflow is missing required markers: {missing_markers}")
        print("REQ-fledge-lanes-010 PASS deterministic structural validator")
        print("REQ-fledge-lanes-011 PASS immutable pull-request Trust workflow")
    except (OSError, tomllib.TOMLDecodeError, ValueError) as error:
        print(error, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
