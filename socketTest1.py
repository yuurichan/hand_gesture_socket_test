import socket
import time

host = "127.0.0.1"
PORT = 25001

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.connect((host, PORT))

#Vector3, pos 0 0 0
startPos = [0, 0, 0]
while True:
    time.sleep(1.0)
    startPos[0] += 1 #increase x value by one
    # Converting V3 (array 3 elements) into a string ("0,0,0")
    posString = ','.join(map(str, startPos))
    print("Current Pos: ", posString)

    sock.sendall(posString.encode("UTF-8"))  # Converting string to Byte, and sending it to C#
    receivedData = sock.recv(1024).decode("UTF-8")  # Receiving data in Byte from C#, and converting it to String
    print(receivedData)
