import json
import random
from client import Client


class Generate(object):

    def __init__(self):
        pass

    @staticmethod
    def clients(number_of_clients):

        with open('data.json') as data_file:
            data = json.load(data_file)

        t_firstname = len(data["firstname"])
        t_lastname = len(data["lastname"])
        t_address = len(data["address"])
        t_status = len(data["status"])
        t_animal = len(data["animal"])
        t_car = len(data["car"])

        clients = []

        while number_of_clients > 0:
            firstname = data["firstname"][random.randint(0, t_firstname - 1)]
            lastname = data["lastname"][random.randint(0, t_lastname - 1)]
            address = data["address"][random.randint(0, t_address - 1)]
            status = data["status"][random.randint(0, t_status - 1)]
            animal = data["animal"][random.randint(0, t_animal - 1)]
            car = data["car"][random.randint(0, t_car - 1)]
            clients.append(Client(firstname, lastname, address, status, animal, car))
            number_of_clients -= 1

        return clients
