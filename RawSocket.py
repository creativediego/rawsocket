import socket
class RawSocket:
    def __init__(self):
        self.raw = None
    def connect(self):
        try:
            self.raw = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
            # headers will be provided manually
            # self.s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
        except socket.error as message:
            print ('Error creating socket. Code: ' + str(message[0]) + ' Message ' + message[1])
            exit()