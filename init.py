import mpc_zebra
import mpc_rfid


def main():
    # TODO: implement RFID reader implementation
    # entered_uid = mpc_rfid.read_new()
    # mpc_zebra.print_label(entered_uid)

    # sample test call. WHILE TESTING PLEASE COMMENT THIS LINE
    mpc_zebra.print_label('E0025E226FC1735W')

if __name__ == '__main__':
    main()
