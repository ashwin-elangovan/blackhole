package ch03

import (
    "io"
    "net"
    "testing"
)

func TestDial(t *testing.T) {
    // Create a listener on the IP address 127.0.0.1 with a random port.
    listener, err := net.Listen("tcp", "127.0.0.1:")
    if err != nil {
        t.Fatal(err)
    }
    done := make(chan struct{})

    // Goroutine to accept incoming connections
		// In the provided code, this goroutine is responsible for continuously accepting incoming TCP connections
		// from clients. It's created using the go keyword followed by an anonymous function func() { ... }.
		// Inside this anonymous function, the logic for accepting incoming connections is implemented.
    go func() {
        // Defer sending a signal to indicate goroutine completion
        defer func() { done <- struct{}{} }()

        // Loop to accept incoming TCP connections
        for {
            // Accept incoming connections
            conn, err := listener.Accept()
            if err != nil {
                // Log any errors but continue listening for connections
                t.Log(err)
                return
            }

            // Goroutine to handle each connection
            go func(c net.Conn) {
                // Defer closing the connection and sending a signal to indicate goroutine completion
                defer func() {
                    c.Close()
                    done <- struct{}{}
                }()

                // Buffer to read data from the connection
                buf := make([]byte, 1024)

                // Loop to read data from the connection
                for {
                    // Read data from the connection into the buffer
                    n, err := c.Read(buf)
                    if err != nil {
                        // If an error occurred while reading, log it
                        if err != io.EOF {
                            t.Error(err)
                        }
                        return
                    }
                    // Log the received data
                    t.Logf("received: %q", buf[:n])
                }
            }(conn)
        }
    }()

    // Dial the listener to establish a connection
    conn, err := net.Dial("tcp", listener.Addr().String())
    if err != nil {
        // If an error occurred while dialing, fail the test
        t.Fatal(err)
    }
    // Close the connection to initiate graceful termination
    conn.Close()

    // Wait for the goroutines to finish
    <-done
    // Close the listener
    listener.Close()
    // Wait for the listener goroutine to finish
    <-done
}
