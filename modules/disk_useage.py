import shutil

def get_disk_useage():
    total, used, free = shutil.disk_usage("/")
    percent = (used / total) * 100
    print(f"/ : {percent:.0f}% used")