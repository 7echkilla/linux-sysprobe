#!/usr/bin/env python3

import argparse

from modules.disk_usage import get_disk_usage
from modules.docker_status import get_docker_status
from modules.kernel_logs import get_kernel_errors
from modules.load_average import get_load_average
from modules.system_info import get_system_info

def main():
    parser = argparse.ArgumentParser(description="Linux system diagnostic tool")

    parser.add_argument("--system", action="store_true")
    parser.add_argument("--disk", action="store_true")
    parser.add_argument("--docker", action="store_true")
    parser.add_argument("--logs", action="store_true")
    parser.add_argument("--load", action="store_true")
    parser.add_argument("--all", action="store_true")

    args = parser.parse_args()

    if (args.system or args.all):
        print("\nSystem Information")
        print("------------------")
        get_system_info()

    if args.disk or args.all:
        print("\nDisk Usage")
        print("----------")
        get_disk_usage()

    if args.docker or args.all:
        print("\nDocker Containers")
        print("-----------------")
        get_docker_status()

    if args.load or args.all:
        print("\nSystem Load")
        print("-----------")
        get_load_average()

    if args.logs or args.all:
        print("\nRecent Kernel Errors")
        print("--------------------")
        get_kernel_errors()

if __name__ == "__main__":
    main()