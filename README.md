# CloudExam – Serverless Examination Submission Platform

## Overview

CloudExam is a containerized examination submission platform built with Python, FastAPI, AWS SDK (Boto3), and DynamoDB Local.

The application allows students to submit examination answers, generates unique submission IDs, stores records, and retrieves previously submitted examinations.

## Architecture

- **Python:** Application logic
- **FastAPI:** REST API
- **Boto3:** DynamoDB integration
- **DynamoDB Local:** Local database
- **Docker:** Application containerization
- **Docker Compose:** Multi-container orchestration
- **Pytest:** Automated testing
- **GitHub Actions:** Continuous integration
- **Terraform:** Infrastructure as Code configuration

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/health` | Health check |
| POST | `/submissions` | Submit an examination |
| GET | `/submissions/{submission_id}` | Retrieve a submission |

## Run Locally

```bash
docker compose up -d --build
```

Open the API documentation:

http://localhost:8001/docs

## Run Tests

```bash
DYNAMODB_ENDPOINT=http://localhost:8002 pytest -v
```

## Continuous Integration

GitHub Actions automatically runs the test suite when code is pushed to the main branch or a pull request is opened.

## Security and Cost

The development environment uses DynamoDB Local. No real AWS resources are required to run the local application.

## Repository

https://github.com/abdoumaiga1/cloudexam

## Project Status

- [x] FastAPI application
- [x] DynamoDB integration
- [x] Docker containerization
- [x] Docker Compose
- [x] Automated tests
- [x] GitHub Actions CI pipeline
- [ ] Security scanning
- [ ] SonarQube integration
- [ ] AWS deployment