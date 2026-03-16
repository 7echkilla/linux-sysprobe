import subprocess

# requires elevated permission
def get_kernel_logs():
    print("\nRecent Kernel Errors")
    print("--------------------")

    try:
        logs = subprocess.check_output(
            ["dmesg", "--level=err", "--ctime"]
        ).decode().splitlines()

        for line in logs[-5:]:
            print(line)

    except Exception:
        print("Unable to read kernel logs")

def run():
    get_kernel_logs()

if __name__ == "__main__":
    run()