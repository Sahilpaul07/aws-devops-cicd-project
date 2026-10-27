
import unittest
from app import app


class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_home_page(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"AWS DevOps CI/CD Pipeline is Working", response.data)

    def test_health_endpoint(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["status"], "healthy")
        self.assertEqual(
            response.json["application"],
            "AWS DevOps CI/CD Pipeline"
        )


if __name__ == "__main__":
    unittest.main()
