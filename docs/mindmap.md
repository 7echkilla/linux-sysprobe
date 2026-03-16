# MindMap

## 1. System Information (Static / Rarely Changing)

These help identify the machine and environment.

OS & Kernel
- Distribution name
- Distribution version
- Kernel version
- Kernel build
- Kernel architecture
- Boot parameters
- Hostname
- Uptime
- Boot time
- Init system (systemd, openrc, etc)

Example:
```
OS: Ubuntu 24.04
Kernel: 6.8.0-25-generic
Arch: x86_64
Init: systemd
Uptime: 2 days 5 hours
```

## 2. CPU Information

Important for performance debugging.

Static CPU Info
- CPU model name
- Vendor (Intel/AMD)
- Microarchitecture
- Number of sockets
- Cores per socket
- Threads per core
- Total logical CPUs
- Cache sizes (L1/L2/L3)
- CPU flags (SSE, AVX, etc)
- Base clock
- Max boost clock
- Virtualization support

Live CPU Metrics
- CPU usage per core
- Total CPU usage
- CPU frequency per core
- CPU temperature
- Load average (1,5,15)
- Context switches/sec
- Interrupt rate
- CPU throttling state
- CPU steal time (important for VMs)

Sources:
```
/proc/cpuinfo
/sys/devices/system/cpu
/proc/stat
```

## 3. GPU Monitoring

Important for developers using compute or graphics workloads.

GPU Info
- GPU name
- Vendor
- Driver version
- VRAM total
- GPU architecture

Live GPU Metrics
- GPU utilization %
- VRAM usage
- GPU temperature
- GPU power usage
- GPU clock
- Fan speed
- Encoder/decoder usage

Tools to integrate with:
- nvidia-smi (NVIDIA)
- radeontop (AMD)
- intel_gpu_top (Intel)

## 4. Memory Monitoring
RAM
- Total RAM
- Used RAM
- Free RAM
- Cached memory
- Buffers
- Available memory
- Memory pressure

Swap
- Swap total
- Swap used
- Swap in/out rate

Advanced
- HugePages
- Memory fragmentation
- OOM events
- Page faults

Sources:
```
/proc/meminfo
/proc/vmstat
```

## 5. Storage / Disk
Disk Info
- Disk model
- Disk type (HDD/SSD/NVMe)
- Capacity
- Sector size
- Mount points
- Filesystem type

Disk Usage
- Used / free space
- Disk utilization %
- Inodes used/free

Disk Performance
- Read speed
- Write speed
- IOPS
- Queue length
- Latency

SMART health
- Disk temperature
- Reallocated sectors
- Wear level (SSD)

Tools:
- smartctl

Sources:
```
/proc/diskstats
/sys/block
```

## 6. Filesystem Monitoring

For each mount:
- Mount point
- Filesystem type
- Capacity
- Used
- Free
- Inodes used
- Read/write throughput
- Mount options

Example:
```
/dev/nvme0n1p2 -> /
ext4
80% used
```

## 7. Process Monitoring

This is a must-have for professional tools.

For each process:
- PID
- User
- CPU %
- Memory %
- Thread count
- Priority / nice
- State
- Runtime
- Command

Advanced
- Per-process IO
- Open file descriptors
- Memory maps
- CPU affinity
- Cgroup

Sources:
```
/proc/[pid]
```

## 8. Network Monitoring
Network Interfaces
- Interface name
- MAC address
- IP addresses
- MTU
- Link speed
- Driver

Traffic
- RX bytes/sec
- TX bytes/sec
- Packets/sec
- Errors
- Drops

Connections
- Active TCP connections
- UDP sockets
- Listening ports

Network stats
- TCP retransmits
- SYN backlog
- packet drops

Sources:
```
/proc/net/dev
/proc/net/tcp
```

## 9. Temperature & Sensors

Hardware health is very useful.

Monitor:
- CPU temperature
- GPU temperature
- Motherboard temperature
- VRM temperature
- Disk temperature
- Fan speeds
- Voltages

Tool integration:
- lm-sensors

Sources:
```
/sys/class/hwmon
```

## 10. Power Monitoring (Laptop / Servers)

If supported:
- Battery level
- Battery health
- Power consumption
- AC adapter status
- Charging rate

Sources:
```
/sys/class/power_supply
```

## 11. Container & Virtualization Detection

Important for modern environments.

Detect:
- Running inside Docker
- Running inside Kubernetes
- VM hypervisor

Hypervisor examples:
- KVM
- VMware
- VirtualBox

Metrics:
- cgroup resource limits
- container CPU usage
- container memory usage

## 12. System Load / Performance Metrics

Useful for diagnosing slow systems.

Monitor:
- Load average
- Run queue length
- CPU steal time
- IO wait
- Scheduler stats
- context switches
- interrupts/sec

## 13. Security Monitoring (Advanced)

Some advanced diagnostics tools include:
- Logged-in users
- Last login
- SSH sessions
- Failed login attempts
- SELinux status
- AppArmor status
- Firewall status

## 14. Logs

Expose system logs:
- Kernel logs
- System logs
- Service logs

Via:
- journalctl

Features:
- log tail
- error highlighting
- filter by service

## 15. Hardware Inventory

Useful for bug reports.

Detect:

**Motherboard**
- Vendor
- Model
- BIOS version

**PCI devices**
- GPUs
- Network cards
- Storage controllers

**Tool integration:**
- lspci

**USB devices**
- Vendor
- Product
- Device class

**Tool:**
- lsusb

## 16. Alerts / Thresholds

Professional tools allow:

Examples:
```
CPU > 90%
RAM < 500MB
Disk > 95%
Temperature > 85°C
```
Then:
- CLI alerts
- logs
- notifications