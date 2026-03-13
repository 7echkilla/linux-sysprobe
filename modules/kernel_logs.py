import subprocess

def get_kernel_errors():
    result = subprocess.run(
        ["dmesg", "--level=err"],
        capture_output=True,
        text=True
    )

    lines = result.stdout.splitlines()

    for line in lines:
        print(line)