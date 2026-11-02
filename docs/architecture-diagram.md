
# CloudExam Architecture Diagram

## 1. Application Architecture

```mermaid
flowchart TD
    USER["API Client / Swagger UI"]

    subgraph APP["Docker Compose - Local Environment"]
        API["FastAPI REST API"]
        LAMBDA["Python Lambda Handler"]
        BOTO["Boto3 Database Layer"]
        DB[("DynamoDB Local")]

        API -->|"Validate HTTP requests"| LAMBDA
        LAMBDA -->|"Save submission"| BOTO
        BOTO -->|"PutItem / GetItem"| DB
        DB -->|"Stored examination record"| BOTO
        BOTO -->|"Retrieved data"| API
    end

    USER -->|"POST /submissions"| API
    USER -->|"GET /submissions/{id}"| API
    USER -->|"GET /health"| API

    classDef client fill:#dbeafe,stroke:#2563eb,color:#1e3a8a
    classDef application fill:#dcfce7,stroke:#16a34a,color:#14532d
    classDef database fill:#fef3c7,stroke:#d97706,color:#78350f

    class USER client
    class API,LAMBDA,BOTO application
    class DB database
```

## 2. DevSecOps CI Pipeline

```mermaid
flowchart TD
    DEV["Developer"]
    GIT["GitHub Repository"]
    CI["GitHub Actions"]

    TEST["Pytest + Coverage"]
    BANDIT["Bandit"]
    AUDIT["pip-audit"]
    GITLEAKS["Gitleaks"]
    SONAR["SonarQube Cloud"]
    RESULT["CI Pipeline Result"]

    DEV -->|"Git push / Pull request"| GIT
    GIT --> CI

    CI --> TEST
    TEST --> BANDIT
    BANDIT --> AUDIT
    AUDIT --> GITLEAKS
    GITLEAKS --> SONAR
    SONAR --> RESULT
```

## 3. Technology Stack

- Python 3.13
- FastAPI
- Pydantic
- AWS SDK for Python (Boto3)
- DynamoDB Local
- Docker and Docker Compose
- GitHub Actions
- Pytest and pytest-cov
- Bandit
- pip-audit
- Gitleaks
- SonarQube Cloud

## 4. Deployment Scope

This is a local development prototype.

The application runs with Docker and DynamoDB Local. GitHub Actions executes CI checks using GitHub-hosted runners.

No production AWS infrastructure is deployed.
