import csv
import sys
import os

CLIENT_TABLE = '.client.csv'
CLIENT_SCHEMA = ['name', 'company', 'email', 'position']
clients = []

def _initialize_clients_from_storage():
    with open(CLIENT_TABLE, mode ='r', encoding='UTF-8') as f:
        reader = csv.DictReader(f, fieldnames= CLIENT_SCHEMA)

        for row in reader:
            clients.append(row)


def _save_client_to_storage():
    tmp_table_name = '{}.tmp'.format(CLIENT_TABLE)
    with open(tmp_table_name, mode = 'w', encoding= 'UTF-8') as f:
        writer = csv.DictWriter(f, fieldnames= CLIENT_SCHEMA)
        writer.writerows(clients)

    os.remove(CLIENT_TABLE)
    os.rename(tmp_table_name, CLIENT_TABLE)


def create_client(client):
    global clients
    if client not in clients:
        clients.append(client)
    else:
        print('Client already is in the client\'s list')


def update_client(client_index):
    global clients
    if client_index == None:
        print('Client is not in client\'s list')
    else:
        if clients[client_index] in clients:
            clients[client_index] = _get_client_field()


def delete_client(client_index):
    global clients
    if client_index == None:
        print('Client is not in client\'s list')
    else:
        if clients[client_index] in clients:
            del clients[client_index]
       


def list_clients():
    global clients
    print('uid | name | company | email | position')
    print('*'*50)
    for i, client in enumerate(clients):
        print('{uid} | {name} | {company} | {email} | {position}'.format(
            uid = i,
            name = client['name'],
            company = client['company'],
            email = client['email'],
            position = client['position']))


def search_client(client_index):
    global clients
    if client_index == None:
        print('Client is not in client\'s list')
    else:
        if clients[client_index] in clients:
            return True


def _print_welcome():
    print('WELCOME TO PLATZI VENTAS')
    print('*' * 50)
    print('What do you like to do today?')
    print('[C]reate client')
    print('[L]ist client\'s')
    print('[U]pdate client')
    print('[D]elete client')
    print('[S]earch client')


def _get_client_field():
    global clients
    client = None
    
    while  not client:
        client = (input('What is the client name? ')).title()
        if client == 'Exit':
            client = None
            break
        
        client = {
            'name': client,
            'company': input('What is the client company? ').title(),
            'email': input('What is the client email? '),
            'position': (input('What is the client position? ')).capitalize(),
        }

    if not client: sys.exit()

    return client
    

def _get_client_name():
    global clients
    client_name = None
    while  not client_name:
        client_name =  (input('What is the client name? ')).title()

        for i, client in enumerate(clients):
            if client['name'] == client_name:
                return i

        if client_name == 'Exit':
            client_name = None
            break

        else: return None

    if not client_name: sys.exit()

    


if __name__=='__main__':

    _initialize_clients_from_storage()

    _print_welcome()

    command = input()
    command = command.upper()

    if command == 'C':
        create_client(_get_client_field())
    elif command == 'L':
        list_clients()
    elif command == 'D':
        delete_client(_get_client_name())
    elif command == 'U':
        update_client(_get_client_name())
    elif command == 'S':
        client_name = _get_client_name()
        found = search_client(client_name)
        if found:
            print('The client is in the client\'s list')
    else:
        print('Invalid command')

    _save_client_to_storage()
    
    

