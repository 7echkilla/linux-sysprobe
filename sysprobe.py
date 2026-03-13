from modules.system_info import get_system_info
from modules.disk_useage import get_disk_useage
from modules.docker_status import get_docker_status
from modules.load_avg import get_load_avg
from modules.kernel_logs import get_kernel_errors

def main():
    print("\nSystem Information")
    print("------------------")
    get_system_info()

    print("\nDisk Usage")
    print("----------")
    get_disk_useage()

    print("\nDocker Containers")
    print("-----------------")
    get_docker_status()

    print("\nSystem Load")
    print("-----------")
    get_load_avg()

    print("\nRecent Kernel Errors")
    print("--------------------")
    get_kernel_errors()

if __name__ == "__main__":
    main()