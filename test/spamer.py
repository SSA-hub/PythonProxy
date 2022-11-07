import requests
import time

url = 'http://localhost:8000/'
for i in range(1000):
    response = requests.get(url)
    assert response.status_code == 200
    time.sleep(0.2)
