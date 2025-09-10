import asyncio
from logging.config import fileConfig

from alembic import context
from sqlalchemy.engine import Connection
from sqlalchemy.ext.asyncio import async_engine_from_config

from src.core import settings
from src.db.models import *

config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata

config.set_section_option(config.config_ini_section, "DB_NAME", settings.db.name)
config.set_section_option(config.config_ini_section, "DB_USER", settings.db.user)
config.set_section_option(
    config.config_ini_section, "DB_PASSWORD", settings.db.password
)
config.set_section_option(config.config_ini_section, "DB_HOST", settings.db.host)
config.set_section_option(config.config_ini_section, "DB_PORT", str(settings.db.port))


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    url = settings.session.url
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()


def do_run_migrations(connection: Connection) -> None:
    """Run migrations within a sync context."""
    context.configure(connection=connection, target_metadata=target_metadata)
    with context.begin_transaction():
        context.run_migrations()


async def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    connectable = async_engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
    )

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)

    await connectable.dispose()


if context.is_offline_mode():
    run_migrations_offline()
else:
    asyncio.run(run_migrations_online())
