from TCP import Tcp_ip
from Controller import Controller
class View:
    Client_so = Tcp_ip()
    Client_co = Controller()
    def Show_Mess(self):
        print("-------SHOW_MESS------\n"
        "1.SEND MESS\n"
        "2.RECEIVED MESSAGE\n"
        "3.EXIT\n"
        "-----------------------\n")
    def Send_mess(self):
        print("-------MENU------\n"
                "SEND MESS: ")
    def Menu_user(self):
        print( "-"*10+"MENU_USER"+"-"*10)
        print("1.Show Mess")
        print("2.Send Mess")
        print("3.Add Friend")
        print("4.Show Friend")
        print("5.Block Friend")
        print("6.Exit")
        print("-"*29)
    def print_Menu(self):

        choice = ''
        print("-"*10+ "MESSENGER APP"+"-"*10)
        print("1. SIGN UP")
        print("2. SIGN IN")
        print("3. LOG OUT")
        print("4. EXIT")
        print("Chon chuc nang 1-4 :")
        choice = input()
        if(choice in ['1','2','3','4']):
            self.Client_so.Socket_Client(choice)
            if(choice == '1'):
                self.Client_co.SignUp()
                self.print_Menu()
            if(choice == '2'):
                choice_user = ''
                self.Client_co.SignIn()
                print(self.Client_co.list_str)
                if("Dang Nhap Thanh Cong" in self.Client_co.list_str):
                    self.Menu_user()
                    print("Choose: ")
                    choice_user = input()
                    if(choice_user in ['1','2','3','4','5']):
                        self.Client_so.Socket_Client(choice_user)
                        if(choice_user == '1'):
                            self.Show_Mess()
                            choice_user_mess = input()
                            self.Client_so.Socket_Client(choice_user_mess)
                        if(choice_user == '2'):
                            self.Send_mess()
                            mess_send = input()
                            self.Client_so.Socket_Client(mess_send)
                            print("Send to (friend_user): ")
                            friend_user = input()
                            self.Client_so.Socket_Client(friend_user)
                    elif(choice_user == '6'):
                        print("OK_BYE")
                    else:
                        self.print_Menu()
        else:
            print("Dang Nhap That Bai")
            self.print_Menu()