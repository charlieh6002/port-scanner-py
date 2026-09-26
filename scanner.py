import socket
import subprocess
import sys
from datetime import datetime #tracks execution time

#---PRE-SCAN---

print("_" * 150)
print()
print("OPEN PORT SCANNER")
print("created by CH")
print("_" * 150)
print()

#get target
print("< enter target host name > ")
target = input("")
targetIP = socket.gethostbyname(target)
portRange = (0, 65535)

#---SCAN-PHASE---

startTime = datetime.now()
print()
print("starting scan (time: {})".format(startTime))
print()
portRange = 0, 100 #default for testing

try:
    for port in range(portRange[0], portRange[1] + 1): #+1 as upper limit is exclusive
        currentSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #temporary file for storing socket information
        result = currentSocket.connect_ex((targetIP, port))
        if result == 0:
            print("port {}  OPEN".format(port))
        currentSocket.close()            
except KeyboardInterrupt:
    print("closing")
    sys.exit()

except socket.gaierror:
    print("hostname could not be resolved. closing")
    sys.exit()

except socket.error:
    print("could not connect to server. closing")
    sys.exit()

endTime = datetime.now()

#---POST---

print()
time = endTime - startTime
print("timet taken, {}s".format(time))
sys.exit()