package main

import (
	"fmt"
	"net"
	"io"
)

func handleConnection(conn net.Conn) {
    defer conn.Close()

    // Create a buffer to store received data
    buf := make([]byte, 1024)
    for {
        // Read data from the connection
        n, err := conn.Read(buf)
        if err != nil {
            if err == io.EOF {
                fmt.Println("Client closed the connection")
            } else {
                fmt.Println("Error reading:", err)
            }
            return
        }
        // Print the received data
        fmt.Printf("Received from client: %s\n", buf[:n])
    }
}

func main() {
	// Listen for incoming connections
	listener, err := net.Listen("tcp", "127.0.0.1:8080")
	if err != nil {
		fmt.Println("Error listening:", err)
		return
	}
	defer listener.Close()

	fmt.Println("Server listening on 127.0.0.1:8080")

	// Accept connections in a loop
	for {
		conn, err := listener.Accept()
		if err != nil {
			fmt.Println("Error accepting connection:", err)
			return
		}
		fmt.Println("Accepted connection from", conn.RemoteAddr())
		// Handle each connection in a separate goroutine
		go handleConnection(conn)
	}
}
