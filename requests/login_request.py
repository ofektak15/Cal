from requests.event import Event
import json
import hashlib


class LoginRequest(Event):
    def __init__(self):
        """
        Constructor
        """
        super().__init__()
        self.command_id = 'LoginRequest'
        self.username = None
        self.password = None

    def pack(self):
        """
        The function doesn't get parameters.
        :return: The function returns a json with all the fields in the class LoginRequest.
        """
        obj = {'command_id': self.command_id, 'username': self.username, 'password': self.password}
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
        self.password = obj['password']

    def handle(self):
        """
        The function handles the request
        :return: The function handles logging in.
        """

        str_db = open('db.json', 'r').read()
        json_db = json.loads(str_db)

        if self.username in json_db['users'].keys():  # if the username exists
            hashed_password = hashlib.md5(self.password.encode()).hexdigest()  # hashing the password
            if hashed_password == json_db['users'][self.username]['password']:  # if the hashed password is correct
                str_modified_db = json.dumps(json_db)
                open('db.json', 'w').write(str_modified_db)
                self.sender_socket.send(b'SUCCESS')
                return

        self.sender_socket.send(b'FAIL')
