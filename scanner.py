import sys
import socket
from datetime import datetime
import time

start_time = datetime.now()
# defining the target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) # Translating hostname to IPv4
else:
    print("Invalid arguments.")   
    print("Syntax: python3 scanner.py <ip>") 


# Adding banner
print("\n")

# Less time consuming but ugly

logo = open("./scanner logo.txt", "r")
print(logo.read())
time.sleep(1)
logo.close()

print("\n")

print("-"*50)
print("Scanning target: "+target)
print("Time started: "+ str(datetime.now()))
print("-"*50)

try:
    for port in range(50, 85):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port))
        if result == 0:
            print(f"Port {port} is open")
        s.close()

except KeyboardInterrupt:
    print("\nExiting program.")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved.")
    sys.exit()

except socket.error:
    print("Could not connect to server.")
    sys.exit()

end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))