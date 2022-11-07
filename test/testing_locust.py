from locust import HttpUser, task, between


class WebsiteUser(HttpUser):
    wait_time = between(5, 50)

    @task
    def get(self):
        self.client.get("/")
