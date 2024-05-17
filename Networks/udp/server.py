import socket

def main():
    # Create a UDP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket to a port
    server_address = ('127.0.0.1', 9999)
    server_socket.bind(server_address)

    print('UDP server is listening on {}:{}'.format(*server_address))

    # Receive and print incoming messages
    while True:
        data, client_address = server_socket.recvfrom(1024)
        print('Received message from {}: {}'.format(client_address, data.decode()))

if __name__ == '__main__':
    main()
