import shutil

from rich import print

def get_disk_usage():
    total, used, free = shutil.disk_usage("/")
    percent = (used / total) * 100
    print(f"/ : {percent:.0f}% used")