#!/usr/bin/env python3

import socket
import struct
import binascii

# Gets the hostname of the source
src_hostname = socket.gethostname()

# Set the source and destination IP address
src_ip_addr = socket.gethostbyname(src_hostname)
dest_ip_addr = socket.gethostbyname('david.choffnes.com') # TODO: INSERT HOST FROM COMMAND LINE

fmt_string = "!BBHHHBBH4s4s"

# The IP HEADER 
def ip_header(src, dest):
    ver = 4
    vhl = 5
    ver = (ver << 4) + vhl
    tos = 0
    total_len = 0

    ident = 54321
    flags = 0

    ttl = 225
    proto = socket.IPPROTO_TCP
    hdr_chk_sum = 0

    src_addr = binascii.hexlify(socket.inet_aton(src)).upper()
    dest_addr = binascii.hexlify(socket.inet_aton(dest)).upper()

    ip_header = struct.pack(fmt_string,
                            ver,
                            tos,
                            total_len,
                            ident,
                            flags,
                            ttl,
                            proto,
                            hdr_chk_sum,
                            src_addr,
                            dest_addr)

    return ip_header



# The TCP HEADER
def tcp_header():
    pass

def main():
    # Create raw socket connection
    project3_sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
    print(ip_header(src_ip_addr, dest_ip_addr))



if __name__ == "__main__":
    main()