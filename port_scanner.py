import socket

def scan_port(target_ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target_ip, port))
        if result == 0:
            print(f"Port {port} is open")
        sock.close()
    except socket.error:
        pass

target_ip = input("Enter the target IP address: ")
start_port = int(input("Enter the start port: "))
end_port = int(input("Enter the end port: "))

# Scan ports in the specified range
for port in range(start_port, end_port + 1):
    scan_port(target_ip, port)
