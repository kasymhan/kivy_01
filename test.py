import json
import socket

import requests
from kivy.app import App
from kivy.config import ConfigParser
from kivy.factory import Factory
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen


class Sign_in(Screen):
    login = ObjectProperty()
    password = ObjectProperty()

    def Sign_in_user(self):
        if self.login.text == '' or self.password.text == '':
            pass
        else:

            url = 'http://127.0.0.1:8080/'
            headers = {
                'Content-type': 'application/json',
                'Accept': 'text/json',
                'Content-Encoding': 'utf-8'
            }
            data = {
                "login": "{}".format(self.login.text),
                'password': '{}'.format(self.password.text),

            }

            answer = requests.post(url, data=json.dumps(data), headers=headers)
            if answer == '404':
                pass
            if answer == '200':
                pass


class Sign_up(Screen):
    fio = ObjectProperty()
    email = ObjectProperty()
    group = ObjectProperty()
    password = ObjectProperty
    password_return = ObjectProperty()

    def New_user(self):
        if self.email.text == '' or \
                self.group.text == '' or \
                self.fio.text == '' or \
                self.password.text == '' or \
                self.password_return == '':
            pass
        elif self.password_return.text != self.password.text:
            pass
        else:
            sock = socket.socket()
            sock.connect(('127.0.0.1', 8080))
            data ={
                "login": "{}".format(self.fio.text),
                'Email': '{}'.format(self.email.text),
                'Password': '{}'.format(self.password.text),
                'pas': '{}'.format(self.password_return.text)
            }
            sock.send(json.dumps(data, ensure_ascii=False).encode("utf-8"))

            data = sock.recv(1024)
            sock.close()
            print(data)
            if data == b'client':
                print(data)
                return 'menu'
            # url = 'http://127.0.0.1:8080'
            # headers = {
            #     'Content-type': 'application/json',
            #     'Accept': 'text/json',
            #     'Content-Encoding': 'utf-8'
            # }
            # data ={
            #     "login": "{}".format(self.fio.text),
            #     'Email': '{}'.format(self.email.text),
            #     'Password': '{}'.format(self.password.text),
            #     'pas': '{}'.format(self.password_return.text)
            # }
            #
            # answer = requests.post(url, data=json.dumps(data), headers=headers)
            # if answer == '404':
            #     pass
            # if answer == '200':
            #     pass


class Menu(Screen):
    pass


pressentation = Builder.load_file('my.kv')


class Myapp(App):
    def __init__(self, **kvargs):
        super(Myapp, self).__init__(**kvargs)

        self.config = ConfigParser()
        self.screen_manager = Factory.ManagerScreens()

    def build(self):
        return self.screen_manager


if __name__ == "__main__":
    Myapp().run()
