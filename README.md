# Clean Architecture With Python

This repository provides a template for building applications using the Clean Architecture principles with Python.

[![Tests](https://github.com/javiertelioz/clean-architecture-python/actions/workflows/tests.yml/badge.svg)](https://github.com/javiertelioz/clean-architecture-python/actions/workflows/tests.yml)

[![Coverage](https://github.com/javiertelioz/clean-architecture-python/raw/main/coverage.svg)](https://github.com/javiertelioz/clean-architecture-python/actions/workflows/tests.yml)

## Technology Stack

- Python
- FastAPI
- SQLAlchemy
- Docker
- pytest
- coverage

## Download the Project

```bash
git clone https://github.com/javiertelioz/clean-architecture-python.git
```

## Setup

Navigate to the project directory:

```bash
cd clean-architecture-python
```

## Run the Application

Start the application using Docker Compose:

```bash
docker-compose up -d
```

Once the application is running, you can access the API documentation at http://localhost:8000/docs.

## Linting

Lint the code using the following command:

```bash
docker-compose run --rm web autopep8 --in-place --aggressive --recursive .
```

## Running Tests

Run the tests using the following command:

```bash
docker-compose run --rm web pytest
```

## Test Coverage

To generate a test coverage report, run the following commands:

```bash
docker-compose run --rm web coverage run -m pytest
docker-compose run --rm web coverage report -m
```

The coverage report will show the percentage of code coverage for the project.

Feel free to customize the code and directory structure to suit your specific needs. Happy coding!
