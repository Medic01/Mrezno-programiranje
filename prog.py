#Program ispisuje IP adresu racunala zadanog argumentom hostname u pozivu programa 
#CNAME i broj porta koji odgovara nazivu usluge navedene u pozivu porgrama(servicename)
#Ispisuje se samo jedan redak, s prvom vraćenom  IPv4 adresom.

#Pretpostavljeni transportni protokol je TCP, a UDP se aktivira koristenjem opcije -u

#Broj porta ispisuje se u dekatskom obliku, a heksadekatski oblik(4 znamenke) aktivira se
#koristenjem opcije -x. Broj porta prikazan je u host byte redoslijedu, a network byte redoslijed se dobiva koristenjem opcije -n

#Argumenti i opcije python prog.py [-t|-u] [-x] [-h|-n] hostname servicename
#-t TCP (default)
#-u UDP
#-x hex (4 hex znamenke, 2 bajta)
#-h host byte order (default)
#-n network byte order

import argparse
import socket
import struct
import sys


def parse_args():
    parser = argparse.ArgumentParser(description='Resolve IP address of given hostname and service name.')
    parser.add_argument('-t', '--tcp', action='store_true', help='Use TCP (default)')
    parser.add_argument('-u', '--udp', action='store_true', help='Use UDP')
    parser.add_argument('-x', '--hex', action='store_true', help='Display port number in hexadecimal (4 digits, 2 bytes)')
    parser.add_argument('-n', '--network-byte-order', action='store_true', help='Display port number in network byte order')
    parser.add_argument('hostname', type=str, help='Hostname to resolve')
    parser.add_argument('service', type=str, help='Service name to resolve')
    return parser.parse_args()


def get_ip_address(hostname, service, proto):
    try:
        addrinfo = socket.getaddrinfo(hostname, service, proto, socket.AF_INET)
    except socket.gaierror as e:
        print(f"prog: {e}", file=sys.stderr)
        sys.exit(1)
    first_addr = addrinfo[0][4][0]
    cname = socket.gethostbyaddr(first_addr)[0]
    port = addrinfo[0][4][1]
    return first_addr, cname, port


def main():
    args = parse_args()

    if args.udp:
        proto = socket.SOCK_DGRAM
    else:
        proto = socket.SOCK_STREAM

    ip_address, cname, port = get_ip_address(args.hostname, args.service, proto)

    if args.network_byte_order:
        port_str = struct.pack('!H', port)
    else:
        port_str = struct.pack('H', port)

    if args.hex:
        port_hex = port_str.hex().zfill(4)
        print(f"{ip_address} ({cname}) {port_hex}")
    else:
        port_dec = int.from_bytes(port_str, byteorder='big')
        print(f"{ip_address} ({cname}) {port_dec}")


if __name__ == '__main__':
    main()
