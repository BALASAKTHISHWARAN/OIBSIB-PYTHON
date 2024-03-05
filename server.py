import socket
import threading

# Function to handle client connections
def handle_client(client_socket, client_address, clients):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message:
                print(f"Connection with {client_address} closed.")
                clients.remove(client_socket)
                client_socket.close()
                break
            print(f"Received from {client_address}: {message}")
            broadcast(message, client_socket, clients)
        except:
            print(f"Error handling connection with {client_address}")
            break

# Function to broadcast message to all clients except sender
def broadcast(message, sender_socket, clients):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message.encode())
            except:
                print("Error broadcasting message")

# Main function
def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 5555))
    server_socket.listen(5)
    print("Server is listening...")

    clients = []

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address} established.")
        clients.append(client_socket)
        client_handler = threading.Thread(target=handle_client, args=(client_socket, client_address, clients))
        client_handler.start()

if __name__ == "__main__":
    main()
