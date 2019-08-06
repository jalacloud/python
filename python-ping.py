import os
import time

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

list = [
    '10.167.136.41',
    '10.167.136.42',
    '10.167.136.55',
    '10.167.136.56',
]

for ip in list:
    response = os.system("ping -c 1 " + ip + " 2>&1 >/dev/null")
    if response == 0:
        status = bcolors.OKGREEN + "Active" + bcolors.ENDC
    else:
        status = bcolors.FAIL + "Inactive" + bcolors.ENDC
    print("Pinging (" + ip + ") - Status: " + status)
    time.sleep(1)
