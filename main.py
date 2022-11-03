from IPPacket import IPPacket
from RawSocket import RawSocket
import socket


def main():
    source = '10.211.55.3'
    dest = '204.44.192.60'
    s = RawSocket()
    s.connect()

    ip = IPPacket(source,dest)
    ip.pack_headers()
    s.raw.sendto(ip.headers, (dest , 0))

main()