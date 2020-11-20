import socket

PRINTER_HOST_IP = "10.0.0.148"
PRINTER_PORT = 9100

UID_DEFAULT_LONG = "ABCDEFGHIJKLMNOP"
UID_SHORT_LEN = 5
UID_DEFAULT_SHORT = UID_DEFAULT_LONG[-UID_SHORT_LEN:]

def print_label(uid_in):
    label_file = open("label_with_logo.zpl")
    zpl_print_str = label_file.read()
    label_file.close()

    zpl_print_str = zpl_print_str.replace(UID_DEFAULT_LONG, uid_in)
    zpl_print_str = zpl_print_str.replace(UID_DEFAULT_SHORT, uid_in[-UID_SHORT_LEN:])
    print(zpl_print_str)

    new_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    new_socket.connect((PRINTER_HOST_IP, PRINTER_PORT))
    new_socket.send(zpl_print_str.encode())
    new_socket.close()
