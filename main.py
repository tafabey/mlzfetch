import sys
if sys.platform == "linux":
    import platforms.linux as provider
else:
    print("This program only runs on Linux")
    sys.exit(1)

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
        "resolution": ""
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
    
    print(f"{sysinfo['username']}@{sysinfo['hostname']}")
    for _ in range(len(sysinfo["username"]) + len(sysinfo["hostname"]) + 1):
        print("-", end="")
    print()
    print(f"OS: {sysinfo['os']}")
    print(f"Host: {sysinfo['host']}")
    print(f"Kernel: {sysinfo['kernel']}")
    print(f"Uptime: {sysinfo['uptime']}")
    print(f"Shell: {sysinfo['shell']}")
    print(f"Resolution: {sysinfo['resolution']}")
    
if __name__ == "__main__":
    main()
