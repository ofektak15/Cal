from consts import Consts
import json
import select
import socket


def main():
    server_socket = socket.socket()
    server_socket.bind(("0.0.0.0", Consts.PORT))
    server_socket.listen(50)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print("running server")
    client_sockets = []  # a list of all the sockets of the clients

    while True:
        all_sockets = [server_socket] + client_sockets
        read_list, write_list, error_list = select.select(all_sockets, client_sockets, [])

        requests = []  # a list that contains all the requests the server needs to handle
        for sock in read_list:
            if sock == server_socket:
                (client_socket, address) = server_socket.accept()  # accepting the client
                print("Accepted new socket from: ", address)
                client_sockets.append(client_socket)  # adding the socket of the client to the list of all client sockets
                continue

            data = sock.recv(1024).decode()  # receiving the data
            print(data)
            if data != '':
                print('***')
                print(data)
                print('***')

                received_json = json.loads(data)
                command_id = received_json['command_id']  # command id
                cls_message = Consts.REQUESTS.get(command_id)  # getting the class of the request

                request = cls_message()
                request.unpack(data)
                request.sender_socket = sock
                requests.append(request)  # adding the request to the requests list

                # handling all the messages list
                for request in requests:
                    return request.handle()


if __name__ == '__main__':
    main()
