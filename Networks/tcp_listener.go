package ch03

import (
    "net"
    "testing"
)

// net.Listen("tcp", "127.0.0.1:0"): This line attempts to create a TCP listener on the loopback address (127.0.0.1) and a randomly chosen port (:0). The use of :0 means the OS will select an available port for listening. This is useful for testing because it avoids port conflicts.

// defer func() { _ = listener.Close() }(): This defers the closing of the listener until the surrounding function (TestListener) returns. The underscore (_) before listener.Close() is used to discard the error returned by listener.Close() since we're only interested in closing the listener and not handling any errors at this point.

// t.Logf("bound to %q", listener.Addr()): This line logs the address the listener is bound to. It's using t.Logf to log a formatted message with the listener's address (listener.Addr()).

func TestListener(t *testing.T) {
    // 1. Attempt to create a network listener using TCP protocol on address 127.0.0.1:0
    listener, err := net.Listen("tcp", "127.0.0.1:0")
    if err != nil {
        t.Fatal(err)
    }
    // 2. Defer the closing of the listener to ensure it's closed after the test function finishes
    defer func() { _ = listener.Close() }()
    // 3. Log the address the listener is bound to
    t.Logf("bound to %q", listener.Addr())
}
