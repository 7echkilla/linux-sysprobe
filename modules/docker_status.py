import subprocess

def get_docker_status():
    try:
        result = subprocess.run(
            ["docker", "ps", "-q"],
            capture_output=True,
            text=True
        )

        containers = result.stdout.strip.split("\n")

        if containers == ['']:
            print("0 running")
        else:
            print(f"{len(containers)} running")
        
    except:
        print(f"Docker not installed")