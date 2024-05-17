import socket

def client(server_ip, server_port):
    server_address = (server_ip, server_port)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect(server_address)
        print(f"Connected to server at {server_address}")
        # Send data to the server
        message = "Hello from client!"
        client_socket.sendall(message.encode('utf-8'))
        print(f"Sent to server: {message}")
        client_socket.close()

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python client.py <server_ip> <server_port>")
        sys.exit(1)

    server_ip = sys.argv[1]
    server_port = int(sys.argv[2])
    client(server_ip, server_port)

# python client.py 127.0.0.1 8080

