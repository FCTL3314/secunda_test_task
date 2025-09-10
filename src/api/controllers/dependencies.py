from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.database import get_async_db
from src.repositories.directory import DirectoryRepository
from src.services.directory import DirectoryService


def get_directory_service(db: AsyncSession = Depends(get_async_db)) -> DirectoryService:
    repository: DirectoryRepository = DirectoryRepository(db)
    return DirectoryService(repository)
