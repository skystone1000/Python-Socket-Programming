import socket 
import threading

HEADER = 64
PORT = 5052
SERVER = "192.168.1.105"
#SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
                break

            output = rectangle(msg)
            print("Sending Output: {}".format(output))
            # print(f"[{addr}] {msg}")
            conn.send(output.encode(FORMAT))

    conn.close()
        

def rectangle(msg):
    values = msg.split(",")
    action = int(values[0])
    length = int(values[1])
    breadth = int(values[2])
    
    if(action == 1):
        area = str(length*breadth)
        return "Area = " + area
    elif(action == 2):
        perimeter = str(2*(length+breadth))
        return "Perimeter = " + perimeter
    else:
        return "Not Valid Input"
    


def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


print("[STARTING] server is starting...")
start()