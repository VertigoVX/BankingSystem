# Banking System - Full Stack Application

The following is a full-stack simple banking transaction management system that allows users to manage financial transactions. The system is built with the following tech stack:

- **Backend**: Python, Flask
- **Frontend**: JavaScript, HTML, SASS
- **Database**: PostgreSQL
- **Testing**: Unit Tests (Python), Integration Tests (Cypress)
- **Containerization**: Docker, Docker Compose

The system allows users to manage financial transactions, including adding, editing, and deleting transactions. It also displays the account balance in real-time

## Features

### Backend

- RESTful API for managing transactions.

```plaintext
Endpoints:

POST /transactions: Add a new transaction

GET /transactions: Retrieve all transactions

GET /transactions/{transactionID}: Retrieve a specific transaction

PUT /transactions/{transactionID}: Modify a transaction

DELETE /transactions/{transactionID}: Remove a transaction
```

- Error handling for invalid data and database errors

## Frontend

Single Page Application (SPA) for managing transactions

### Features:

- Add, edit, and delete transactions

- Real-time account balance display

- User-friendly error messages

Styled with SASS for a modern and intuitive interface

## Testing

- **Unit Tests:** Test the backend models and controllers.

- **Integration Tests:** Test the frontend using Cypress.

## Docker

- Containerized backend, frontend, and PostgreSQL database.

- Easy setup and deployment using Docker Compose.

## Prerequisites

Before setting up the application, ensure you have the following installed:

1. [Docker Desktop](https://www.docker.com/products/docker-desktop) and docker compose
2. [Python](https://www.python.org/) and pip

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/VertigoVX/BankingSystem.git
cd BankingSystem
```

Step 2: Build and Run with Docker Compose
Build and Start the Containers:

```bash
docker-compose up --build
```

### Access the Application:

- Frontend: Open http://localhost:80 in your browser.

- Backend API: Accessible at http://localhost:5000.

- Swagger UI: Accessible at http://localhost:5000/ui.

### Stop the Containers:

```bash
docker-compose down
```