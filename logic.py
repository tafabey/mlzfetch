import os

def read_username():
    try:
        return os.getlogin()
    except OSError:
        return "error"

def read_hostname():
    with open("/proc/sys/kernel/hostname") as host:
        return host.read().rstrip("\n")

def read_osname():
    with open("/etc/os-release") as os_release:
        for line in os_release:
            if line.startswith("PRETTY_NAME=\""):
                return line[13:-1]
