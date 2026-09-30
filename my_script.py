import json
import os
import platform
import socket
import sys
import getpass
from datetime import *


def detect_os() -> str:
    system = platform.system()
    if system == "Windows":
        return "Windows"
    elif system == "Linux":
        return "Linux"
    else:
        return f"Unknown ({system})"


def collect_os_info() -> dict:
    info = {
        "os": {
            "name": detect_os(),
            "release": platform.release(),
            "version": platform.version(),
            "machine": platform.machine(),
            "architecture": platform.architecture()[0],
            "processor": platform.processor() or "неизвестно",
        },
        "python": {
            "version": platform.python_version(),
            "implementation": platform.python_implementation(),
            "executable": sys.executable,
        },
        "user": {
            "username": getpass.getuser(),
            "home_dir": os.path.expanduser("~"),
            "current_dir": os.getcwd(),
        },
        "network": {
            "hostname": socket.gethostname(),
            "ip_address": socket.gethostbyname(socket.gethostname()),
        },
        "cpu": {
            "cores_logical": os.cpu_count(),
        },
        "collected_at": datetime.now().isoformat(timespec="seconds"),
    }
    return info


def save_to_json(data: dict, filename: str = "os_info.json") -> None:
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def main() -> None:
    os_info = collect_os_info()

    print(f"ОС: {os_info['os']['name']}")
    print(f"Версия: {os_info['os']['release']}")
    print(f"Пользователь: {os_info['user']['username']}")

    filename = "os_info.json"
    save_to_json(os_info, filename)
    print(f"Данные сохранены в файл: {filename}")


if __name__ == "__main__":
    main()
