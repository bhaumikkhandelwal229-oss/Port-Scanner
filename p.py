import socket
from datetime import datetime

print("====================================")
print("        PYTHON PORT SCANNER         ")
print("====================================")

# Ask user for target
target = input("Enter target IP or domain: ")

# Ask for port range
start_port = int(input("Enter starting port: "))
end_port = int(input("Enter ending port: "))

print("\nScanning target:", target)
print("Scanning ports:", start_port, "to", end_port)
print("------------------------------------")

# Start time
start_time = datetime.now()

try:
    for port in range(start_port, end_port + 1):

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        result = s.connect_ex((target, port))

        if result == 0:
            try:
                service = socket.getservbyport(port)
            except:
                service = "Unknown Service"

            print(f"Port {port} is OPEN ({service})")

        s.close()

except KeyboardInterrupt:
    print("\nScan stopped by user")

except socket.gaierror:
    print("Hostname could not be resolved")

except socket.error:
    print("Could not connect to server")

# End time
end_time = datetime.now()
total_time = end_time - start_time

print("------------------------------------")
print("Scanning completed in:", total_time)