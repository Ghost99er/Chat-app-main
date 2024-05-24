# Peer-to-Peer Chat Application

This is a simple Peer-to-Peer Chat Application implemented in Python using the `socket` library and Tkinter for the graphical user interface.

## Features

- Allows multiple clients to connect to a central server.
- Clients can send and receive messages in real-time.
- Supports both local and networked communication.

## Prerequisites

- Python 3.x
- Tkinter (usually included with Python installations)

## Running the Application

- Download the Chat-App file

### Running the Server (Host)

1. Enter the server details:
   - **Server IP**: The IP address of the server machine.
     - To find your IP address:
       - Press `Win + R`, type `cmd`, and press Enter.
       - Type `ipconfig` and press Enter.
       - Look for the "IPv4 Address" under the network connection you are using (e.g., Wi-Fi or Ethernet).
   - **Server Port**: A port number (e.g., 9999).
2. Enter username
3. Enter IP address 
4. enter port number (Use 9999 for defult)
5. Click the "Start Server" button. The server will start and wait for connections.


### Running the Client (User)

1. Start the application on the client machine.
2. Enter a unique username.
3. Enter the server's public IP address and port number.
4. Click "Connect to Server".
5. Type messages and click "Send" to communicate.

## Contributors

- Ghost99er

## License

This project is licensed under the [MIT License](LICENSE.md).
