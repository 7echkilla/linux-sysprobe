# Linux System Diagnostic Tool

A Python-based diagnostic tool that provides real-time system metrics and performance data, such as CPU usage, disk usage and more. It is designed to be modular, allowing additional diagnostic plugins to be added easily.

The tool is built with **Typer** to provide a user-friendly CLI and it includes a live dashboard for monitoring multiple system metrics simultaneously. Heavily inspired by Linux debugging workflows used in production systems.

### Features
- Modular design: Easily extendable with custom plugins
- CLI commands: View various system metrics through simple commands
- Live dashboard: Monitor multiple system metrics simultaneously in real-time

## Installation
1. Clone the repository: `git clone https://github.com/7echkilla/linux-probe.git`
2. Install the tool: `pip install -e .`

### Requirements
- Python3.10+
- `psutil` for system metrics
- `typer` for CLI 

## Usage
1. List all available modules: `probe --help`
2. Live dashboard: `probe-monitor`

## Plugin System

The project is designed with modular plugins. You can easily add new plugins by creating new modules under the `probe/modules` directory. Each plugin should subclass `Module` and implement its `get_data()` method to return a dictionary of diagnostic data. The plugin will then be automatically discovered and available as a command under Typer.