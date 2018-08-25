from TCP import Tcp_ip

class Controller:
    Client_so = Tcp_ip()
    list_str = []
    def SignUp(self):
        print("username: ",end= ' ')
        username = input()
        self.Client_so.Socket_Client(username)
        print("password: ",end= ' ')
        password = input()
        self.Client_so.Socket_Client(password)
        print("sex: ",end= ' ')
        sex = input()
        self.Client_so.Socket_Client(sex)
        print("birthday: ",end= ' ')
        birthday = input()
        self.Client_so.Socket_Client(birthday)
        print("fullname: ",end= ' ')
        fullname = input()
        self.Client_so.Socket_Client(fullname)
        print("address: ",end= ' ')
        address =input()
        self.Client_so.Socket_Client(address)
    def SignIn(self):
        print("-"*10+"Nhap Thong Tin Dang Nhap"+"-"*10)
        print("username: ", end=' ')
        username = input()
        self.Client_so.Socket_Client(username)
        print("password: ", end=' ')
        password = input()
        self.Client_so.Socket_Client(password)
        self.list_str = self.Client_so.list_ser_str

