import os

def read_username():
    try:
        return os.getlogin()
    except OSError:
        return "error"

def read_hostname():
    with open("/proc/sys/kernel/hostname", "r") as hostname:
        return hostname.read().rstrip("\n")

def read_os():
    with open("/etc/os-release", "r") as os_release:
        for line in os_release:
            if line.startswith("PRETTY_NAME=\""):
                return line[13:-2]

def read_host():
    with open("/sys/class/dmi/id/product_name", "r") as host:
        return host.read().rstrip("\n")

def read_kernel():
    osname = []
    with open("/proc/sys/kernel/ostype", "r") as ostype:
        osname.append(ostype.read().rstrip())
    with open("/proc/sys/kernel/osrelease", "r") as osrelease:
        osname.append(osrelease.read().rstrip())
    return " ".join(osname)
            
def read_uptime():
    hours = 0
    minutes = 0
    with open("/proc/uptime", "r") as uptime:
        minutes = int(float(uptime.read().split()[0]) / 60.0)
        hours = int(minutes / 60.0)
        minutes = int(minutes % 60)
    return hours, minutes

def read_shell():
    ppid = os.getppid()
    with open(f"/proc/{ppid}/comm", "r") as comm:
        return comm.read().strip()

def read_resolution():
    full_path = "/sys/class/drm"
    for folder in os.listdir(full_path):
        if os.path.exists(f"{full_path}/{folder}/enabled"):
            with open(f"{full_path}/{folder}/enabled", "r") as enabled:
                if enabled.readline().strip() == "enabled":
                    with open(f"{full_path}/{folder}/modes", "r") as modes:
                        return modes.readline().strip()
def read_cpu():
    with open("/proc/cpuinfo", "r") as cpuinfo:
        for line in cpuinfo:
            if line.startswith("model name"):
                return line.split(":")[1].strip()
