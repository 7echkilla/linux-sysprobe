# Linux System Diagnostic CLI Tool

Linux system diagnostics CLI tool that aggregates low-level system information from core Linux interfaces including:
- /proc
- /sys
- dmesg
- journalctl
- Docker runtime

The tool helps developers quickly inspect system health, kernel errors and container activity. Heavily inspired by Linux debugging workflows used in production systems.

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

sysprobe --system
sysprobe --disk
sysprobe --docker
sysprobe --logs
sysprobe --all
sysprobe --json
```

## Project Structure
```
linux-sysprobe/
│
├── sysprobe.py
├── modules/
│   ├── system_info.py
│   ├── disk_usage.py
│   ├── docker_status.py
│   ├── kernel_logs.py
│   └── load_avg.py
│
├── README.md
└── requirements.txt
```

