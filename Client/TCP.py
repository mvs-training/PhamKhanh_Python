import socket

class Tcp_ip:
    list_ser_str =[]
    def Socket_Client(self, buff):
        soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        soc.connect(("127.0.0.1", 12345))
        soc.send(buff.encode("utf8"))  # we must encode the string to bytes
        result_bytes = soc.recv(4096)  # the number means how the response can be in bytes
        result_string = result_bytes.decode("utf8")  # the return will be in bytes, so decode
        print("Result from server is {}".format(result_string))
        if(result_string =='Dang Nhap Thanh Cong'):
            self.list_ser_str.append(result_string)
