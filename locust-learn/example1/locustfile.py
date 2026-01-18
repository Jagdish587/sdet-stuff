import random
from locust import HttpUser, task, between

class AuthUser(HttpUser):
    wait_time = between(1, 2)

    def on_start(self):
        """Runs once when a user starts"""
        response = self.client.post(
            "/login",
            json={
                "username": "admin",
                "password": "secret"
            }
        )

        # Save token for later requests
        self.token = response.json()["token"]
        self.headers = {
            "Authorization": self.token
        }

    @task(2)
    def get_users(self):
        self.client.get("/api/users", headers=self.headers)

    @task(1)
    def create_user(self):
        self.client.post(
            "/api/users",
            headers=self.headers,
            json={
                "id": random.randint(1, 100000),
                "name": "Test User"
            }
        )
