import os
import platform

def get_system_info():
    kernel = platform.release()
    cpu_cores = os.cpu_count()
    mem_total = 0

    with open("/proc/meminfo") as file:
        for line in file:
            if "MemTotal" in line:
                mem_total = int(line.split()[1]) / 1024 / 1024

    with open("/proc/uptime") as file:
        uptime_seconds = float(file.readline().split()[0])

    hours = int(uptime_seconds // 3600)

    print("System Information")
    print("------------------")

    print(f"Kernel: {kernel}")
    print(f"CPU Cores: {cpu_cores}")
    print(f"Memory: {mem_total:.2f} GB")
    print(f"Uptime: {hours} hours")

def run():
    get_system_info()

if __name__ == "__main__":
    run()