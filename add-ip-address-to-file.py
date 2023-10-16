#-------------------------------------------------------------------------------------------------------------------
# Importación de biblioteca/módulo para el script

# Biblioteca / módulo con funciones relacionadas con direcciones IP
import ipaddress

# Biblioteca / módulo para funciones relacionadas con el sistema operativo que usa el script
import os

# Biblioteca / módulo para identificar el sistema operativo
import platform


#-------------------------------------------------------------------------------------------------------------------
# Declaración de variables

# Variable para especificar el fichero de entrada de las direcciones IP
filename = "ip-address-of-attackers.txt"


#-------------------------------------------------------------------------------------------------------------------
# Declaración de funciones

# Función para realizar la limpieza de pantalla al principio del script
def clear_screen():
    operative_system = platform.system()
    if (operative_system != 'Linux') and (operative_system != 'Windows'):
        print('Neither Linux or Windows, the script will stop the execution')
        exit(1)
    elif (operative_system == 'Linux'):
        os.system('clear')
    elif (operative_system == 'Windows'):
        os.system('cls')


# Función para comprobar si la inserción es una dirección IP válida
def is_valid_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False


# Función para comprobar si la dirección IP a insertar existe o no en el fichero de direcciones
def ip_exists(filename, ip):
    with open(filename, 'r') as f:
        lines = f.readlines()

    return ip in [line.strip() for line in lines]


# Función para añadir la dirección IP al fichero en el caso de no existir y ordena el contenido del fichero
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


# Función principal que pregunta por una IP y llama al resto de funciones
def main():
    clear_screen()
    while True:
        ip = input("Introduce una dirección IP (o 'q' para terminar): ")
        
        if ip == 'q':
            break
        
        if is_valid_ip(ip):
            add_and_sort_ip(filename, ip)
        else:
            print("La dirección IP '{}' no es válida. Por favor, introduce una dirección IP válida.".format(ip))

    print("Script terminado.")


#-------------------------------------------------------------------------------------------------------------------
# Ejecución de la función principal

if __name__ == "__main__":
    main()
