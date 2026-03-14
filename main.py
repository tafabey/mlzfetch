import os
import platforms.linux as logic

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
        "shell": ""
    }
    
    sysinfo["username"] = logic.read_username()
    sysinfo["hostname"] = logic.read_hostname()
    sysinfo["os"] = logic.read_os()
    sysinfo["host"] = logic.read_host()
    sysinfo["kernel"] = logic.read_kernel()
    
    sysinfo["uptime_hours"], sysinfo["uptime_mins"] = logic.read_uptime()
    if sysinfo["uptime_hours"] > 1:
        sysinfo["uptime"] = " ".join([sysinfo["uptime"], str(sysinfo["uptime_hours"]), "hours"]).strip()
    elif sysinfo["uptime_hours"] == 1:
        sysinfo["uptime"] = " ".join([sysinfo["uptime"], "1 hour"]).strip()
    if sysinfo["uptime_mins"] > 1:
        sysinfo["uptime"] = " ".join([sysinfo["uptime"], str(sysinfo["uptime_mins"]), "mins"]).strip()
    elif sysinfo["uptime_mins"] == 1:
        sysinfo["uptime"] = " ".join(sysinfo["uptime"], "1 min").strip()

    sysinfo["shell"] = logic.read_shell()
    
    print(f"{sysinfo['username']}@{sysinfo['hostname']}")
    for _ in range(len(sysinfo["username"]) + len(sysinfo["hostname"]) + 1):
        print("-", end="")
    print()
    print(f"OS: {sysinfo['os']}")
    print(f"Host: {sysinfo['host']}")
    print(f"Kernel: {sysinfo['kernel']}")
    print(f"Uptime: {sysinfo['uptime']}")
    print(f"Shell: {sysinfo['shell']}")

if __name__ == "__main__":
    main()
