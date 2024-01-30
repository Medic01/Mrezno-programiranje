import sys
import socket

def run_server(port):
    
    try:
        
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server_socket.bind(('localhost', port))
        print(f'Server running on port {port}')
        
        while True:
            data, address = server_socket.recvfrom(256)
            line = data.decode().strip()
            
            char_count = len(line)
            a_count = line.count('a')
            
            response = f'{char_count} chars \n{a_count} a'
            server_socket.sendto(response.encode(), address)
        
    except OSError as e:
        print(f'Error starting server: {e}', file=sys.stderr)
        sys.exit()

if __name__ == '__main__':
    
    port = 1234
    
    if len(sys.argv) > 1 and sys.argv[1] == '-p' and len(sys.argv) > 2:
        port = int(sys.argv[2])
    
    run_server(port)