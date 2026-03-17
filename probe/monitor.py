import time

from probe.loader import load_modules

def run(interval=1):
    """
    Load metrics for live monitoring
    """
    plugins = load_modules()

    try:
        while True:
            print("\033c", end="")
            print("=== Live Metrics ===\n")

            for plugin in plugins.values():
                data = plugin.get_data()
                format = " | ".join(f"{metric}: {value}" for metric, value in data.items())

                print(f"{plugin.name:10} {format}")

            print("\nPress Ctrl+C to exit")
            time.sleep(interval)

    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    run()