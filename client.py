import socket
from consts import Consts
from requests.create_event import CreateEvent
from requests.login_request import LoginRequest
from requests.get_events import GetEvents


class Client(object):
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((Consts.HOST, Consts.PORT))

    def create_event(self, event_name, username):
        """
        TODO: לתעד
        :param event_name:
        :param username:
        :return:
        """
        request = CreateEvent()

        request.event_name = event_name
        request.username = username

        self.sock.send(request.pack().encode())
        status = self.sock.recv(1024*1024).decode()

        if status == "SUCCESS":
            return True
        return False

    def get_events(self, username):
        """
        TODO: לתעד
        :param username:
        :return:
        """
        request = GetEvents()

        request.username = username

        self.sock.send(request.pack().encode())
        return self.sock.recv(1024*1024).decode()
