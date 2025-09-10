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
3.  Run docker services: `docker compose --env-file .env -f docker/local/docker-compose.yml up -d` or `make up_local_services`
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

# Task description:

Тестовое задание "Создание REST API приложения"


Описание.
Необходимо реализовать REST API приложения для справочника Организаций, Зданий, Деятельности.
1. Организация - Представляет собой карточку организации в справочнике и должна содержать в себе следующую информацию:
   * Название: Например ООО “Рога и Копыта”
   * Номер телефона: организация может иметь несколько номеров телефонов (2-222-222, 3-333-333, 8-923-666-13-13)
   * Здание: Организация должна находится в одном конкретном здании (Например, Блюхера, 32/1)
   * Деятельность: Организация может заниматься несколькими видами деятельностей (Например, “Молочная продукция”, “Мясная продукция”)
2. Здание - Содержит в себе как минимум информацию о конкретном здании, а именно:
   * Адрес: Например - г. Москва, ул. Ленина 1, офис 3
   * Географические координаты: Местоположение здания должно быть в виде широты и долготы.
3. Деятельность - позволяет классифицировать род деятельности организаций в каталоге. Имеет название и может в древовидном виде вкладываться друг в друга. Пример возможного дерева деятельности:
  - Еда
    - Мясная продукция
    - Молочная продукция
  - Автомобили
    - Грузовые
  - Легковые
      - Запчасти
      - Аксессуары
4. Стэк - стэк fastapi+pydantic+sqlalchemy+alembic


Функционал приложения.
Взаимодействие с пользователем происходит посредством HTTP запросов к API серверу с использованием статического API ключа. Все ответы должны быть в формате JSON. Необходимо реализовать следующие методы:
* список всех организаций находящихся в конкретном здании
* список всех организаций, которые относятся к указанному виду деятельности
* список организаций, которые находятся в заданном радиусе/прямоугольной области относительно указанной точки на карте. список зданий
* вывод информации об организации по её идентификатору
* искать организации по виду деятельности. Например, поиск по виду деятельности «Еда», которая находится на первом уровне дерева, и чтобы нашлись все организации, которые относятся к видам деятельности, лежащим внутри. Т.е. в результатах поиска должны отобразиться организации с видом деятельности Еда, Мясная продукция, Молочная продукция.
* поиск организации по названию
* ограничить уровень вложенности деятельностей 3 уровням


Задание
* Спроектировать БД + Создать необходимые миграции + Заполнить БД тестовыми данными
* Реализовать API согласно разделу Функционал приложения
* Завернуть приложения в Docker контейнер, чтобы его можно было развернуть на любой машине (Если необходимо, то написать инструкцию по разворачиванию)
* Добавить в проект документацию Swagger UI или Redoc с описание
