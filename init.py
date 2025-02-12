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
        if not os.path.exist(os.path.join("testfile",f"{item}MB.test")):
            print(f"Generating {item}MB.test")
            filename = os.path.join(absLocation, f"{item}MB.test")
            with open(filename, 'wb') as f:
                f.write(bytearray(int(item) * 1024 * 1024))
        else:
            print(f"{item}MB.test file exists. Skipping...")
    return True
