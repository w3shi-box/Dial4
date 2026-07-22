---
name: environment_validation
description: Validates host runtime paths, OS configurations, and Python dependency maps.
allowed-tools:
  - run_command
---

# Environment Validation Skill

Use this skill during session initialization to ensure the workspace is fully functional.

## Workflow Sequence
1. Check the local Python interpreter environment.
2. Invoke the local `diagnostic.py` script to parse configuration flags.
3. Confirm that the validation output returns a clean status before editing project assets.
