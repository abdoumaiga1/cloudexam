
import json
import logging
import uuid
from datetime import datetime, timezone

from database import save_submission

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):

    try:
        body = event.get("body")

        if isinstance(body, str):
            body = json.loads(body)
        elif body is None:
            body = {}

        student_id = body.get("student_id")
        exam_id = body.get("exam_id")
        answers = body.get("answers")

        if not student_id or not exam_id or not isinstance(answers, dict) or not answers:
            return {
                "statusCode": 400,
                "body": json.dumps({
                    "message": "Invalid examination submission"
                })
            }

        submission = {
            "submission_id": str(uuid.uuid4()),
            "student_id": student_id,
            "exam_id": exam_id,
            "answers": answers,
            "submitted_at": datetime.now(timezone.utc).isoformat(),
            "status": "SUBMITTED"
        }

        save_submission(submission)

        logger.info(
            "Submission saved: %s",
            submission["submission_id"]
        )

        return {
            "statusCode": 201,
            "body": json.dumps({
                "message": "Exam submitted successfully",
                "submission_id": submission["submission_id"]
            })
        }

    except (json.JSONDecodeError, TypeError):
        return {
            "statusCode": 400,
            "body": json.dumps({
                "message": "Invalid JSON request"
            })
        }

    except Exception:
        logger.exception("Submission failed")

        return {
            "statusCode": 500,
            "body": json.dumps({
                "message": "Internal server error"
            })
        }
