import socket

HEADER = 64
PORT = 5052
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "192.168.1.105"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

def calculate():
    print("Calculating the Area and Perimeter of Rectangle")
    length = input("Enter your Length: ") 
    breadth = input("Enter your Breadth: ")
    action = input("What do you want to perform: 1.Area 2.Perimeter => ")

    msg = action + ',' + length + ',' + breadth
    print("Contacting Server")
    send(msg)

calculate()
send(DISCONNECT_MESSAGE)