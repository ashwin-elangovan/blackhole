import socket

def main():
    # Create a UDP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Send messages to the server
    server_address = ('127.0.0.1', 9999)
    messages = ['Hello', 'How are you?', 'Goodbye']

    for message in messages:
        client_socket.sendto(message.encode(), server_address)
        print('Sent message to server:', message)

    # Close the socket
    client_socket.close()

if __name__ == '__main__':
    main()
