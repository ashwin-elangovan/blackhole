package main // Declares that this file is part of the main package

import (
	"fmt"  // Imports the fmt package, which provides functions for formatting and printing
	"net"  // Imports the net package, which provides support for networking operations
)

func main() { // Defines the entry point of the program
	// Connect to the server
	conn, err := net.Dial("tcp", "127.0.0.1:8080") // Initiates a TCP connection to the specified address
	if err != nil { // Checks if there was an error during connection
		fmt.Println("Error connecting:", err) // Prints the error message
		return // Exits the program if there was an error
	}
	defer conn.Close() // Defers closing the connection until the function returns

	fmt.Println("Connected to server at 127.0.0.1:8080") // Prints a message indicating successful connection

	// Send data to the server
	message := "Hello from client!"                              // Defines the message to send
	_, err = conn.Write([]byte(message))                         // Writes the message to the connection
	if err != nil {                                              // Checks if there was an error while sending
		fmt.Println("Error sending:", err)                       // Prints the error message
		return                                                   // Exits the program if there was an error
	}
	fmt.Println("Sent to server:", message)                      // Prints a message indicating successful sending
}
