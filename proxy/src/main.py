from fastapi import FastAPI
from starlette.responses import Response
from threading import Thread
import time
import requests
import json

from modhashring.hashring import HashRing


app = FastAPI()
targets = []
with open('appsettings.json', 'r') as config_file:
    config = json.load(config_file)
    targets = config['ports']
ring = HashRing(nodes=targets)
deleted = []
count = 0


def try_connect():
    global deleted, ring
    while True:
        for d in deleted:
            url = d + 'ping/'
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    ring.add_node(d)
                    deleted.remove(d)
            except requests.ConnectionError:
                a = 1
        time.sleep(1)


t = Thread(target=try_connect)
t.start()


def send_get():
    global ring, count
    node = ring.get_node(count)
    if node is None:
        return Response(status_code=500, content=b'All servers is off')
    server = node

    while True:
        try:
            response = requests.get(server)
            break
        except requests.ConnectionError:
            ring.delete_node(node)
            deleted.append(node)
            if ring.get_n() < 1:
                return Response(status_code=500, content=b'All servers is off')
            node = ring.get_node(count)
            server = node

    count += 1
    return Response(status_code=response.status_code, content=response.content)


@app.get('/')
def get():
    return send_get()
