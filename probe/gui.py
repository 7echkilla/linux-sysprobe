import time

from probe.loader import load_plugins

def run(interval=1):
    """Load live dashboard"""

    plugins = load_plugins()

    while True:

        print("\033c", end="")
        print("=== Live Dashboard ===\n")

        for plugin in plugins.values():
            data = plugin.collect()
            formatted = " | ".join(f"{k}: {v}" for k, v in data.items())

            print(f"{plugin.name:10} {formatted}")

        print("\nPress Ctrl+C to exit")
        time.sleep(interval)

if __name__ == "__main__":
    run()