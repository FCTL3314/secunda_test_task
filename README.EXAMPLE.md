# 📖 Table of contents

[![Python](https://img.shields.io/badge/Python-3.12-3777A7?style=flat-square)](https://www.python.org/)
[![Litestar](https://img.shields.io/badge/Litestar-2.15.1-EDB641?style=flat-square)](https://www.python.org/)
[![Msgspec](https://img.shields.io/badge/Msgspec-0.18.2-EBEBEB?style=flat-square)](https://www.python.org/)
[![Black](https://img.shields.io/badge/Style-Black-black?style=flat-square)](https://black.readthedocs.io/en/stable/)

<ul>
  <li>
    <b>
      <a href="#-description">Description</a>
    </b>
  </li>

  <li>
    <b>
      <a href="#-installation">Installation</a>
    </b>
  </li>
</ul>

# 💽 Installation

1. #### Clone or download the repository.
2. #### Fill `.env.dist` with the required variables or leave the filled ones for test start and rename the file to `.env`.
3. #### Run docker services: `docker-compose -f docker/docker-compose.yml up -d`
4. #### Open http://localhost:8000/schema

> Для тестового запуска, переменные из .env.dist менять не нужно, просто переименуйте файл в .env.

# 📃 Description

#### Тестовое задание для отбора на вакансию от ИП Жушма Артём.
> Миграции применяются в `entrypoint.sh` при запуске контейнера.

**Использовал:**
* Asyncpg для асинхронных запросов к базе данных.
* AdvanceAlchemy как обёртку поверх SQLAlchemy и Alembic.
* Msgspec для представления DTO объектов.
* БД - PostgreSQL
* Docker для инфраструктуры приложения.
* Пакетный менеджер Poetry.
