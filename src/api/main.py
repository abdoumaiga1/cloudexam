

import sys
import json
import logging
from pathlib import Path

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from botocore.exceptions import BotoCoreError, ClientError

sys.path.insert(
    0,
    str(Path(__file__).resolve().parents[1] / "lambda")
)

from database import table
from submit_exam import lambda_handler

logger = logging.getLogger(__name__)

app = FastAPI(
    title="CloudExam API",
    description="Serverless examination submission platform",
    version="1.0.0"
)


class ExamSubmission(BaseModel):
    student_id: str = Field(min_length=1)
    exam_id: str = Field(min_length=1)
    answers: dict[str, str] = Field(min_length=1)


@app.get("/health")
def health_check():
    logger.info("Health check requested")

    return {
        "status": "healthy",
        "application": "CloudExam"
    }


@app.post("/submissions", status_code=201)
def create_submission(payload: ExamSubmission):

    logger.info(
        "Submission request received for student: %s",
        payload.student_id
    )

    event = {
        "body": payload.model_dump_json()
    }

    response = lambda_handler(event, None)

    if response["statusCode"] != 201:
        logger.warning(
            "Submission rejected with status code: %s",
            response["statusCode"]
        )

        raise HTTPException(
            status_code=response["statusCode"],
            detail=json.loads(response["body"])
        )

    logger.info(
        "Submission successfully processed for student: %s",
        payload.student_id
    )

    return json.loads(response["body"])


@app.get(
    "/submissions/{submission_id}",
    responses={
        404: {"description": "Submission not found"},
        503: {"description": "Database temporarily unavailable"}
    }
)
def get_submission(submission_id: str):

    logger.info(
        "Retrieving submission: %s",
        submission_id
    )

    try:
        response = table.get_item(
            Key={"submission_id": submission_id}
        )

        item = response.get("Item")

        if not item:
            logger.warning(
                "Submission not found: %s",
                submission_id
            )

            raise HTTPException(
                status_code=404,
                detail="Submission not found"
            )

        logger.info(
            "Submission retrieved successfully: %s",
            submission_id
        )

        return item

    except HTTPException:
        raise

    except (BotoCoreError, ClientError):
        logger.exception(
            "Database error retrieving submission: %s",
            submission_id
        )

        raise HTTPException(
            status_code=503,
            detail="Database temporarily unavailable"
        )
