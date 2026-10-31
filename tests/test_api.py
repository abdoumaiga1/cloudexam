

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]

sys.path.insert(0, str(PROJECT_ROOT))

from fastapi.testclient import TestClient
from src.api.main import app

client = TestClient(app)


def test_health_endpoint():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_create_submission():
    payload = {
        "student_id": "student-005",
        "exam_id": "medical-exam-003",
        "answers": {
            "question-1": "A",
            "question-2": "B"
        }
    }

    response = client.post("/submissions", json=payload)

    assert response.status_code == 201

    data = response.json()

    assert data["message"] == "Exam submitted successfully"
    assert data["submission_id"]


def test_get_nonexistent_submission():
    response = client.get("/submissions/nonexistent-id")

    assert response.status_code == 404
