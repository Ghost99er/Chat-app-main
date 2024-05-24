import socket
import threading
from tkinter import *

# List to store all connected clients
clients = []

def handle_client(client_socket, text_widget):
    while True:
        try:
            message = client_socket.recv(1024).decode("utf-8")
            if not message:
                break
            broadcast(message, client_socket)
            text_widget.insert(END, f"{message}\n")
        except ConnectionResetError:
            break
    clients.remove(client_socket)
    client_socket.close()

def broadcast(message, client_socket):
    for client in clients:
        if client != client_socket:
            try:
                client.send(message.encode("utf-8"))
            except:
                clients.remove(client)
                client.close()

def start_server(text_widget, server_ip_entry, server_port_entry):
    server_ip = server_ip_entry.get()
    server_port = int(server_port_entry.get())
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((server_ip, server_port))
    server.listen(5)
    text_widget.insert(END, f"Server started on {server_ip}:{server_port}, waiting for connections...\n")

    while True:
        client_socket, addr = server.accept()
        clients.append(client_socket)
        text_widget.insert(END, f"Accepted connection from {addr}\n")
        client_handler = threading.Thread(target=handle_client, args=(client_socket, text_widget))
        client_handler.start()

def send_message(peer_socket, message_entry, text_widget, username):
    message = f"{username}: {message_entry.get()}"
    peer_socket.send(message.encode("utf-8"))
    text_widget.insert(END, f"{message}\n")
    message_entry.delete(0, END)

def connect_to_server(text_widget, server_ip_entry, server_port_entry, message_entry, username):
    server_ip = server_ip_entry.get()
    server_port = int(server_port_entry.get())
    peer_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    peer_socket.connect((server_ip, server_port))
    
    threading.Thread(target=receive_messages, args=(peer_socket, text_widget)).start()

    send_button = Button(root, text="Send", command=lambda: send_message(peer_socket, message_entry, text_widget, username))
    send_button.pack()

def receive_messages(peer_socket, text_widget):
    while True:
        try:
            message = peer_socket.recv(1024).decode("utf-8")
            if not message:
                break
            text_widget.insert(END, f"{message}\n")
        except ConnectionResetError:
            break
    peer_socket.close()

def show_instructions():
    instructions = Toplevel(root)
    instructions.title("Instructions")
    text_widget = Text(instructions, wrap="word", width=50, height=20)
    text_widget.pack()

    instructions_text = """
    Instructions for Running the Peer-to-Peer Chat Application

    Running the Server (Host):
    1. Ensure you have your public IP address.
       - Visit a site like https://www.whatismyip.com/ to find your public IP.
    2. Set up port forwarding on your router:
       - Log into your router's admin panel.
       - Forward the chosen port (e.g., 9999) to your local IP address.
    3. Start the application on the server machine.
    4. Enter the public IP address and port number.
    5. Click "Start Server".

    Running the Client (User):
    1. Start the application on the client machine.
    2. Enter a unique username.
    3. Enter the server's public IP address and port number.
    4. Click "Connect to Server".
    5. Type messages and click "Send" to communicate.
    """

    text_widget.insert(END, instructions_text)
    text_widget.config(state=DISABLED)

def main():
    global root
    root = Tk()
    root.title("Peer-to-Peer Chat")

    text_widget = Text(root)
    text_widget.pack()

    username_entry = Entry(root)
    username_entry.insert(0, "Enter Username")
    username_entry.pack()

    server_ip_entry = Entry(root)
    server_ip_entry.insert(0, "Enter Server IP")
    server_ip_entry.pack()

    server_port_entry = Entry(root)
    server_port_entry.insert(0, "Enter Server Port")
    server_port_entry.pack()

    message_entry = Entry(root)
    message_entry.pack()

    start_button = Button(root, text="Start Server", command=lambda: threading.Thread(target=start_server, args=(text_widget, server_ip_entry, server_port_entry)).start())
    start_button.pack()

    connect_button = Button(root, text="Connect to Server", command=lambda: connect_to_server(text_widget, server_ip_entry, server_port_entry, message_entry, username_entry.get()))
    connect_button.pack()

    instructions_button = Button(root, text="Show Instructions", command=show_instructions)
    instructions_button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
