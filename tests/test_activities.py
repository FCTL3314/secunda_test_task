from http import HTTPStatus

import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_read_organizations_by_activity(client: AsyncClient, headers: dict[str, str]):
    response = await client.get("/api/v1/activities/1/organizations", headers=headers)
    assert response.status_code == HTTPStatus.OK
    assert isinstance(response.json(), list)


@pytest.mark.asyncio
async def test_search_organizations_by_activity_name(client: AsyncClient, headers: dict[str, str]):
    response = await client.get("/api/v1/activities/search/", params={"name": "Мясная"}, headers=headers)
    assert response.status_code == HTTPStatus.OK
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0
