from http import HTTPStatus

import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_read_buildings(client: AsyncClient, headers: dict[str, str]):
    response = await client.get("/api/v1/buildings/", headers=headers)
    assert response.status_code == HTTPStatus.OK
    assert isinstance(response.json(), list)
