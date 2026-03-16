# Linux System Diagnostic Tool

A Linux system diagnostics tool that aggregates low-level system information from core Linux interfaces including:
- /proc
- /sys
- dmesg
- journalctl
- Docker runtime

The tool helps developers quickly inspect system health, kernel errors and container activity. Heavily inspired by Linux debugging workflows used in production systems.

The primary functions are:
- Inspect system state interactively
- Generate a support bundle for debugging

## Features

- System information (CPU, memory, kernel)
- Disk usage
- Docker container status
- System load averages
- Recent kernel errors

## Example Usage

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .

probe system
```