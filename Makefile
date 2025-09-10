######    Variables    ######
# Base directory
BASE_DIR := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))

# Environment
ENV_PATH=${BASE_DIR}.env

# Docker
LOCAL_DOCKER_COMPOSE_PROJECT_NAME=app_local
LOCAL_DOCKER_COMPOSE_FILE_PATH=${BASE_DIR}docker/local/docker-compose.yml

# Migrations (Alembic)
ALEMBIC_CONFIG=${BASE_DIR}migrations/alembic.ini

######    Shortcuts    ######
# Local Docker Services
up_local_services:
	docker compose --env-file ${ENV_PATH} -p ${LOCAL_DOCKER_COMPOSE_PROJECT_NAME} -f ${LOCAL_DOCKER_COMPOSE_FILE_PATH} up -d
down_local_services:
	docker compose --env-file ${ENV_PATH} -p ${LOCAL_DOCKER_COMPOSE_PROJECT_NAME} -f ${LOCAL_DOCKER_COMPOSE_FILE_PATH} down
rebuild_local_services:
	docker compose --env-file ${ENV_PATH} -p ${LOCAL_DOCKER_COMPOSE_PROJECT_NAME} -f ${LOCAL_DOCKER_COMPOSE_FILE_PATH} up -d --build
restart_local_services: down_local_services up_local_services

# Migrations (Alembic)
apply_migrations:
	alembic -c ${ALEMBIC_CONFIG} upgrade head

create_migration:
	alembic -c ${ALEMBIC_CONFIG} revision --autogenerate -m "$(name)"

# Linting & Formatting
lint:
	ruff check .
format:
	ruff format . && ruff check . --fix
