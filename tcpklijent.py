import sys
import socket
import argparse

def tcp_client(server_ip, port):
    try:

        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        server_address = (server_ip, port)
        client_socket.connect(server_address)
        
        filename = input().strip()
        
        client_socket.sendall(filename.encode())
        
        response = client_socket.recv(4096)
        
        print(response.decode())
        
        client_socket.close()
        
    except ConnectionRefusedError:
        print("Unable to connect to the server.", file=sys.stderr)
        sys.exit(1)
    except socket.gaierror:
        print("The specified server IP address is not valid.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print("Error:", str(e), file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', dest='port', type=int, default=1234, help='Server port')
    parser.add_argument('server_ip', help='Server IP address')
    args = parser.parse_args()

    tcp_client(args.server_ip, args.port)