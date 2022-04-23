from requests.event import Event
import json
import hashlib


class GetEvents(Event):
    def __init__(self):
        """
        Constructor
        """
        super().__init__()
        self.command_id = 'GetEvents'
        self.username = None

    def pack(self):
        """
        The function doesn't get parameters.
        :return: The function returns a json with all the fields in the class ''.
        """
        obj = {'command_id': self.command_id, 'username': self.username}
        return json.dumps(obj)

    def unpack(self, data):
        """
        The function takes all the arguments from the json (data) and puts them in the members of this class.
        :param data: a json file.
        :return: The function doesn't return a value.
        """
        obj = json.loads(data)
        self.command_id = obj['command_id']
        self.username = obj['username']

    def handle(self):
        """
        The function handles the request
        :return: The function handles logging in.
        """

        str_db = open('db.json', 'r').read()
        json_db = json.loads(str_db)

        events_list = json_db['users'][self.username]['events']

        #bytes_events_list = json.dumps(events_list).encode()

        #self.sender_socket.send(bytes_events_list)
        self.sender_socket.send(b'ofek')
