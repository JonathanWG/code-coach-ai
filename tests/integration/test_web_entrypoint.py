from src.entrypoints.web.app import app
import pytest


def test_generate_challenge_endpoint():
    with app.test_client() as client:
        response = client.post("/generate_challenge/", json={
            "theme": "array manipulation python",
            "difficulty": "Medium"
        })

        assert response.status_code == 200
        data = response.get_json()
        assert data["status"] == "success"
        assert "challenge" in data
        challenge = data["challenge"]
        assert "title" in challenge
        assert "description" in challenge
        assert isinstance(challenge["tags"], list)

        print("Generated Challenge from Endpoint:", challenge)