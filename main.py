import sys
if sys.platform == "linux":
    import platforms.linux as provider
else:
    print("This program only runs on Linux")
    sys.exit(1)
import colors

def main():
    sysinfo = {
        "username": "",
        "hostname": "",
        "os": "",
        "host": "",
        "kernel": "",
        "uptime_hours": 0,
        "uptime_mins": 0,
        "uptime": "",
        "shell": "",
        "resolution": "",
        "cpu": "",
        "memory": ""
    }
    
    sysinfo["username"] = provider.read_username()
    sysinfo["hostname"] = provider.read_hostname()
    sysinfo["os"] = provider.read_os()
    sysinfo["host"] = provider.read_host()
    sysinfo["kernel"] = provider.read_kernel()
    
    sysinfo["uptime_hours"], sysinfo["uptime_mins"] = provider.read_uptime()
    if sysinfo["uptime_hours"] > 1:
        sysinfo["uptime"] = " ".join([sysinfo["uptime"], str(sysinfo["uptime_hours"]), "hours"]).strip()
    elif sysinfo["uptime_hours"] == 1:
        sysinfo["uptime"] = " ".join([sysinfo["uptime"], "1 hour"]).strip()
    if sysinfo["uptime_mins"] > 1:
        sysinfo["uptime"] = " ".join([sysinfo["uptime"], str(sysinfo["uptime_mins"]), "mins"]).strip()
    elif sysinfo["uptime_mins"] == 1:
        sysinfo["uptime"] = " ".join(sysinfo["uptime"], "1 min").strip()

    sysinfo["shell"] = provider.read_shell()
    sysinfo["resolution"] = provider.read_resolution()
    sysinfo["cpu"] = provider.read_cpu()
    sysinfo["memory"] = provider.read_memory()
    
    print(f"{colors.BOLD}{sysinfo['username']}@{sysinfo['hostname']}{colors.END}")
    for _ in range(len(sysinfo["username"]) + len(sysinfo["hostname"]) + 1):
        print("-", end="")
    print()
    print(f"{colors.BLUE}OS{colors.END}: {sysinfo['os']}")
    print(f"{colors.BLUE}Host{colors.END}: {sysinfo['host']}")
    print(f"{colors.BLUE}Kernel{colors.END}: {sysinfo['kernel']}")
    print(f"{colors.BLUE}Uptime{colors.END}: {sysinfo['uptime']}")
    print(f"{colors.BLUE}Shell{colors.END}: {sysinfo['shell']}")
    print(f"{colors.BLUE}Resolution{colors.END}: {sysinfo['resolution']}")
    print(f"{colors.BLUE}CPU{colors.END}: {sysinfo['cpu']}")
    print(f"{colors.BLUE}Memory{colors.END}: {sysinfo['memory']}")
    
if __name__ == "__main__":
    main()
