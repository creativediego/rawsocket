import dataclasses from dataclass
import struct

@dataclass
class IP():
    def __init__(self, dest="", src=""):
        self.dest = dest
        self.src = src
        self.raw = None
        self.ip_creation()


    def ip_creation():
        ip_ver=4
        ip_vhl=5

        self.ip_ver = (ip_ver << 4) + ip_vhl

        ip_dsc=0
        ip_ecn=0

        self.ip_dfc = (ip_dsc << 2) + ip_ecn

        self.ip_length = 0
        self.ip_id = 54321

        ip_rsv=0
        ip_dtf=0
        ip_mrf=0
        ip_flag_offset=0

        self.ip_flg = (ip_rsv << 7) + (ip_dtf << 6) + (ip_mrf << 5) + (ip_frag_offset)

        self.ip_ttl = 225
        self.ip_proto = socket.IPPROTO_TCP

        self.ip_chk_sum = 0

        self.ip_src_addr = socket.inet_aton(self.src)
        self.ip_dest_addr = socket.inet_aton(self.dest)

        return

    def create_ip(self):
        self.raw = struct.pack('!BBHHHBBH4s4s',self.ip_ver, self.ip_dfc, self.ip_length, self.ip_id,self.ip_flg,self.ip_ttl, self.ip_proto, self.ip_chk_sum, self.ip_src_addr, self.ip_dest_addr)
        return raw





    

