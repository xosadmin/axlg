import os
from utils import runCommand
from conf import sysconfig
import platform

def detectSys():
    opera_sys = platform.system()
    if opera_sys == "Linux":
        dist = platform.linux_distribution()
        return str(dist)
    else:
        return "Unknown"

def initDependRun():
    dependencies = ["ping","traceroute","mtr"]
    notFoundDepends = []
    for item in dependencies:
        if not os.path.exists(f"/bin/{item}") and not os.path.exists(f"/usr/sbin/{item}"):
            notFoundDepends.append(item)
    if len(notFoundDepends) > 0:
        print(f"Error: Dependency {notFoundDepends} not satisfied.")
        return notFoundDepends
    else:
        return True

def testFileGen():
    absLocation = os.path.join("testfile")
    testFileSize = ["10","100","1000"]
    if not os.path.exists(absLocation):
        os.makedirs(absLocation)
    for item in testFileSize:
        print(f"Generating {item}MB.test")
        filename = os.path.join(absLocation, f"{item}MB.test")
        with open(filename, 'wb') as f:
            f.write(bytearray(int(item) * 1024 * 1024))
    return True

os_sys = detectSys().lower()
if os_sys != "unknown":
    initdep = initDependRun()
    if initdep:
        testFileGen()
        print("Complete.")
    else:
        for item in initdep:
            if os_sys == "centos" or os_sys == "fedora" or os_sys == "almalinux" or os_sys == "rockylinux":
                runCommand(["yum","-y","install",item])
            elif os_sys == "ubuntu" or os_sys == "debian":
                runCommand(["apt","-y","install",item])
            else:
                print("Cannot find suitable installation method(s). Exiting...")
                exit(1)
else:
    print("Unsupported OS. Exiting...")
    exit(1)
