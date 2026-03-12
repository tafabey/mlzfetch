import logic

def main():
    sysinfo = {
        "username": "",
        "hostname": "",
        "os": "",
        "host": "",
        "kernel": ""
    }
    
    sysinfo["username"] = logic.read_username()
    sysinfo["hostname"] = logic.read_hostname()
    sysinfo["os"] = logic.read_os()
    sysinfo["host"] = logic.read_host()
    sysinfo["kernel"] = logic.read_kernel()
    
    print(f"{sysinfo['username']}@{sysinfo['hostname']}")
    for _ in range(len(sysinfo["username"]) + len(sysinfo["hostname"]) + 1):
        print("-", end="")
    print()
    print(f"OS: {sysinfo['os']}")
    print(f"Host: {sysinfo['host']}")
    print(f"Kernel: {sysinfo['kernel']}")

if __name__ == "__main__":
    main()
