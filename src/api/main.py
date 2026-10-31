
import sys
from pathlib import Path

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

sys.path.insert(
    0,
    str(Path(__file__).resolve().parents[1] / "lambda")
)

from database import save_submission, table

from submit_exam import lambda_handler

app = FastAPI(
    title="CloudExam API",
    description="Serverless examination submission platform",
    version="1.0.0"
)


class ExamSubmission(BaseModel):
    student_id: str
    exam_id: str
    answers: dict[str, str] = Field(min_length=1)


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "application": "CloudExam"
    }


@app.post("/submissions", status_code=201)
def create_submission(payload: ExamSubmission):
    import json

    event = {
        "body": payload.model_dump_json()
    }

    response = lambda_handler(event, None)

    if response["statusCode"] != 201:
        raise HTTPException(
            status_code=response["statusCode"],
            detail=json.loads(response["body"])
        )

    return json.loads(response["body"])


@app.get("/submissions/{submission_id}")
def get_submission(submission_id: str):

    response = table.get_item(
        Key={"submission_id": submission_id}
    )

    item = response.get("Item")

    if not item:
        raise HTTPException(
            status_code=404,
            detail="Submission not found"
        )

    return item
