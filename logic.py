import os

def read_username():
    try:
        return os.getlogin()
    except OSError:
        return "error"

def read_hostname():
    with open("/proc/sys/kernel/hostname") as hostname:
        return hostname.read().rstrip("\n")

def read_os():
    with open("/etc/os-release") as os_release:
        for line in os_release:
            if line.startswith("PRETTY_NAME=\""):
                return line[13:-2]

def read_host():
    with open("/sys/class/dmi/id/product_name") as host:
        return host.read().rstrip("\n")

def read_kernel():
    osname = []
    with open("/proc/sys/kernel/ostype") as ostype:
        osname.append(ostype.read().rstrip())
    with open("/proc/sys/kernel/osrelease") as osrelease:
        osname.append(osrelease.read().rstrip())
    return " ".join(osname)
            
