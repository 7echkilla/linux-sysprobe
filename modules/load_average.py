def get_load_average():
    with open("/proc/loadavg") as file:
        load = file.read().split()

    print(f"1m: {load[0]}")
    print(f"5m: {load[1]}")
    print(f"15m: {load[2]}")