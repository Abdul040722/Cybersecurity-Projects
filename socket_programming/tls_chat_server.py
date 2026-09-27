import socket
import ssl
import threading

HOST = '127.0.0.1'
PORT = 8443

# Dictionary to map connected usernames to their active TLS sockets
clients = {}
clients_lock = threading.Lock()

def handle_client(client_socket, client_address):
    username = None
    try:
        # Prompt client to set a username
        client_socket.sendall(b"ENTER_USERNAME")
        username = client_socket.recv(1024).decode('utf-8').strip()

        with clients_lock:
            if username in clients or not username:
                client_socket.sendall(b"ERROR Username taken or invalid. Disconnecting.\n")
                client_socket.close()
                return
            clients[username] = client_socket

        print(f"[+] User '{username}' connected from {client_address}")
        client_socket.sendall(b"SUCCESS Connected to TLS Direct Messaging Server.\n")

        while True:
            data = client_socket.recv(4096)
            if not data:
                break

            message = data.decode('utf-8').strip()

            # Expecting format "target_user: text message"
            if ":" not in message:
                client_socket.sendall(b"SYSTEM Format error. Use 'recipient_username: message'\n")
                continue

            target_user, text = message.split(":", 1)
            target_user = target_user.strip()
            text = text.strip()

            # Direct Routing
            with clients_lock:
                target_socket = clients.get(target_user)

            if target_socket:
                formatted_msg = f"[{username} -> You]: {text}\n"
                try:
                    target_socket.sendall(formatted_msg.encode('utf-8'))
                except Exception:
                    client_socket.sendall(f"SYSTEM Failed to send message to {target_user}.\n".encode('utf-8'))
            else:
                client_socket.sendall(f"SYSTEM User '{target_user}' not found or offline.\n".encode('utf-8'))

    except (ssl.SSLError, ConnectionResetError, OSError) as e:
        print(f"[-] Connection error with {client_address}: {e}")
    finally:
        if username:
            with clients_lock:
                if username in clients:
                    del clients[username]
            print(f"[-] User '{username}' disconnected.")
        client_socket.close()

def start_server():
    # Set up TLS Context
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile="server.crt", keyfile="server.key")

    raw_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    raw_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    raw_socket.bind((HOST, PORT))
    raw_socket.listen(5)

    print(f"[*] TLS Direct Chat Server listening on {HOST}:{PORT}...")

    try:
        while True:
            newsocket, fromaddr = raw_socket.accept()
            # Wrap standard socket in TLS layer
            connstream = context.wrap_socket(newsocket, server_side=True)
            thread = threading.Thread(target=handle_client, args=(connstream, fromaddr), daemon=True)
            thread.start()
    except KeyboardInterrupt:
        print("\n[*] Server shutting down.")
    finally:
        raw_socket.close()

if __name__ == "__main__":
    start_server()
