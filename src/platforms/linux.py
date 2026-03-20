import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import colors

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

def read_memory():
    with open("/proc/meminfo", "r") as meminfo:
        for line in meminfo:
            if line.startswith("MemTotal"):
                memory = line.split(":")[1].strip()
                memory = int(memory[:-3])
                memory = float(memory / (1024 * 1024))
            elif line.startswith("MemAvailable"):
                available = line.split(":")[1].strip()
                available = int(available[:-3])
                available = float(available / (1024 * 1024))
                used = memory - available
        return f"{used: .2f} GiB / {memory: .2f} GiB"
    return None

def distro_logo():
    osname = read_os().strip().split()[0].lower()
    if os.path.exists(f"/home/{os.getlogin()}/.local/share/mlzfetch/logos/{osname}.txt"):
        with open(f"/home/{os.getlogin()}/.local/share/mlzfetch/logos/{osname}.txt") as logo:
            return logo.read().format(**colors.COLORS)
    else:
        return None
