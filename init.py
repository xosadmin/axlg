import os
from utils import runCommand
from conf import sysconfig

def initDependRun():
    dependencies = ["ping","traceroute","mtr"]
    notFoundDepends = []
    for item in dependencies:
        result = runCommand([item])
        if result == "Error: Command not found":
            notFoundDepends.append(item)
    if len(notFoundDepends) > 0:
        print(f"Error: Dependency {notFoundDepends} not satisfied.")
        return False
    else:
        return True

def testFileGen():
    absLocation = os.path.join("testfile")
    testFileSize = sysconfig["TestFileSize"]
    if not os.path.exists(absLocation):
        os.makedirs(absLocation)
    for item in testFileSize:
        filename = os.path.join(absLocation, f"{item}MB.test")
        with open(filename, 'wb') as f:
            f.write(bytearray(int(item) * 1024 * 1024))
    return True

