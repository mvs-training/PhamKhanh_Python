import sqlite3
global c
global conn
class Model:
    def Open(self):
        self.conn = sqlite3.connect('messenger.db')
        self.c = self.conn.cursor()
    def Select_All(self, username: object) -> object:
        self.Open()
        self.c.execute('SELECT * FROM user WHERE username = ?', (username,))
        row = self.c.fetchone()
        if(row in self.c.execute('SELECT * FROM user WHERE username = ?', (username,))):
            return 1
        else:
            return 0
    def SQL_Reg(self, username, password, sex, birthday, fullname, address):
        puschase = (username, password, sex, birthday, fullname, address)
        self.c.execute('INSERT INTO user (username, password, sex, birth, name, address) VALUES (?,?,?,?,?,?)', puschase)
        self.conn.commit()


    def Check_Login(self, username, password):
        self.Open()
        self.c.execute('SELECT * FROM user WHERE username = ? and password = ?', (username,) + (password,))
        row = self.c.fetchone()
        if(row in self.c.execute('SELECT * FROM user WHERE username = ? and password = ?', (username,) + (password,))):
            return row[0]
        else:
            return 0

    def Check_id(self, username):
        self.Open()
        self.c.execute('SELECT * FROM user WHERE username = ?', (username,))
        row = self.c.fetchone()
        if (row in self.c.execute('SELECT * FROM user WHERE username = ?', (username,))):
            return row[0]
        else:
            return 0


    def Select_Mask(self):
        self.c.execute("select max(id) from user")
        id = self.c.fetchone()[0]
        return id
    def Insert_Mask(self, id, fullname, sex, address):
        purchase =(id, fullname, sex, address)
        self.c.execute("INSERT INTO mask_user VALUES (?,?,?,?)", purchase)
        self.conn.commit()

    def SQL_Show_Mess_send(self, id):
        self.c.execute("select message.content from message,user where user.id=message.idsen and user.id=?", (id,))
        return self.c.fetchone()
    def SQL_Show_Mess_recv(self, id):
        self.c.execute("select message.content from message,user where user.id=message.idrec and user.id=?", (id,))
        return self.c.fetchone()
    def Search_fr(self, username):
        self.c.execute("SELECT id FROM user WHERE username = ?", (username,))
        return self.c.fetchone()


    """def Show_Mess_Detail(self, id1, friend_name):
        id2 = self.Search_fr(friend_name)
        self.c.execute("SELECT * FROM message,user WHERE(idsen = ? OR idsen = ?) AND(idrec = ? OR idrec = ?) and user.id = message.idsen", (id1, id2,) + (id1, id2,))
        print(self.c.fetchone())
    """
    def Send_Mess(self , id_u, mess, friend_user):
        self.Open()
        self.c.execute('SELECT * FROM user WHERE username = ?', (friend_user,))
        row = self.c.fetchone()
        if (row in self.c.execute('SELECT * FROM user WHERE username = ?', (friend_user,))):
            id_fr = row[0]
            self.c.execute("INSERT INTO message VALUES (?,?,?,?,?,?)", (id_u, id_fr, mess, 'a', 'a', 'a'))
            self.conn.commit()
    def Add_fr(self, id_user, friend_user):
        self.Open()
        id_fr = self.Check_id(friend_user)
        self.c.execute("INSERT INTO friend VALUES (?,?,?)", (id_user, id_fr, 'a'))
        self.conn.commit()