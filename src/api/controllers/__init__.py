from fastapi import APIRouter, Depends

from src.api.controllers import buildings, organizations, activities, system
from src.api.middlewares import verify_api_key

base_router: APIRouter = APIRouter()
v1_router: APIRouter = APIRouter(prefix="/api/v1", dependencies=[Depends(verify_api_key)])

v1_router.include_router(buildings.router)
v1_router.include_router(organizations.router)
v1_router.include_router(activities.router)
base_router.include_router(system.router)
base_router.include_router(v1_router)
