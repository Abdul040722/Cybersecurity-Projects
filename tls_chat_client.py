import socket
import ssl
import threading
import sys

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 8443

def receive_messages(tls_socket):
    """Continuously listens for incoming messages from the server."""
    while True:
        try:
            data = tls_socket.recv(4096)
            if not data:
                print("\n[!] Connection to server closed.")
                break
            print(f"\r{data.decode('utf-8')}\n> ", end="")
        except Exception:
            break

def start_client():
    # Set up TLS Context (Disabling verification for local self-signed certs)
    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE

    raw_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        tls_socket = context.wrap_socket(raw_socket, server_hostname=SERVER_HOST)
        tls_socket.connect((SERVER_HOST, SERVER_PORT))
    except Exception as e:
        print(f"Failed to connect to server: {e}")
        return

    # Handle registration
    prompt = tls_socket.recv(1024).decode('utf-8')
    if prompt == "ENTER_USERNAME":
        username = input("Enter your username: ").strip()
        tls_socket.sendall(username.encode('utf-8'))

        response = tls_socket.recv(1024).decode('utf-8')
        print(response)
        if "ERROR" in response:
            tls_socket.close()
            return

    # Start incoming message listener thread
    recv_thread = threading.Thread(target=receive_messages, args=(tls_socket,), daemon=True)
    recv_thread.start()

    print("--- Instructions ---")
    print("Send direct messages using the format: recipient_username: message")
    print("Type 'exit' or 'quit' to close.\n")

    try:
        while True:
            user_input = input("> ").strip()
            if user_input.lower() in ('exit', 'quit'):
                break
            if user_input:
                tls_socket.sendall(user_input.encode('utf-8'))
    except KeyboardInterrupt:
        pass
    finally:
        tls_socket.close()
        print("Disconnected.")

if __name__ == "__main__":
    start_client()
