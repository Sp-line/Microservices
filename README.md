# 🏗️ Microservices Architecture with FastAPI & Fief

A production-ready microservices template built with **Python 3.12** and **FastAPI**, featuring **Clean Architecture**, **Domain-Driven Design (DDD)**, and a dedicated Authentication service using **Fief**.

---

## 🚀 Key Features

- **Microservices Architecture**: Modular design ready for scaling.
- **Clean Architecture & DDD**: Clear separation of concerns (API, Services, Repositories, Models).
- **Modern Stack**:
  - **FastAPI** (High performance async framework)
  - **SQLAlchemy 2.0** (Async ORM)
  - **Pydantic V2** (Data validation)
  - **Alembic** (Database migrations)
- **Authentication**: Centralized Auth server using [Fief](https://www.fief.dev/) (Open Source Auth).
- **Infrastructure**: Fully containerized with **Docker** & **Docker Compose**.
- **Database**: PostgreSQL (Async) + Redis (Caching/Broker).

---

## 📂 Project Structure

The repository is organized as a monorepo containing independent services:

```text
microservices/
├── users/               # 👤 Users Microservice
│   ├── alembic/         # DB Migrations
│   ├── api/             # REST API Endpoints (Routing)
│   ├── core/            # Config & Security
│   ├── models/          # Database Models
│   ├── repositories/    # Data Access Layer
│   ├── schemas/         # Pydantic DTOs
│   ├── services/        # Business Logic
│   ├── validators/      # Complex Validation Rules
│   ├── main.py          # Entry point
│   ├── Dockerfile       # Service container definition
│   └── docker-compose.yml # Infrastructure orchestration
└── README.md            # Project documentation
```

---

## 🛠 Tech Stack

| Category | Technology |
| :--- | :--- |
| **Language** | Python 3.12 |
| **Framework** | FastAPI |
| **Database** | PostgreSQL 15 |
| **ORM** | SQLAlchemy (AsyncPG) |
| **Auth Provider** | Fief (OIDC/OAuth2) |
| **Cache/Broker** | Redis 7 |
| **Migrations** | Alembic |
| **Containerization** | Docker, Docker Compose |
| **Package Manager** | Poetry |

---

## ⚡ Getting Started
The project is designed to run entirely in Docker.

1. **Prerequisites**
   - Docker & Docker Compose installed.

2. **Clone the Repository**
    ```bash
    git clone https://github.com/Sp-line/Microservices.git
    cd microservices
    ```

3. Environment Setup
   - Navigate to the users service directory and set up the environment variables.
    ```bash
    cd users
    cp .env.template .env
    # Edit .env to configure your settings (DB, Fief, etc.)
    ```

4. **Run with Docker**
    ```bash
    docker compose up --build
    ```

---

## 🔌 API Documentation
Once the services are running, you can access the interactive documentation:

| Service | URL | Description |
| :--- | :--- | :--- |
| **Users API** | [http://localhost:8001/docs](http://localhost:8001/docs) | Swagger UI for User management |
| **Fief Auth** | [http://localhost:8000/docs](http://localhost:8000/docs) | Fief Authentication Server |

---

## 🔧 Development

### Running Migrations
Migrations are applied automatically on container startup via `docker-entrypoint.sh`.

To create a new migration manually inside the running container:

```bash
# 1. Generate a new migration file based on model changes
docker compose exec users alembic revision --autogenerate -m "your_migration_message"

# 2. Apply the migration to the database
docker compose exec users alembic upgrade head
```

## 🔒 Authentication Flow (Fief)
This project uses Fief as an external identity provider.

The Users Service connects to Fief via API to validate tokens and manage webhooks.

POST /webhooks/ endpoints in the Users Service listen for events from Fief (e.g., User Created, User Updated) to keep the local database in sync.


