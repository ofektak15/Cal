from requests.create_event import CreateEvent
from requests.login_request import LoginRequest
from requests.get_events import GetEvents


class Consts(object):
    # A dictionary that contains all the types of the requests
    REQUESTS = {
        'CreateEvent': CreateEvent,
        'LoginRequest': LoginRequest,
        'GetEvents': GetEvents
    }

    PORT = 8080
    HOST = '127.0.0.1'
