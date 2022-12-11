import bluetooth
import RPi.GPIO as GPIO
from hx711 import HX711
import struct

hx = HX711(24,23)
hx.set_reading_format("MSB","MSB")
hx.set_reference_unit(4619)
hx.reset()
hx.tare()
    
hostMACAddress = 'B8:27:EB:A1:CD:D7'
port = 3 
backlog = 1
size = 1024

uuid = "47b02853-3bcf-4f1c-b682-ccb98cf85f79"

s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
while True: 
    s.bind((hostMACAddress,port))
    s.listen(backlog)
    bluetooth.advertise_service(s, "Scale",
        service_id=uuid,
        service_classes=[uuid, bluetooth.SERIAL_PORT_CLASS],
        profiles=[bluetooth.SERIAL_PORT_PROFILE]
        )
    
    while True:
        client, address = s.accept()
        print("Connection from", address)
        try:
            while True:
                data = client.recv(size)
                if data:
                    command = data.decode('UTF-8')
                    if command == 'data':
                        weight = hx.get_weight(5)
                        client.send(bytes(str(weight), 'UTF-8'))    
                    elif command == 'tare':
                        hx.tare()    
                    else:
                        print("Received unknown command")         
        except (IOError) as e:
            print("Error:", e)
            client.close()
        else:
            client.close()
