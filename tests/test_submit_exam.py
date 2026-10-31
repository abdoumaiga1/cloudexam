



import json
from submit_exam import lambda_handler


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
