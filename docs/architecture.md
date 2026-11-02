
# CloudExam - System Architecture

## 1. Project Overview

CloudExam is a Python-based examination submission platform designed to demonstrate cloud-native application development, DevOps automation, and DevSecOps security practices.

The application exposes REST APIs that allow users to submit examination answers and retrieve previously submitted examinations.

The project uses a local development environment with Docker and DynamoDB Local.

## 2. Architecture Components

### FastAPI
Provides REST API endpoints:
- GET /health
- POST /submissions
- GET /submissions/{submission_id}

Responsibilities:
- Accept HTTP requests
- Validate incoming data
- Return appropriate HTTP responses
- Handle database retrieval errors

### Python Lambda Handler
Located in src/lambda/submit_exam.py.

Responsibilities:
- Process examination submissions
- Validate submission data
- Generate unique submission IDs
- Generate UTC submission timestamps
- Save examination records
- Handle processing errors

### DynamoDB and Boto3
The database layer uses Boto3 to communicate with DynamoDB Local.

Responsibilities:
- Save examination submissions
- Retrieve submitted examination records
- Support local database testing

### Docker
Docker containerizes the FastAPI application.

Docker Compose runs:
- CloudExam API
- DynamoDB Local

## 3. Data Flow

1. A client sends an HTTP request through Swagger UI or another API client.
2. FastAPI validates the request.
3. The Lambda handler processes the examination submission.
4. Boto3 sends the record to DynamoDB Local.
5. The API returns a successful response.
6. Users can retrieve saved submissions using their submission ID.

## 4. DevSecOps Pipeline

GitHub Actions automatically runs the CI workflow when code is pushed to the main branch or a pull request targets main.

Pipeline stages:

1. Checkout source code.
2. Configure Python 3.13.
3. Install project dependencies.
4. Start DynamoDB Local.
5. Create the database table.
6. Run automated tests with coverage.
7. Run Bandit security analysis.
8. Run pip-audit dependency vulnerability scanning.
9. Run Gitleaks secret detection.
10. Run SonarQube Cloud analysis.

## 5. Testing and Security

Current project results:

- 13 automated tests passing locally.
- 95% overall code coverage.
- 100% coverage for the database module.
- 100% coverage for the Lambda handler.
- 0 Bandit security issues.
- No known Python dependency vulnerabilities found by pip-audit.
- No secrets detected by Gitleaks in the successful CI run.
- SonarQube Quality Gate previously passed.

## 6. Technology Stack

| Technology | Purpose |
|---|---|
| Python 3.13 | Application language |
| FastAPI | REST API framework |
| Pydantic | Request validation |
| Boto3 | DynamoDB integration |
| DynamoDB Local | Local database |
| Docker | Application containerization |
| Docker Compose | Local orchestration |
| Pytest | Automated testing |
| Bandit | Python security scanning |
| pip-audit | Dependency vulnerability scanning |
| Gitleaks | Secret detection |
| SonarQube Cloud | Code quality analysis |
| GitHub Actions | CI automation |

## 7. Deployment Scope

CloudExam currently runs as a local prototype using Docker and DynamoDB Local.

GitHub Actions runs automated checks on GitHub-hosted runners.

The project has not been deployed to AWS Lambda, API Gateway, or a production DynamoDB service.

Terraform infrastructure files are maintained as learning artifacts. No Terraform infrastructure is applied.

## 8. Future Improvements

- Add authentication and authorization.
- Introduce role-based access control.
- Add structured JSON logging.
- Implement API rate limiting.
- Add integration and load testing.
- Design an AWS deployment architecture.
- Add infrastructure deployment automation.
