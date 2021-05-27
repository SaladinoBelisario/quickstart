import socket
import struct
import sys
from time import sleep

if __name__ == '__main__':

    host = '127.0.0.1'
    port = 10015

    tm_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Dummy packet
    header = 82
    hour = 2
    minute = 3
    second = 4
    robot_id = 5
    cluster_size = 6
    nav_cycles = 7
    i_sys = 8
    i_mot = 9
    v_uc = 10
    tmp_uc = 11
    tmp_top = 12
    tmp_bottom = 13
    mx = 14
    my = 15
    mz = 16
    tbd = [b'\xAA'] * 20
    end = 76
    crch = 19
    crcl = 20
    packet = struct.pack('>B3B2B3H2B2H3H20c3B',
                         header,
                         hour, minute, second,
                         robot_id,
                         cluster_size, nav_cycles,
                         i_sys, i_mot, v_uc,
                         tmp_uc, tmp_top, tmp_bottom,
                         mx, my, mz,
                         *tbd,
                         end,
                         crch,
                         crcl
                         )

    while True:

        tm_socket.sendto(packet, (host, port))
        print(packet)

        sleep(1)
