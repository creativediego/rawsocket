
import binascii
import socket
ip = binascii.hexlify(socket.inet_aton('10.10.10.2'))
import struct
from random import randint

class IPPacket:
    def __init__(self, source_ip: str, dest_ip: str):
        self.source_ip: bytes = socket.inet_aton(source_ip)
        self.dest_ip: bytes = socket.inet_aton(dest_ip)
        self.headers: bytes = b''
    
    def pack_headers(self):
        version = 4
        ihl = 5
        version_ihl = (version << 4 ) + ihl
        type_of_service = 0
        total_length = 0
        indentification = randint(0, 0xFFFF) # random 16-bit id number
        flag_offset = 0
        time_to_live = 255 #default linux
        protocol = socket.IPPROTO_TCP
        checksum = 0 # will be calculated automatically
        
        # Build the header
        self.headers = struct.pack('!BBHHHBBH4s4s', version_ihl, type_of_service, \
            total_length, indentification, flag_offset, time_to_live, protocol, checksum, \
                self.source_ip, self.dest_ip)
        print(self.headers)
        return self.headers








