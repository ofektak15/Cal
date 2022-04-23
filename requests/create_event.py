from requests.event import Event
import json


class CreateEvent(Event):
    def __init__(self):
        """
        Constructor
        """
        super().__init__()
        self.command_id = 'CreateEvent'
        self.event_name = None
        self.start_date = None
        self.start_time = None
        self.end_date = None
        self.end_time = None
        self.location = None
        self.username = None

    def pack(self):
        """
        The function doesn't get parameters.
        :return: The function returns a json with all the fields in the class CreateEvent.
        """
        obj = {'command_id': self.command_id, 'event_name': self.event_name, 'start_date': self.start_date,
               'start_time': self.start_time, 'end_date': self.end_date, 'end_time': self.end_time,
               'location': self.location, 'username': self.username}
        return json.dumps(obj)

    def unpack(self, data):
        """
        The function takes all the arguments from the json (data) and puts them in the members of this class.
        :param data: a json file.
        :return: The function doesn't return a value.
        """
        obj = json.loads(data)
        self.command_id = obj['command_id']
        self.event_name = obj['event_name']
        self.start_date = obj['start_date']
        self.start_time = obj['start_time']
        self.end_date = obj['end_date']
        self.end_time = obj['end_time']
        self.location = obj['location']
        self.username = obj['username']

    def handle(self):
        """
        # TODO: לתעד
        :return:
        """
        str_db = open('db.json', 'r').read()
        json_db = json.loads(str_db)

        # TODO: אני עורך את התוכן שנמצא בשדה הזה, לא יוצר אירוע חדש
        json_db['users'][self.username]['events'].append({})
        arr_events = json_db['users'][self.username]['events']
        json_db['users'][self.username]['events'][len(arr_events-1)]['event_name'] = self.event_name
        json_db['users'][self.username]['events'][len(arr_events - 1)]['start_date'] = self.start_date
        json_db['users'][self.username]['events'][len(arr_events - 1)]['start_time'] = self.start_time
        json_db['users'][self.username]['events'][len(arr_events - 1)]['end_date'] = self.end_date
        json_db['users'][self.username]['events'][len(arr_events - 1)]['end_time'] = self.end_time
        json_db['users'][self.username]['events'][len(arr_events - 1)]['location'] = self.location

        str_modified_db = json.dumps(json_db)
        open('db.json', 'w').write(str_modified_db)

        self.sender_socket.send(b'SUCCESS')
