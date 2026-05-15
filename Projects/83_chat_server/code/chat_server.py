import socket, threading

HOST = ""
PORT = 9999
clients = []
nicknames = []

def broadcast(message, sender=None):
    for client in clients[:]:
        if client != sender:
            try:
                client.send(message)
            except Exception:
                idx = clients.index(client)
                clients.remove(client)
                nicknames.pop(idx)

def handle_client(client, addr):
    try:
        client.send("NICK".encode())
        nick = client.recv(1024).decode().strip()
        nicknames.append(nick)
        clients.append(client)
        print(f"{nick} joined from {addr}")
        broadcast(f"[{nick} joined the chat!]".encode())
        while True:
            msg = client.recv(1024)
            if not msg: break
            broadcast(f"{nick}: {msg.decode()}".encode(), client)
            print(f"{nick}: {msg.decode().strip()}")
    except Exception:
        pass
    finally:
        if client in clients:
            idx = clients.index(client)
            nicknames.pop(idx)
            clients.remove(client)
        broadcast(f"[Someone left the chat]".encode())
        client.close()

print("Chat Server")
print("===========")
print(f"Starting server on port {PORT}")
print("Connect with: python3 chat_client.py <server_ip>")
print("Press Ctrl+C to stop")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen(10)

try:
    while True:
        client, addr = server.accept()
        t = threading.Thread(target=handle_client, args=(client, addr), daemon=True)
        t.start()
except KeyboardInterrupt:
    print("\nServer stopped.")
    server.close()
