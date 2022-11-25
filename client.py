import bluetooth

serverMACAddress = 'B8:27:EB:A1:CD:D7'
port = 3
s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
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
