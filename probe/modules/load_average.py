import os

def get_load_average():
    print("\nLoad Average")
    print("------------")

    load1, load5, load15 = os.getloadavg()

    print(f"1 min: {load1}")
    print(f"5 min: {load5}")
    print(f"15 min: {load15}")

def run():
    get_load_average()

if __name__ == "__main__":
    run()