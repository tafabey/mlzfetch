import sys
if sys.platform == "linux":
    from platforms import linux as provider
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
        "memory": "",
        "distro_logo": ""
    }

    infolines = []
    
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
    sysinfo["distro_logo"] = provider.distro_logo()
    
    infolines.append(f"\t{colors.BOLD}{sysinfo['username']}@{sysinfo['hostname']}{colors.END}")

    empty_line = ""
    for _ in range(len(sysinfo["username"]) + len(sysinfo["hostname"]) + 1):
        empty_line = empty_line + "-"

    infolines.append(f"\t{empty_line}")
    infolines.append(f"{colors.BLUE}OS{colors.END}: {sysinfo['os']}")
    infolines.append(f"{colors.BLUE}Host{colors.END}: {sysinfo['host']}")
    infolines.append(f"{colors.BLUE}Kernel{colors.END}: {sysinfo['kernel']}")
    infolines.append(f"{colors.BLUE}Uptime{colors.END}: {sysinfo['uptime']}")
    infolines.append(f"{colors.BLUE}Shell{colors.END}: {sysinfo['shell']}")
    infolines.append(f"{colors.BLUE}Resolution{colors.END}: {sysinfo['resolution']}")
    infolines.append(f"{colors.BLUE}CPU{colors.END}: {sysinfo['cpu']}")
    infolines.append(f"{colors.BLUE}Memory{colors.END}: {sysinfo['memory']}")

    count = 0
    if sysinfo["distro_logo"] is not None:
        for line in sysinfo["distro_logo"].splitlines():
            print(f"{line}", end="")
            try:
                print(f"\t{infolines[count]}")
            except IndexError:
                print()
            count += 1
    else:
        for line in infolines:
            print(line)
if __name__ == "__main__":
    main()
