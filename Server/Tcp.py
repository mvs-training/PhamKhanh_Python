from Controller import Controller
from Model import Model


class Tcp_Ip:
    list_client = []
    Server_con = Controller()
    check_login = 0
    check_id = 0
    list_server =[]
    Server_mo = Model()
    def do_some_stuffs_with_input(self,input_string):
        """
        This is where all the processing happens.

        Let's just read the string backwards
        """
        return input_string[0::]

    def client_thread(self,conn, ip, port, MAX_BUFFER_SIZE=4096):
        # the input is in bytes, so decode it
        input_from_client_bytes = conn.recv(MAX_BUFFER_SIZE)

        # MAX_BUFFER_SIZE is how big the message can be
        # this is test if it's sufficiently big
        import sys
        siz = sys.getsizeof(input_from_client_bytes)
        if siz >= MAX_BUFFER_SIZE:
            print("The length of input is probably too long: {}".format(siz))

        # decode input and strip the end of line
        input_from_client = input_from_client_bytes.decode("utf8").rstrip()
        res = self.do_some_stuffs_with_input(input_from_client)
        print("Client : {}".format(res))
        self.list_client.append(res)
        if(self.check_login == 0):
            #SignUP
            if(self.list_client[0] == '1' and len(self.list_client) == 7):
                self.Server_con.SignUp(self.list_client[1], self.list_client[2], self.list_client[3], self.list_client[4],self.list_client[5], self.list_client[6])
                print(self.list_client)
                if(self.Server_con.check != 0):
                    res2 = "Da Ton Tai Tai Khoan"
                    vysl2 = res2.encode("utf8")
                    conn.sendall(vysl2)
                    self.list_client.clear()
                else:
                    res2 = "Dang ky thanh cong"
                    vysl2 = res2.encode("utf8")
                    conn.sendall(vysl2)
                    self.list_client.clear()
            #SignIN
            elif(self.list_client[0] == '2' and len(self.list_client) == 3):
                self.Server_con.SignIn(self.list_client[1], self.list_client[2])
                print(self.list_client)
                self.check_id = self.Server_con.check
                if(self.Server_con.check != 0):
                    res3 = "Dang Nhap Thanh Cong"
                    vysl3 = res3.encode("utf8")
                    conn.sendall(vysl3)
                    self.list_client.clear()
                    self.check_login = 1
                else:
                    res4 = "Dang Nhap That Bai"
                    vysl4 = res4.encode("utf8")
                    conn.sendall(vysl4)
                    self.list_client.clear()

            else:
                res5 = "OK"
                vysl5 = res5.encode("utf8")  # encode the result string
                conn.sendall(vysl5)  # send it to client

        else: #AFTER SIGNIN
            self.Server_mo.Open()
            resp = ''
            if(self.list_client[0] == '1' and len(self.list_client) == 2 and self.list_client[1] == '1'):
                self.Server_con.Show_Mess_send()
                self.list_server = self.Server_con.list_ser_con
                resp = " ".join(self.list_server[0])
                vysl_resp = resp.encode("utf8")
                conn.sendall(vysl_resp)
                self.list_server.clear()
                self.Server_con.list_ser_con.clear()
            if (self.list_client[0] == '1' and len(self.list_client) == 2 and self.list_client[1] == '2'):
                self.Server_con.Show_Mess_recv()
                self.list_server = self.Server_con.list_ser_con
                resp = " ".join(self.list_server[0])
                vysl_resp = resp.encode("utf8")
                conn.sendall(vysl_resp)
                self.list_server.clear()
                self.Server_con.list_ser_con.clear()
            """if(self.list_client[0] == '2' and len(self.list_client) == 2):
                self.Server_mo.Show_Mess_Detail(self.check_id,self.list_client[1])"""
            if(self.list_client[0] == '2' and len(self.list_client) == 3):
                self.Server_mo.Send_Mess(self.check_id, self.list_client[1], self.list_client[2])
                self.list_client.clear()
            if(self.list_client[0] == '3' and len(self.list_client) == 2):
                self.Server_mo.Add_fr(self.check_id , self.list_client[1])
                self.list_client.clear()








        conn.close()  # close connection
        print('Connection ' + ip + ':' + port + " ended")

    def start_server(self):
        import socket
        soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # this is for easy starting/killing the app
        soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        print('Socket created')

        try:
            soc.bind(("127.0.0.1", 12345))
            print('Socket bind complete')
        except socket.error as msg:
            import sys
            print('Bind failed. Error : ' + str(sys.exc_info()))
            sys.exit()

        # Start listening on socket
        soc.listen(10)
        print('Socket now listening')

        # for handling task in separate jobs we need threading
        from threading import Thread

        # this will make an infinite loop needed for
        # not reseting server for every client
        while True:
            conn, addr = soc.accept()
            ip, port = str(addr[0]), str(addr[1])
            print('Accepting connection from ' + ip + ':' + port)
            try:
                Thread(target=self.client_thread(conn, ip, port)).start()

            except:
                print("Terible error!")
                import traceback
                traceback.print_exc()
        soc.close()



