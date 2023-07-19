import ipaddress

def is_valid_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

def ip_exists(filename, ip):
    with open(filename, 'r') as f:
        lines = f.readlines()

    return ip in [line.strip() for line in lines]

def add_and_sort_ip(filename, ip):
    if not ip_exists(filename, ip):
        with open(filename, 'a+') as f:
            f.write(ip + '\n')

    with open(filename, 'r') as f:
        lines = f.readlines()

    lines = [line.strip() for line in lines if is_valid_ip(line.strip())]
    lines = sorted(lines, key=ipaddress.ip_address)

    with open(filename, 'w') as f:
        for line in lines:
            f.write(line + '\n')

filename = "ip-address-of-attackers.txt"

while True:
    ip = input("Introduce una dirección IP (o 'q' para terminar): ")
    
    if ip == 'q':
        break
    
    if is_valid_ip(ip):
        add_and_sort_ip(filename, ip)
    else:
        print("La dirección IP '{}' no es válida. Por favor, introduce una dirección IP válida.".format(ip))

print("Script terminado.")