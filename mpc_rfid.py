import serial
import time
import datetime
import serial.tools.list_ports

# ASCII commands to access NFC RFID scanner
SUCCESS_BEEP = '010900030419F00000'
FAILURE_BEEP = '010900030420F00000'
UID_READ_REQ = '010C00030410002101020000'
AGC_TOGGLE = '0109000304F0000000'
AMPM_TOGGLE = '0109000304F1FF0000'
DISPLAY_UID = '010B000304140601000000'

# Error Messages
Message1 = 'Error 1: UID not Found'
Message2 = 'Error 2: Please tap badge near reader'
Message3 = 'Error 3: Badge Not Found'

# To get a list of ports
comlist = serial.tools.list_ports.comports()
connected = []
for element in comlist:
    connected.append(element.device)
    # print("Connected COM ports: ", connected)


# Function to Initialize the Serial Port
def init_serial():
    global ser
    ser = serial.Serial()
    ser.baudrate = 115200
    for i in connected:
        ser.port = i                    # COM Port Name
    ser.timeout = 0.05                  # Specify the TimeOut in seconds,
    # Wait till set timeout sec then return all bytes that were received
    # Here UID data response received  in 0.05 sec.
    ser.open()                          # Opens SerialPort
    if ser.isOpen():                    # print port open or closed
        print('Open COM Port is :', ser.portstr)
    else:
        print("Port must be configured before it can be used.")


def read_uid():
    global ser
    global UID
    UID_read = [UID_READ_REQ, AGC_TOGGLE, AMPM_TOGGLE, DISPLAY_UID]  # UID read commands
    for command in UID_read:
        time.sleep(0.11)  # minimum delay
        ser.write(command.encode('ascii'))  # transfer data (write commnads to nfc)
        UID = ser.read(5000)                # reads response(UID of badge) from badge
    data_received = UID.decode('ascii')     # store data received
    length = len(data_received)             # length of data received
    a = list()                              # to separate UID from received data
    b = ""                                  # to make string for UID
    k = 8                                   # 8 byte
    for i in range(0, length):
        if data_received[i] == '[' and data_received[i + 1] != ',':
            for j in range(i + 1, i + 17):
                a.append(data_received[j])
    try:                                    # to except
        while k >= 1:                       # is to reverse and arrange uid into it's actual format
            k = k - 1
            b += a[2 * k]
            b += a[2 * k + 1]
        if len(b) != 16 and len(b) >= 16:   # it is to remove dummy data or the data other then uid
            ser.write(FAILURE_BEEP.encode('ascii'))
            time.sleep(0.05)
            return Message1                 # Please tap badge near reader
        elif b[0] == '[' and b[1] == ',':
            ser.write(FAILURE_BEEP.encode('ascii'))
            time.sleep(0.05)
            return Message1                 # Please tap badge near reader
        else:
            ser.write(SUCCESS_BEEP.encode('ascii'))
            return b                        # returns found UID
    except:
        ser.write(FAILURE_BEEP.encode('ascii'))
        time.sleep(0.05)
        return Message2                     # Please tap badge near reader


#code to scan until a new NFC tag is detected, then return ID
def read_new():
    new_uid = ''
    try:
        init_serial()                                       # serial port init
        ser.write(SUCCESS_BEEP.encode('ascii'))
        global UID
        CurrentDT = datetime.datetime.now()                 # To show current date and time
        # print("-----Date and Time: ", CurrentDT)
        time.sleep(1)
        print('Reading NFC ID...')
        time.sleep(1)        # Delay for error
        c = 1                # continuously detect Badgs
        while c == 1:
            Response = read_uid()       # Reads badge UID
            if len(Response) == 16:
                c = 0
                ser.write(SUCCESS_BEEP.encode('ascii'))
                # print('NFC UID: ', Response)
                new_uid = Response
                # print('NFC UID: ', new_uid)
                ser.write(SUCCESS_BEEP.encode('ascii'))
                time.sleep(0.5)
            else:
                print(Response)  # incase of error
                ser.write(FAILURE_BEEP.encode('ascii'))
                time.sleep(0.5)
                c = 1
    except serial.SerialException:
        print('Error: Attempting to use a port that is not open or aready in use')

    return new_uid
