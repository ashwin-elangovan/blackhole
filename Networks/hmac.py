import hmac
import hashlib

# Define the secret key (should be securely generated and distributed)
secret_key = b'my_secret_key'

def generate_mac(message, key=secret_key):
    """
    Generate the MAC value for a given message using HMAC-SHA256.
    """
    mac = hmac.new(key, message, hashlib.sha256)
    return mac.hexdigest()

def verify_mac(message, mac_value, key=secret_key):
    """
    Verify the MAC value for a given message.
    Returns True if the MAC value is valid, False otherwise.
    """
    expected_mac = generate_mac(message, key)
    return hmac.compare_digest(expected_mac, mac_value)

# Example usage
message = b'Hello, World!'

# Generate the MAC value
mac_value = generate_mac(message)
print(f"MAC value: {mac_value}")

# Verify the MAC value
if verify_mac(message, mac_value):
    print("MAC verification successful. Message is authentic.")
else:
    print("MAC verification failed. Message is not authentic.")

# Simulate tampering with the message
tampered_message = b'Hello, World?'

# Verify the MAC value for the tampered message
if verify_mac(tampered_message, mac_value):
    print("MAC verification successful. Message is authentic.")
else:
    print("MAC verification failed. Message is not authentic.")
