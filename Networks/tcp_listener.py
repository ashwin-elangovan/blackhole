import socket
import unittest

# TCP socket provides bidirectional connections
class TestListener(unittest.TestCase):
    def test_listener(self):
        # Attempt to create a TCP listener on localhost and a randomly chosen port
        # We create a TCP socket using socket.socket(socket.AF_INET, socket.SOCK_STREAM). AF_INET indicates IPv4, and SOCK_STREAM indicates a TCP socket.
        listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # We bind the socket to the loopback address 127.0.0.1 and port 0. The use of port 0 allows the operating system to choose an available port.
        listener.bind(('127.0.0.1', 0))
        listener.listen(1)  # Listen for incoming connections, allowing a maximum of 1 connection
        addr = listener.getsockname()  # Get the address the listener is bound to
        # Log the address the listener is bound to
        print(f"Bound to {addr}")

        # Close the listener
        listener.close()

if __name__ == "__main__":
    unittest.main()
