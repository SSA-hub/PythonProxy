from fastapi import FastAPI
from starlette import status
from starlette.responses import Response
from apscheduler.schedulers.background import BackgroundScheduler
import time
import logging

app = FastAPI()
start = time.time()
s = BackgroundScheduler()
s.start()
count = 0
logging.getLogger().setLevel(logging.INFO)
logging.getLogger('apscheduler.executors.default').propagate = False


@app.get('/')
def get():
    global count
    count += 1
    return Response(status_code=status.HTTP_200_OK, content="Hello, world!")


@app.get('/ping/')
def get():
    return Response(status_code=status.HTTP_200_OK)


def log():
    global count, start
    message = str(time.time() - start) + " : " + str(count)
    logging.log(20, message)


s.add_job(log, 'interval', seconds=10)
