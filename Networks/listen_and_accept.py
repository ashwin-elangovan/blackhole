import socket
import threading

def handle_connection(conn):
    while True:
        # data = conn.recv(1024): This receives data from the client connection conn in chunks of up to 1024
        # bytes and assigns it to the variable data.
        data = conn.recv(1024)
        if not data:
            break
        print(f"Received: {data.decode('utf-8')}")
    conn.close()

def server():
    # Create a TCP socket
    # with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket::
    # This creates a TCP socket server_socket using IPv4 (AF_INET) and the TCP protocol (SOCK_STREAM).
    # The with statement ensures the socket is closed properly after use.
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        # Bind the socket to localhost and a random port
        # server_socket.bind(('127.0.0.1', 0)): This binds the server socket to the localhost (127.0.0.1)
        # and a random port. The 0 indicates that the OS should choose an available port.
        server_socket.bind(('127.0.0.1', 3000))
        # server_socket.listen(5): This sets the server socket to listen for incoming connections with a
        # maximum queue size of 5 pending connections.
        # Listen for incoming connections
        server_socket.listen(5)
        print(f"Server listening on {server_socket.getsockname()}")

        # Accept incoming connections in a loop
        while True:
            conn, addr = server_socket.accept()
            print(f"Accepted connection from {addr}")
            # Start a new thread to handle the connection
            threading.Thread(target=handle_connection, args=(conn,), daemon=True).start()

def client(server_address):
    # Create a TCP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        # Connect to the server
        client_socket.connect(server_address)
        print(f"Connected to server at {server_address}")
        # data = "Hello, server!"
        # client_socket.sendall(data.encode('utf-8'))
        # Close the connection immediately to initiate graceful termination
        client_socket.close()

# Start the server in a separate thread
server_thread = threading.Thread(target=server, daemon=True)
server_thread.start()

# Wait for a short time to ensure the server is up and running
import time
time.sleep(1)

# Get the server address from the server thread
server_address = server()

# Start the client
client(server_address)
