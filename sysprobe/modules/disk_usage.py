import shutil

def run():
    total, used, free = shutil.disk_usage("/")
    
    percent_used = (used / total) * 100
    percent_free = (free / total) * 100

    print("\nDisk Usage")
    print("----------")
    print(f"/ : {percent_used:.1f}% used, {percent_free:.1f}% free")