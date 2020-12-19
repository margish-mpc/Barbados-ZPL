import sys
import mpc_zebra

def main():
    print('Zebra Printer IP Addr for 4"x1": %s' % (sys.argv[1]))
    print('Zebra Printer IP Addr for 2"x1": %s' % (sys.argv[2]))
    print('nRF device ID: %s' % (sys.argv[3]))
    print('MPC serial number: %s' % (sys.argv[4]))
    ip_4x1 = sys.argv[1]
    ip_2x1 = sys.argv[2]
    nRF_id = sys.argv[3]
    mpc_sn = sys.argv[4]
    mpc_zebra.print_label_4x1(ip_4x1, nRF_id)
    mpc_zebra.print_label_2x1(ip_2x1, nRF_id)

if __name__ == '__main__':
    main()
