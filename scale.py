import socket
import RPi.GPIO as GPIO
from hx711 import HX711

hx = HX711(24,23)
hx.set_reading_format("MSB","MSB")
hx.set_reference_unit(4619)
hx.reset()
hx.tare()

print("Tare done !")

hostMACAddress = 'B8:27:EB:A1:CD:D7' # The MAC address of a Bluetooth adapter on the server. The server might have multiple Bluetooth adapters.
port = 3 # 3 is an arbitrary choice. However, it must match the port used by the client.
backlog = 1
size = 1024
s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
s.bind((hostMACAddress,port))
s.listen(backlog)
try:
    client, address = s.accept()
    while 1:
        data = client.recv(size)
        if data:
            weight = hx.get_weight(5)
            client.send(bytes(str(weight), 'UTF-8'))
    
except:	
    print("Closing socket")	
    client.close()
    s.close()
