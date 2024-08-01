import socket
from datetime import datetime

# Yaygın port-hizmet eşlemelerini içeren bir sözlük
port_services = {
    20: "FTP",
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    67: "DHCP",
    68: "DHCP",
    69: "TFTP",
    80: "HTTP",
    110: "POP3",
    119: "NNTP",
    123: "NTP",
    143: "IMAP",
    161: "SNMP",
    162: "SNMP",
    443: "HTTPS",
    445: "SMB",
    993: "IMAPS",
    995: "POP3S",
    1080: "SOCKS",
    1433: "MSSQL",
    1434: "MSSQL",
    3306: "MySQL",
    3389: "RDP",
    5900: "VNC",
    8080: "HTTP-Proxy"
}

def get_service_name(port, protocol):
    return port_services.get(port, "Unknown Service")

def scan_port(ip, port, protocol):
    sock = socket.socket(socket.AF_INET, protocol)
    sock.settimeout(1)
    result = sock.connect_ex((ip, port))
    sock.close()
    return result == 0

ip_address = input("Tarama yapılacak IP adresini girin: ")
start_port = int(input("Başlangıç portunu girin: "))
end_port = int(input("Bitiş portunu girin: "))

print(f"IP adresi {ip_address} üzerinde port taraması başlıyor...")
print(f"Taranan port aralığı: {start_port}-{end_port}")
start_time = datetime.now()

for port in range(start_port, end_port + 1):
    service = get_service_name(port, socket.SOCK_STREAM)
    if scan_port(ip_address, port, socket.SOCK_STREAM):
        print(f"Port {port}/TCP ({service}) açık!")
    else:
        print(f"Port {port}/TCP ({service}) kapalı.")
    
    service = get_service_name(port, socket.SOCK_DGRAM)
    if scan_port(ip_address, port, socket.SOCK_DGRAM):
        print(f"Port {port}/UDP ({service}) açık!")
    else:
        print(f"Port {port}/UDP ({service}) kapalı.")

end_time = datetime.now()
total_time = end_time - start_time
print(f"Tarama tamamlandı! Geçen süre: {total_time}")
