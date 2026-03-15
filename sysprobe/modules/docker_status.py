import subprocess

def get_docker_status():
    print("\nDocker Containers")
    print("-----------------")

    try:
        output = subprocess.check_output(
            ["docker", "ps", "-q"]
        ).decode()

        containers = len(output.splitlines())
        print(f"{containers} running")

    except Exception:
        print("Docker not available")

def run():
    get_docker_status()

if __name__ == "__main__":
    run()