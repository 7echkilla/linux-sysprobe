import json
import datetime
from sysprobe.modules import system

def run():
    data = {
        "timestamp": str(datetime.datetime.now()),
        "system": system.run()
    }

    with open("sysprobe_report.json", "w") as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    run()