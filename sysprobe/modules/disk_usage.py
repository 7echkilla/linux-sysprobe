import shutil
import psutil

def get_real_partitions():
    valid_filesystems = {"ext4", "xfs", "btrfs", "ntfs", "vfat"}
    partitions = []

    for partition in psutil.disk_partitions():
        if (partition.fstype.lower() not in valid_filesystems):
            continue

        if (partition.device.startswith("/dev/loop")):
            continue

        partitions.append(partition)

    return partitions

def run():
    constant = 1024 ** 3

    print("\nDisk Usage")
    print("----------------------------------------------------------------")
    print(f"{'Mount':<20}{'Total(GB)':>10}{'Used(GB)':>10}{'Free(GB)':>10}{'Use%':>8}")
    print("----------------------------------------------------------------")

    for partition in get_real_partitions():
        try:
            usage = psutil.disk_usage(partition.mountpoint)
            total = usage.total / constant
            used = usage.used / constant
            free = usage.free / constant
            
            print(f"{partition.mountpoint:<20}{total:>10.1f}{used:>10.1f}{free:>10.1f}{usage.percent:>7}%")

        except PermissionError:
            print(f"Permission denied for {partition}")

if __name__ == "__main__":
    run()