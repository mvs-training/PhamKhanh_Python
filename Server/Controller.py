import sqlite3
from Model import Model
class Controller:
    Server_mo = Model()
    check = 0
    list_ser_con = []
    def SignUp(self, username, password, sex, birthday, fullname, address):
        self.check = self.Server_mo.Select_All(username)
        if(self.check != 0) :
            print("Da Ton Tai Tai Khoan")
        else:
            self.Server_mo.SQL_Reg(username, password, sex, birthday, fullname, address)
            id_mask = self.Server_mo.Select_Mask()
            self.Server_mo.Insert_Mask(id_mask, fullname, sex, address)
            print("SAVED.OK")
    def SignIn(self, username, password):
        self.check = self.Server_mo.Check_Login(username, password)
        if(self.check != 0):
            print("Dang Nhap Thanh Cong")
        else:
            print("Dang Nhap That Bai")
    def Show_Mess_send(self):
        self.list_ser_con.append(self.Server_mo.SQL_Show_Mess_send(self.check))

    def Show_Mess_recv(self):
        self.list_ser_con.append(self.Server_mo.SQL_Show_Mess_recv(self.check))

