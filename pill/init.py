import sys
#import mpc_zebra
#import mpc_rfid
#import mpc_logger

def main():
    entered_uid = ''
    last_printed_uid = ''
    while True:
        entered_uid = mpc_rfid.read_new()
        if len(entered_uid) > 0 and entered_uid != last_printed_uid:
            mpc_zebra.print_label(entered_uid)
            mpc_logger.log_uid(entered_uid)
            last_printed_uid = entered_uid

if __name__ == '__main__':
    # main()
    print(f"Arguments count: {len(sys.argv)}")
    for i, arg in enumerate(sys.argv):
        print(f"Argument {i:>6}: {arg}")
