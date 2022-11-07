from locust import HttpUser, task, between


class WebsiteUser(HttpUser):
    wait_time = between(5, 50)

    @task
    def get(self):
        self.client.get("/")

# py -m locust -f testing_locust.py --host=http://localhost:8000
