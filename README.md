# Linux System Diagnostic Tool

A Python-based diagnostic tool that provides real-time system metrics and performance data, such as CPU usage, disk usage and more. It is designed to be modular, allowing additional diagnostic plugins to be added easily.

The tool is built with **Typer** to provide a user-friendly CLI and it includes a live dashboard for monitoring multiple system metrics simultaneously. Heavily inspired by Linux debugging workflows used in production systems.

### Features
- Modular design: Easily extendable with custom plugins
- CLI commands: View various system metrics through simple commands
- Live dashboard: Monitor multiple system metrics simultaneously in real-time

## Installation
1. Clone the repository: `git clone https://github.com/7echkilla/probe.git`
2. Install the tool: `pip install -e .`

## Usage
1. List all available modules: `probe --help`
2. Live dashboard: `probe-gui`