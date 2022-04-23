from client import Client
import eel
import random

client = Client()  # creating a client


@eel.expose
def create_event(event_name, username):
    print("create event")
    status = client.create_event(event_name, username)
    return status


@eel.expose
def get_events(username):
    print("get_events")
    name_of_events = client.get_events(username)
    print(name_of_events)
    return name_of_events


def main():
    eel.init('')
    rnd = random.randint(0, 3000)
    print('using port: {}'.format(8080 + rnd))
    eel.start('calendar_table.html', disable_cache=True, size=(400, 675), port=8080 + rnd)


if __name__ == '__main__':
    main()

