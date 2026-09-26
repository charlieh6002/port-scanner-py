import socket
import subprocess
import sys
from datetime import datetime #tracks execution time

#get target
target = input("enter target host name: ")
targetIP = socket.gethostbyname(target)