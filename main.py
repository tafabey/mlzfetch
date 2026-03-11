import os

sysinfo = {
    "username": "",
    "hostname": ""
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
