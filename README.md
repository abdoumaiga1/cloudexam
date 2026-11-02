
# CloudExam – Cloud-Native Examination Submission Platform

[![CloudExam CI](https://github.com/abdoumaiga1/cloudexam/actions/workflows/ci.yml/badge.svg)](https://github.com/abdoumaiga1/cloudexam/actions/workflows/ci.yml)

CloudExam is a Python-based examination submission platform designed to demonstrate cloud-native application development, containerization, automated testing, and DevSecOps practices.

The application exposes REST APIs for submitting and retrieving examination records. It uses FastAPI, a Python Lambda-style handler, Boto3, and DynamoDB Local.

> **Project scope:** CloudExam currently runs as a local prototype using Docker and DynamoDB Local. GitHub Actions executes automated CI checks on GitHub-hosted runners. No production AWS infrastructure is deployed.

## Key Features

- REST API development with FastAPI.
- Examination submission processing using Python.
- Unique submission ID generation.
- UTC submission timestamps.
- Data storage and retrieval using Boto3 and DynamoDB Local.
- Request validation and error handling.
- Structured application logging.
- Docker containerization and Docker Compose.
- Automated testing with Pytest and coverage reporting.
- Automated security and code-quality analysis.

## Architecture

### Application Architecture

![CloudExam Application Architecture](docs/architecture-diagram.md)

The application follows this request flow:

1. A client submits an examination through Swagger UI or an API client.
2. FastAPI validates the incoming request.
3. The Python Lambda handler processes the submission.
4. Boto3 communicates with DynamoDB Local.
5. The application stores and retrieves examination records.

### DevSecOps Pipeline

The GitHub Actions workflow automates testing and security checks.

The pipeline includes:

- Pytest and coverage reporting.
- Bandit source-code security scanning.
- pip-audit dependency vulnerability scanning.
- Gitleaks secret detection.
- SonarQube Cloud code-quality analysis.

See [Architecture Documentation](docs/architecture.md) and [Architecture Diagrams](docs/architecture-diagram.md).

## Technology Stack

| Technology | Purpose |
|---|---|
| Python 3.13 | Application development |
| FastAPI | REST API framework |
| Pydantic | Request validation |
| Boto3 | DynamoDB integration |
| DynamoDB Local | Local database |
| Docker | Application containerization |
| Docker Compose | Local orchestration |
| Pytest | Automated testing |
| pytest-cov | Test coverage |
| Bandit | Python security scanning |
| pip-audit | Dependency vulnerability scanning |
| Gitleaks | Secret detection |
| SonarQube Cloud | Code-quality analysis |
| GitHub Actions | CI automation |
| Terraform | Infrastructure as Code learning artifact |

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/health` | Check application health |
| POST | `/submissions` | Submit an examination |
| GET | `/submissions/{submission_id}` | Retrieve an examination submission |

### Example Submission

Request:

```json
{
  "student_id": "student-101",
  "exam_id": "medical-exam-001",
  "answers": {
    "question-1": "A",
    "question-2": "B",
    "question-3": "C"
  }
}
```

Successful response:

```json
{
  "message": "Exam submitted successfully",
  "submission_id": "generated-uuid"
}
```

A successful submission returns HTTP `201 Created`.

## Run Locally

### Prerequisites

- Python 3.13
- Docker Desktop
- Docker Compose
- Git

### Clone the Repository

```bash
git clone https://github.com/abdoumaiga1/cloudexam.git
cd cloudexam
```

### Start the Application

```bash
docker compose up -d --build
```

Check running containers:

```bash
docker compose ps
```

### Access Swagger UI

Open:

http://localhost:8001/docs

### Stop the Application

```bash
docker compose down
```

## Run Automated Tests

Activate your Python virtual environment and run:

```bash
DYNAMODB_ENDPOINT=http://localhost:8002 pytest -v
```

Generate a coverage report:

```bash
DYNAMODB_ENDPOINT=http://localhost:8002 pytest \
  --cov=src \
  --cov-report=term-missing \
  --cov-report=xml
```

## Testing and Security Results

Latest verified local results:

| Metric | Result |
|---|---:|
| Automated tests | 13 passed |
| Overall code coverage | 95% |
| Database module coverage | 100% |
| Lambda handler coverage | 100% |
| Bandit security findings | 0 |
| Known dependency vulnerabilities | 0 |

The latest GitHub Actions workflow also completed successfully, including Gitleaks and SonarQube Cloud analysis.

These results reflect the latest verified test and CI runs; they may change as the project evolves.

## Repository Structure

```text
cloudexam/
├── .github/
│   └── workflows/
│       └── ci.yml
├── docs/
│   ├── architecture.md
│   └── architecture-diagram.md
├── infrastructure/
│   └── main.tf
├── src/
│   ├── api/
│   │   └── main.py
│   └── lambda/
│       ├── database.py
│       └── submit_exam.py
├── tests/
│   ├── test_api.py
│   ├── test_database.py
│   └── test_submit_exam.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── sonar-project.properties
└── README.md
```

## Security and Cost Considerations

- Local application testing uses DynamoDB Local.
- Dummy local credentials are used for local database access.
- No production AWS credentials are required for local development.
- No AWS infrastructure is provisioned by the current workflow.
- Terraform files are maintained as learning artifacts and are not applied.

## Future Improvements

- Implement authentication and authorization.
- Introduce role-based access control.
- Add API rate limiting.
- Add integration and load testing.
- Design and implement an AWS deployment.
- Automate infrastructure provisioning with Terraform.
- Add production monitoring and observability.

## Project Repository

See the [Application Architecture Diagram](docs/architecture-diagram.md).
---

**CloudExam — Demonstrating Cloud DevOps, Python Development, Automation, and DevSecOps Engineering.**
