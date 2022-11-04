#!/usr/bin/env python3

import socket

# Gets the hostname of the source
src_hostname = socket.gethostbyname()

# Set the source and destination IP address
src_ip_addr = socket.gethostbyname(src_hostname)
dest_ip_addr = socket.gethostbyname('') # TODO: INSERT HOST

# The IP HEADER 
def ip_header():
    pass

# The TCP HEADER
def tcp_header():
    pass

def main():
    # Create raw socket connection
    project3_sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)



if __name__ == "__main__":
    main()