import logic

def main():
    sysinfo = {
        "username": "",
        "hostname": "",
        "osname": ""
    }
    
    sysinfo["username"] = logic.read_username()
    sysinfo["hostname"] = logic.read_hostname()
    sysinfo["osname"] = logic.read_osname()
    
    print(f"{sysinfo['username']}@{sysinfo['hostname']}")
    for _ in range(len(sysinfo["username"]) + len(sysinfo["hostname"]) + 1):
        print("-", end="")
    print()
    print(f"OS: {sysinfo['osname']}")

if __name__ == "__main__":
    main()
