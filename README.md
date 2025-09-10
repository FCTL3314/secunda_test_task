# REST API for a Directory Application

[![Python](https://img.shields.io/badge/Python-3.12-3777A7?style=flat-square)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100.0-05998b?style=flat-square)](https://fastapi.tiangolo.com/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-d71f00?style=flat-square)](https://www.sqlalchemy.org/)
[![Pytest](https://img.shields.io/badge/Pytest-8.2.2-0A9EDC?style=flat-square)](https://pytest.org/)
[![Ruff](https://img.shields.io/badge/Style-Ruff-black?style=flat-square)](https://docs.astral.sh/ruff/)

<ul>
  <li>
    <b>
      <a href="#-description">Description</a>
    </b>
  </li>
  <li>
    <b>
      <a href="#-technology-stack">Technology Stack</a>
    </b>
  </li>
  <li>
    <b>
      <a href="#-installation">Installation</a>
    </b>
  </li>
    <li>
    <b>
      <a href="#-api-functionality">API Functionality</a>
    </b>
  </li>
  <li>
    <b>
      <a href="#-tests">Tests</a>
    </b>
  </li>
</ul>

# 📃 Description

This project is a REST API for a directory application that manages organizations, buildings, and their activities. It allows users to retrieve information about organizations based on their location, activities, and other criteria.

> Migrations are applied via `entrypoint.sh` when the container starts.

# 🛠️ Technology Stack

*   **FastAPI**: For building the REST API.
*   **Pydantic**: For data validation.
*   **SQLAlchemy**: For ORM and database interaction.
*   **Alembic**: For database migrations.
*   **Asyncpg**: For asynchronous PostgreSQL queries.
*   **PostgreSQL**: As the main database.
*   **Docker**: For containerization and infrastructure.
*   **UV**: As the package manager.

# 💽 Installation

1.  Clone or download the repository.
2.  Fill `.env.dist` with the required variables or leave the default ones for a test start, then rename the file to `.env`.
3.  Run docker services: `docker-compose -f docker/local/docker-compose.yml up -d` or `make up_local_services`
4.  The API documentation will be available at http://127.0.0.1:8080/docs

> For a test launch, you don't need to change the variables in .env.dist, just rename the file to .env.

# ⚙️ API Functionality

Interaction with the API is done via HTTP requests using a static API key. All responses are in JSON format. The following methods are implemented:

*   Get a list of all organizations in a specific building.
*   Get a list of all organizations related to a specified activity.
*   Get a list of organizations within a given radius/rectangular area relative to a specified point on the map.
*   Get information about an organization by its ID.
*   Search for organizations by activity, including sub-activities.
*   Search for an organization by name.

# 🧪 Tests

Tests can be run inside the application container with the following command in the app container:

```bash
uv run pytest
```
