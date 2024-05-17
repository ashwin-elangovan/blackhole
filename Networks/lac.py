import socket

# Create a TCP socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    # Connect to the server
    client_socket.connect(('127.0.0.1', 53853))
    print(f"Connected to server at {('127.0.0.1', 53853)}")

    # Send data to the server
    data = "Hello, server!"
    client_socket.sendall(data.encode('utf-8'))

    # Close the connection
    client_socket.close()
