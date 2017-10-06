import socket
import threading
import inspect
import sys
import re


def _listen(app, client_connection, client_address):
    try:
        request = client_connection.recv(1024).decode('utf-8')
        app.set_request(request)
        # print(request)
        # print(app.responses)
        for x in app.responses:
            client_connection.send(x)
        client_connection.close()
    except:
        client_connection.close()


def start(app, module, port = 8080):
    for name, action in inspect.getmembers(sys.modules[module]):
        if re.compile("^route_([a-zA-Z0-9\_])*$").match(name):
            action()

    mysocket = socket.socket()
    mysocket.bind(('127.0.0.1', port))
    print('server run at 127.0.0.1:{}...'.format(port))
    mysocket.listen(5)
    while True:
        client_connection, client_address = mysocket.accept()
        threading.Thread(target=_listen, args=(app, client_connection, client_address)).start()
