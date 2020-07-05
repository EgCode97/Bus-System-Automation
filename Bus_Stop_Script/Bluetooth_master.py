# Get the transmited data from buses and upload it to server with the API
# 1- Scan devices
# 2- Connect to device
# 3- Make sure it's a valid device sending the verification command (A) must receive and "A" after sending
# IF VALID DEVICES GO ON... ELSE SKIP TO BREAK CONNECTION AND AND SCAN AGAIN
# 4- Request for bus ID
# 5- Break connection
# 6- Upload data via API

import serial
import serial.tools.list_ports
import time
import requests
import datetime
#---------------------------------------------------------------------------------
#   Blueeth module commands
COMMAND_SCAN = "AT+INQ\r\n" # Scan for slave blueetooth devices -> returns the scanned devices with a number and MAC address
COMMAND_CONNECT = "AT+CONN*\r\n" # 

COMMAND_GET_ID = "B"
COMMAND_DISCONNECT = chr(0)

UPLOAD_URL = 'http://localhost:8000/api'

class BusStop:
    def __init__(self):
        self.connected_devices = list()
        self.checked_bus = list()
        self.comport = self.get_comport()

    def get_comport(self):
        'Get the comport in wich the Bluetooth module is connected. Returns None if no module is connected'
        for port in [comport.device for comport in serial.tools.list_ports.comports()]:
            comport = serial.Serial(port, baudrate= 9600, timeout = 0.25)

            comport.write(b'AT\r\n')
            if not comport.read(4):
                comport.close()
            else:
                return comport

    def receive(self, bytes_num : int = 1) -> str:
        'Receive a specific amount of bytes and the return a string, if bytes num is omited then is taken as 1'
        if self.comport:
            return self.comport.read(bytes_num).decode()

    def send(self, message : str) -> None:
        if self.comport:
            self.comport.write(message.encode())

    def scan_devices(self) -> dict:
        'Scan all the slave devices in range and returns a dict with items as "scan_number":"device_mac"'
        bus_stop.send(COMMAND_SCAN)
        scan = str()
        while not scan.endswith("INQE"):
            scan += bus_stop.receive()
        
        scan_list = scan.split('\r\n')
        scan_list.pop(0)
        scan_list.pop(-1)

        scanned_dict = dict()
        for device in scan_list:
            try:
                device_number, device_mac = device.split("=")   # returns a ["+INQ:1", "MAC ADDRESS"]
                scanned_dict[device_number[-1]] = device_mac
            except:
                pass
            
        return scanned_dict

    def connect_device(self, scan_num : str):
        print(f"CONNECTING {scan_num}")
        self.send( COMMAND_CONNECT.replace('*', scan_num) )
        response = str()
        while not "+Connected\r\n" in response:
            response += self.receive()
        print(response)
        return response

    def upload_data(self, bus_id: int):
        data = {
            'token': 'gAAAAABfAkRyH9AUJUCmjDhv-HQ3TuGlkvd65_mtNAqQVo-xuvA_wqVamd0DWXyWe3joVwUiVcJeKWFcibks8Z6kxIGNXky0RNIwPaGWih6lk0sYhuAr8HDOeYMlYn21zX_t-J8T28-06GCQ-hUfVPYkAvDNAjs7Kw==',
            'id': bus_id,
            'time': datetime.datetime.now(),
            'current_location': 'La mata'
        }

        response = requests.post(UPLOAD_URL, data=data)
        




bus_stop = BusStop()
while True:
    scan = bus_stop.scan_devices()
    #scan['8'] ='0x508CB15175E9'

    print(f"SCAN -> {scan}")

    for device in scan:
        device_mac = scan[device]
 
        if device_mac in bus_stop.connected_devices:
            print(f"DEVICE '{device}' HAVE ALREDY BEEN CONNECTED")
            continue

        bus_stop.connect_device(device)

        time.sleep(5)
        print("CONECTADO")
        bus_stop.connected_devices.append(device_mac)


        bus_stop.send( "B" )
        time.sleep(0.2)
        bus_id = ord(bus_stop.receive(20).encode())

        print(f"ID -> {bus_id}")

        bus_stop.upload_data(bus_id)

        time.sleep(0.1)
        bus_stop.send( COMMAND_DISCONNECT )
        print("DESCONECTADO\n")
        time.sleep(30)
        print("REINICIANDO\n")


print(bus_stop.connected_devices)