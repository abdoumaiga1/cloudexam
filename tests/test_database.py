
import sys
from pathlib import Path
from uuid import uuid4
from datetime import datetime, timezone

sys.path.insert(
    0,
    str(Path(__file__).resolve().parents[1] / "src" / "lambda")
)

from database import save_submission, table


def test_save_submission():
    submission_id = str(uuid4())

    submission = {
        "submission_id": submission_id,
        "student_id": "student-001",
        "exam_id": "exam-001",
        "answers": {
            "question-1": "A",
            "question-2": "B"
        },
        "submitted_at": datetime.now(timezone.utc).isoformat(),
        "status": "SUBMITTED"
    }

    result = save_submission(submission)

    assert result["submission_id"] == submission_id

    response = table.get_item(
        Key={"submission_id": submission_id}
    )

    assert response["Item"]["student_id"] == "student-001"
