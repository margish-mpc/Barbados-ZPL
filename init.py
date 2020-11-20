import mpc_zebra
import mpc_rfid


def main():
    entered_uid = ''
    last_printed_uid = ''
    while True:
        entered_uid = mpc_rfid.read_new()
        if len(entered_uid) > 0 and entered_uid != last_printed_uid:
            mpc_zebra.print_label(entered_uid)
            last_printed_uid = entered_uid

if __name__ == '__main__':
    main()
