import sys
import socket

def run_client(server_ip, port):
    
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        while True:
            line = sys.stdin.readline().strip()
            client_socket.sendto(line.encode(), (server_ip, port))
            
            response, _ = client_socket.recvfrom(256)
            result = response.decode().split('\n')
            char_count = int(result[0].split()[0])
            a_count = int(result[1].split()[0])

            print(f'{char_count} characters')
            print(f'{a_count} a')
        
    except OSError as e:
        print(f'Error connecting to server: {e}', file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    port = 1234
    server_ip = ''

    if len(sys.argv) > 1 and sys.argv[1] == '-p' and len(sys.argv) > 2:
        port = int(sys.argv[2])

    if len(sys.argv) > 3:
        server_ip = sys.argv[3]

    if not server_ip:
        print('Usage: udpklient.py [-p port] server_IP', file=sys.stderr)
        sys.exit(1)

    run_client(server_ip, port)