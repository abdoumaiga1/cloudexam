import json
import submit_exam

from submit_exam import lambda_handler
from unittest.mock import patch


def test_complete_exam_submission():
    event = {
        "body": json.dumps({
            "student_id": "student-002",
            "exam_id": "medical-exam-001",
            "answers": {
                "question-1": "A",
                "question-2": "C",
                "question-3": "B"
            }
        })
    }

    response = lambda_handler(event, None)

    assert response["statusCode"] == 201

    result = json.loads(response["body"])

    assert result["message"] == "Exam submitted successfully"
    assert result["submission_id"]


def test_invalid_json():
    event = {
        "body": "{invalid-json"
    }

    response = lambda_handler(event, None)

    assert response["statusCode"] == 400
    assert json.loads(response["body"])["message"] == "Invalid JSON request"


def test_missing_submission_fields():
    event = {
        "body": json.dumps({
            "student_id": "student-003"
        })
    }

    response = lambda_handler(event, None)

    assert response["statusCode"] == 400
    assert json.loads(response["body"])["message"] == "Invalid examination submission"


def test_empty_answers():
    event = {
        "body": json.dumps({
            "student_id": "student-004",
            "exam_id": "medical-exam-002",
            "answers": {}
        })
    }

    response = lambda_handler(event, None)

    assert response["statusCode"] == 400


def test_missing_request_body():
    event = {}

    response = lambda_handler(event, None)

    assert response["statusCode"] == 400


def test_database_save_failure():
    event = {
        "body": json.dumps({
            "student_id": "student-005",
            "exam_id": "medical-exam-003",
            "answers": {
                "question-1": "A"
            }
        })
    }

    with patch(
        "submit_exam.save_submission",
        side_effect=Exception("Database unavailable")
    ):
        response = lambda_handler(event, None)

    assert response["statusCode"] == 500
    assert json.loads(response["body"])["message"] == "Internal server error"
