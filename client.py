import socket

serverMACAddress = 'B8:27:EB:A1:CD:D7'
port = 3
s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
s.connect((serverMACAddress,port))
print("Connected !")
while 1:
    #text = input()
    text = "data"
    if text == "quit":
        break
    s.send(bytes(text, 'UTF-8'))
    data = s.recv(1024)
    print(data)
s.close()
