import sys
import socket
import argparse
import os

def tcp_server(port):
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        server_address = ('', port)
        server_socket.bind(server_address)
        
        server_socket.listen(1)
        
        while True:
            print('Waiting for connection...')
            
            client_socket, client_address = server_socket.accept()
            print('Connected to: ', client_address)
            
            filename = client_socket.recv(4096).decode().strip()
            
            if filename.lower() == 'end':
                break
            
            if '/' in filename or '\\' in filename:
                error_msg = "Illegal characters in file name."
                print(error_msg, file=sys.stderr)
                client_socket.sendall(error_msg.encode())
                client_socket.close()
                continue
            
            if not os.path.isfile(filename):
                error_msg = f"File '{filename}' does not exist!"
                print(error_msg, file=sys.stderr)
                client_socket.sendall(error_msg.encode())
                client_socket.close()
                continue
            
            try:
                with open(filename, 'r') as file:
                    file_content = file.read()
                
                client_socket.sendall(file_content.encode())
            
            except Exception as e:
                error_msg = f"Error while reading file '{filename}': {str(e)}"
                print(error_msg, file=sys.stderr)
                client_socket.sendall(error_msg.encode())
                client_socket.close()
                continue
            
            print(f"File sent '{filename}'")
            
            client_socket.close()
        
        server_socket.close()
        
    except Exception as e:
        print("Error: ", str(e), file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
   
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', dest='port', type=int, default=1234, help='Client port')
    args = parser.parse_args()

    tcp_server(args.port)