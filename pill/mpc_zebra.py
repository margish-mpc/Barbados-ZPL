import socket

PRINTER_PORT = 9100

UID_DEFAULT_LONG = "ABCDEFGHIJKLMNOP"
UID_SHORT_LEN = 6
UID_DEFAULT_SHORT = UID_DEFAULT_LONG[-UID_SHORT_LEN:]

def print_label_4x1(ip, uid_in):
    label_file = open("label_4x1.zpl")
    zpl_print_str = label_file.read()
    label_file.close()

    zpl_print_str = zpl_print_str.replace(UID_DEFAULT_LONG, uid_in)
    zpl_print_str = zpl_print_str.replace(UID_DEFAULT_SHORT, uid_in[-UID_SHORT_LEN:])
    print(zpl_print_str)
    return
    new_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    new_socket.connect((ip, PRINTER_PORT))
    new_socket.send(zpl_print_str.encode())
    new_socket.close()

def print_label_2x1(ip, uid_in):
    label_file = open("label_2x1.zpl")
    zpl_print_str = label_file.read()
    label_file.close()

    zpl_print_str = zpl_print_str.replace(UID_DEFAULT_LONG, uid_in)
    zpl_print_str = zpl_print_str.replace(UID_DEFAULT_SHORT, uid_in[-UID_SHORT_LEN:])
    print(zpl_print_str)
    return
    new_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    new_socket.connect((ip, PRINTER_PORT))
    new_socket.send(zpl_print_str.encode())
    new_socket.close()
