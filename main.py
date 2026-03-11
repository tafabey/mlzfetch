import os

sysinfo = {
    "username": "",
    "hostname": "",
    "osname": ""
}

try:
    sysinfo["username"] = os.getlogin()
except OSError:
    print("Can't find username")

with open("/proc/sys/kernel/hostname") as hostname:
    sysinfo["hostname"] = hostname.read().rstrip("\n")

print(f"{sysinfo.get('username')}@{sysinfo.get('hostname')}")
for _ in range(len(sysinfo.get("username")) + len(sysinfo.get("hostname")) + 1):
    print("-", end="")
print()

with open("/etc/os-release") as osname:
    for line in osname:
        if line.startswith("PRETTY_NAME=\""):
            sysinfo["osname"] = line[13:-1]
            sysinfo["osname"] = sysinfo["osname"].rstrip('"')

print(f"OS: {sysinfo.get("osname")}")
