import socket
import threading

def handle_connection(conn):
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print(f"Received: {data.decode('utf-8')}")
    conn.close()

def server(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind(('127.0.0.1', port))
        server_socket.listen(5)
        print(f"Server listening on 127.0.0.1:{port}")
        while True:
            conn, addr = server_socket.accept()
            print(f"Accepted connection from {addr}")
            threading.Thread(target=handle_connection, args=(conn,), daemon=True).start()

if __name__ == "__main__":
    port = 8080  # Change this to your desired port
    server(port)
